# Plugins

This section explains how to extend MkDocs functionality using plugins. Plugins allow you to enhance your documentation system beyond its default capabilities.

In real-world projects, plugins are used to improve usability, automate workflows, and add advanced features. However, they must be used carefully to avoid complexity and maintenance issues.

---

## What are plugins in MkDocs

Plugins are extensions that modify or enhance the behavior of MkDocs during the build process.

They can:

- add new features (for example, search or macros)  
- modify content dynamically  
- improve navigation and structure  
- integrate external systems  

Plugins are configured in the `mkdocs.yml` file.

---

## Add plugins to mkdocs.yml

### Basic configuration

```yaml
plugins:
  - search
```

---

### Multiple plugins

```yaml
plugins:
  - search
  - macros
```

---

## Core plugins you should use

### Search plugin (default)

```yaml
plugins:
  - search
```

---

### Why search is essential

* users prefer searching over browsing
* improves discoverability of content
* reduces navigation dependency

---

## mkdocs-macros-plugin

### Installation

```
pip install mkdocs-macros-plugin

```

---

### Configuration

```yaml
plugins:
  - macros
```

---

### What it does

Allows you to use variables and dynamic content in Markdown.

---

### Example

```markdown
Project version: {{ version }}
```

---

## mkdocs-awesome-pages-plugin

### Installation

```
pip install mkdocs-awesome-pages-plugin

```

---

### What it does

* automatically generates navigation based on file structure
* allows better control using `.pages` files

---

### When to use it

Use it when:

* documentation grows large
* manual navigation becomes difficult to maintain

---


## mkdocs-minify-plugin

### Installation

```bash
pip install mkdocs-minify-plugin
```

---

### What it does

* compresses HTML output
* reduces page size

---

## Plugin selection strategy

Choosing plugins is not about adding as many as possible.

### Use plugins when:

* there is a clear functional need
* the benefit outweighs the complexity

---

### Avoid plugins when:

* the feature is not essential
* it introduces unnecessary dependencies
* it complicates the build process

---

## Validation checklist

Before proceeding:

* required plugins are installed
* plugins are configured in `mkdocs.yml`
* versions are pinned in `requirements.txt`
* no unnecessary plugins are included

---

## What’s next

Now that you understand how to extend MkDocs using plugins, the next step is to run and validate your documentation locally.

👉 Go to: **Local development**

---
