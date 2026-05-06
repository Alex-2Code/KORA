# KORA GitHub Actions Roadmap

Date: `2026-05-06`

## Purpose

Actions should gradually protect quality and claim safety as KORA grows.

Automation should start lightweight and advisory, then become stricter when the project has enough contributor volume and stable workflows.

## Phase 1 Actions

- Python smoke test
- markdown diff/check
- basic docs link check
- no old repo URL check

## Phase 2 Actions

- claim-scan workflow
- benchmark command smoke workflow
- examples list smoke workflow
- PR title/checklist validation

## Phase 3 Actions

- release checklist validation
- paper artifact validation
- benchmark result schema validation
- contributor docs validation

## Claim-Scan Candidates

Candidate terms:

- production cost
- real API
- energy reduction
- production benchmark
- broad workload superiority
- government validation
- formal partnership
- guaranteed
- proven cost reduction

The workflow should flag these terms for review rather than automatically assuming the surrounding text is unsafe.

## Caution

Actions should not block productive early contribution too aggressively.

Start advisory, then make required checks later.

Early goals:

- catch obvious broken docs
- catch old repository URLs
- remind reviewers about claim-sensitive language
- preserve velocity for small contributor PRs
