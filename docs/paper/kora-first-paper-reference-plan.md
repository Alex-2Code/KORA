# KORA First Paper Reference Plan

## Purpose

This document defines reference targets and verification status for the first KORA paper. It is a planning scaffold for collecting references without adding unverified citations, invented BibTeX entries, or unsupported claims.

## Reference Rules

- Do not add fake citations.
- Verify every paper or project before citing it.
- Prefer peer-reviewed papers, official project papers, official documentation, or stable public technical reports.
- Record source type for each candidate reference.
- Record verification status for each candidate reference.
- Do not overstate similarity, difference, or superiority.

## Progress Notes

### Verification Pass 1

Completed on 2026-05-11.

- Verified references collected: 10.
- Categories covered: LLM serving and inference systems, agent/tool routing and orchestration, deterministic/programmatic AI workflows, caching and retrieval-augmented generation, workflow orchestration / DAG systems, benchmarking and reproducibility, local model runtime systems, and systems artifact evaluation practices.
- Remaining gaps: additional agent/tool-use references, semantic-cache references, reproducibility-methodology references, official Ollama or other local-runtime references, and target-venue artifact evaluation guidance.
- Bibliography status: BibTeX not added in this pass; final bibliography remains pending.
- Manuscript status: no manuscript citation integration in this pass.

### Manuscript Integration Pass 1

Completed on 2026-05-11.

- Manuscript v0.2 created.
- Verified references from pass 1 integrated into v0.2 as preliminary citation labels.
- Preliminary references section added to the manuscript using verified tracker entries only.
- Final citation style, final bibliography normalization, and BibTeX remain pending.
- No fake citations or unsupported production, API-cost, energy, production-validation, broad superiority, or cited-system superiority claims added.

### Citation Audit v0.1

Completed on 2026-05-11.

- Citation audit v0.1 created.
- References [R01] through [R10] checked for manuscript use, References-section presence, tracker status, and source traceability.
- Claim-support mapping added for related-work context and the KORA 80/100 benchmark result.
- Bibliography normalization and citation style selection remain pending.

### Verification Pass 2

Completed on 2026-05-11.

- Additional verified references collected: 8.
- New verified labels: `[R11]` through `[R18]`.
- Categories covered: agent/tool-use and agentic workflows, program-aided language-model workflows, semantic caching, local model runtime systems, reproducibility programs/checklists, and venue-specific artifact evaluation guidance.
- Manuscript integration deferred; references are tracker/audit entries only until a later manuscript pass.
- Remaining gaps: synthetic workload and benchmark-construction references, optional additional semantic-cache references, and final target-venue citation/artifact guidance.
- Bibliography status: BibTeX not added in this pass; final citation style and bibliography normalization remain pending.

### Manuscript v0.3 Reference Integration Plan

Completed on 2026-05-11.

- Manuscript v0.3 reference integration plan created.
- References `[R11]` through `[R18]` mapped to candidate manuscript sections and integration decisions.
- Selected references will be integrated later based on the plan.
- Remaining gaps: synthetic workload / benchmark-construction references and final target-venue citation/artifact guidance.
- At plan creation time, manuscript v0.3 had not yet been created.
- BibTeX and final citation style remain pending.

### Manuscript Integration Pass 2

Completed on 2026-05-11.

- Manuscript v0.3 created.
- References `[R11]`, `[R12]`, and `[R13]` integrated into v0.3 as agent/tool-use and programmatic workflow background.
- References `[R14]` through `[R18]` remain optional, deferred, or tracker/audit-only according to the v0.3 integration plan.
- Remaining gaps: synthetic workload / benchmark-construction references and final target-venue citation/artifact guidance.
- BibTeX and final citation style remain pending.

## Reference Categories

### 1. LLM serving and inference systems

Why this category matters:

KORA discusses reducing model invocations in deterministic-heavy workloads, so the paper needs background on systems that optimize serving, inference throughput, scheduling, batching, and runtime efficiency.

What kind of reference is needed:

Peer-reviewed systems papers, official project papers, official technical reports, or stable project documentation for LLM serving and inference systems.

Target count:

3-5 verified references.

Verification status:

Partially verified. See [KORA first paper reference tracker](kora-first-paper-reference-tracker.md).

### 2. Agent/tool routing and orchestration

Why this category matters:

KORA routes work through execution-control paths before inference. The paper should distinguish deterministic-first execution control from agent loops, tool calling, planners, and model-centered orchestration.

What kind of reference is needed:

Verified papers, official docs, or stable technical reports covering agent frameworks, tool routing, graph-based agents, or orchestration patterns.

Target count:

2-4 verified references.

Verification status:

Partially verified. See [KORA first paper reference tracker](kora-first-paper-reference-tracker.md).

### 3. Deterministic/programmatic AI workflows

Why this category matters:

KORA relies on deterministic routes, structured handlers, policy checks, and validation boundaries when model inference is not required.

What kind of reference is needed:

References on programmatic control, typed or structured AI workflows, validation-centered execution, constrained generation, or deterministic components around model systems.

Target count:

2-4 verified references.

Verification status:

Partially verified. See [KORA first paper reference tracker](kora-first-paper-reference-tracker.md).

### 4. Caching and retrieval-augmented generation

Why this category matters:

KORA must be positioned clearly against caching and retrieval-augmented generation. Caching can reuse previous results, and RAG can ground generation, but KORA's contribution is execution-control routing before deciding whether inference is needed.

What kind of reference is needed:

Foundational RAG papers or surveys, plus verified references for caching or semantic-cache systems if they are directly relevant.

Target count:

3-5 verified references.

Verification status:

Partially verified. See [KORA first paper reference tracker](kora-first-paper-reference-tracker.md).

### 5. Workflow orchestration / DAG systems

Why this category matters:

KORA uses task paths and execution-control concepts that are adjacent to workflow orchestration and DAG execution, while applying them to model-call boundaries and validation counters.

What kind of reference is needed:

Official docs, project papers, or technical reports for workflow orchestration, task graphs, DAG execution, or distributed workflow systems.

Target count:

2-4 verified references.

Verification status:

Partially verified. See [KORA first paper reference tracker](kora-first-paper-reference-tracker.md).

### 6. Benchmarking and reproducibility

Why this category matters:

The first KORA paper depends on reproducible deterministic-heavy benchmark evidence and local/no-network validation language. It needs references that support careful benchmark design and transparent reproduction.

What kind of reference is needed:

References on benchmark methodology, reproducibility, synthetic workloads, artifact reporting, and evaluation transparency.

Target count:

2-4 verified references.

Verification status:

Partially verified. See [KORA first paper reference tracker](kora-first-paper-reference-tracker.md).

### 7. Local model runtime systems

Why this category matters:

Local model runtime validation is future work. The paper should cite local runtime systems only after verifying official sources and only as context, not as current KORA evidence.

What kind of reference is needed:

Official docs, project papers, or stable technical reports for local model runtime systems.

Target count:

1-3 verified references.

Verification status:

Partially verified. See [KORA first paper reference tracker](kora-first-paper-reference-tracker.md).

### 8. Systems papers with artifact evaluation practices

Why this category matters:

KORA's paper should follow systems-style evidence discipline: clear claims, reproducible commands, artifact boundaries, and explicit limitations.

What kind of reference is needed:

Artifact evaluation guidelines, systems conference artifact practices, or papers that model clear reproduction and evaluation reporting.

Target count:

2-4 verified references.

Verification status:

Partially verified. See [KORA first paper reference tracker](kora-first-paper-reference-tracker.md).

## Candidate Reference Slots

| Slot | Category | Candidate / target | Source type | Why needed | Verification status | Notes |
|---|---|---|---|---|---|---|
| R01 | LLM serving and inference systems | vLLM / PagedAttention paper | Paper | Background on LLM serving efficiency and inference systems | Verified in pass 1 | See tracker for verified citation and source URL. |
| R02 | LLM serving and inference systems | MLPerf Inference Benchmark | Paper | Background for serving benchmark methodology and comparability | Verified in pass 1 | See tracker for verified citation and source URL. |
| R03 | LLM serving and inference systems | ONNX Runtime official documentation | Official docs | Stable project context for inference runtime behavior | Verified in pass 1 | Use only as runtime background; do not imply current KORA integration. |
| R04 | Agent/tool routing and orchestration | LangGraph official documentation | Official docs | Context for graph-based agent execution | Verified in pass 1 | Position KORA as deterministic-first execution control, not a general agent framework. |
| R05 | Deterministic/programmatic AI workflows | DSPy paper | Paper | Support discussion of programmatic LM workflows | Verified in pass 1 | Avoid presenting DSPy as deterministic-first model-call avoidance. |
| R06 | Caching and retrieval-augmented generation | RAG foundational paper | Paper | Establish RAG background and contrast with KORA | Verified in pass 1 | Avoid claiming KORA replaces RAG. |
| R07 | Workflow orchestration / DAG systems | Apache Airflow DAG docs | Official docs | Background for explicit execution paths and workflow vocabulary | Verified in pass 1 | Do not claim KORA is a general-purpose workflow scheduler. |
| R08 | Workflow orchestration / DAG systems | Snakemake workflow engine paper | Paper / DOI-backed metadata | Background for reproducible workflow systems | Verified in pass 1 | Use as workflow/reproducible-pipeline context only. |
| R09 | Local model runtime systems | llama.cpp official repository | Official repository | Context for future local model runtime work | Verified in pass 1 | Future-work context only unless KORA local runtime evidence exists. |
| R10 | Systems papers with artifact evaluation practices | ACM Artifact Review and Badging | Official policy | Support artifact and reproduction discipline | Verified in pass 1 | Use for artifact-practice framing, not as validation of KORA results. |
| R11 | Agent/tool routing and orchestration | ReAct | Paper | Context for reasoning/action and tool-use patterns | Verified in pass 2 | Use as agent/tool-use background only. |
| R12 | Agent/tool routing and orchestration | Toolformer | Paper | Context for model-centered API/tool-use training | Verified in pass 2 | Do not imply KORA uses Toolformer-style training. |
| R13 | Deterministic/programmatic AI workflows | PAL | Paper | Context for program-aided model workflows | Verified in pass 2 | Do not present as KORA model-call avoidance evidence. |
| R14 | Caching and retrieval-augmented generation | GPTCache | Paper / ACL Anthology | Distinguish semantic cache reuse from pre-inference execution control | Verified in pass 2 | Do not use to support KORA production cost or API-cost claims. |
| R15 | Local model runtime systems | Ollama official docs and repository | Official docs / repository | Context for future local model validation | Verified in pass 2 | Future-work context only unless KORA Ollama evidence exists. |
| R16 | Benchmarking and reproducibility | NeurIPS reproducibility program report | Paper | Context for reproducibility programs and checklist discipline | Verified in pass 2 | Do not imply KORA has venue reproducibility approval. |
| R17 | Systems papers with artifact evaluation practices | USENIX NSDI artifact guidance | Official venue guidance | Support artifact and reproduction discipline | Verified in pass 2 | Does not imply KORA artifact approval. |
| R18 | Systems papers with artifact evaluation practices | MLSys artifact evaluation guidance | Official venue guidance | Support ML/systems artifact appendix expectations | Verified in pass 2 | Does not imply KORA artifact approval. |
| R19 | Benchmarking and reproducibility | Synthetic workload evaluation reference | Paper or technical report | Context for local/no-network synthetic workload design | Pending | Keep claim language narrow. |

## Next Verification Procedure

1. Search official sources first.
2. Verify title, authors, year, venue or publisher, and stable source URL or DOI.
3. Confirm relevance to the specific paper section before citation.
4. Add a citation only after verification.
5. Add BibTeX later, after the citation metadata has been checked.
6. Update the manuscript only after references are verified.
