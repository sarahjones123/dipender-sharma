# Project setup

This section explains how to create and structure a MkDocs project in a way that is scalable, maintainable, and aligned with real-world documentation systems.

Most tutorials stop at running a single command (`mkdocs new`). While that creates a working project, it does not explain how to structure documentation for long-term growth.

This guide focuses on building a foundation that works for real teams and production environments.

---

## Create a new MkDocs project

### Command

````

mkdocs new my-docs
cd my-docs

````

---

## What this command actually does

Running `mkdocs new` generates a minimal project structure:

```
my-docs/
├── docs/
│   └── index.md
└── mkdocs.yml
```

This is intentionally simple, but it is not sufficient for real-world use.

---

## Understand the default structure

Before modifying the project, it is important to understand each component.

### docs/

This directory contains all documentation content.

* all Markdown files live here
* supports nested folders for organizing topics
* serves as the source of truth for your documentation

---

### index.md

This is the default homepage of your documentation site.

* rendered as the landing page
* should provide an overview of your documentation
* acts as an entry point for users

---

### mkdocs.yml

This is the configuration file that controls your entire documentation system.

It defines:

* site metadata (name, description)
* navigation structure
* theme configuration
* plugins and extensions

This file determines how your documentation is presented to users.

---

## Why the default structure is not enough

The default structure works for small demos, but it breaks down as documentation grows.

Common problems:

* flat structure becomes difficult to navigate
* topics are not logically grouped
* scaling leads to clutter and inconsistency

To avoid this, you need a structured approach from the beginning.

---

## Design a scalable documentation structure

A production-ready structure separates content into logical domains.

### Recommended structure

```
my-docs/
├── docs/
│   ├── index.md
│   ├── mkdocs/
│   │   ├── introduction.md
│   │   ├── prerequisites.md
│   │   ├── installation.md
│   │   └── project-setup.md
│   ├── git/
│   │   ├── introduction.md
│   │   ├── basics.md
│   │   └── branching.md
│   └── assets/
│       └── images/
├── mkdocs.yml
├── requirements.txt
└── .github/
    └── workflows/
        └── deploy.yml
```

---

## Why this structure works

### Logical grouping of topics

* separates MkDocs and Git into independent sections
* improves discoverability
* reduces cognitive load for users

---

### Scalability

* supports adding new sections without restructuring existing content
* prevents flat navigation issues

---

### Maintainability

* makes it easier for multiple contributors to work independently
* reduces merge conflicts

---

### Alignment with real projects

This structure mirrors how documentation is organized in production systems.

---

## Organize content using directories

### Topic-based grouping

Each folder represents a topic or domain.

Example:

```
docs/mkdocs/
docs/git/
```

This allows:

* clear separation of concerns
* independent evolution of topics

---

### File naming conventions

Use consistent, descriptive file names:

* `introduction.md`
* `installation.md`
* `deployment.md`

Avoid:

* generic names like `doc1.md`
* inconsistent naming patterns

---

## Configure navigation in mkdocs.yml

After organizing files, define navigation explicitly.

### Example configuration

```yaml
site_name: Documentation portal

nav:
  - Home: index.md
  - MkDocs:
      - Introduction: mkdocs/introduction.md
      - Prerequisites: mkdocs/prerequisites.md
      - Installation: mkdocs/installation.md
      - Project setup: mkdocs/project-setup.md
  - Git:
      - Introduction: git/introduction.md
      - Basics: git/basics.md
      - Branching: git/branching.md
```

---

## Why explicit navigation is important

* ensures predictable structure
* prevents accidental ordering issues
* improves user experience

Without explicit navigation, MkDocs may generate structure based on file order, which is not reliable.

---

## Add assets directory

Create a dedicated directory for static assets:

```
docs/assets/images/
```

### Why this matters

* keeps content and assets organized
* prevents clutter in content directories
* makes it easier to manage images and diagrams

---

## Real-world repository considerations

### Include requirements.txt

This file defines project dependencies.

Example:

```
mkdocs==1.5.3
mkdocs-material==9.5.0
```

---

### Add CI/CD configuration

Create a workflow file:

```
.github/workflows/deploy.yml
```

This enables:

* automatic builds
* automatic deployment

---

### Keep documentation close to code (optional)

In some projects, documentation is stored alongside application code.

Example:

```
project-root/
├── src/
├── docs/
├── mkdocs.yml
```

This ensures documentation evolves with the product.

---

## Validate your project structure

Before proceeding, verify the following:

* directories are logically organized
* file names are consistent
* navigation is defined in `mkdocs.yml`
* assets are stored separately

---

## Common mistakes to avoid

### Flat structure

Avoid placing all files directly under `docs/`.

---

### Missing navigation configuration

Do not rely on automatic navigation generation.

---

### Mixing unrelated topics

Keep domains separate (for example, Git vs MkDocs).

---

### Poor naming conventions

Inconsistent naming leads to confusion and poor maintainability.

---

## What’s next

Now that your project structure is ready, the next step is to start writing high-quality documentation content using Markdown.

👉 Go to: **Writing content**

---