# Prerequisites

This section ensures that your environment is correctly set up before working with MkDocs. Instead of only listing tools to install, it focuses on validating your setup and avoiding common issues that occur in real-world projects.

A properly configured environment reduces setup friction, prevents deployment failures, and ensures that your documentation workflow remains stable across systems.

---

## Overview of required tools

To work with MkDocs, you need the following:

- Python (3.8 or later)  
- pip (Python package manager)  
- Git (version control system)  
- GitHub account (for hosting and deployment)  
- Code editor (recommended: VS Code)  

Each of these tools plays a specific role in the documentation workflow.

---

## Why these tools are required

Understanding *why* each tool is needed helps you troubleshoot issues later.

### Python

MkDocs is a Python-based tool distributed as a package. Python is required to:

- install MkDocs and plugins  
- run the local development server  
- build the static site  

Without Python, MkDocs cannot function.

---

### pip

pip is used to install and manage Python packages.

You will use pip to:

- install MkDocs  
- install themes such as Material  
- install plugins  

---

### Git

Git is used to manage version control for your documentation.

It enables:

- tracking changes to documentation files  
- collaborating through pull requests  
- maintaining version history  

---

### GitHub

GitHub is used for:

- hosting your repository  
- deploying documentation using GitHub Pages  
- running CI/CD pipelines  

---

### Code editor

A code editor is required to write and manage Markdown files.

Recommended features:

- Markdown preview  
- syntax highlighting  
- Git integration  

---

## Install and validate Python

### Step 1: check if Python is installed

Run the following command:

```
python --version

```

or:

```
python3 --version
```

### Expected result

You should see a version output such as:

```
Python 3.10.5
```

---

### Step 2: verify pip installation

Run:

```bash
pip --version
```

or:

```bash
pip3 --version
```

### Expected result

You should see pip version details along with the Python version.

---

### Common issues and fixes

#### Python not recognized

If you see an error like:

```
'python' is not recognized as an internal or external command
```

**Cause:**
Python is not added to the system PATH.

**Fix:**

* reinstall Python and enable "Add Python to PATH"
* or manually add Python to environment variables

---

#### Multiple Python versions

If your system has multiple Python versions:

* use `python3` instead of `python`
* consider using virtual environments (covered later in the series)

---

## Install and validate Git

### Step 1: check Git installation

Run:

```bash
git --version
```

### Expected result

```
git version 2.x.x
```

---

### Step 2: configure Git

Set your username and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

### Why this matters

Every commit in your repository is associated with a user identity. Without configuration:

* commits may fail
* authorship tracking becomes inconsistent

---

### Step 3: verify configuration

Run:

```bash
git config --list
```

Ensure your name and email are correctly set.

---

## Set up GitHub account

### Why GitHub is required

GitHub is used to:

* host your documentation repository
* enable GitHub Pages for deployment
* run CI/CD workflows

---

### Recommended setup

* create a GitHub account
* enable two-factor authentication (recommended for security)
* create a test repository to verify access

---

## Install a code editor

### Recommended: Visual Studio Code

Visual Studio Code provides:

* built-in Git integration
* Markdown preview
* extension support

---

### Recommended extensions

* Markdown preview enhanced
* GitLens
* YAML support

---

## Environment validation checklist

Before proceeding, ensure the following:

* Python is installed and accessible via terminal
* pip is installed and working
* Git is installed and configured
* GitHub account is active
* code editor is set up

---

## Real-world environment considerations

### Use virtual environments (recommended)

In real projects, you should avoid installing packages globally.

Why this matters:

* prevents dependency conflicts
* isolates project-specific packages
* ensures reproducibility

This will be covered in detail in later sections.

---

### Use requirements.txt for dependency management

In production environments, dependencies are tracked using a `requirements.txt` file.

Example:

```
mkdocs
mkdocs-material
```

Why this matters:

* ensures consistent environments across team members
* simplifies setup for new contributors
* supports CI/CD pipelines

---

### Align Python versions across teams

Inconsistent Python versions can cause:

* plugin compatibility issues
* build failures

Best practice:

* standardize Python version across the team
* document it in the repository

---

## Common mistakes to avoid

### Installing packages globally

This can lead to version conflicts across projects.

---

### Skipping environment validation

Many issues occur because tools are installed but not properly configured.

---

### Ignoring Git configuration

Incorrect Git setup can cause problems with commits and collaboration.

---

## Troubleshooting guide

### MkDocs not found after installation

**Cause:**
pip installs the package, but the executable is not in PATH.

**Fix:**

* reinstall using `pip install mkdocs`
* verify PATH includes Python Scripts directory

---

### Permission errors during installation

**Cause:**
insufficient permissions for global installation

**Fix:**

* use `--user` flag
* or use a virtual environment

---

### GitHub authentication issues

**Cause:**
incorrect credentials or missing SSH setup

**Fix:**

* use personal access tokens instead of passwords
* configure SSH keys

---

## What’s next

Now that your environment is ready, the next step is to install MkDocs and set up your first project.

👉 Go to: **Installation**

---