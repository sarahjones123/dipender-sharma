# Deployment using GitHub Pages

This section explains how to deploy your MkDocs documentation using GitHub Pages. It focuses on both the mechanics of deployment and the reasoning behind each step.

In real-world projects, deployment is not just about making the site available online. It is about ensuring consistency, reliability, and automation.

---

## What is GitHub Pages

GitHub Pages is a static site hosting service provided by GitHub. It allows you to publish websites directly from a repository.

For MkDocs, GitHub Pages is commonly used because:

- it supports static content  
- it integrates directly with Git workflows  
- it requires no additional infrastructure  

---

## How MkDocs deployment works

MkDocs generates a static site in the `site/` directory.

### What happens internally

1. MkDocs processes Markdown files  
2. HTML, CSS, and JavaScript files are generated  
3. output is stored in the `site/` directory  
4. files are pushed to a special branch (`gh-pages`)  
5. GitHub Pages serves content from this branch  

---

## Deployment methods

There are two main approaches:

- manual deployment (using MkDocs command)  
- automated deployment (using CI/CD)  

---

## Method 1: manual deployment

### Step 1: ensure your repository is ready

- project is committed to GitHub  
- default branch is available (for example, `main`)  

---

### Step 2: deploy using MkDocs

```bash
mkdocs gh-deploy

```

What this command does:

* builds the documentation site
* creates or updates the `gh-pages` branch
* pushes the generated site to GitHub

---

### Step 3: verify deployment

After deployment, your site will be available at:

```
https://<username>.github.io/<repository-name>/
```

---

## Enable GitHub Pages

If the site does not appear:

1. go to repository settings
2. navigate to "Pages"
3. select the `gh-pages` branch
4. save changes

---

## When to use manual deployment

Manual deployment is suitable for:

* personal projects
* initial setup and testing
* small documentation systems

---

## Method 2: automated deployment (recommended)

In production environments, deployment should be automated.

---

## Why automation matters

Automation ensures:

* consistent deployment process
* reduced manual effort
* faster updates
* fewer errors

---

## GitHub Actions workflow

Create a workflow file:

```
.github/workflows/deploy.yml
```

---

### Example workflow

```yaml
name: deploy docs

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: checkout repository
        uses: actions/checkout@v3

      - name: set up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.x

      - name: install dependencies
        run: |
          pip install -r requirements.txt

      - name: deploy documentation
        run: |
          mkdocs gh-deploy --force
```

---

## What this workflow does

* triggers on every push to `main`
* installs dependencies
* builds the documentation
* deploys to GitHub Pages

---

## Why this is production-ready

* no manual intervention required
* consistent across environments
* integrates with version control

---

## Understanding the gh-pages branch

The `gh-pages` branch contains only the generated site.

### Key points

* do not edit this branch manually
* it is automatically updated during deployment
* it contains static files only

---

## Custom domain (optional)

You can configure a custom domain for your documentation.

### Steps

1. add a `CNAME` file in your repository
2. configure domain in GitHub Pages settings

---

## Common deployment issues

### Site not loading

**Cause:**

* GitHub Pages not enabled
* incorrect branch selected

**Fix:**

* verify Pages settings
* select `gh-pages` branch

---

### 404 errors

**Cause:**

* incorrect base URL
* missing files

**Fix:**

* verify repository name in URL
* rebuild and redeploy

---

### Assets not loading

**Cause:**

* incorrect paths
* missing files

**Fix:**

* use relative paths
* verify assets exist in `docs/`

---

### Deployment fails in CI/CD

**Cause:**

* missing dependencies
* incorrect Python version

**Fix:**

* verify `requirements.txt`
* align Python version

---

## Best practices for deployment

### Use automation

Avoid manual deployment in team environments.

---

### Validate locally before deployment

Always run:

```bash
mkdocs serve --strict
```

---

### Pin dependencies

Ensure consistent builds across environments.

---

### Keep deployment simple

Avoid unnecessary complexity in workflows.

---

## Validation checklist

Before deployment:

* site builds successfully
* no errors in strict mode
* navigation and links are correct
* dependencies are defined

---

## What’s next

Now that your documentation is deployed, the next step is to automate and optimize the deployment pipeline.

👉 Go to: **CI/CD automation**

---