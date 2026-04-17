# Changelog

## v0.1 alpha public surface

Current public alpha snapshot for KORA.

### Public CLI surface

- `python3 -m kora examples list`
- `python3 -m kora run <example>`
- `python3 -m kora telemetry`

### Runnable examples

- `hello_kora`
- `retry_demo`
- `direct_vs_kora`
- `real_workload_harness`
- `stress_test`

### Reproducible first-run path

```bash
python3 -m kora examples list
python3 -m kora run hello_kora
python3 -m kora run retry_demo
python3 -m kora run direct_vs_kora -- --offline
python3 -m kora telemetry --input docs/reports/sample_telemetry_input.json
```

### Documentation

- The first run -> telemetry -> benchmark progression is now explicit.

### Limitations

- This is an alpha surface.
- This is not a production release.
