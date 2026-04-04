# Local development

This section explains how to run, validate, and debug your MkDocs project locally. Local development is a critical part of the documentation workflow because it allows you to verify changes before publishing them.

In real-world projects, local development is not just about previewing content. It is about ensuring correctness, consistency, and stability before deployment.

---

## Why local development matters

Skipping local validation can lead to:

- broken navigation  
- rendering issues  
- missing assets  
- deployment failures  

A proper local development workflow ensures that issues are caught early and resolved quickly.

---

## Start the local development server

### Command

```
mkdocs serve

```


When you run `mkdocs serve`, MkDocs:

1. builds the documentation site
2. starts a local web server
3. watches for file changes
4. automatically reloads the browser

---

## Access the local site

By default, the site is available at:

```
http://127.0.0.1:8000
```

Open this URL in your browser to preview your documentation.

---

## Live reload workflow

One of the most powerful features of MkDocs is live reload.

### How it works

* you edit a Markdown file
* MkDocs detects the change
* the site is rebuilt automatically
* the browser refreshes

---

### Why this matters

* reduces feedback loop time
* improves writing efficiency
* allows rapid iteration

---

## What to validate during local development

Local development is not just about viewing content. You should actively validate the following.

---

### Navigation

* all pages appear in the correct order
* links are working correctly
* no missing or broken entries

---

### Content rendering

* headings are formatted correctly
* code blocks render properly
* tables display as expected

---

### Links

* internal links resolve correctly
* no broken references
* cross-links navigate properly

---

### Assets

* images load correctly
* paths are valid
* no missing files

---

### Theme and UI

* colors and fonts are applied correctly
* navigation is usable
* layout is responsive

---

## Use strict mode for validation

### Command

```bash
mkdocs serve --strict
```

---

## What strict mode does

Strict mode treats warnings as errors.

This helps identify:

* broken links
* missing files
* configuration issues

---

### Why this is important

In production systems, warnings often lead to user-facing issues. Strict mode ensures higher quality and reliability.

---


## Validation checklist

Before proceeding:

* site runs locally without errors
* navigation is correct
* content renders properly
* no broken links or missing assets
* strict mode passes without issues

---

## What’s next

Now that you can run and validate your documentation locally, the next step is to deploy it using GitHub Pages.

👉 Go to: **Deployment using GitHub Pages**

---