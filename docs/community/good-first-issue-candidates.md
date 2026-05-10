# Good First Issue Candidates

## Purpose

These are candidate tasks for future GitHub issues. They are not active assignments until maintainers review and explicitly approve issue creation.

## Documentation Candidates

### Add an example output block for customer-support triage local validation

Goal: Show a short, claim-safe sample output from the local/no-network customer-support triage example.

Files likely touched: `docs/workloads/customer-support-triage.md`, `docs/benchmarks/local-validation-reviewer-packet.md`.

Acceptance criteria: The example uses synthetic counters only, does not include raw prompts or provider responses, and links to the reviewer packet.

Suggested labels: `good first issue`, `documentation`, `examples`, `validation`, `claim-safe`.

Estimated size: small.

### Improve glossary for validation counters

Goal: Clarify terms such as `baseline_model_calls`, `kora_model_calls`, `avoided_model_calls`, and `model_escalations`.

Files likely touched: `docs/telemetry-and-observability.md`, `docs/benchmarks/local-validation-reviewer-packet.md`.

Acceptance criteria: Each counter has a concise definition and the wording distinguishes local/no-network counters from production evidence.

Suggested labels: `good first issue`, `documentation`, `validation`, `claim-safe`.

Estimated size: small.

### Add a short FAQ entry explaining local no-network validation

Goal: Add a short public FAQ entry that explains why local validation does not require API keys or external providers.

Files likely touched: `docs/README.md`, `docs/benchmarks/local-validation-reviewer-packet.md`, or a future FAQ file.

Acceptance criteria: The entry states that examples use synthetic workloads and do not prove production cost reduction or real API-cost reduction.

Suggested labels: `good first issue`, `documentation`, `validation`, `claim-safe`.

Estimated size: small.

### Add README link to contributor pathway

Goal: Make the contributor pathway easy to find from the README.

Files likely touched: `README.md`.

Acceptance criteria: README gains a concise link without expanding marketing copy.

Suggested labels: `good first issue`, `documentation`.

Estimated size: small.

### Add docs note for generated report artifacts

Goal: Explain where generated Markdown reports should be written and when they should not be committed.

Files likely touched: `docs/benchmarks/local-validation-reviewer-packet.md`, `CONTRIBUTING.md`.

Acceptance criteria: The note recommends `/tmp` or another local path and warns against committing raw provider responses, secrets, or private data.

Suggested labels: `good first issue`, `documentation`, `validation`, `claim-safe`.

Estimated size: small.

### Improve claim-safe wording examples

Goal: Add more examples of allowed and not-allowed wording for benchmark and local validation claims.

Files likely touched: `docs/claims/kora-public-language-guide.md`, `docs/claims/kora-claim-registry.md`.

Acceptance criteria: New examples preserve the approved alpha claim and explicit non-claims.

Suggested labels: `documentation`, `claim-safe`, `help wanted`.

Estimated size: medium.

### Add troubleshooting entry for report path permissions

Goal: Help users resolve errors when `--report-md` points to a non-writable location.

Files likely touched: `docs/benchmarks/local-validation-reviewer-packet.md`, possibly example docs.

Acceptance criteria: The entry suggests a writable local path and does not add machine-local paths.

Suggested labels: `good first issue`, `documentation`, `validation`.

Estimated size: small.

### Add workload schema field explanations

Goal: Explain each field used by synthetic workload specs in plain language.

Files likely touched: `docs/workloads/customer-support-triage.md`, future workload docs.

Acceptance criteria: Field explanations cover route class, expected route, validation rule, privacy class, and expected response type.

Suggested labels: `documentation`, `workload`, `validation`.

Estimated size: medium.

## Test Candidates

### Add tests for report boundary language

Goal: Ensure generated validation reports keep explicit non-claim language.

Files likely touched: `tests/test_validation_report.py`, `tests/test_customer_support_triage_fake_validation.py`.

Acceptance criteria: Tests fail if reports drop the production, real API-cost, provider, or energy non-claims.

Suggested labels: `good first issue`, `tests`, `validation`, `claim-safe`.

Estimated size: small.

### Add tests for workload route class counts

Goal: Check that synthetic customer-support route class counts stay aligned with expected counters.

Files likely touched: `tests/test_customer_support_triage_workload.py`.

Acceptance criteria: Tests verify deterministic and model-required class totals.

Suggested labels: `tests`, `workload`, `validation`.

Estimated size: small.

### Add tests for adapter selector error messages

Goal: Confirm unsupported adapter choices fail clearly.

Files likely touched: `tests/test_model_call.py`, CLI-related tests.

Acceptance criteria: Tests cover invalid adapter names and clear error text.

Suggested labels: `tests`, `validation`.

Estimated size: small.

### Add tests for local runtime placeholder failure behavior

Goal: Ensure design-only runtime placeholders remain fail-closed.

Files likely touched: `tests/test_model_call.py`, `tests/test_customer_support_triage_fake_validation.py`.

Acceptance criteria: Tests prove no provider call is attempted and error messaging is explicit.

Suggested labels: `tests`, `validation`, `claim-safe`.

Estimated size: small.

### Add tests for README/doc link integrity if repo supports it

Goal: Catch broken relative links in public docs.

Files likely touched: new or existing docs test file, `pyproject.toml` only if a dependency-free approach is used.

Acceptance criteria: Test covers key Markdown links without adding heavy dependencies.

Suggested labels: `tests`, `documentation`, `help wanted`.

Estimated size: medium.

## Workload Candidates

### Draft RAG answer-routing synthetic workload spec

Goal: Define a sanitized synthetic workload for RAG answer-routing decisions.

Files likely touched: `docs/workloads/`.

Acceptance criteria: Spec separates deterministic retrieval checks from model-required answer generation and includes privacy boundaries.

Suggested labels: `workload`, `documentation`, `validation`, `discussion-needed`.

Estimated size: medium.

### Draft agent budget-guard synthetic workload spec

Goal: Define a synthetic workload for agent tasks with budget and escalation rules.

Files likely touched: `docs/workloads/`.

Acceptance criteria: Spec includes request classes, budget rules, validation expectations, and non-claim boundaries.

Suggested labels: `workload`, `documentation`, `validation`, `discussion-needed`.

Estimated size: medium.

### Expand customer-support triage workload to 100 synthetic requests

Goal: Extend the existing synthetic workload with broader coverage while keeping all data fake.

Files likely touched: `docs/workloads/customer-support-triage.md`, example fixtures if used.

Acceptance criteria: Adds balanced deterministic and model-required cases, with no private data or real identifiers.

Suggested labels: `workload`, `examples`, `validation`.

Estimated size: medium.

### Add validation rules for structured lookup routes

Goal: Make lookup placeholder validation more explicit.

Files likely touched: `docs/workloads/customer-support-triage.md`, tests if behavior exists.

Acceptance criteria: Rules explain expected lookup placeholders without implying real backend integration.

Suggested labels: `workload`, `documentation`, `validation`.

Estimated size: small.

### Add synthetic multilingual support triage samples without private data

Goal: Draft synthetic multilingual samples for future routing validation.

Files likely touched: `docs/workloads/customer-support-triage.md` or a new workload note.

Acceptance criteria: Samples use fake content only and avoid claims about broad language coverage.

Suggested labels: `workload`, `examples`, `discussion-needed`, `claim-safe`.

Estimated size: medium.

## KORA Studio Candidate Issues

Use the [KORA Studio planning docs](../kora-studio/README.md) as the starting point for these candidates. The current planning packet includes the [v0.1 product spec](../kora-studio/kora-studio-v0-1-product-spec.md), [MVP user flow](../kora-studio/kora-studio-mvp-user-flow.md), [architecture plan](../kora-studio/kora-studio-architecture.md), [KORA Boost copy system](../kora-studio/kora-boost-copy-system.md), and [UI composition guide](../kora-studio/kora-studio-ui-composition.md).

Use the [implementation breakdown](../kora-studio/kora-studio-implementation-breakdown.md), [report viewer requirements](../kora-studio/report-viewer-requirements.md), [dashboard counter schema](../kora-studio/dashboard-counter-schema.md), and [fixtures plan](../kora-studio/fixtures-plan.md) to split future KORA Studio work into small reviewed issues. Do not create issues until maintainers explicitly approve them.

### Draft KORA Studio MVP user flow

Goal: Describe a small user flow for inspecting local validation reports.

Files likely touched: `docs/community/` or future Studio planning docs.

Acceptance criteria: Flow is clearly future planning and does not claim a shipped product.

Suggested labels: `kora-studio`, `documentation`, `discussion-needed`.

Estimated size: medium.

### Define validation report viewer requirements

Goal: List fields and states a report viewer should show.

Files likely touched: future Studio planning docs.

Acceptance criteria: Requirements focus on local reports, aggregate counters, safety boundaries, and no raw provider responses.

Suggested labels: `kora-studio`, `validation`, `documentation`.

Estimated size: medium.

### Create static mockup for local validation report viewer

Goal: Create a static, non-runtime mockup for a local report viewer.

Files likely touched: future docs or examples area after maintainer approval.

Acceptance criteria: Mockup uses sample synthetic data only and does not add app dependencies.

Suggested labels: `kora-studio`, `examples`, `help wanted`.

Estimated size: medium.

### Add sample JSON fixture for Studio dashboard

Goal: Add a small synthetic fixture for future dashboard planning.

Files likely touched: future fixture location after maintainer approval.

Acceptance criteria: Fixture includes aggregate counters only, no raw prompts, no private data, and no provider responses.

Suggested labels: `kora-studio`, `validation`, `examples`.

Estimated size: small.

### Define dashboard counter cards

Goal: Specify counter cards for total requests, baseline model calls, KORA model calls, and avoided model-call events.

Files likely touched: future Studio planning docs.

Acceptance criteria: Text distinguishes local/no-network events from production evidence.

Suggested labels: `kora-studio`, `documentation`, `claim-safe`.

Estimated size: small.

### Define workload selector UI

Goal: Describe a future UI for selecting synthetic workload reports.

Files likely touched: future Studio planning docs.

Acceptance criteria: Selector is scoped to local files or fixtures and does not imply provider integration.

Suggested labels: `kora-studio`, `documentation`, `discussion-needed`.

Estimated size: small.

### Define report export/download behavior

Goal: Specify safe export behavior for generated reports.

Files likely touched: future Studio planning docs.

Acceptance criteria: Export guidance warns against secrets, private data, raw provider responses, and unsupported claims.

Suggested labels: `kora-studio`, `validation`, `documentation`, `claim-safe`.

Estimated size: medium.

### Create first static report packet viewer prototype

Goal: Build a local static prototype for reading a sample report packet after maintainer approval.

Files likely touched: future prototype directory.

Acceptance criteria: Prototype uses synthetic sample data only, has no real provider integration, and avoids new runtime dependencies unless approved.

Suggested labels: `kora-studio`, `examples`, `help wanted`, `discussion-needed`.

Estimated size: medium.

## Labels To Use Later

- `good first issue`
- `documentation`
- `tests`
- `examples`
- `validation`
- `workload`
- `kora-studio`
- `help wanted`
- `discussion-needed`
- `claim-safe`

## Issue Creation Note

These candidates should be converted into real GitHub issues only after maintainer review and explicit approval.
