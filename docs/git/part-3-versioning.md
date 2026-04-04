# Part 3: From Editing Files to Managing Versions

In Part 2, we mapped how documentation moves through a workflow system — from draft to production — and how Git and GitHub coordinate that movement.

This article goes deeper into the structural layer underneath that workflow.

What moves through the system is not just text. It is **versioned state**.

By the end of this article you will understand:

- Why Git thinks in changesets rather than files
- What a documentation state is and why it matters
- How atomic commits reduce review friction and protect history
- How `git revert` works structurally — not just conceptually
- The discipline that aligns documentation with a development team's release cycle

---

## The Real Shift: Files vs Versions

Most writers think in files.

- "I updated the installation guide."
- "I revised the API page."
- "I fixed a section."

Git does not think in files. Git thinks in **changesets**.

For every change, Git records:

- What changed
- Why it changed
- When it changed
- Who changed it

The unit of thinking moves from file editing to version management. That shift is foundational to working effectively in a Docs-as-Code environment.

---

## Editing Is Linear. Versioning Is Structured.

**Traditional editing workflow:**

```
File → Modify → Save → Overwrite
```

**Version-controlled workflow:**

```
Edit → Stage → Commit → Compare → Review → Merge
```

In the traditional workflow, saving a file replaces its previous state. There is no history, no recovery point, no record of intent.

In the version-controlled workflow, you are not replacing content. You are creating a structured timeline of intentional states. Each commit is a checkpoint — a snapshot of the entire documentation system at a specific moment in time.

Git stores these checkpoints in a connected sequence where every commit references the one before it. Each commit represents:

- A snapshot of the complete documentation at that moment
- A recorded decision with a descriptive message
- A historical reference point
- A recoverable state

Documentation becomes temporal — structured in time, not just in folders. This is what makes it possible to trace every change, understand why it was made, and reverse it if necessary.

---

## What Is a Documentation State?

A **documentation state** is the complete, versioned snapshot of your documentation at a specific commit.

It is not a single file. It is not a paragraph. It is the entire documentation system as it existed at that moment in history.

**View the history of documentation states:**

```bash
git log
```

Each entry in `git log` represents a distinct documentation state — a moment when someone made a deliberate, recorded change.

**Compare your current working state with the last commit:**

```bash
git diff
```

This command shows exactly how the current state differs from the previous one — line by line, addition by addition, deletion by deletion.

Thinking in states changes how you approach editing. Instead of asking *"Did I update the file?"* you begin asking *"What new state am I creating?"* That question aligns documentation work with how software releases are versioned and managed.

---

## Atomic Change: A Workflow Discipline

Atomic change means a single commit represents **one logical unit of work**.

Not one file. Not one page. One intention.

**Non-atomic commit — avoid this:**

```bash
git commit -m "update docs for release"
```

Inside that single commit might be:

- A deprecated API parameter removed
- Formatting corrected throughout
- A new onboarding section added
- A broken link fixed

From a reviewer's perspective, this creates real problems. Which change relates to the feature? Which one introduced risk? Which change can be safely reverted without affecting the others?

**Atomic commits — use this pattern instead:**

```bash
git commit -m "docs: remove deprecated 'authToken' parameter from v2 API"
git commit -m "fix: resolve broken link in troubleshooting guide"
git commit -m "docs: add onboarding prerequisites section"
```

Each commit isolates a single decision. Each one can be reviewed, understood, and reversed independently.

---

### Conventional Commits

The examples above follow the **Conventional Commits** specification — a standard that uses consistent prefixes to make commit history both human-readable and machine-readable.

Common prefixes used in documentation:

| Prefix | When to use it |
|--------|---------------|
| `docs:` | Adding or updating documentation content |
| `fix:` | Correcting errors, broken links, or inaccurate information |
| `feat:` | Documenting a new feature |
| `chore:` | Maintenance tasks — formatting, file reorganisation |
| `refactor:` | Restructuring content without changing meaning |

Adopting this convention makes your commit history searchable, filterable, and immediately interpretable by any developer on your team.

---

### Why Atomic Commits Matter Operationally

Atomic commits produce:

- A cleaner `git log` that is meaningful at a glance
- Faster Pull Request review — reviewers evaluate one change at a time
- Precise rollback — a single commit can be reversed without affecting unrelated changes
- Fewer merge conflicts — smaller, focused changes are less likely to overlap
- A clear audit trail for documentation decisions

They transform documentation from a collection of edits into a sequence of controlled, attributable state transitions.

---

## Reversibility Is Structural

Version control makes changes reversible — not because it feels safe, but because of how it is built.

Git does not overwrite history. Every commit references the one before it. Every state is preserved.

**To reverse a specific documentation state:**

```bash
git revert <commit-hash>
```

`git revert` does not delete the original commit. It creates a **new commit** that applies the inverse of the specified change. The previous state remains in the history, intact and recoverable.

This guarantees:

- Mistakes are traceable — you can find exactly when and why a change was made
- Bad changes are reversible — without destroying surrounding history
- History remains intact — no information is silently lost
- Rollbacks are targeted — you reverse one decision, not everything since

Over time, this structural safety changes how writers approach documentation. Reversibility enables confident refactoring because every state is preserved and every decision is recoverable.

> **Note:** To find the commit hash you want to revert, run `git log` and copy the hash from the relevant commit entry.

---

## A Practical Discipline to Start Today

To build version thinking into your daily workflow:

1. Make smaller commits — one logical change per commit
2. Separate unrelated changes — do not bundle formatting fixes with content updates
3. Write precise commit messages using Conventional Commits prefixes
4. Run `git diff` before committing to review exactly what you are about to record
5. Ask before every commit: *What new documentation state am I creating?*

If the answer to that question is unclear, the commit contains too many changes. Split it.

---

## Why This Matters in Fast-Moving Teams

In teams shipping weekly — or daily — documentation drift is a real operational risk.

| Without version discipline | With version discipline |
|---------------------------|------------------------|
| Docs fall behind code changes | Every change is logged against a specific moment |
| Context disappears over time | Every state is recoverable |
| Reviews slow down — too much to evaluate at once | Atomic commits make reviews faster and more focused |
| History becomes noisy and unusable | Commit history becomes a meaningful audit trail |
| Unclear what version of docs matches what version of product | Every documentation state is traceable to a point in time |

Version discipline is what keeps documentation aligned with a fast-moving product — not through effort alone, but through structure.

---

## Summary

- Git thinks in **changesets**, not files — every commit records what changed, why, when, and by whom
- A **documentation state** is the complete snapshot of your documentation at a specific commit — not a file, the entire system
- `git log` shows the history of documentation states; `git diff` shows how one state differs from another
- **Atomic commits** — one logical unit of work per commit — reduce review friction, enable precise rollback, and produce a meaningful audit trail
- **Conventional Commits** prefixes (`docs:`, `fix:`, `feat:`) make commit history readable and searchable
- `git revert` creates a new commit that reverses a previous one — it preserves history rather than deleting it
- Version discipline keeps documentation aligned with fast-moving development teams

---

## Next in This Series

→ [Part 4 — Pull Requests: Controlling Documentation State](part-4-pull-requests.md)

---
