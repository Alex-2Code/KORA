# KORA First Paper Related Work Map

## Purpose

This document maps reference categories needed before submission. It does not add citations yet. References should be collected, verified, and added later with accurate BibTeX or venue metadata.

## Related Work Categories

### LLM Serving and Inference Systems

Purpose:

Cite systems that optimize serving, inference throughput, scheduling, batching, and runtime efficiency.

Use this category as background for model-serving efficiency. Avoid claiming that KORA outperforms these systems unless direct evidence is collected later.

### LLM Agents and Tool Routing

Purpose:

Cite work on routing tasks through tools, planners, agent loops, or execution policies.

Use this category to position KORA near tool-using systems while emphasizing that the paper focuses on deterministic-first execution control before model invocation.

### Programmatic / Deterministic AI Workflows

Purpose:

Cite work where deterministic code, typed interfaces, policy checks, structured execution, or programmatic control complements model inference.

Use this category to explain why structured work should not always begin with model inference.

### Caching and Retrieval-Augmented Generation

Purpose:

Explain how KORA differs from caching and RAG:

- KORA is not just cache lookup.
- KORA controls execution path before model invocation.
- KORA includes validation, telemetry, and model escalation boundaries.

Caching and RAG may reduce repeated work or ground generation, but KORA's paper should frame its contribution as execution-control routing before inference.

### Workflow Orchestration and DAG Execution

Purpose:

Cite task graph, workflow, and DAG execution systems as background, while positioning KORA for AI execution control.

Use this category to explain how KORA borrows the discipline of explicit execution paths while adapting it to model-call boundaries and validation counters.

### Evaluation and Reproducibility

Purpose:

Cite work on reproducible benchmarks, synthetic workloads, artifact reporting, and transparent evaluation.

Use this category to justify local/no-network validation, aggregate counter reporting, and clear claim boundaries.

## Reference Collection TODO

- Collect 15-25 references.
- Prefer peer-reviewed or official project papers/docs.
- Avoid unsupported comparisons.
- Add BibTeX later.
- Verify all citations before submission.
- Do not add fake citations.
- Do not invent paper titles.
- Do not cite sources without verifying later.
