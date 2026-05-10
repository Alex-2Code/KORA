# KORA Studio Fixtures Plan

## Purpose

This plan defines safe fixture types for future KORA Studio prototypes before runtime code exists.

Fixtures should use synthetic, aggregate, local-only data and should not imply that KORA Studio is implemented.

## Sample Fixture Types

- local validation summary fixture
- customer-support summary fixture
- Markdown report fixture
- project/chat mock fixture
- execution trace mock fixture
- dashboard counter fixture

## Local Validation Summary Fixture

This fixture should mirror the JSON summary shape emitted by:

```bash
python3 -m kora run real_model_call_validation_fake -- --offline
```

It should include aggregate fields only, such as total requests, baseline model calls, KORA model calls, avoided model calls, validation counts, adapter labels, and no-network status.

## Customer-Support Summary Fixture

This fixture should mirror the customer-support triage local validation example:

```bash
python3 -m kora run customer_support_triage_fake_validation -- --offline
```

It should use synthetic workload metadata and aggregate counters only.

## Markdown Report Fixture

A future Markdown report fixture may be derived from:

```bash
python3 -m kora run customer_support_triage_fake_validation -- --offline --report-md /tmp/kora_customer_support_validation.md
```

Generated reports should remain local by default. Commit only a reviewed synthetic fixture if maintainers explicitly choose one for public docs or tests.

## Project/Chat Mock Fixture

Project/chat mock data should include:

- fake project names
- placeholder messages
- Standard Mode / KORA Boost mode state
- execution trace placeholders
- local runtime status placeholders

Do not include private user conversations, raw prompts from real users, or provider responses.

## Data Safety Rules

- no private data
- no real customer data
- no proprietary datasets
- no raw provider responses
- no secrets or API keys
- no private campaign material
- no generated reports committed by default

## Future Fixture Path Suggestions

Potential future fixture paths:

- `docs/kora-studio/fixtures/`
- `examples/kora_studio_static_mock/fixtures/`
- `tests/fixtures/kora_studio/`

Choose the path in a future implementation task based on whether the fixture is documentation-only, example-facing, or test-only.
