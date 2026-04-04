# Part 2: Git vs GitHub — Understanding the Documentation Workflow

---

## Overview

In Part 1, we covered Git fundamentals — how it tracks changes, records commits, and allows you to work safely on your local machine.

This article moves from local version control to collaborative workflow.

By the end of this article you will understand:

- The precise difference between Git and GitHub
- How documentation moves from private draft to shared production
- The four-phase workflow technical writers follow in Docs-as-Code environments
- The commands that connect your local machine to your team

---

## The Problem This Article Solves

You can write clean commits.
You can create organised branches.
You can maintain a complete local history.

But if your documentation never leaves your laptop, collaboration never begins.

This is where GitHub enters the picture.

Understanding the difference between Git and GitHub is not about comparing tools. It is about understanding how documentation moves from private draft to shared production.

---

## Git vs GitHub — The Clear Distinction

| Function | Git | GitHub |
|----------|-----|--------|
| Tracks file changes | ✔ | |
| Records version history | ✔ | |
| Works offline | ✔ | |
| Stores repository online | | ✔ |
| Enables team collaboration | | ✔ |
| Manages Pull Requests | | ✔ |
| Provides review tools | | ✔ |

Git manages change history on your local machine.
GitHub manages team workflow in the cloud.

Both are necessary in a professional documentation workflow. Git can exist without GitHub. GitHub cannot exist without Git.

---

## The Documentation Workflow: From Laptop to Live

This is the practical sequence technical writers follow in Docs-as-Code environments. Each phase has a clear purpose and a defined boundary.

---

### Phase 1 — Local Drafting

You begin on your local machine.

```bash
# Edit your Markdown files, then stage and commit your changes
git add filename.md
git commit -m "Add authentication section to API quickstart guide"
```

At this stage, your work is entirely private. No one else can see it. This is your structured drafting environment — version-controlled and recoverable at any point.

---

### Phase 2 — Push to GitHub

When you are ready to share your work, push your branch to the remote repository:

```bash
git push origin branch-name
```

> **What `git push` does:** It uploads the commits from your local branch to the matching branch on GitHub, making your work visible to the rest of your team for the first time.

After pushing:

- Your team can see your branch
- Your changes are backed up online
- Collaboration becomes possible

Your documentation has moved from local draft to shared workspace.

---

### Phase 3 — Pull Request and Review

A **Pull Request (PR)** is a formal proposal to merge your branch into the `main` version of the documentation. This is where GitHub becomes essential to the workflow.

Inside a Pull Request, your team can:

- View the **Diff** — a line-by-line comparison where additions appear in green and deletions in red
- Leave comments on specific lines
- Suggest edits directly in the file
- Approve the changes or request revisions

The Diff is particularly powerful for documentation review. It isolates exactly what changed, which allows reviewers to focus on the delta rather than rereading the entire document.

For technical writers, this replaces the cycle of emailing documents back and forth. Discussion happens directly around the content — transparently, traceably, and permanently recorded in the repository history.

---

### Phase 4 — Merge to Main

Once a Pull Request is reviewed and approved, it is merged into the `main` branch.

At this point:

- Your changes become part of the official documentation
- The repository history updates permanently
- The team works from the new version going forward

In many Docs-as-Code environments, merging to `main` automatically triggers a CI/CD pipeline that rebuilds and publishes the live documentation site. Merge often equals publish.

Documentation has now completed its full journey:

```
Draft → Reviewed → Approved → Production
```

---

## The End-to-End Workflow

```
Edit → Commit → Push → Pull Request → Review → Merge
```

| Stage | Purpose |
|-------|---------|
| **Edit** | Create or update documentation content |
| **Commit** | Record intentional changes with a descriptive message |
| **Push** | Share your branch with the team on GitHub |
| **Pull Request** | Formally propose your changes for review |
| **Review** | Validate accuracy, clarity, and completeness |
| **Merge** | Publish approved content to the main version |

---

## Why This Workflow Matters

Before Git and GitHub workflows, documentation commonly lived in shared drives, email threads, and Google Docs with unclear version history.

The result was predictable:

- Conflicting versions with no clear source of truth
- Approvals that were verbal or buried in email chains
- Edits lost between versions
- Persistent confusion about what was final

With Git and GitHub:

| Problem | How Git and GitHub solve it |
|---------|----------------------------|
| Conflicting versions | Every change is recorded on a named branch |
| Unclear approvals | Pull Requests require explicit review and approval |
| Lost edits | Every commit is permanent and recoverable |
| No source of truth | `main` is always the authoritative version |

The result is documentation that is controlled, traceable, and intentional at every stage.

---

## Essential Commands for This Workflow

### Pull the Latest Version

```bash
git pull
```

> **What `git pull` does:** It downloads the latest commits from the remote repository on GitHub and merges them into your current local branch. Always run this before starting new work to ensure you are working from the most current version of the documentation.

---

### Create a New Branch

```bash
git checkout -b feature/update-api-guide
```

> **What this does:** `git checkout` switches branches. The `-b` flag creates a new branch before switching to it. The name after `-b` is your branch name — use something descriptive that identifies the work you are doing.

Never commit directly to `main`. Always create a branch for new work.

---

### Push a Branch to GitHub

```bash
git push origin branch-name
```

Uploads your committed changes to GitHub. Replace `branch-name` with the name of your branch.

---

### Check What Has Changed

```bash
git status
```

Run this before every `git add` and before every `git commit`. It tells you exactly what is modified, what is staged, and what is untracked — without changing anything.

---

## Common Mistakes and How to Avoid Them

| Mistake | Consequence | How to avoid it |
|---------|-------------|-----------------|
| Not running `git pull` before starting work | You edit an outdated version and create conflicts | Run `git pull` at the start of every working session |
| Pushing directly to `main` | Unreviewed changes go live immediately | Always work on a named branch |
| Vague commit messages | Version history becomes meaningless | Describe what the change does, not just that it happened |
| Oversized Pull Requests | Hard to review, more likely to introduce errors | Keep each PR focused on one logical documentation unit |

---

## Summary

- **Git** manages version history locally — commits, branches, and change records on your machine
- **GitHub** manages collaboration in the cloud — storage, review, and team workflow
- Documentation moves through four phases: **Draft → Reviewed → Approved → Production**
- The end-to-end sequence is: **Edit → Commit → Push → Pull Request → Review → Merge**
- `git pull` retrieves the latest version from GitHub before you begin work
- `git checkout -b branch-name` creates a new branch for safe, independent work
- Pull Requests replace informal review cycles with a structured, traceable process
- Merging to `main` is the publication step — in many environments it triggers automatic deployment

---

## Next in This Series

→ [Part 3 — From Editing Files to Managing Versions](part-3-versioning.md)

---