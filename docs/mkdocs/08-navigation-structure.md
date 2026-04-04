# Navigation structure

This section explains how to design and implement an effective navigation structure in MkDocs. Navigation is one of the most critical aspects of documentation because it determines how users discover and access information.

In real-world documentation systems, navigation is not an afterthought. It is a deliberate design decision based on user behavior, content structure, and scalability requirements.

---

## Navigation in MkDocs

Navigation is defined in the `mkdocs.yml` file using the `nav` field.

### Example

```yaml
nav:
  - Home: index.md
  - MkDocs:
      - Introduction: mkdocs/introduction.md
      - Installation: mkdocs/installation.md
```

This configuration controls:

* sidebar structure
* page hierarchy
* ordering of content

---

## Navigation vs file structure

It is important to understand that:

> file structure and navigation structure are not the same

### File structure

* how files are organized in directories
* optimized for maintainability

### Navigation structure

* how content is presented to users
* optimized for usability

You should design both independently but keep them aligned.

---

## Designing navigation for this project

Given your documentation includes Git and MkDocs, structure navigation by domain.

### Recommended structure

```yaml
nav:
  - Home: index.md

  - MkDocs:
      - Introduction: mkdocs/introduction.md
      - Prerequisites: mkdocs/prerequisites.md
      - Installation: mkdocs/installation.md
      - Project setup: mkdocs/project-setup.md
      - Writing content: mkdocs/writing-content.md
      - Configuration: mkdocs/configuration.md
      - Theming: mkdocs/theming-material.md
      - Navigation: mkdocs/navigation-structure.md

  - Git:
      - Introduction: git/introduction.md
      - Basics: git/basics.md
      - Branching: git/branching.md
```

---

## Why this structure works

### Domain-based grouping

* separates MkDocs and Git into independent sections
* improves clarity and discoverability

---

### Logical progression

MkDocs topics follow a natural flow:

1. introduction
2. setup
3. usage
4. advanced topics

---

### Scalability

New topics can be added without restructuring existing navigation.

---

## Multi-level navigation

MkDocs supports nested navigation.

### Example

```yaml
nav:
  - MkDocs:
      - Getting started:
          - Introduction: mkdocs/introduction.md
          - Installation: mkdocs/installation.md
      - Advanced:
          - Configuration: mkdocs/configuration.md
          - Theming: mkdocs/theming-material.md
```

---

## When to use multi-level navigation

Use nested navigation when:

* content grows beyond a manageable size
* topics can be logically grouped into subcategories

---

## When to avoid deep nesting

Avoid more than three levels:

* reduces usability
* increases navigation complexity

---

## Ordering navigation

Navigation order should reflect user intent.

### Common patterns

* beginner → advanced
* setup → usage → deployment
* conceptual → practical

---

## Navigation anti-patterns

### Flat navigation

Too many items at the same level:

* overwhelms users
* reduces clarity

---

### Over-nested navigation

Too many levels:

* makes navigation difficult
* hides important content

---

### Inconsistent labeling

Mixing styles:

* "Install MkDocs"
* "Setup"
* "How to configure"

This creates confusion.

---

## Improving navigation with Material features

Material theme enhances navigation with features such as:

### Navigation sections

```yaml
theme:
  features:
    - navigation.sections
```

---

### Tabs

```yaml
theme:
  features:
    - navigation.tabs
```

---

### Why these features matter

* improve visual hierarchy
* make navigation easier to scan
* enhance user experience

---

## Cross-linking vs navigation

Navigation is not the only way users move through documentation.

### Use cross-links for:

* related topics
* prerequisite steps
* deeper explanations

---

### Example

```markdown
See [Installation](../installation.md) for setup instructions.
```

---


## Validation checklist

Before finalizing navigation:

* structure is shallow and intuitive
* labels are clear and consistent
* related content is grouped together
* navigation matches user workflows

---

## What’s next

Now that navigation is structured correctly, the next step is to extend functionality using plugins.

👉 Go to: **Plugins**

---