# Pedro Balbino

I build AI systems that have to pass an audit: agents and retrieval pipelines where the audit trail, the decision
provenance and the cost ceiling are part of the design.

### Code you can run

| Repository | What it does | What you can check |
| --- | --- | --- |
| [deps-train](https://github.com/yolo-labz/deps-train) | Merges an organisation's safe Dependabot pull requests on a timer and holds the rest with a reason | Every decision is appended to a log with the head commit it was made on. Try `uvx --from git+https://github.com/yolo-labz/deps-train deps-train --org <org> --dry-run` |
| [wa](https://github.com/yolo-labz/wa) | A WhatsApp daemon in Go with allowlist and rate controls | 23 releases. The latest carries SLSA provenance: `gh attestation verify wa_2.3.0_linux_amd64.tar.gz --owner yolo-labz` |
| [anthropic-throttle-proxy](https://github.com/yolo-labz/anthropic-throttle-proxy) | Paces Anthropic API traffic across clients with per-bearer queues | A live dashboard of the queues |
| [quality-gates](https://github.com/yolo-labz/quality-gates) | Three deterministic pull-request gates as one composite GitHub Action | The gates run on their own pull requests |
| [claude-mac-chrome](https://github.com/yolo-labz/claude-mac-chrome) | Addresses Chrome profiles and tabs from macOS scripts without relying on window order | Releases ship with a Sigstore signature, in-toto provenance and two SBOMs |
| [noctalia-appmenu](https://github.com/yolo-labz/noctalia-appmenu) | A global menu for noctalia-shell on niri: Rust bridge and Quickshell widget | 55 releases |

More at [github.com/yolo-labz](https://github.com/yolo-labz).

### Measured records

- [Agent output guard](https://portfolio.home301server.com.br/en/projects/fleet-refusal-guard): a guard flagged 127 of
  76,474 agent messages and 126 of the flags were wrong. After three narrow fixes, one.
- [Agent workspace guard](https://portfolio.home301server.com.br/en/projects/fleet-workspace-guard): closing the last
  pane deleted a workspace and nothing said so. The confirmation now has to name what it destroys.
- [Silent failure](https://portfolio.home301server.com.br/en/projects/fleet-silent-reload): a reload ended in
  `|| true` and reported success for four days while doing nothing.
- [Tax-filing agent](https://portfolio.home301server.com.br/en/projects/compliance-tax-agent): capped at 40 tool turns
  per filing, every number re-validated against its source span.
- [Legal-domain RAG](https://portfolio.home301server.com.br/en/projects/legal-domain-rag): per-jurisdiction retrieval
  with a deterministic citation validator.

### Writing

- [Hooks are advice, rulesets are law](https://blog.home301server.com.br/posts/2026-07-11-git-rulesets-hooks-defense-in-depth/)
- [A 4-host NixOS fleet with multi-agent worktree guards](https://blog.home301server.com.br/posts/2026-05-14-nixos-fleet-multi-agent-worktree-guards/)
- [SLSA L2 + Sigstore keyless: a solo-dev supply-chain canon for OSS plugin repos](https://blog.home301server.com.br/posts/2026-05-13-slsa-sigstore-solo-dev-supply-chain/)

### What I work with

- **AI**: RAG on pgvector with hybrid search and reranking, agents, MCP integrations, eval harnesses
- **Backend**: Go, Python, TypeScript. Event-driven systems on Kafka and SQS with outbox and idempotency
- **Infrastructure**: AWS, Docker, Terraform, and a private multi-host NixOS fleet with reproducible builds
- **Data**: PostgreSQL, Redis, OpenTelemetry

[Portfolio](https://portfolio.home301server.com.br) · [Blog](https://blog.home301server.com.br) · [LinkedIn](https://www.linkedin.com/in/balbinopedro/) · [pedrobalbino@proton.me](mailto:pedrobalbino@proton.me)
