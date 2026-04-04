import yaml

def generate_md_from_openapi(file):
    with open(file) as f:
        spec = yaml.safe_load(f)

    paths = spec.get("paths", {})
    md = "# API Endpoints\n\n"

    for path, methods in paths.items():
        md += f"## {path}\n"
        for method, details in methods.items():
            md += f"- **{method.upper()}**: {details.get('summary')}\n"

    return md

if __name__ == "__main__":
    md_content = generate_md_from_openapi("openapi/openapi.yaml")

    with open("docs/api/generated.md", "w") as f:
        f.write(md_content)

    print("✅ API docs generated at docs/api/generated.md")