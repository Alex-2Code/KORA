# KORA Community Manager Guide

Date: 2026-05-07

Current release: `v0.3.0-alpha`

Release URL: https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha

## Purpose

This guide helps KORA community managers handle GitHub Discussions, Issues, PR triage, benchmark reproduction questions, and release sharing.

It is an operations guide, not a technical proof document. Use it to route conversations, keep public language accurate, and escalate unclear or risky topics to maintainers.

For channel-specific release copy and social/community announcement templates, use the [KORA Social Media Announcement Guide](KORA_SOCIAL_MEDIA_ANNOUNCEMENT_GUIDE.md).

## Social Launch Focus

For the `v0.3.0-alpha` launch, start with the [KORA Social Media Announcement Guide](KORA_SOCIAL_MEDIA_ANNOUNCEMENT_GUIDE.md). It gives public-safe message examples, benchmark boundaries, and technical visual placeholder guidance.

The main social emphasis should be:

- Hook: Most AI apps call the model too soon.
- Shift: KORA puts execution control before inference.
- Mechanism: task graphs, deterministic-first execution, validation before escalation, telemetry around every path, and model calls only when needed.
- Evidence: KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.
- Next validation: real model-call runtime paths, support triage, RAG routing, and agent budget-guard workloads.
- CTA: Clone the repo. Run the alpha. Inspect the path. Bring a workload.
- the release URL: https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha

Keep this section focused on launch momentum. Use the rest of this guide for moderation, issue triage, claim-boundary review, and maintainer escalation.

## Current Project State

- KORA `v0.3.0-alpha` is available as a GitHub prerelease.
- Release URL: https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha
- Release assets: none.
- Raw benchmark artifacts uploaded: none.
- Package version remains `0.1.0a0`.

## Safe Benchmark Claim

Use this wording when describing the current bounded benchmark result:

> KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.

Do not strengthen, generalize, or shorten this claim in a way that removes the workload boundary.

## What Community Managers May Say

Community managers may use these phrases:

- KORA `v0.3.0-alpha` is a prerelease.
- KORA includes an initial runtime-path benchmark harness.
- KORA provides a reproducible local evidence-generation flow.
- KORA includes JSON output, Markdown evidence packet generation, and telemetry summary commands.
- KORA's current evidence is bounded to a deterministic-heavy 100-task benchmark workload.
- KORA is expanding validation across real model-call paths, support triage, RAG routing, and agent budget-guard workloads.
- Developers can clone the repo, run the alpha, inspect the path, and bring a workload.
- KORA does not upload raw benchmark artifacts as release assets.
- The current benchmark flow is a non-production benchmark scaffold.

## What Community Managers Must Not Say

Do not state or imply:

- production cost reduction proof
- real API-cost reduction proof
- production benchmark proof
- full runtime-integrated benchmark evidence
- broad workload superiority proof
- energy reduction evidence
- formal government validation
- signed partner validation unless actually signed and documented
- guaranteed adoption or funding

Escalate to maintainers if a user asks for wording that would imply any of these claims.

## GitHub Discussions Operating Model

Discussions are for conversation, clarification, and early ideas. Convert a discussion into an Issue only when there is a concrete action a maintainer or contributor can take.

| Category | Belongs there | Does not belong there | Convert to Issue when | Escalate when |
|---|---|---|---|---|
| Announcements | Release notes, project updates, roadmap summaries | Support requests, bug reports, private security reports | Announcement uncovers a docs task or reproducible bug | Release wording or claim boundary is uncertain |
| Q&A | Setup questions, command clarification, evidence-path questions | Feature requests with implementation scope | Answer needs a docs fix or repeated setup pain is visible | Expected counters mismatch or user requests unsupported claims |
| Ideas | Early proposals, workload ideas, reviewer feedback | Confirmed bugs, security issues | Proposal has clear scope, acceptance criteria, or implementation plan | Proposal changes release, package version, benchmark wording, or artifact policy |
| Benchmark Reproduction | Local reproduction attempts, command output questions, counter comparisons | Broad performance claims, raw artifact upload requests | User provides exact command, environment, and mismatch details | Counters differ from expected values or language overclaims results |
| Show and Tell | Community experiments, integrations, examples | Claims that KORA proves production outcomes | Example reveals a reusable doc/example improvement | User presents external results as official KORA validation |
| Contributor Help | How to start contributing, triage help, good first issue questions | General chat without a repo action | A contributor chooses a concrete docs/code task | Contributor wants to change claim-sensitive files |

## GitHub Issues Operating Model

Issues should be actionable work items, not general chat. If a report is mainly discussion, move it to Discussions and ask for details.

Recommended issue types:

- Bug report
- Documentation issue
- Benchmark reproduction issue
- Feature proposal

For benchmark-related issues, ask for:

- exact command run
- environment notes, including OS, Python version, install mode, and whether `--offline` was used
- expected counters
- actual counters
- whether generated artifacts are local-only
- confirmation that the report does not add overclaiming language

Benchmark issue checklist:

- [ ] Exact command is included.
- [ ] Environment notes are included.
- [ ] Expected vs actual counters are included.
- [ ] Generated artifacts are described as local-only or attached intentionally for review.
- [ ] The issue does not claim production/API-cost/energy proof.

## Pull Request Triage Guidance

Community managers should look for:

- generated artifacts accidentally committed
- raw benchmark JSON or Markdown committed
- risky claim language
- release assets, tag creation, or GitHub Release changes
- package version changes
- broad changes to README, CHANGELOG, docs reports, benchmark wording, or release language
- missing validation command output

Claim-boundary checklist:

- [ ] Safe claim is preserved exactly when benchmark results are discussed.
- [ ] No production cost/API-cost/energy proof is claimed.
- [ ] No broad workload superiority claim is added.
- [ ] No formal government or partner validation is implied.
- [ ] Generated benchmark outputs remain in `/tmp` or another user-provided path unless a maintainer explicitly approves otherwise.

Escalate PRs that touch:

- `README.md`
- `CHANGELOG.md`
- `docs/reports/`
- `docs/claims/`
- `docs/benchmarks/`
- `experiments/`
- `.github/`
- release, package, tag, or artifact policy files

## Labels

Recommended labels:

- `type:bug`
- `type:docs`
- `type:benchmark`
- `type:telemetry`
- `type:question`
- `type:proposal`
- `type:community`
- `status:triage`
- `status:needs-info`
- `status:accepted`
- `status:blocked`
- `good-first-issue`
- `claim-boundary-review`
- `artifact-policy-review`

Use `claim-boundary-review` when an issue, discussion, or PR changes public benchmark wording, release wording, README language, changelog text, report language, or external-facing claims.

Use `artifact-policy-review` when an issue, discussion, or PR proposes committing generated outputs, uploading raw benchmark artifacts, attaching release assets, changing artifact retention, or changing where generated reports are stored.

## Response Templates

### Welcoming A New User

Thanks for checking out KORA. The best starting points are the README, the docs index, and the `v0.3.0-alpha` prerelease notes. If you are reproducing the benchmark path, please use the documented offline commands and keep generated outputs local unless a maintainer asks for them.

### Benchmark Reproduction Question

The current bounded benchmark claim is:

> KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.

Please share the exact command you ran, your Python version, whether you used `--offline`, and the counters you saw for total tasks, deterministic routes, fallback/model-candidate routes, avoided simulated model invocations, mismatch count, and telemetry event count.

### Correcting Overclaiming

Thanks for the writeup. We need to keep the wording bounded to the current evidence. KORA's current public claim is limited to a reproducible 100-task deterministic-heavy benchmark workload. Please avoid claims about production cost reduction, real API-cost reduction, production benchmark proof, broad workload superiority, or energy reduction.

### Asking For Missing Environment Details

Could you add the exact command, OS, Python version, install method, and whether `--offline` was used? For benchmark reports, please also include expected vs actual counters and confirm whether any generated JSON or Markdown files are local-only.

### Redirecting General Chat To Discussions

This looks better suited for GitHub Discussions because it is exploratory rather than a concrete bug or task. Please open it under the closest category, and if it becomes actionable we can convert it into an Issue.

### Converting Actionable Reports Into Issues

This now has enough detail to track as an Issue. Please include the command, environment, expected output, actual output, and any relevant logs. Avoid attaching raw generated benchmark artifacts unless a maintainer asks for them.

### Release Announcement Wording

KORA `v0.3.0-alpha` is available as a GitHub prerelease: https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha

Most AI apps call the model too soon. KORA puts execution control before inference through task graphs, deterministic-first execution, validation before escalation, telemetry around every path, and model calls only when needed.

KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.

This prerelease includes an initial runtime-path benchmark harness, a reproducible local evidence-generation flow, Markdown evidence packet generation, and telemetry-connected summary commands.

This is bounded prerelease evidence. It does not claim production cost reduction proof, real API-cost reduction proof, production benchmark proof, full runtime-integrated benchmark evidence, broad workload superiority proof, energy reduction evidence, formal government validation, signed partner validation, or guaranteed adoption or funding.

## Escalation Rules

Escalate to maintainers if:

- a user claims production cost, real API-cost, or energy proof
- a user reports a mismatch in expected counters
- a user proposes uploading raw artifacts
- a user requests release assets
- a user reports a security issue
- a user proposes package version or release changes
- a user opens a PR that changes README, CHANGELOG, docs/reports, benchmark wording, release wording, or claim-sensitive docs
- a user asks whether KORA has formal government validation, signed partner validation, guaranteed adoption, or funding commitments

Security issues should be routed through `SECURITY.md`, not public discussion threads.

## Artifact Policy

- Generated JSON and Markdown reports should stay in `/tmp` or user-provided output paths.
- Generated raw benchmark artifacts are not committed.
- Release assets are not uploaded unless explicitly approved.
- Raw benchmark artifacts are not uploaded unless explicitly approved.
- Community managers should not ask users to upload raw benchmark artifacts unless a maintainer has requested them for a specific review.

## Maintainer Handoff Checklist

When escalating to maintainers, include:

- [ ] Link to the discussion, issue, or PR.
- [ ] User's command and output summary.
- [ ] Environment summary.
- [ ] Whether counters match expected values.
- [ ] Whether claim language is safe.
- [ ] Whether artifacts were attached or proposed.
- [ ] Suggested label.
- [ ] Urgency and reason.
- [ ] Any suspected security, release, package-version, or artifact-policy impact.

## Quick Public Announcement Draft

KORA `v0.3.0-alpha` is available as a GitHub prerelease:

https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha

This prerelease adds an initial runtime-path benchmark harness, a reproducible local evidence-generation flow, Markdown evidence packet generation, and telemetry-connected summary commands.

Current bounded benchmark claim:

> KORA reduced model invocations by 80% in a reproducible deterministic-heavy benchmark workload.

This prerelease does not claim production cost reduction proof, real API-cost reduction proof, production benchmark proof, full runtime-integrated benchmark evidence, broad workload superiority proof, energy reduction evidence, formal government validation, signed partner validation, or guaranteed adoption or funding.

To reproduce locally, use the documented offline commands and keep generated JSON/Markdown outputs in `/tmp` or another user-provided path unless a maintainer explicitly approves a different artifact path.
