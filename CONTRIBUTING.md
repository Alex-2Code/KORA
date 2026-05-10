# Contributing to KORA

## Project status

Current published release: [`v0.2.0-alpha`](https://github.com/Krako-Labs/KORA/releases/tag/v0.2.0-alpha).

KORA remains alpha / prerelease software with a small terminal-first public surface. The current focus is keeping the CLI, examples, telemetry path, benchmark evidence, and release smoke checks reliable while the project matures.

KORA is not a production release yet. Contributions should be conservative, well-scoped, and easy to verify.

## Contributor path

Start here when orienting yourself:

- [README.md](README.md): project overview, current release status, quickstart, examples, and bounded benchmark evidence.
- [docs/README.md](docs/README.md): public docs navigation, current evidence path, artifact policy, and historical report labels.
- [experiments/README.md](experiments/README.md): deterministic-heavy benchmark workload and regeneration flow.
- [CHANGELOG.md](CHANGELOG.md): release history.
- [SECURITY.md](SECURITY.md): supported reporting path for security issues.
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md): community expectations.
- [GOVERNANCE.md](GOVERNANCE.md): project governance expectations.
- [docs/community/contact-and-discussion-routes.md](docs/community/contact-and-discussion-routes.md): current route guidance for questions, workload proposals, bugs, security issues, and PRs.
- [.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE/): issue templates.
- [.github/pull_request_template.md](.github/pull_request_template.md): pull request checklist.

## Who this project is for

KORA is for developers and researchers building AI systems that need stronger execution control.

Good contributors are interested in:

- deterministic-first execution
- explicit task graphs
- bounded model invocation
- schema validation
- telemetry and repeatable verification
- clear examples and documentation

## Local setup

Start from a clean checkout of the repository.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ".[dev]"
```

The editable install should install KORA and its development dependencies into the virtual environment.

## First verification commands

Before making changes, run the release smoke check:

```bash
./scripts/release_smoke.sh
```

Then run the test suite:

```bash
python3 -m pytest -q
```

Both commands should pass before you open a pull request.

## How to choose a first issue

For a first contribution, choose a task that is small and easy to review.

Good first issues usually:

- touch one or two files
- improve clarity without changing behavior
- add or tighten a narrow test
- explain an existing example or telemetry artifact
- preserve the current public CLI surface

Avoid starting with large runtime changes, new public commands, broad refactors, or changes that alter model-routing semantics.

## Finding a first contribution

Use the [contributor pathway](docs/community/contributor-pathway.md) to choose the right route for questions, bugs, PRs, and workload proposals.

For current route guidance, see [contact and discussion routes](docs/community/contact-and-discussion-routes.md).

For candidate tasks that maintainers may later convert into GitHub issues, see [good first issue candidates](docs/community/good-first-issue-candidates.md).

For validation workload ideas, use the [workload proposal template](docs/community/workload-proposal-template.md). Keep proposals synthetic or sanitized and do not include secrets, private data, proprietary datasets, or raw provider responses.

## Good first contribution types

Good first contribution types include:

- docs improvements
- example explanations
- small tests
- telemetry docs
- benchmark docs
- CLI help wording

If you are unsure whether a change expands the public surface, open an issue or discussion before implementing it.

## Branch and PR workflow

Use a short topic branch name:

```bash
git switch -c your-name/small-description
```

Keep pull requests focused. A good PR should explain:

- what problem it solves
- what files changed
- how behavior is affected, if at all
- what verification commands were run

Prefer one logical change per PR. Do not bundle documentation cleanup, runtime edits, and unrelated formatting in the same pull request.

## Verification expectations

Use verification that matches the change type. Include the commands and results in your PR description.

For documentation-only changes, check that public docs use relative repo paths and do not add unsupported claims. When relevant, scan changed docs for machine-local paths:

```bash
rg -n "/Users/|/home/" <changed-docs>
```

For CLI or example changes, run the CLI smoke checks and the relevant example:

```bash
python3 -m kora --help
python3 -m kora examples list
python3 -m kora run <example_name>
```

For benchmark or evidence changes, run tests and follow the regeneration flow in [experiments/README.md](experiments/README.md). Keep raw benchmark JSON artifacts governed by [docs/reports/benchmark_artifact_policy.md](docs/reports/benchmark_artifact_policy.md).

```bash
python3 -m pytest
```

For general code changes, run the full test suite and at least one relevant CLI smoke test:

```bash
python3 -m pytest
python3 -m kora --help
python3 -m kora run direct_vs_kora -- --offline
```

If your change touches a specific module, also run the relevant focused test file when possible:


```bash
python3 -m pytest tests/test_executor.py -q
python3 -m pytest tests/test_task_ir.py -q
```

## Claim hygiene

Do not claim:

- production cost reduction proof
- real API-cost reduction proof
- production benchmark proof
- full runtime-integrated benchmark evidence
- broad workload superiority proof
- energy reduction evidence

If you reference current benchmark evidence, use only this bounded claim:

> In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline.

## Local-path hygiene

Public docs should use relative repo paths. Do not include machine-local absolute paths, and keep local-only context outside public documentation.

## Contribution rules

- Keep PRs small.
- Do not include unrelated refactors.
- Run tests before opening a PR.
- Do not expand the public CLI or public task surface without prior discussion.
- Keep KORA deterministic-first: deterministic work should run before model inference when possible.
- Do not introduce hidden model calls.
- Keep retries, budgets, and validation explicit.
- Preserve schema validation around model outputs.
- Avoid broad claims in docs unless they are backed by committed verification artifacts.

## Community expectations

Be direct, practical, and respectful.

Good project communication is specific:

- describe the concrete issue
- explain the tradeoff
- show the verification result
- ask for review when scope is uncertain

KORA values careful, measurable changes over large speculative additions.
