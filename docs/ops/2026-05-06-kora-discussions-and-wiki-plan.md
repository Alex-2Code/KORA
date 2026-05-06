# KORA Discussions And Wiki Plan

Date: `2026-05-06`

## Purpose

Discussions and Wiki should help turn external interest into structured community participation.

Discussions are for conversation and early signal collection. Wiki is for beginner-friendly onboarding. Official evidence and claim language remain in versioned repository docs.

## GitHub Discussions Categories

### Announcements

Purpose:

- share official project updates and links to releases, docs, and roadmap items

Example posts:

- release note link
- new contributor guide link
- benchmark evidence update link

Moderation rule:

- official claims must follow `docs/claims/`

Convert to issue when:

- a reply identifies actionable work or a docs gap

### Q&A

Purpose:

- answer user and contributor questions

Example posts:

- install questions
- first-run issues
- architecture questions

Moderation rule:

- answer with links when possible; mark uncertain claims for review

Convert to issue when:

- a question reveals a bug, missing docs, or reproducible failure

### Benchmark Results

Purpose:

- collect reproducibility reports and benchmark questions

Example posts:

- benchmark command output
- environment report
- result discrepancy

Moderation rule:

- benchmark results should include environment and command details

Convert to issue when:

- a result suggests a bug, docs issue, or methodology change

### Use Cases

Purpose:

- collect real-world scenarios and possible workload examples

Example posts:

- AI app routing scenario
- deterministic preprocessing idea
- validation-heavy workflow

Moderation rule:

- do not present use-case interest as validation

Convert to issue when:

- a use case can become an example, workload, or benchmark task

### Ideas

Purpose:

- collect proposals before they become scoped work

Example posts:

- CLI improvement idea
- docs improvement idea
- workflow extension idea

Moderation rule:

- ask for concrete expected behavior

Convert to issue when:

- scope, owner, and done criteria are clear

### Contributors

Purpose:

- help new contributors find roles and first tasks

Example posts:

- introduction
- role interest
- first contribution question

Moderation rule:

- no personal resumes in public issues/discussions

Convert to issue when:

- a contributor is ready to take a concrete task

### Research & Paper

Purpose:

- discuss methodology, reproducibility, and paper roadmap questions

Example posts:

- benchmark methodology question
- related work suggestion
- reproducibility concern

Moderation rule:

- paper/publication claims require review

Convert to issue when:

- a research question becomes a tracked paper or benchmark task

### AI-assisted Contributions

Purpose:

- guide contributors using LLMs or vibe-coding tools

Example posts:

- safe workflow question
- prompt improvement
- generated PR review question

Moderation rule:

- contributors remain accountable for AI-generated output

Convert to issue when:

- a proposed AI-assisted contribution has a narrow scope

## Wiki Plan

Recommended pages:

- Start Here
- What is KORA?
- How to Join
- Community Roles
- How to Run the Benchmark
- How to Open an Issue
- How to Submit a Pull Request
- AI-assisted Contribution Rules
- Weekly Community Rhythm
- Claim Boundaries
- FAQ

## Repo Docs Versus Wiki Boundary

- Official evidence and claims stay in repo docs.
- Beginner-friendly handbook content can live in Wiki.
- Important Wiki content should eventually link back to versioned docs.
- The Wiki should not become the only source for release, claim, or benchmark evidence.

## Moderation Principles

- no unsupported claims
- no personal resumes in public issues/discussions
- no partner/government validation language without approval
- benchmark results should include environment and command details
