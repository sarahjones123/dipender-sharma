# Part 1: Git Basics for Technical Writers

This article explains Git fundamentals in plain language for technical writers, documentation specialists, and non-developers who need to work confidently in Git-based environments.

No prior experience with Git or the command line is assumed.

By the end of this article you will understand:

- What Git is and what problem it solves
- The three stages Git uses to track changes
- The core concepts every technical writer needs to know
- The essential commands for a basic documentation workflow
- How Git differs from GitHub

---

## Why This Matters — A Real Scenario

Imagine you are updating a product guide while a developer is fixing bugs in the same repository.

Without Git, one of you could overwrite the other's work. There is no history of what changed, no way to recover an earlier version, and no structured process for reviewing updates before they go live.

With Git, both of you work in parallel on separate branches. Every change is recorded with a clear message. Nothing is published until it has been reviewed and approved.

This is why Git is essential for technical writers working in modern, collaborative documentation environments.

---

## What Is Git?

Git is a **distributed version control system** — a tool that records changes to files over time and allows multiple people to work on the same project without overwriting each other's work.

With Git, you can:

- See exactly what changed in a document, line by line
- Understand who made each change and when
- Restore any earlier version of a file at any point
- Experiment safely without affecting the published version
- Collaborate with developers using the same workflow they already use

Unlike cloud tools such as Google Docs, Git works **locally on your computer**. You control when changes are saved and when they are shared with the rest of the team.

---

## Why Git Matters for Technical Writers

Git is not a developer-only tool. For technical writers, it enables:

- **Version history** — every edit is recorded and recoverable
- **Safe collaboration** — multiple contributors without file conflicts
- **Structured reviews** — changes are proposed and approved before publication
- **Docs-as-Code workflows** — documentation treated with the same rigour as software

Using Git turns documentation from a collection of files scattered across folders and drives into a **managed, auditable system**.

---

## Core Concepts

### Repository

A repository — commonly called a **repo** — is a project folder tracked by Git. It contains:

- Your documentation files
- A hidden `.git` directory that stores the complete change history

Think of a repository as the permanent home of your documentation project. Everything related to that project — files, history, branches, contributors — lives inside it.

---

### Commit

A commit is a **saved snapshot** of your project at a specific point in time.

Each commit has:

- A unique identifier
- The name of the person who made the change
- A timestamp
- A message describing what changed and why

For technical writers, commits function as documented editing milestones. You can return to any commit and see exactly what the documentation looked like at that moment.

A good commit message answers one question: *what does this change do?*

```
# Too vague
git commit -m "Update"

# Clear and useful
git commit -m "Clarify authentication steps in API quickstart guide"
```

---

### Branch

A branch is an **independent line of work** within a repository.

When you create a branch, you get a separate copy of the documentation to work on. Changes on your branch do not affect the main version until they are reviewed and approved.

Common branch names you will encounter:

| Branch | Purpose |
|--------|---------|
| `main` | The stable, published version of the documentation |
| `feature/update-api-guide` | Work in progress on a specific section |
| `fix/broken-links` | A targeted correction |

Branches allow you to work on multiple updates simultaneously without interference.

---

### The Three Stages of Git

This is the concept most beginners find confusing. Git tracks changes across three distinct stages:

```
Working Directory → Staging Area → Repository
```

| Stage | What it is | What happens here |
|-------|-----------|-------------------|
| **Working Directory** | Your local files | You edit documentation here |
| **Staging Area** | A preparation zone | You select which changes to include in the next commit |
| **Repository** | The permanent record | Committed snapshots are stored here |

The staging area gives you deliberate control over what gets saved. You can edit ten files but commit only three — staging lets you make that selection before anything is permanently recorded.

---

## Essential Commands

> **Note:** These commands are run in your terminal (Mac/Linux) or command prompt (Windows). If you have not opened a terminal before, search for "Terminal" on Mac or "Command Prompt" on Windows to get started.

---

### Initialise a Repository

```bash
git init
```

Creates a new Git repository in the current folder. Run this once when starting a new documentation project.

---

### Check Status

```bash
git status
```

Shows which files have been modified, which are staged, and which are untracked. This is the safest command to run at any point — it tells you exactly where you are without changing anything.

Run `git status` frequently, especially before committing.

---

### Stage Files

```bash
# Stage a specific file
git add filename.md

# Stage all changed files
git add .
```

Moves changes from your working directory into the staging area. Use `git add .` carefully — review what you are staging before using it.

---

### Commit Changes

```bash
git commit -m "Add Git basics documentation for technical writers"
```

Creates a permanent snapshot of everything in the staging area. The message in quotes is your commit message — make it specific and descriptive.

---

### View History

```bash
git log
```

Displays the full commit history of the project — author, timestamp, and message for every commit. Use this to understand what has changed and when.

---

### Push to a Remote Repository

```bash
git push origin main
```

Uploads your committed changes to the remote repository on GitHub, making them visible to your team.

---

## Git vs GitHub

These two tools are frequently confused. They are not the same thing.

| | Git | GitHub |
|--|-----|--------|
| **What it is** | Version control system | Cloud hosting platform |
| **Where it runs** | Locally on your machine | In the cloud |
| **Primary function** | Tracks and records changes | Stores repos and enables collaboration |
| **Internet required** | No — works offline | Yes |
| **Who made it** | Linus Torvalds, 2005 | GitHub Inc., 2008 |

You use Git to manage changes to your documentation.
You use GitHub to store those changes online and collaborate with others.

Git can exist without GitHub. GitHub cannot exist without Git.

---

## What to Ignore for Now

As a technical writer getting started with Git, you do not need to understand the following yet:

- **Rebasing** — reorganising commit history
- **Stashing** — temporarily shelving uncommitted changes
- **Cherry-picking** — applying individual commits across branches
- **Merge conflicts** — resolving competing changes between branches

Focus on repositories, commits, branches, and the basic workflow. Everything else builds on that foundation and will be introduced when it is relevant.

---

## Common Mistakes and How to Avoid Them

| Mistake | Why it matters | How to avoid it |
|---------|---------------|-----------------|
| Vague commit messages | Future you — and your team — cannot understand what changed | Always describe *what* the change does, not just *that* it changed |
| Committing everything blindly | Unintended changes end up in the permanent record | Run `git status` before every commit |
| Working directly on `main` | Errors go live immediately without review | Always create a branch for new work |
| Large infrequent commits | Hard to review and hard to reverse | Commit small, logical units of work |

---

## Best Practices for Technical Writers

- Commit small, focused changes — one logical update per commit
- Write commit messages that describe the change, not just the file
- Use Markdown for all documentation files
- Keep `main` clean — only merge reviewed, approved changes
- Run `git status` before staging and before committing
- Pull the latest version before starting new work to avoid conflicts

---

## Summary

This article covered the foundational concepts of Git for technical writers:

- **Git** is a version control system that records changes to files over time, locally on your machine
- A **repository** is the tracked home of your documentation project — files, history, and contributors all in one place
- A **commit** is a permanent snapshot with a descriptive message — your documentation audit trail
- A **branch** is an independent line of work that keeps changes separate until reviewed and approved
- Git tracks changes across three stages: **Working Directory → Staging Area → Repository**
- The essential commands for a basic workflow are `git status`, `git add`, `git commit`, `git log`, and `git push`
- **Git** manages changes locally; **GitHub** stores and shares them in the cloud — they are not the same tool

---

## Next in This Series

→ [Part 2 — Git vs GitHub: Understanding the Documentation Workflow](part-2-git-vs-github.md)

---
