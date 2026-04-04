# Writing content

This section explains how to write high-quality documentation for MkDocs. It focuses on clarity, structure, and consistency rather than just Markdown syntax.

In real-world documentation, writing is not just about formatting text. It is about helping users complete tasks, understand systems, and find information quickly.

---

## Why writing quality matters

Poorly written documentation leads to:

- increased support requests  
- user confusion and frustration  
- incorrect system usage  
- loss of trust in the product  

High-quality documentation:

- reduces dependency on support teams  
- improves user onboarding  
- enables self-service learning  
- scales across teams and products  

---

## Follow a documentation-first mindset

Before writing content, understand this principle:

> documentation is a product, not a byproduct

This means:

- content should be intentional, not reactive  
- structure should be designed, not improvised  
- consistency should be enforced across pages  

---

## Types of documentation content

Every documentation page should fall into one of these categories.

### Concept

Explains ideas, systems, or features.

**Purpose:**
- help users understand *what* something is and *why* it exists  

**Example:**
- What is MkDocs  
- How static site generation works  

---

### Task (how-to)

Provides step-by-step instructions.

**Purpose:**
- help users complete a specific action  

**Example:**
- Install MkDocs  
- Deploy to GitHub Pages  

---

### Reference

Provides structured, factual information.

**Purpose:**
- act as a lookup resource  

**Example:**
- mkdocs.yml configuration options  
- plugin settings  

---

## Why this classification matters

Mixing content types in a single page leads to:

- confusion  
- poor readability  
- unclear user intent  

Each page should have a **single primary purpose**.

---

## Writing principles (based on Google style guide)

### Use sentence case

- capitalize only the first word and proper nouns  

**Correct:**
- Install MkDocs  
- Configure navigation  

---

### Use clear and direct language

Avoid unnecessary words.

**Avoid:**
> In order to install MkDocs, you need to...

**Use:**
> Install MkDocs using the following command.

---

### Use active voice

**Avoid:**
> The file is created by MkDocs.

**Use:**
> MkDocs creates the file.

---

### Write for scanning

Users do not read documentation line by line. They scan.

Use:

- headings  
- bullet points  
- short paragraphs  

---

## Structuring a documentation page

A well-structured page follows a predictable pattern.

### Recommended structure

1. title  
2. short introduction (what and why)  
3. main content (steps, explanation, or reference)  
4. examples  
5. edge cases or notes  
6. next steps  

---

## Writing task-based content

Task-based documentation is the most common type.

### Example structure

````
## Install MkDocs

Install MkDocs using pip.

### Step 1: activate virtual environment

```
source venv/bin/activate
```

### Step 2: install MkDocs

```
pip install mkdocs
```

````

---

### Best practices for tasks

- use numbered steps for sequences  
- keep steps short and actionable  
- avoid combining multiple actions in one step  

---

## Writing conceptual content

Conceptual content explains systems and ideas.

### Example structure

```markdown
## How MkDocs works

MkDocs converts Markdown files into a static website.

### Key components

- Markdown files  
- mkdocs.yml  
- themes  
````

---

### Best practices for concepts

* focus on clarity, not depth overload
* use examples to reinforce understanding
* avoid implementation details

---

## Writing reference content

Reference content should be structured and scannable.

### Example structure

```markdown
## Configuration options

| Field       | Description                          |
|------------|--------------------------------------|
| site_name  | Name of the documentation site       |
| theme      | Defines the visual appearance        |
```

---

### Best practices for reference

* use tables for structured data
* keep descriptions precise
* avoid storytelling

---

## Writing effective headings

Headings define how users navigate content.

### Good headings

* describe the content clearly
* are specific and actionable

**Examples:**

* Configure navigation
* Install dependencies
* Define project structure

---

### Avoid vague headings

**Avoid:**

* Overview
* Details
* Miscellaneous

---

## Use code blocks effectively

Code blocks should be:

* minimal
* accurate
* directly usable

### Example

```bash
mkdocs serve
```

---

### Best practices

* avoid unnecessary commands
* explain what the command does
* ensure commands are tested

---

## Cross-link related content

Documentation should be connected.

### Example

```markdown
For setup instructions, see [Installation](../installation.md).
```

---

### Why this matters

* improves navigation
* reduces duplication
* creates a cohesive experience

---

## Maintain consistency across pages

Consistency improves usability.

### Maintain consistency in:

* terminology
* formatting
* heading structure
* tone

---

## Real-world writing considerations

### Write for different audiences

Your documentation may be used by:

* developers
* testers
* product managers
* new joiners

Write in a way that is accessible but not oversimplified.

---

### Avoid assumptions

Do not assume:

* prior knowledge
* environment setup
* familiarity with tools

Always provide necessary context.

---

### Keep content modular

Avoid large, monolithic pages.

Instead:

* break content into smaller topics
* link related pages

---

## Content quality checklist

Before publishing a page, verify:

* headings follow sentence case
* content has a clear purpose (concept, task, or reference)
* steps are actionable and complete
* examples are accurate
* terminology is consistent

---

## What’s next

Now that you know how to write high-quality documentation, the next step is to configure your MkDocs project using `mkdocs.yml`.

👉 Go to: **Configuration**

---