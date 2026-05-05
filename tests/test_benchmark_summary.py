from experiments.summarize_benchmark_results import CLAIM_BOUNDARY, build_summary_markdown


def minimal_direct_result() -> dict[str, object]:
    return {
        "benchmark_name": "deterministic_heavy_v1",
        "mode": "direct-baseline",
        "workload_path": "experiments/workloads/deterministic_heavy_v1_100.json",
        "total_tasks": 100,
        "requires_model_false": 80,
        "requires_model_true": 20,
        "simulated_model_invocations": 100,
    }


def minimal_kora_result() -> dict[str, object]:
    return {
        "benchmark_name": "deterministic_heavy_v1",
        "mode": "kora-controlled",
        "workload_path": "experiments/workloads/deterministic_heavy_v1_100.json",
        "total_tasks": 100,
        "requires_model_false": 80,
        "requires_model_true": 20,
        "simulated_model_invocations": 20,
        "avoided_model_invocations_vs_direct_baseline": 80,
        "avoided_model_invocation_rate": 0.8,
        "deterministic_output_checks": 80,
        "deterministic_output_mismatches": 0,
        "fallback_candidates_skipped_for_output_check": 20,
    }


def test_build_summary_markdown_from_minimal_result_artifacts() -> None:
    markdown = build_summary_markdown(minimal_direct_result(), minimal_kora_result())

    assert "# KORA Benchmark Result Summary - deterministic_heavy_v1" in markdown
    assert "| Workload | `experiments/workloads/deterministic_heavy_v1_100.json` |" in markdown
    assert "| Total tasks | 100 |" in markdown
    assert "| Deterministic/no-model tasks | 80 |" in markdown
    assert "| Fallback/model-candidate tasks | 20 |" in markdown
    assert "| Direct-baseline simulated model invocations | 100 |" in markdown
    assert "| KORA-controlled simulated model invocations | 20 |" in markdown
    assert "| Avoided simulated model invocations | 80 |" in markdown
    assert "| Avoided invocation rate | 80% |" in markdown
    assert "| Deterministic expected-output checks | 80 |" in markdown
    assert "| Deterministic expected-output mismatches | 0 |" in markdown
    assert "| Fallback candidates skipped for output check | 20 |" in markdown


def test_build_summary_markdown_includes_claim_boundary() -> None:
    markdown = build_summary_markdown(minimal_direct_result(), minimal_kora_result())

    assert CLAIM_BOUNDARY in markdown
    assert "not production cost proof" in markdown
    assert "real API-cost proof" in markdown
    assert "energy-reduction evidence" in markdown
