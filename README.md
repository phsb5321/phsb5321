# Pedro H S Balbino — Senior AI & Full-Stack Engineer

> Production AI features — RAG, agents, LLM pipelines — and the backend + infra
> that ship them. 6+ years across regulated and high-traffic systems.

### Shipped (anonymized clients · real numbers)
- **Multilingual education chatbot, 100K+ DAU** — 4-agent LangGraph + Azure OpenAI RAG; +40% knowledge-base precision. *(global EdTech platform)*
- **Event-driven retail backend, ~10K transactions/day** — decomposed a 1M+ LOC monolith into per-channel BFF + broker + dispatcher (strangler-fig); checkout p99 ≤ 500 ms. *(tier-1 LATAM retailer)*
- **Compliance-grade RAG for a tier-1 LATAM bank** — ~10K filings/day under LGPD + 5-year audit replay; forced-citation + span validation → zero hallucinated decisions in production.
- **Legal-domain RAG on AWS Bedrock** — 15M-document corpus across 5 jurisdictions; deterministic citation validator. *(LATAM legal-tech)*

### Open source — a verifiable supply chain
[github.com/yolo-labz](https://github.com/yolo-labz) — tools shipped with **Sigstore-signed, SLSA/in-toto-attested** releases + dual-format SBOMs (CycloneDX 1.7 + SPDX 2.3). OpenSSF Scorecard up to **7.9**. Verify any release with `gh attestation verify` / `cosign`.
- **wa** (Go) — WhatsApp Multi-Device daemon + JSON-RPC client; 20 signed releases, multi-arch (deb/rpm/apk/darwin), Go-native SBOMs + OpenVEX.
- **kokoro-speakd** (Python) — persistent Kokoro TTS daemon, <500 ms warm calls. `pip install kokoro-speakd`.
- **claude-mac-chrome** (Shell) — deterministic multi-profile Chrome automation; Scorecard 7.9.
- + `linkedin-chrome-copilot`, `claude-classroom-submit`, `fand`.

### What I build
- **AI / LLM** — RAG (pgvector · hybrid + rerank), agents (LangGraph), MCP integrations, eval harnesses
- **Backend** — Go · Python · TypeScript (NestJS / Node); event-driven (Kafka, SQS/SNS), outbox + saga + idempotency
- **Cloud / infra** — AWS (Bedrock, Lambda, ECS, Step Functions), Docker, Kubernetes, Terraform; a private 5-host NixOS / nix-darwin fleet (200+ modules, reproducible builds)
- **Data** — PostgreSQL + pgvector, Redis, OpenTelemetry

### Credentials
AWS Solutions Architect – Professional · Google Data Analytics · on GitHub since 2017

### Find me
[Portfolio](https://pedro.home301server.com.br) · [Blog](https://blog.home301server.com.br) — architecture writeups (C4 + Y-statements + fitness functions) · [LinkedIn](https://www.linkedin.com/in/balbinopedro/) · [pedrobalbino@proton.me](mailto:pedrobalbino@proton.me)
