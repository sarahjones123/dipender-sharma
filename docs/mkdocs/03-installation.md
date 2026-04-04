# Installation

This section covers how to install MkDocs in a way that is reliable, reproducible, and aligned with real-world development practices.

---

## Step 1: create a project directory

Create a directory for your documentation project:

```bash
mkdir mkdocs-project
cd mkdocs-project
```

---

## Step 2: create a virtual environment

### Create the environment

```bash
python -m venv venv
```

This creates a local environment inside the project directory.

---

### Activate the environment

#### macOS / Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

---

### Verify activation

After activation, your terminal should display the environment name:

```bash
(venv) user@system:~/mkdocs-project
```

This confirms that packages will be installed locally within the project.

---

## Step 3: upgrade pip

Before installing MkDocs, upgrade pip to avoid compatibility issues:

```bash
pip install --upgrade pip
```

---

## Step 4: install MkDocs

Install MkDocs inside the virtual environment:

```bash
pip install mkdocs
```

---

## Step 5: install Material theme

Install the Material theme, which is widely used in production documentation:

```bash
pip install mkdocs-material
```

---

## Why Material theme is used

Material for MkDocs provides:

* modern UI and responsive design
* built-in search and navigation features
* customization options for branding

It eliminates the need to build a custom frontend.

---

## Step 6: verify installation

### Check MkDocs version

```bash
mkdocs --version
```

### Expected output

```bash
mkdocs, version X.X.X
```

---

### Verify theme installation

Run:

```bash
pip list
```

Ensure the following packages are present:

* mkdocs
* mkdocs-material

---

## Step 7: freeze dependencies

Create a `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

### Example output

```
mkdocs==1.5.3
mkdocs-material==9.x.x
```

---

### Why this is critical

* ensures consistent setup across environments
* allows new contributors to install dependencies easily
* supports CI/CD pipelines

---

## Step 8: validate environment setup

Before moving forward, validate your setup.

### Checklist

* virtual environment is activated
* MkDocs is installed
* Material theme is installed
* `requirements.txt` is created

---

## Real-world installation workflow

In a production environment, installation typically follows this flow:

1. clone repository
2. create virtual environment
3. install dependencies using `requirements.txt`
4. start local server

### Example

```bash
git clone <repository-url>
cd project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

---

## Common installation issues

### MkDocs command not found

**Cause:**
virtual environment is not activated or PATH is incorrect

**Fix:**

* activate the virtual environment
* reinstall MkDocs inside the environment

---

### Permission denied errors

**Cause:**
attempting global installation without permissions

**Fix:**

* avoid global installs
* use virtual environments

---

### pip install fails

**Cause:**

* outdated pip
* network issues
* incompatible Python version

**Fix:**

```bash
pip install --upgrade pip
```

---

### Theme not applied

**Cause:**
Material theme installed but not configured

**Fix:**
update `mkdocs.yml`:

```yaml
theme:
  name: material
```

---

## Advanced considerations

### Pin dependency versions

Avoid using latest versions without control.

Example:

```
mkdocs==1.5.3
mkdocs-material==9.5.0
```

This prevents unexpected breaking changes.

---

### Use separate environments per project

Each documentation project should have its own environment.

This avoids:

* plugin conflicts
* version mismatches

---

### Prepare for CI/CD

Ensure that:

* `requirements.txt` is committed
* no global dependencies are required
* setup can be reproduced using a single command

---

## What’s next

Now that MkDocs is installed and verified, the next step is to create a project and understand its structure.

👉 Go to: **Project setup**


---
