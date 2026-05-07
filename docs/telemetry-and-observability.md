# Telemetry and Observability

KORA is a structural system.

Structure without observability degrades into assumption.
<br>Telemetry in KORA is not optional instrumentation.

It is a structural requirement.

---

## 1. Purpose

Observability enables:

- Cost transparency
- Latency profiling
- Decomposition effectiveness measurement
- Budget enforcement auditing
- Experimental falsifiability

Without telemetry, structural claims cannot be verified.

---

## 2. Telemetry Model

Each Task emits structured telemetry events.

Core event lifecycle:

```mermaid
flowchart TD
    A[Task Created]
    A --> B[Execution Started]
    B --> C[Execution Completed]
    C --> D[Validation Result]
    D --> E[Aggregation]
```

<br>Each stage produces structured log entries.

---

## 3. Task-Level Metrics

Each task must record:

| Metric | Description |
|---------|-------------|
| task_id | Unique task identifier |
| task_type | deterministic, model, aggregation |
| start_time | Execution start timestamp |
| end_time | Execution end timestamp |
| duration_ms | Execution duration |
| model_used | Model backend if applicable |
| tokens_in | Input tokens consumed |
| tokens_out | Output tokens generated |
| retries | Retry count |
| validation_status | success or failure |

Telemetry is per-task, not per-request only.
<br>Atomic observability preserves structure.

---

## 4. Request-Level Metrics

Aggregated across entire task graph:

| Metric | Description |
|---------|-------------|
| total_tasks | Number of tasks executed |
| model_invocations | Count of model tasks |
| deterministic_tasks | Count of deterministic tasks |
| total_tokens | Sum of tokens consumed |
| total_latency_ms | End-to-end latency |
| total_retries | Total retries across graph |
| failure_count | Number of task failures |

Request-level metrics support break-even analysis.

---

## 5. Cost Accounting Model

Total request cost is computed as:

C_total = Σ(model_token_cost) + Σ(structural_overhead)

Where:

model_token_cost = tokens_in + tokens_out multiplied by pricing model.

Structural overhead includes:

- DAG validation cost
- Schema validation cost
- Deterministic execution cost

Cost must be decomposable per task.

---

## 6. Latency Profiling

Latency is decomposed into:

| Component | Description |
|-----------|-------------|
| T_construct | Task construction time |
| T_dag | DAG validation time |
| T_det | Deterministic execution time |
| T_model | Model invocation time |
| T_validation | Schema validation time |
| T_aggregation | Aggregation time |

Total latency:

T_total = T_construct + T_dag + T_det + T_model + T_validation + T_aggregation

Latency analysis is structural, not monolithic.

---

## 7. Failure Classification

Failures must be categorized explicitly.

| Failure Type | Description |
|---------------|-------------|
| ValidationFailure | Schema mismatch |
| TimeoutFailure | Exceeded max_time_ms |
| BudgetFailure | Exceeded max_tokens |
| DependencyFailure | Upstream task failure |
| ExecutionFailure | Deterministic execution error |
| RoutingFailure | Backend invocation failure |

Each failure type must emit telemetry event.

No silent failure.

---

## 8. Retry Tracking

Retry events include:

- Retry attempt number
- Cause of retry
- Model used in retry
- Remaining budget

Retries must be auditable.

Repeated retries signal decomposition or schema issues.

---

## 9. Routing Observability

When routing decisions occur, log:

- Task id
- Selected backend
- Alternative candidates
- Policy decision reason

This ensures routing neutrality remains visible.

Routing must be explainable.

---

## 10. Distributed Execution Telemetry

In distributed environments, telemetry must include:

- Node identifier
- Execution location
- Network latency
- Serialization overhead


```mermaid
flowchart LR
    A[Task Node 1] --> B[Telemetry Collector]
    C[Task Node 2] --> B
    D[Remote LLM] --> B
    B --> E[Central Log Store]
```

Distributed telemetry preserves cross-node visibility.

---

## 11. Observability Invariants

The system must guarantee:

- **Every task emits telemetry**
- **Every model invocation is logged**
- **Every failure is classified**
- **Every retry is recorded**
- **Every routing decision is traceable**

No silent execution.

---

## 12. Experimental Measurement

Telemetry supports falsifiable evaluation:

- Invocation reduction measurement
- Token savings quantification
- Overhead calculation
- Retry stability assessment
- Decomposition coverage analysis

Structure is measurable only if telemetry is complete.

---

## 13. Current Public Counters

These are the current counters new contributors are most likely to see in CLI output, sample telemetry reports, and benchmark docs.

### Telemetry Summary Counters

The `python3 -m kora telemetry --input <run.json>` command summarizes run or report JSON. The committed sample input is `docs/reports/sample_telemetry_input.json`.

| Counter | Meaning |
|---|---|
| `ok` | Whether the summarized run/report completed successfully. |
| `total_time_ms` | Total run/report duration in milliseconds, either read from the input or derived from event timings when available. |
| `total_llm_calls` | Count of non-skipped adapter/model events in the summarized run/report, or the explicit top-level value if present. |
| `tokens_in` | Input token count read from the input or summed from event usage fields. |
| `tokens_out` | Output token count read from the input or summed from event usage fields. |
| `events_ok` | Count of successful KORA events. |
| `events_fail` | Count of failed KORA events. |
| `events_skipped` | Count of events marked as skipped. |
| `stage_counts` | Event counts grouped by stage, such as `DETERMINISTIC` or `ADAPTER`. |
| `budget_breaches` | Count of top-level or event errors marked as budget breaches. |
| `escalation_required` | Count of top-level or event errors marked `ESCALATE_REQUIRED`. |
| `estimated_cost_usd` | Optional estimate from model and token counters when pricing data is available. This is not proof of real API billing. |

### First-Run Demo Counters

`python3 -m kora run direct_vs_kora -- --offline` prints a local offline mock comparison. It is useful for understanding output shape and routing behavior, but it is not production benchmark evidence.

| Counter | Meaning |
|---|---|
| `llm_calls_direct_total` | Total simulated direct-path model calls across the offline demo cases. |
| `llm_calls_kora_total` | Total simulated KORA-controlled model calls across the offline demo cases. |
| `llm_calls_reduced_total` | Difference between the simulated direct-path and KORA-controlled call totals in the offline demo. |
| `tokens_in_direct_total` | Simulated direct-path input token total in the offline demo. |
| `tokens_in_kora_total` | Simulated KORA-controlled input token total in the offline demo. |
| `tokens_out_direct_total` | Simulated direct-path output token total in the offline demo. |
| `tokens_out_kora_total` | Simulated KORA-controlled output token total in the offline demo. |

Offline demo counters are simulated local counters. They are not real API-cost or billing counters.

### Benchmark Evidence Counters

The current deterministic-heavy benchmark path is documented in `experiments/README.md` and `docs/reports/benchmark_artifact_policy.md`.

| Counter | Meaning |
|---|---|
| `total tasks` | Number of tasks in the benchmark workload. |
| `deterministic/no-model tasks` | Workload tasks marked as not requiring a model candidate. |
| `fallback/model-candidate tasks` | Workload tasks marked as requiring a model candidate. |
| `direct-baseline simulated model invocations` | Simulated model invocations for a naive direct baseline. |
| `KORA-controlled simulated model invocations` | Simulated model invocations for the KORA-controlled benchmark mode. |
| `avoided simulated model invocations` | Difference between direct-baseline and KORA-controlled simulated invocation counts. |
| `avoided invocation rate` | Avoided simulated invocations divided by direct-baseline simulated invocations. |
| `deterministic outputs checked` | Deterministic workload outputs compared with expected outputs. |
| `mismatches` | Deterministic expected-output mismatches. |
| `fallback/model-candidate skipped` | Fallback/model-candidate tasks skipped for deterministic output checking. |

Benchmark invocation counters are simulated benchmark counters. They do not prove production cost reduction, real API-cost reduction, production benchmark performance, full runtime-integrated benchmark behavior, broad workload superiority, or energy reduction.

---

## 14. Storage and Retention

Telemetry storage must:

- Support structured querying
- Preserve task relationships
- Allow correlation by trace_id
- Retain historical experiments

Retention policy must balance audit needs and storage cost.

---

## 15. Performance Implications

Telemetry introduces overhead.

Logging must:

- Be non-blocking
- Avoid synchronous I/O in critical path
- Batch writes when possible
- Respect global budget constraints

Observability must not dominate execution.

---

## Closing Position

Telemetry is not decoration.

It is enforcement.

Without telemetry:

- Budget governance cannot be audited.
- Break-even cannot be measured.
- Decomposition cannot be validated.
- Routing cannot be trusted.

**Structure must be observable.**
