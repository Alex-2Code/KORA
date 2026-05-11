# KORA First Paper Normalized Bibliography v0.1

## Purpose

This document normalizes bibliography records for `[R01]` through `[R24]` before BibTeX preparation.

It is a structured bibliography-planning table. It does not generate BibTeX, does not modify the manuscript, and does not make the paper submission-ready.

## Scope

This normalized bibliography covers:

- references `[R01]` through `[R24]`
- the current reference tracker
- citation audit v0.1
- citation style decision
- reference metadata audit v0.1

This pass does not generate BibTeX. This pass does not modify manuscript v0.3. The paper remains not submission-ready.

## Normalization Rules

- Preserve stable `[Rxx]` labels.
- Do not invent missing metadata.
- Separate paper/preprint references, official docs, official repositories, and artifact/evaluation guidance.
- Use organization owner for official docs and repositories when an individual author list is not appropriate.
- Mark unresolved fields explicitly.
- Track whether a record is ready for BibTeX.
- Keep venue-specific conversion deferred.
- Keep tracker-only references out of the manuscript References section unless they are cited in manuscript text later.

## Normalized Bibliography Table

| ID | Normalized reference label | Source type | Authors / Organization | Title | Venue / Publisher / Host | Year / Date | URL / DOI | Manuscript status | Metadata status | BibTeX readiness | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `[R01]` | Kwon et al., PagedAttention | paper / arXiv / DOI | Woosuk Kwon; Zhuohan Li; Siyuan Zhuang; Ying Sheng; Lianmin Zheng; Cody Hao Yu; Joseph E. Gonzalez; Hao Zhang; Ion Stoica | Efficient Memory Management for Large Language Model Serving with PagedAttention | SOSP 2023; arXiv | 2023 | https://arxiv.org/abs/2309.06180; https://doi.org/10.48550/arXiv.2309.06180 | integrated in manuscript v0.3 | complete enough for normalized bibliography | likely ready after final normalization | Related-work context only; does not support KORA superiority over serving systems. |
| `[R02]` | Janapa Reddi et al., MLPerf Inference | paper / arXiv | Vijay Janapa Reddi et al. | MLPerf Inference Benchmark | arXiv; venue/status pending normalization | 2019; revised 2020 | https://arxiv.org/abs/1911.02549 | integrated in manuscript v0.3 | needs author-list and venue/status normalization | needs author/venue review | Benchmark-methodology background only; not KORA evidence. |
| `[R03]` | ONNX Runtime documentation | official docs | ONNX Runtime project / Microsoft | ONNX Runtime | ONNX Runtime official documentation | date unavailable; accessed 2026-05-11 | https://onnxruntime.ai/docs/ | integrated in manuscript v0.3 | official docs reference; access-date treatment needed | official docs/repos requiring style decision | Runtime background only; does not imply current KORA ONNX Runtime integration. |
| `[R04]` | LangGraph Graph API documentation | official docs | LangChain | LangGraph Graph API overview | LangGraph official documentation | date unavailable; accessed 2026-05-11 | https://docs.langchain.com/oss/python/langgraph/graph-api | integrated in manuscript v0.3 | official docs reference; access-date treatment needed | official docs/repos requiring style decision | Agent orchestration context only; KORA is framed as deterministic-first execution control. |
| `[R05]` | Khattab et al., DSPy | paper / arXiv | Omar Khattab; Arnav Singhvi; Paridhi Maheshwari; Zhiyuan Zhang; Keshav Santhanam; Sri Vardhamanan; Saiful Haq; Ashutosh Sharma; Thomas T. Joshi; Hanna Moazam; Heather Miller; Matei Zaharia; Christopher Potts | DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines | arXiv; venue/status pending normalization | 2023 | https://arxiv.org/abs/2310.03714 | integrated in manuscript v0.3 | needs venue/status normalization | needs author/venue review | Programmatic LM workflow context only. |
| `[R06]` | Lewis et al., Retrieval-Augmented Generation | paper / arXiv / DOI | Patrick Lewis; Ethan Perez; Aleksandra Piktus; Fabio Petroni; Vladimir Karpukhin; Naman Goyal; Heinrich Kuttler; Mike Lewis; Wen-tau Yih; Tim Rocktaschel; Sebastian Riedel; Douwe Kiela | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | NeurIPS 2020; arXiv | 2020 | https://arxiv.org/abs/2005.11401; https://doi.org/10.48550/arXiv.2005.11401 | integrated in manuscript v0.3 | complete enough for normalized bibliography | likely ready after final normalization | RAG contrast only; does not imply KORA replaces retrieval-grounded generation. |
| `[R07]` | Apache Airflow DAG documentation | official docs | Apache Software Foundation / Apache Airflow project | Dags | Apache Airflow 3.2.1 documentation | date unavailable; accessed 2026-05-11 | https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html | integrated in manuscript v0.3 | official docs reference; access-date treatment needed | official docs/repos requiring style decision | Workflow/DAG vocabulary only; does not claim KORA is a general-purpose scheduler. |
| `[R08]` | Koster and Rahmann, Snakemake | paper / DOI | Johannes Koster; Sven Rahmann | Snakemake-a scalable bioinformatics workflow engine | Bioinformatics 28(19), 2520-2522 | 2012 | https://doi.org/10.1093/bioinformatics/bts480 | integrated in manuscript v0.3 | complete enough for normalized bibliography | likely ready after final normalization | Reproducible workflow background only. |
| `[R09]` | llama.cpp repository | official repo | ggml-org | llama.cpp: LLM inference in C/C++ | GitHub repository | date unavailable; accessed 2026-05-11 | https://github.com/ggml-org/llama.cpp | integrated in manuscript v0.3 | official repository reference; access-date treatment needed | official docs/repos requiring style decision | Future local-runtime context only; no current KORA integration evidence. |
| `[R10]` | ACM Artifact Review and Badging | official policy / artifact guidance | Association for Computing Machinery | Artifact Review and Badging - Current | ACM policy page | Version 1.1, 2020 | https://www.acm.org/publications/policies/artifact-review-and-badging-current | integrated in manuscript v0.3 | official policy reference; venue-style treatment pending | artifact/evaluation guidance requiring venue-style decision | Artifact-practice framing only; does not imply formal artifact approval. |
| `[R11]` | Yao et al., ReAct | paper / arXiv / DOI | Shunyu Yao; Jeffrey Zhao; Dian Yu; Nan Du; Izhak Shafran; Karthik Narasimhan; Yuan Cao | ReAct: Synergizing Reasoning and Acting in Language Models | ICLR 2023; arXiv | 2023 | https://arxiv.org/abs/2210.03629; https://doi.org/10.48550/arXiv.2210.03629 | integrated in manuscript v0.3 | complete enough for normalized bibliography | likely ready after final normalization | Agent/tool-use context only; no KORA outperformance claim. |
| `[R12]` | Schick et al., Toolformer | paper / arXiv / DOI | Timo Schick; Jane Dwivedi-Yu; Roberto Dessi; Roberta Raileanu; Maria Lomeli; Luke Zettlemoyer; Nicola Cancedda; Thomas Scialom | Toolformer: Language Models Can Teach Themselves to Use Tools | arXiv; venue/status pending normalization | 2023 | https://arxiv.org/abs/2302.04761; https://doi.org/10.48550/arXiv.2302.04761 | integrated in manuscript v0.3 | needs venue/status normalization | needs author/venue review | Model-centered tool-use context only. |
| `[R13]` | Gao et al., PAL | paper / arXiv / DOI | Luyu Gao; Aman Madaan; Shuyan Zhou; Uri Alon; Pengfei Liu; Yiming Yang; Jamie Callan; Graham Neubig | PAL: Program-aided Language Models | arXiv; venue/status pending normalization | 2022; revised 2023 | https://arxiv.org/abs/2211.10435; https://doi.org/10.48550/arXiv.2211.10435 | integrated in manuscript v0.3 | needs venue/status normalization | needs author/venue review | Program-aided workflow context only; not KORA model-call avoidance evidence. |
| `[R14]` | Bang, GPTCache | paper / ACL Anthology / DOI | Fu Bang | GPTCache: An Open-Source Semantic Cache for LLM Applications Enabling Faster Answers and Cost Savings | NLP-OSS 2023; Association for Computational Linguistics; pages 212-218 | 2023 | https://aclanthology.org/2023.nlposs-1.24/; https://doi.org/10.18653/v1/2023.nlposs-1.24 | tracker/audit-only; optional future integration | complete enough for normalized bibliography | likely ready after final normalization | Title includes cost-related wording; do not use as KORA production cost or real API-cost evidence. |
| `[R15]` | Ollama documentation and repository | official docs / official repo | Ollama | Ollama's documentation; Ollama official repository | Ollama documentation; GitHub repository | date unavailable; accessed 2026-05-11 | https://docs.ollama.com/; https://github.com/ollama/ollama | tracker/audit-only; optional future integration | official docs/repo reference; access-date treatment needed | official docs/repos requiring style decision | Future local-runtime context only; no current KORA Ollama integration evidence. |
| `[R16]` | Pineau et al., NeurIPS reproducibility report | paper / arXiv / DOI | Joelle Pineau; Philippe Vincent-Lamarre; Koustuv Sinha; Vincent Lariviere; Alina Beygelzimer; Florence d'Alche-Buc; Emily Fox; Hugo Larochelle | Improving Reproducibility in Machine Learning Research (A Report from the NeurIPS 2019 Reproducibility Program) | arXiv; report/status pending normalization | 2020 | https://arxiv.org/abs/2003.12206; https://doi.org/10.48550/arXiv.2003.12206 | tracker/audit-only; optional future integration | needs venue/status normalization | needs author/venue review | Reproducibility-program background only. |
| `[R17]` | USENIX NSDI artifact guidance | official venue guidance | USENIX Association | NSDI '26 Call for Artifacts | USENIX official conference page | 2025-2026 | https://www.usenix.org/conference/nsdi26/call-for-artifacts | tracker/audit-only; deferred until venue/artifact planning | official artifact guidance; venue-style treatment pending | artifact/evaluation guidance requiring venue-style decision | Does not imply KORA artifact approval. |
| `[R18]` | MLSys artifact evaluation guidance | official venue guidance | MLSys | Call for Artifact Evaluations | MLSys official conference page | 2023 | https://mlsys.org/Conferences/2023/CallForAE | tracker/audit-only; deferred until venue/artifact planning | official artifact guidance; venue-style treatment pending | artifact/evaluation guidance requiring venue-style decision | Does not imply KORA artifact approval. |
| `[R19]` | Srivastava et al., BIG-bench | benchmark suite paper / arXiv / DOI | Aarohi Srivastava et al. | Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models | Transactions on Machine Learning Research; arXiv | 2022 | https://arxiv.org/abs/2206.04615; https://doi.org/10.48550/arXiv.2206.04615 | tracker/audit-only methodology/background | needs author-list normalization | needs author/venue review | Benchmark-suite construction context only; not KORA production benchmark evidence. |
| `[R20]` | Liang et al., HELM | benchmark suite paper / arXiv / DOI | Percy Liang et al. | Holistic Evaluation of Language Models | Transactions on Machine Learning Research; arXiv | 2023 | https://arxiv.org/abs/2211.09110; https://doi.org/10.48550/arXiv.2211.09110 | tracker/audit-only methodology/background | needs author-list normalization | needs author/venue review | Holistic evaluation context only; does not imply KORA broad benchmark coverage. |
| `[R21]` | Jimenez et al., SWE-bench | benchmark paper / arXiv / DOI | Carlos E. Jimenez; John Yang; Alexander Wettig; Shunyu Yao; Kexin Pei; Ofir Press; Karthik Narasimhan | SWE-bench: Can Language Models Resolve Real-World GitHub Issues? | ICLR 2024; arXiv | 2024 | https://arxiv.org/abs/2310.06770; https://doi.org/10.48550/arXiv.2310.06770 | tracker/audit-only methodology/background | complete enough for normalized bibliography | likely ready after final normalization | Benchmark-construction example only; no KORA comparison against SWE-bench. |
| `[R22]` | Liu et al., AgentBench | benchmark paper / arXiv / DOI | Xiao Liu et al. | AgentBench: Evaluating LLMs as Agents | ICLR 2024; arXiv | 2024 | https://arxiv.org/abs/2308.03688; https://doi.org/10.48550/arXiv.2308.03688 | tracker/audit-only methodology/background | needs author-list normalization | needs author/venue review | Agent benchmark background only; no KORA outperformance claim. |
| `[R23]` | Kiela et al., Dynabench | benchmark paper / arXiv / DOI | Douwe Kiela et al. | Dynabench: Rethinking Benchmarking in NLP | NAACL 2021; arXiv | 2021 | https://arxiv.org/abs/2104.14337; https://doi.org/10.48550/arXiv.2104.14337 | tracker/audit-only methodology/background | needs author-list normalization | needs author/venue review | Dynamic benchmark context only; not KORA production evidence. |
| `[R24]` | Ribeiro et al., CheckList | benchmark/test-design paper / ACL Anthology / DOI | Marco Tulio Ribeiro; Tongshuang Wu; Carlos Guestrin; Sameer Singh | Beyond Accuracy: Behavioral Testing of NLP Models with CheckList | ACL 2020; pages 4902-4912 | 2020 | https://aclanthology.org/2020.acl-main.442/; https://doi.org/10.18653/v1/2020.acl-main.442 | tracker/audit-only methodology/background | complete enough for normalized bibliography | likely ready after final normalization | Behavior-oriented evaluation design context only; does not imply broad KORA behavioral testing. |

## BibTeX Readiness Summary

Likely ready after final normalization:

- `[R01]`, `[R06]`, `[R08]`, `[R11]`, `[R14]`, `[R21]`, `[R24]`

Needs author/venue review:

- `[R02]`, `[R05]`, `[R12]`, `[R13]`, `[R16]`, `[R19]`, `[R20]`, `[R22]`, `[R23]`

Official docs/repos requiring style decision:

- `[R03]`, `[R04]`, `[R07]`, `[R09]`, `[R15]`

Artifact/evaluation guidance requiring venue-style decision:

- `[R10]`, `[R17]`, `[R18]`

Not ready for BibTeX:

- Any reference whose author-list handling, venue/status, official-docs access-date treatment, or venue-guidance style remains unresolved.
- No BibTeX is generated in this document.

## Metadata Gap List

Missing or uncertain author/org:

- `[R02]`, `[R19]`, `[R20]`, `[R22]`, `[R23]`: author-list expansion or final `et al.` handling requires review before BibTeX.

Missing or uncertain venue/status:

- `[R02]`, `[R05]`, `[R12]`, `[R13]`, `[R16]`: arXiv or report status needs final venue/status normalization.
- `[R19]`, `[R20]`, `[R22]`, `[R23]`: author-list and venue/status details require final normalization before BibTeX.

Official docs date/access-date treatment:

- `[R03]`, `[R04]`, `[R07]`, `[R09]`, `[R15]`: official docs or repository entries need final organization-owner, entry-type, and access-date formatting.

DOI/URL issues:

- No missing source URL was identified in the tracker for `[R01]` through `[R24]`.
- DOI availability differs by source type. Official docs, repositories, and venue guidance pages use stable source URLs rather than DOI records.

Venue-specific formatting needs:

- `[R10]`, `[R17]`, `[R18]`: artifact policy or venue guidance pages need final venue-style treatment.
- Venue-specific conversion remains deferred for all records until target venue or report format is selected.

## Claim-Safety Note

The normalized bibliography does not change claim support.

- External references remain related-work, methodology, background, reproducibility, artifact-practice, or future-work support only.
- KORA's 80/100 result remains supported by KORA deterministic-heavy benchmark docs and evidence.
- These references do not support production cost reduction proof.
- These references do not support real API-cost reduction proof.
- These references do not support energy reduction evidence.
- These references do not support production benchmark proof.
- These references do not support broad workload superiority.
- Artifact guidance references do not imply formal artifact approval.

## Next Step

Next steps:

1. Resolve high-risk metadata gaps.
2. Prepare preliminary BibTeX only for records with complete verified fields.
3. Keep the paper not submission-ready until BibTeX, bibliography, and final claim audit are stable.
