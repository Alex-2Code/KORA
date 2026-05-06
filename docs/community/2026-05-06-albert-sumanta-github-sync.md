# Albert-Sumanta GitHub Sync Setup

Date: `2026-05-06`

## Purpose

This document defines the initial GitHub-based operating system for Albert and Sumanta to coordinate KORA community, content, outreach, benchmark feedback, and partner-interest tracking.

## Why GitHub Is The Source Of Truth

GitHub should be the source of truth because KORA is an open-source project and the repository is where public work, documentation, issues, discussions, and evidence boundaries can be reviewed together. Telegram and other channels can move quickly, but decisions, follow-ups, public claims, and reusable process should resolve back into GitHub.

Using GitHub as the operating base gives KORA:

- a durable public record of community and evidence work
- clear ownership for follow-ups
- reviewable content and claim boundaries
- a way to turn feedback into issues, docs, and benchmark tasks
- a shared workflow for Albert, Sumanta, and future contributors

## Role Split

Albert:

- technical authority
- final claim approval
- investor, EIC, and partner narrative owner
- final reviewer for claim-sensitive content
- final reviewer for benchmark and evidence wording

Sumanta:

- community and ecosystem activation
- outreach coordination
- feedback collection
- early builder engagement
- first-pass issue triage for community and content work
- weekly community feedback summary preparation

## What Lives In GitHub Issues

- community tasks
- content drafts needing review
- outreach follow-ups
- benchmark feedback from users
- partner-interest tracking
- questions that need a concrete owner or decision
- recurring weekly sync issues

## What Lives In GitHub Discussions

- open-ended community questions
- onboarding threads
- public feedback from builders
- early use-case discussion
- announcement follow-ups
- non-urgent ecosystem conversation

## What Lives In GitHub Projects

- status tracking for community and evidence operations
- weekly priorities
- blocked work
- Albert review queue
- published or completed community items
- partner-lead follow-up status

Recommended GitHub Project board:

- `KORA Community & Evidence Ops`

Recommended columns:

- Backlog
- Ready
- In Progress
- Needs Albert Review
- Approved
- Published / Done
- Blocked

## What Lives In docs/community

- operating manuals
- weekly summary templates
- approved language references
- community workflows
- onboarding guides for contributors and community coordinators
- durable summaries of recurring process decisions

## What Stays In Telegram

- lightweight daily coordination
- quick community responses
- informal reminders
- real-time handoff notes
- pointers back to GitHub issues, discussions, or docs

Telegram should not be the only place where important decisions, claim approvals, partner status, or benchmark feedback live.

## Recommended Labels

- `community`
- `content`
- `outreach`
- `benchmark`
- `partner-lead`
- `github-discussion`
- `telegram`
- `linkedin`
- `twitter`
- `needs-albert-review`
- `approved`
- `blocked`
- `claim-sensitive`

## Sumanta Permission Model

Sumanta can:

- create issues
- comment in discussions
- update project status
- open PRs for `docs/community` changes

Sumanta should not:

- push directly to `main`
- change repository settings
- publish claim-sensitive content without review
- describe partner or institutional interest as validation unless signed or documented

## Content Approval Levels

Level A: free to publish using approved language.

Examples:

- community reminders
- links to existing docs
- neutral announcements about open issues
- invitations to try examples or share feedback

Level B: needs Albert review.

Examples:

- benchmark summaries
- investor-facing copy
- EIC-facing copy
- partner-facing copy
- posts mentioning results, impact, adoption, or institutional interest

Level C: prohibited or special approval required.

Examples:

- claims outside the approved benchmark boundary
- statements implying signed partners without documentation
- statements implying institutional validation without documentation
- release announcements not tied to an actual release
- technical claims that have not been reviewed by Albert

## Weekly Rhythm

- Daily lightweight GitHub/project updates.
- Two content review windows per week.
- One weekly sync issue.
- One weekly community feedback summary.

## First 10 Suggested GitHub Issues To Create Manually

1. Create the `KORA Community & Evidence Ops` project board.
2. Add recommended community and claim-boundary labels.
3. Enable or configure GitHub Discussions for KORA community questions.
4. Draft the first approved KORA community one-liner and short description.
5. Prepare a pinned GitHub Discussion for early builder feedback.
6. Create the first weekly community sync issue.
7. Collect first-run feedback from developers using the CLI examples.
8. Collect benchmark evidence questions from early readers.
9. Draft Sumanta's first LinkedIn/X/Twitter content batch for Albert review.
10. Create the first partner-interest tracking issue using the partner lead template.
