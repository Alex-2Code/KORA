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

## Reference Categories

### 1. LLM serving and inference systems

Why this category matters:

KORA discusses reducing model invocations in deterministic-heavy workloads, so the paper needs background on systems that optimize serving, inference throughput, scheduling, batching, and runtime efficiency.

What kind of reference is needed:

Peer-reviewed systems papers, official project papers, official technical reports, or stable project documentation for LLM serving and inference systems.

Target count:

3-5 verified references.

Verification status:

Pending.

### 2. Agent/tool routing and orchestration

Why this category matters:

KORA routes work through execution-control paths before inference. The paper should distinguish deterministic-first execution control from agent loops, tool calling, planners, and model-centered orchestration.

What kind of reference is needed:

Verified papers, official docs, or stable technical reports covering agent frameworks, tool routing, graph-based agents, or orchestration patterns.

Target count:

2-4 verified references.

Verification status:

Pending.

### 3. Deterministic/programmatic AI workflows

Why this category matters:

KORA relies on deterministic routes, structured handlers, policy checks, and validation boundaries when model inference is not required.

What kind of reference is needed:

References on programmatic control, typed or structured AI workflows, validation-centered execution, constrained generation, or deterministic components around model systems.

Target count:

2-4 verified references.

Verification status:

Pending.

### 4. Caching and retrieval-augmented generation

Why this category matters:

KORA must be positioned clearly against caching and retrieval-augmented generation. Caching can reuse previous results, and RAG can ground generation, but KORA's contribution is execution-control routing before deciding whether inference is needed.

What kind of reference is needed:

Foundational RAG papers or surveys, plus verified references for caching or semantic-cache systems if they are directly relevant.

Target count:

3-5 verified references.

Verification status:

Pending.

### 5. Workflow orchestration / DAG systems

Why this category matters:

KORA uses task paths and execution-control concepts that are adjacent to workflow orchestration and DAG execution, while applying them to model-call boundaries and validation counters.

What kind of reference is needed:

Official docs, project papers, or technical reports for workflow orchestration, task graphs, DAG execution, or distributed workflow systems.

Target count:

2-4 verified references.

Verification status:

Pending.

### 6. Benchmarking and reproducibility

Why this category matters:

The first KORA paper depends on reproducible deterministic-heavy benchmark evidence and local/no-network validation language. It needs references that support careful benchmark design and transparent reproduction.

What kind of reference is needed:

References on benchmark methodology, reproducibility, synthetic workloads, artifact reporting, and evaluation transparency.

Target count:

2-4 verified references.

Verification status:

Pending.

### 7. Local model runtime systems

Why this category matters:

Local model runtime validation is future work. The paper should cite local runtime systems only after verifying official sources and only as context, not as current KORA evidence.

What kind of reference is needed:

Official docs, project papers, or stable technical reports for local model runtime systems.

Target count:

1-3 verified references.

Verification status:

Pending.

### 8. Systems papers with artifact evaluation practices

Why this category matters:

KORA's paper should follow systems-style evidence discipline: clear claims, reproducible commands, artifact boundaries, and explicit limitations.

What kind of reference is needed:

Artifact evaluation guidelines, systems conference artifact practices, or papers that model clear reproduction and evaluation reporting.

Target count:

2-4 verified references.

Verification status:

Pending.

## Candidate Reference Slots

| Slot | Category | Candidate / target | Source type | Why needed | Verification status | Notes |
|---|---|---|---|---|---|---|
| R01 | LLM serving and inference systems | To verify: vLLM paper or official technical report | Paper or official technical report | Background on LLM serving efficiency and inference systems | Pending | Do not cite until title, authors, year, and source are verified. |
| R02 | LLM serving and inference systems | To verify: LLM serving scheduler or batching system paper | Paper | Background for serving optimization context | Pending | Avoid implying KORA outperforms serving systems. |
| R03 | LLM serving and inference systems | To verify: official inference runtime documentation | Official docs | Stable project context for inference runtime behavior | Pending | Use only if docs are stable and relevant. |
| R04 | Agent/tool routing and orchestration | To verify: LangChain/LangGraph routing docs or paper if applicable | Official docs or paper | Context for tool routing and graph-based agent execution | Pending | Position KORA as deterministic-first execution control, not a general agent framework. |
| R05 | Agent/tool routing and orchestration | To verify: agent tool-use or planner reference | Paper or technical report | Context for model-centered tool routing | Pending | Do not overstate similarity. |
| R06 | Deterministic/programmatic AI workflows | To verify: structured output or programmatic AI workflow reference | Paper, docs, or technical report | Support discussion of structured and deterministic work around model systems | Pending | Must not support unsupported production claims. |
| R07 | Deterministic/programmatic AI workflows | To verify: validation or guardrail workflow reference | Paper, docs, or technical report | Context for validation boundaries | Pending | Verify scope before use. |
| R08 | Caching and retrieval-augmented generation | To verify: RAG survey or foundational RAG paper | Paper or survey | Establish RAG background and contrast with KORA | Pending | Avoid claiming KORA replaces RAG. |
| R09 | Caching and retrieval-augmented generation | To verify: semantic caching or LLM cache reference | Paper, docs, or technical report | Distinguish cache reuse from pre-inference execution control | Pending | Use only if relevant to model-call avoidance discussion. |
| R10 | Workflow orchestration / DAG systems | To verify: Ray / workflow orchestration system paper or docs | Paper or official docs | Context for task graphs, orchestration, and distributed execution | Pending | Do not claim KORA is a distributed workflow engine. |
| R11 | Workflow orchestration / DAG systems | To verify: DAG workflow system reference | Paper or official docs | Background for explicit execution paths | Pending | Verify current project/source status. |
| R12 | Benchmarking and reproducibility | To verify: benchmark reproducibility reference | Paper, guideline, or technical report | Support reproducible evaluation framing | Pending | Use for methodology, not as evidence of KORA results. |
| R13 | Benchmarking and reproducibility | To verify: synthetic workload evaluation reference | Paper or technical report | Context for local/no-network synthetic workload design | Pending | Keep claim language narrow. |
| R14 | Local model runtime systems | To verify: local model runtime official docs or technical report | Official docs or technical report | Context for future local model validation | Pending | Future-work context only unless evidence exists. |
| R15 | Systems papers with artifact evaluation practices | To verify: artifact evaluation / reproducibility references | Guideline, paper, or official docs | Support artifact and reproduction discipline | Pending | Prefer official artifact-evaluation guidance. |

## Next Verification Procedure

1. Search official sources first.
2. Verify title, authors, year, venue or publisher, and stable source URL or DOI.
3. Confirm relevance to the specific paper section before citation.
4. Add a citation only after verification.
5. Add BibTeX later, after the citation metadata has been checked.
6. Update the manuscript only after references are verified.
