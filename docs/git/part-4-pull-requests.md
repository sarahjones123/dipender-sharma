# Part 4: Pull Requests — Controlling Documentation State

In Part 3, we defined documentation as versioned state — a structured snapshot of documentation at a specific point in time.

Every commit creates a new state. But not every state should become authoritative.

Before a documentation state is merged into `main`, deployed, and made visible to users, it must be validated. In Docs-as-Code environments, that validation mechanism is the Pull Request.

This article examines Pull Requests not as conversation tools, but as structural control systems that determine which documentation state becomes production documentation.

By the end of this article you will understand:

- What a production documentation state is and how it differs from a proposed state
- Why a Pull Request is a validation mechanism, not just a collaboration tool
- How the diff functions as the engine of documentation review
- What weak and strong documentation PRs look like in practice
- How enforcement is what makes Pull Requests function as governance

---

## What Is a Production Documentation State?

A **production documentation state** is the version of documentation that has been merged into the primary branch, deployed to a live documentation site or treated as the live source of truth, and made accessible to end users. It is the version your users actually read.

A state becomes **authoritative** when it has passed through a defined validation process — requiring human approval, passing automated checks, or both — and has been merged into the primary branch by someone with merge authority.

Without that process, a state is proposed, not authoritative.

When a Pull Request is merged, it transitions a proposed documentation state into a production documentation state. That transition is controlled, not casual.

---

## From Versioning to Validation

Part 3 focused on how documentation is versioned. Pull Requests introduce the next layer: validation.

- A commit **creates** a state
- A Pull Request **proposes** that state for adoption
- A merge **approves** it for production

This is controlled state transition. Governance, in this context, means a structured and enforced process that determines whether a proposed documentation state is permitted to become production documentation. The key word is enforced — without enforcement, you have discussion, not control.

---

## Why a Pull Request Is More Than Collaboration

It is common to describe Pull Requests as collaboration tools. That description is incomplete.

Collaboration can exist without control. A shared Google Doc allows collaboration — but it does not enforce state transitions. Anyone can edit. Nothing gates what becomes the authoritative version.

A Pull Request can enforce:

| Mechanism | What it does |
|-----------|-------------|
| **Mandatory reviews** | At least one designated reviewer must approve before merge is permitted |
| **Approval thresholds** | A specific number of approvers must sign off |
| **Passing CI checks** | Automated tests, link validation, or linting must complete successfully |
| **Branch protection rules** | Direct pushes to `main` are blocked at the repository level |

These are distinct enforcement mechanisms, not interchangeable options. The right combination depends on your team's risk tolerance and release cadence.

Together, they prevent unvalidated documentation states from entering production.

Collaboration is the interface. Validation is the function.

---

## The Diff — The Engine of Validation

At the core of every Pull Request is a diff — a precise comparison between the proposed state and the current production state.

**Compare the tip of your feature branch to the tip of main:**

```bash
git diff main..feature-branch
```

> **Note on dot syntax:** Two dots (`..`) compares the current tip of both branches directly. Three dots (`...`) compares the feature branch to the common ancestor of both branches, which can produce unexpected output in active repositories. For reviewing proposed changes against current production, use two dots.

Reviewers are not rereading entire documents. They are validating change units — exactly what changed, line by line.

If your commits are atomic, the diff is focused and readable. If your commits are bundled and unfocused, the diff becomes cognitive overload that slows review and increases the chance that errors pass undetected.

Pull Requests make version discipline visible. A diff exposes whether you are thinking in structured states — or just editing files.

---

## Weak vs. Strong Documentation Pull Requests

The difference between a weak and a strong PR is not cosmetic. It determines how quickly a change can be reviewed, and how safely it can be reversed.

---

### Weak Pull Request

**Title:** `updates`

**Description:** `Updated docs for latest changes.`

**Commits inside:**
- Rewrote API introduction
- Fixed 12 typos
- Updated authentication section
- Changed formatting across 4 files
- Added new feature documentation

**Problems:**

- Multiple unrelated concerns bundled into one proposed state
- No explanation of intent — reviewers must infer context from the diff alone
- Difficult to isolate which change introduced a problem
- Reverting requires undoing everything, not just the problematic change
- PR description will appear permanently in the repository history as a meaningless record

---

### Strong Pull Request

**Title:** `docs: align authentication guide with v2 API release`

**Description:** `Updates the authentication documentation to reflect the removal of the authToken parameter in v2. Adds a new example request and updates error response references. No formatting-only changes included.`

**Commits:**

```bash
git commit -m "docs: remove deprecated authToken parameter from v2 API"
git commit -m "docs: add v2 authentication example request"
git commit -m "fix: correct 401 error code description"
```

**What this enables:**

- Scope is immediately clear to any reviewer before they open the diff
- Intent is documented in the PR record permanently — searchable, attributable, traceable
- Diff is focused and readable
- If the v2 release is delayed, this PR can be held or reverted cleanly

---

### Selective Rollback — How It Works in Practice

Because a strong PR represents one logical change, it can be reversed precisely.

**To revert a merge commit:**

```bash
git revert -m 1 <merge-commit-hash>
```

> **Note:** Reverting a merge commit requires the `-m 1` flag, which tells Git to treat the first parent of the merge commit (the `main` branch) as the mainline. Without this flag, Git will return an error because merge commits have more than one parent. Run `git log` to find the merge commit hash.

The smaller and more focused the PR, the more precise the rollback. Reverting a focused PR does not cascade into unrelated changes — only the intended logical unit is reversed.

---

## Enforcement Is What Makes It Governance

A Pull Request only functions as a control gate when enforcement is configured at the repository level.

Without branch protection rules, a PR is optional ceremony. Any contributor can bypass it with a direct push to `main`.

With enforcement in place:

- Required reviewers must approve — merge is blocked until they do
- CI checks must pass — broken links, linting errors, or build failures prevent merge
- Direct pushes to `main` are blocked entirely at the repository level

That gate protects the integrity of the production documentation state. Disciplined teams treat documentation PRs with the same seriousness as code PRs — both modify production-facing artifacts, and both carry the same responsibility.

---

## Common Failure Modes

When PR discipline weakens, documentation systems degrade in predictable ways:

| Failure pattern | Consequence |
|----------------|-------------|
| Treating documentation as low-risk and bypassing review | Errors reach production without validation |
| Bundling formatting, structural, and feature changes in one PR | Reviewers cannot evaluate changes independently |
| Merging large diffs late in a release cycle | Review time is shortest when risk is highest |
| PR descriptions that state what changed without explaining why | Context is lost from the permanent record |

Each pattern increases uncertainty about what a documentation state contains and why it exists. Uncertainty slows review and makes incidents harder to diagnose.

---

## How Technical Writers Strengthen the Control Layer

As a technical writer, your responsibility is not only to write clearly — but to submit clearly structured proposals for documentation state transition.

Before opening a Pull Request, verify:

- Does this PR represent a single logical change?
- Is the intent documented in the description — not just what changed, but why?
- Is the diff focused enough that a reviewer can evaluate it without losing context?
- Would a reviewer understand the full scope without needing to ask clarifying questions?

If the answer to any of these is no, refine the PR before requesting review.

A Pull Request is a proposal to make a new version of your documentation the version your users read. That is the responsibility it carries.

---

## The Progression So Far

| Part | Focus |
|------|-------|
| Part 1 | How Git works — mechanics |
| Part 2 | How documentation moves through a workflow |
| Part 3 | What documentation states are and how versioning structures them |
| Part 4 | How documentation states are validated before reaching production |

The series has moved from mechanics to structure to control. Documentation is no longer treated as editable text outside the engineering lifecycle — it is version-controlled, state-managed, and governed through the same Pull Request discipline that controls production code.

---

## Summary

- A **production documentation state** is merged, deployed, and accessible to users — it is the version users actually read
- A Pull Request transitions a **proposed** state into a **production** state — that transition requires validation, not just submission
- The **diff** is the engine of review — `git diff main..feature-branch` shows exactly what has changed between the proposed and current production state
- **Atomic, focused PRs** are faster to review and safer to revert than bundled ones
- Reverting a merge commit requires `git revert -m 1 <merge-commit-hash>` — the `-m 1` flag is required for merge commits
- **Enforcement** — branch protection rules, required reviewers, CI checks — is what makes a Pull Request function as governance rather than optional ceremony

---

## Next in This Series

→ [Part 5 — CI/CD for Technical Writers: How Documentation Goes from Repository to Live Site](part-5-cicd-pipelines.md)

---
