# KORA Repository Migration Checklist

Date: `2026-05-06`

Purpose: document the public-safe migration of KORA from Albert's personal GitHub account to the Krako-Labs organization before broader community, paper, EIC, investor, and partner activity begins.

## 1. Current Repository State

- Previous repo location: Albert's personal GitHub account
- Official repo URL after migration: https://github.com/Krako-Labs/KORA
- Public truth before migration: `origin/main`
- Current public HEAD: `376b6406bfdbf7381e55e0d9bb0c75fc8dac38dc`
- Published release: `v0.2.0-alpha`
- Current release URL: https://github.com/Krako-Labs/KORA/releases/tag/v0.2.0-alpha
- Migration note: `Krako-Labs` is the actual final organization. The earlier `Krako-cloud` planning placeholder is superseded.

Current safe benchmark claim:

> In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline.

## 2. Migration Rationale

KORA moved from Albert's personal GitHub account to `Krako-Labs` so the official project home matches the organization that will steward the project, documentation, community surface, and future governance. A personal account was acceptable for early incubation, but the official repo should live under the organization before the project is presented more broadly.

The move should happen before broader public community activation because early contributors, readers, and stakeholders will form habits around the canonical URL. Moving first reduces link churn, avoids confusing forks or duplicated issue trackers, and gives the project a cleaner operational base for docs, issue templates, permissions, and project boards.

This supports paper, EIC, investor, partner, and community readiness by making the repository easier to cite, share, govern, and maintain. The organization URL makes the project look less like a private working copy and more like the official open-source home for the KORA effort.

Albert's technical origin story should be preserved in the README, release history, changelog, and early commit history. The migration should frame Albert as the originator and initial technical lead while making `Krako-Labs/KORA` the official maintained home going forward.

## 3. Recommended Migration Approach

Preferred option: transfer the existing repository from Albert's personal GitHub account to `Krako-Labs/KORA`.

Reasons:

- Preserves stars, watchers, forks, issues, pull requests, releases, tags, and commit history in one canonical repository.
- Keeps `v0.2.0-alpha` release history attached to the same project.
- Lets GitHub redirects help existing links continue to resolve, subject to GitHub's redirect caveats.
- Avoids creating an unnecessary duplicate repository with split history.

Alternative option: create a new `Krako-Labs/KORA` repository and leave the personal repository as an archive notice.

This is only preferable if transfer permissions, organization policy, or repository-name conflicts block a direct transfer. It creates more operational work because releases, links, settings, and community surfaces must be recreated or clearly redirected.

Recommendation: use the direct GitHub repository transfer to `Krako-Labs/KORA`, then run a short post-transfer URL and settings cleanup pass.

## 4. Pre-Transfer Checklist

- Confirm Albert has the required admin permissions on the personal source repository.
- Confirm Albert has permission to create or receive repositories in the `Krako-Labs` organization.
- Confirm the target repo name `KORA` is available under `Krako-Labs`.
- Confirm no critical open PRs are pending or mid-review.
- Confirm release and tag state:
  - Tag `v0.2.0-alpha` exists.
  - GitHub Release `v0.2.0-alpha` exists.
  - Release is a prerelease.
  - No release assets are expected for this release.
  - No raw benchmark JSON artifacts are expected for this release.
- Confirm the local repo and working directories are backed up or recoverable.
- Confirm public docs are ready for URL updates after migration.
- Confirm the migration is not being presented as a new release.

## 5. Transfer Execution Checklist

Manual GitHub steps for Albert:

1. Open the source repository settings in Albert's personal GitHub account.
2. Go to the repository transfer section.
3. Select transfer owner: `Krako-Labs`.
4. Confirm repository name: `KORA`.
5. Complete the GitHub confirmation flow.
6. After transfer, open https://github.com/Krako-Labs/KORA.
7. Confirm the repository, releases, tags, issues, pull requests, and settings are present.

Do not ask Codex to perform the repository transfer.

Expected target URL after transfer:

- https://github.com/Krako-Labs/KORA

Expected redirect behavior caveat:

- GitHub usually redirects old repository URLs after a transfer, but redirects can be affected by future repository creation, rename, or ownership changes. Treat redirects as compatibility support, not as the canonical long-term URL.

## 6. Post-Transfer Technical Checklist

- Update local git remote:

```bash
git remote set-url origin git@github.com:Krako-Labs/KORA.git
```

- Verify the remote:

```bash
git remote -v
git fetch --prune origin --tags
git rev-parse origin/main
git tag --list "v0.2.0-alpha"
git ls-remote --tags origin "refs/tags/v0.2.0-alpha"
```

- Verify `origin/main` still resolves to the expected migrated public HEAD or a documented successor commit.
- Verify tags migrated correctly.
- Verify the `v0.2.0-alpha` GitHub Release exists at the new organization URL.
- Verify README links and badges.
- Verify CHANGELOG release links.
- Verify docs links under `docs/`.
- Search for old personal-repository URLs and the superseded Krako-cloud planning placeholder, then replace them where appropriate.

- Keep old URLs only where historical context is explicitly useful.
- Verify CLI smoke tests still pass:

```bash
python3 -m pytest
python3 -m kora --help
python3 -m kora examples list
python3 -m kora run direct_vs_kora -- --offline
```

## 7. Post-Transfer Community Setup Checklist

- Enable Issues.
- Enable Discussions.
- Create or configure a Project board for release polish, docs, onboarding, benchmark evidence, and community tasks.
- Add labels for:
  - `good first issue`
  - `documentation`
  - `benchmark`
  - `onboarding`
  - `release-polish`
  - `claim-boundary`
  - `runtime-evidence`
- Add issue templates for bug reports, documentation improvements, benchmark/evidence requests, and community questions.
- Add Sumanta with the appropriate organization and repository permissions.
- Protect `main` if appropriate:
  - require pull requests before merge
  - require status checks once CI is configured
  - restrict force pushes
  - require branch to be up to date before merge if the project adopts that policy

## 8. Claim and Communication Boundaries

Approved migration message:

> KORA has moved from Albert's personal GitHub account to the `Krako-Labs` organization so the project has a clear official home before broader community, paper, EIC, investor, and partner activity begins. Albert's early technical authorship and release history remain preserved in the repository history.

Approved benchmark claim:

> In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline.

Do-not-claim list:

- Do not claim production cost reduction.
- Do not claim real API cost reduction.
- Do not claim production benchmark proof.
- Do not claim broad workload superiority.
- Do not claim government validation.
- Do not claim formal partnership.
- Do not claim energy reduction.
- Do not claim guaranteed outcomes.
- Do not claim proven cost reduction.

Communication boundaries:

- Avoid presenting the migration as a new release.
- Avoid presenting the migration as new technical evidence.
- Avoid presenting unsigned partner or government interest as validation.
- Keep `v0.2.0-alpha` claims bounded to the reproducible simulated benchmark evidence already released.
- State that raw benchmark JSON artifacts were not uploaded for `v0.2.0-alpha`.
- State that no release assets were uploaded for `v0.2.0-alpha`.

## 9. Recommended Next Tasks

- Task 125: update repo URLs and remote references after migration.
- Task 126: create Albert-Sumanta GitHub sync setup.
- Task 127: create KORA Claim Registry.
- Task 128: create Sumanta Community OS and LLM operating manual.
