# Missing Evidence Checklist

## Needed Before First Draft

- Confirm latest benchmark command and output.
- Capture deterministic-heavy benchmark result in a reviewer-safe summary.
- Capture customer-support local validation result.
- Confirm all commands pass on a clean checkout.
- Identify exact tables to include.

## Nice To Have Before Draft

- Expanded 100-request customer-support workload.
- Local model runtime validation, for example Ollama.
- p50/p95 latency for deterministic vs model-required routes.
- Repeated runs.
- Qualitative examples of deterministic route classes.

## Draft v0 Next Evidence Priorities

- Clean command transcript.
- Latency p50/p95.
- Expanded 100-request customer-support workload.
- Local model runtime validation.
- Repeated runs.

## Priority after manuscript v0.1

- Clean command transcript.
- Latency p50/p95.
- Expanded 100-request customer-support workload.
- Local model runtime validation.
- Repeated runs.
- Figure generation.
- Bibliography/references.
- Manuscript v0.2 reference-integration review.
- Citation audit v0.1 review.
- Final verified bibliography.

## References and figures needed

- Additional verified related work references.
- Final citation format and bibliography normalization.
- Final citation audit review.
- Verified BibTeX entries if a BibTeX workflow is selected.
- Figure 1 architecture.
- Figure 2 execution-control layer.
- Figure 3 benchmark result.
- Figure 4 customer-support routing.
- Table finalization.

## Not Needed For First Paper

- OpenAI/Claude API cost validation.
- Production traffic.
- Energy measurement.
- Hosted KORA Studio.
- Real customer data.

## References and bibliography status

First verified reference pass:

- 10 references partially collected across the target related-work categories.
- Verified references recorded in the reference tracker.
- Manuscript v0.2 created with verified references integrated as preliminary citation labels.
- Citation audit v0.1 created.
- Final citation format, final bibliography, and BibTeX still pending.

Additional reference verification pass 2:

- 8 additional references verified and recorded as `[R11]` through `[R18]`.
- Agent/tool-use, semantic caching, local-runtime, reproducibility-program, and venue artifact-guidance coverage improved.
- Manuscript integration for `[R11]` through `[R18]` is still pending.
- Final citation style, final bibliography, and BibTeX still pending.

Additional reference categories still pending:

- Synthetic workload and benchmark-construction references.
- Optional additional semantic caching references if the manuscript discusses caching in more detail.
- Target-venue-specific citation and artifact guidance after venue selection.

## Follow-Up Papers / Technical Reports

- OpenAI/Claude API cost reduction technical report.
- Energy/sustainability paper.
- Production-like application workload report.
