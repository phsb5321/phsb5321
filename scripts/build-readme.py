#!/usr/bin/env python3
"""Refresh the README "Latest" section from live yolo-labz releases + blog RSS.

Idempotent: only the content between the <!-- KEY:start --> / <!-- KEY:end -->
markers is rewritten, so hand-authored README prose is never touched. Failures
degrade to a placeholder line rather than blanking the section.
"""
import re
import subprocess
import urllib.request

REPOS = [
    "wa", "kokoro-speakd", "claude-mac-chrome",
    "linkedin-chrome-copilot", "fand", "claude-classroom-submit",
]
BLOG_FEED = "https://blog.home301server.com.br/index.xml"


def latest_releases():
    rows = []
    for r in REPOS:
        try:
            p = subprocess.run(
                ["gh", "api", f"repos/yolo-labz/{r}/releases/latest",
                 "--jq", '.tag_name + "\\t" + .html_url + "\\t" + .published_at'],
                capture_output=True, text=True, timeout=30)
            if p.returncode == 0 and p.stdout.strip():
                tag, url, date = p.stdout.strip().split("\t")
                rows.append((date, f"- [`{r}` {tag}]({url}) — {date[:10]}"))
        except Exception:
            continue
    rows.sort(reverse=True)
    return "\n".join(line for _, line in rows[:6]) or "_no releases found_"


def latest_writing():
    try:
        xml = urllib.request.urlopen(BLOG_FEED, timeout=20).read().decode("utf-8", "ignore")
        items = re.findall(r"<item>.*?<title>(.*?)</title>.*?<link>(.*?)</link>.*?</item>",
                           xml, re.S)[:4]
        clean = lambda s: re.sub(r"<!\[CDATA\[|\]\]>|<.*?>", "", s).strip()
        out = "\n".join(f"- [{clean(t)}]({l.strip()})" for t, l in items)
        return out or "_no posts found_"
    except Exception:
        return "_writing feed unavailable_"


def inject(text, key, content):
    return re.sub(
        rf"(<!-- {key}:start -->).*?(<!-- {key}:end -->)",
        lambda m: f"{m.group(1)}\n{content}\n{m.group(2)}",
        text, flags=re.S)


def main():
    with open("README.md", encoding="utf-8") as f:
        readme = f.read()
    readme = inject(readme, "RELEASES", latest_releases())
    readme = inject(readme, "WRITING", latest_writing())
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)
    print("README Latest section refreshed.")


if __name__ == "__main__":
    main()
