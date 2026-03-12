import os
import urllib.request
import json
import re

USERNAME = "dns-114"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
README_PATH = "README.md"
MAX_STARS = 10

START_MARKER = "<!-- STARS:START -->"
END_MARKER = "<!-- STARS:END -->"


def get_starred_repos():
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{USERNAME}/starred?per_page=100&page={page}"
        req = urllib.request.Request(url)
        req.add_header("Authorization", f"token {TOKEN}")
        req.add_header("Accept", "application/vnd.github.v3+json")
        req.add_header("User-Agent", "update-stars-action")
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
        if not data:
            break
        repos.extend(data)
        if len(data) < 100:
            break
        page += 1
    return repos[:MAX_STARS]


def build_section(repos):
    lines = []
    lines.append(START_MARKER)
    lines.append("")
    lines.append("## Toolbox")
    lines.append("")
    lines.append("> Repos I follow and use in my workflow.")
    lines.append("")
    lines.append("| Repository | Description | Stars |")
    lines.append("|---|---|---|")
    for repo in repos:
        name = repo["full_name"]
        url = repo["html_url"]
        desc = repo.get("description") or ""
        if len(desc) > 60:
            desc = desc[:57] + "..."
        stars = repo.get("stargazers_count", 0)
        stars_fmt = f"{stars:,}"
        lines.append(f"| [{name}]({url}) | {desc} | ⭐ {stars_fmt} |")
    lines.append("")
    lines.append(END_MARKER)
    return "\n".join(lines)


def update_readme(section):
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
        re.DOTALL
    )
    if pattern.search(content):
        new_content = pattern.sub(section, content)
    else:
        new_content = content + "\n\n" + section + "\n"
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("README updated.")


if __name__ == "__main__":
    repos = get_starred_repos()
    section = build_section(repos)
    update_readme(section)
