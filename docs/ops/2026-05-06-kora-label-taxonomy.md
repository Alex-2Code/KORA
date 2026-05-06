# KORA Label Taxonomy

Date: `2026-05-06`

## Purpose

Labels make KORA issues and PRs navigable for contributors, operators, Sumanta, the Korean ops coordinator, and future maintainers.

Labels should help route work quickly without turning triage into a heavy process.

## Label Groups

Area:

- `area:core`
- `area:docs`
- `area:benchmark`
- `area:community`
- `area:paper`
- `area:eic`
- `area:investor`
- `area:partner`
- `area:ops`
- `area:github`

Type:

- `type:bug`
- `type:feature`
- `type:docs`
- `type:question`
- `type:discussion`
- `type:benchmark-result`
- `type:use-case`
- `type:outreach`
- `type:partner-lead`
- `type:paper-contribution`

Difficulty:

- `good first issue`
- `help wanted`
- `difficulty:easy`
- `difficulty:medium`
- `difficulty:hard`

Review:

- `needs-albert-review`
- `needs-technical-review`
- `needs-community-review`
- `needs-claim-review`

Status:

- `status:backlog`
- `status:ready`
- `status:in-progress`
- `status:blocked`
- `status:done`
- `status:deferred`

Claim sensitivity:

- `claim-safe`
- `claim-sensitive`
- `do-not-publish`

Evidence:

- `evidence:benchmark`
- `evidence:runtime`
- `evidence:real-workload`
- `evidence:community`
- `evidence:partner`
- `evidence:paper`

## Label Usage Rules

- Apply labels during issue intake or PR review.
- Any maintainer or trusted operator can apply routine labels.
- `needs-albert-review`, `needs-claim-review`, `claim-sensitive`, and `do-not-publish` trigger Albert review before external publication.
- Status labels should map to Project board columns where practical.
- Area labels should be used to route work to the right operating track.
- Evidence labels should be used when an issue contains benchmark results, runtime notes, user feedback, use cases, partner-interest signals, or paper evidence.

## Initial Recommended Labels To Create First

Create this smaller first batch before the full taxonomy:

- `area:core`
- `area:docs`
- `area:benchmark`
- `area:community`
- `area:ops`
- `type:bug`
- `type:docs`
- `type:question`
- `type:benchmark-result`
- `type:partner-lead`
- `good first issue`
- `help wanted`
- `needs-albert-review`
- `needs-technical-review`
- `needs-claim-review`
- `status:blocked`
- `claim-sensitive`
- `claim-safe`
- `evidence:benchmark`
- `evidence:community`
