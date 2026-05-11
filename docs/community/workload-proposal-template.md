# Workload Proposal Template

## Purpose

This template helps developers propose workloads for KORA validation.

Good workload proposals explain where deterministic routing, validation rules, escalation rules, or budget controls may avoid unnecessary model-call events while preserving correctness and safety.

For route guidance, see [Contact and Discussion Routes](contact-and-discussion-routes.md). Workload proposals can use the issue template now; GitHub Discussions are the recommended route once enabled.

## Before You Submit

Use synthetic or sanitized data only.

Do not include:

- secrets
- API keys
- private user/customer data
- proprietary datasets
- raw provider responses
- private credentials
- production logs

## Proposal Fields

- Workload name
- Workload type
- Current model/API/local runtime used, if any
- Approximate request volume
- Deterministic/repetitive request types
- Model-required request types
- Validation rules
- Expected outputs/properties
- Privacy class
- Can results be public?
- Contact or GitHub handle, optional

## Example Proposal

```text
Workload name:
Synthetic customer-support triage

Workload type:
Support request routing and response validation

Current model/API/local runtime used, if any:
None for the proposal. Local/no-network validation is preferred for the first pass.

Approximate request volume:
12 synthetic requests for the first draft; 100 synthetic requests for a later expanded draft.

Deterministic/repetitive request types:
- Password reset instructions
- Refund policy link requests
- Shipping status instructions
- Account email change instructions
- Standard return window questions
- Order status lookup placeholders

Model-required request types:
- Ambiguous complaint
- Multi-intent request
- Unusual policy edge case
- Sensitive escalation

Validation rules:
- required_link_present
- policy_value_matches
- lookup_placeholder_present
- escalation_reason_present
- no_private_data_emitted

Expected outputs/properties:
- Deterministic FAQ requests route to known handlers.
- Policy requests return approved policy keys.
- Lookup requests use placeholder routes only.
- Ambiguous or sensitive requests include an escalation reason.
- Aggregate counters include baseline model-call events, KORA-routed model-call events, and avoided model-call events.

Privacy class:
synthetic

Can results be public?
Yes, if the workload remains synthetic and the report includes only aggregate counters and claim-safe boundary language.

Contact or GitHub handle, optional:
GitHub handle only; no private contact details required.
```

## Synthetic RAG Routing Example

```text
Workload name:
Synthetic policy-answer routing

Workload type:
RAG answer routing and validation

Current model/API/local runtime used, if any:
None for the proposal. The first pass should use local synthetic fixtures only.

Approximate request volume:
20 synthetic questions split between source-backed answers and ambiguous queries.

Deterministic/repetitive request types:
- Questions that match one approved source paragraph exactly.
- Questions that ask for a known policy value already present in a source.
- Questions that can be answered by returning a source title and section key.

Model-required request types:
- Ambiguous questions that match multiple source sections.
- Questions with missing source coverage.
- Questions that require a short explanation of why escalation is needed.

Validation rules:
- source_present
- source_section_matches
- answer_uses_approved_source
- escalation_reason_present
- no_private_data_emitted

Expected outputs/properties:
- Source-backed questions include the selected source key.
- Ambiguous or unsupported questions include an escalation reason.
- Aggregate counters separate deterministic source-backed routes from
  model-required routes.

Privacy class:
synthetic

Can results be public?
Yes, if all source snippets and questions are synthetic and reports contain only
aggregate counters and claim-safe language.
```

## Claim Boundary

Accepted workloads do not automatically imply production validation, production cost reduction, real API-cost reduction, broad workload superiority, or energy reduction.

KORA's local no-network validation examples show that KORA can measure avoided model-call events in synthetic workloads. Production or provider-specific claims require separate reviewed evidence and explicit approval.
