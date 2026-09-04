#!/usr/bin/env python3
"""Tier-1 validation for the public parent routing surface.

ALLOWLIST DESIGN
----------------
This checker asserts known-good public routes and identifiers. It does
**not** encode private repository names, private locators, or other
forbidden strings as a denylist.

A denylist would publish the inventory the public/private boundary exists
to protect. An allowlist fails closed: unrecognized route targets on the
governed routing surface are defects. Absence from this public router is
not evidence that a private component does not exist.

Moving or current state must be generated or omitted. A file cannot cite
the commit that contains it.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "LICENSE",
    "README.md",
    "CONTEXT.md",
    "ROUTES.md",
    "THESIS.md",
    "HORIZON.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "AGENTS.md",
    "decisions/README.md",
    "decisions/SAOS-ADR-001.md",
    "decisions/SAOS-ADR-002.md",
    "scripts/validate_parent.py",
    ".github/workflows/ci.yml",
    ".markdownlint-cli2.yaml",
    ".lychee.toml",
)

# Known-good public GitHub repositories. This is an allowlist, not a
# census of every repository in the program.
PUBLIC_CHILD_REPOS = frozenset(
    {
        "jryski/sovereign-memory-core",
        "jryski/Supabase_user_MCP",
        "jryski/Household-OS",
        "WireSpeedComputing/Sovereign-Vault",
        "jryski/Public_AI_SKills",
    }
)
PARENT_REPO = "jryski/sovereign-ai-os"
ALLOWED_GITHUB_REPOS = PUBLIC_CHILD_REPOS | {PARENT_REPO}

INTERNAL_ROUTE_TARGETS = frozenset(
    {
        "THESIS.md",
        "HORIZON.md",
        "README.md",
        "CONTEXT.md",
        "ROUTES.md",
        "LICENSE",
        "SECURITY.md",
        "CONTRIBUTING.md",
        "AGENTS.md",
        "decisions/",
        "decisions/README.md",
        "decisions/SAOS-ADR-001.md",
        "decisions/SAOS-ADR-002.md",
    }
)

CONTRIBUTION_KINDS = frozenset({"orientation", "generic-upstream"})

GOVERNED_ROUTING_FILES = ("README.md", "ROUTES.md", "CONTEXT.md")
LINE_LENGTH_EXEMPT = frozenset({"THESIS.md", "HORIZON.md", "LICENSE"})
PROSE_LINE_LENGTH = 120

SHA_RE = re.compile(r"\b[0-9a-f]{40}\b", re.IGNORECASE)
GITHUB_REPO_RE = re.compile(
    r"https://github\.com/([^/\s)#]+)/([^/\s)#]+)", re.IGNORECASE
)
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
CURRENCY_RES = (
    re.compile(r"source baseline", re.IGNORECASE),
    re.compile(r"current (?:main|head) at", re.IGNORECASE),
    re.compile(r"as of commit", re.IGNORECASE),
    re.compile(r"this (?:file|document) is current", re.IGNORECASE),
    re.compile(r"v0\.1 candidate", re.IGNORECASE),
)

TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".toml", ".py", ".txt"}
TEXT_NAMES = {"LICENSE"}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        if path.suffix in TEXT_SUFFIXES or path.name in TEXT_NAMES:
            files.append(path)
    return sorted(files)


def parse_tables(text: str) -> list[list[list[str]]]:
    tables: list[list[list[str]]] = []
    current: list[list[str]] = []
    for raw in text.splitlines():
        if raw.startswith("|"):
            cells = [cell.strip() for cell in raw.strip().strip("|").split("|")]
            current.append(cells)
        elif current:
            tables.append(current)
            current = []
    if current:
        tables.append(current)
    return tables


def normalize_table(rows: list[list[str]]) -> tuple[list[str], list[list[str]]]:
    if len(rows) < 2:
        return [], []
    headers = [h.strip() for h in rows[0]]
    body: list[list[str]] = []
    for row in rows[1:]:
        if row and all(re.fullmatch(r":?-{3,}:?", cell or "") for cell in row):
            continue
        body.append(row)
    return headers, body


def first_link_target(cell: str) -> str | None:
    match = MD_LINK_RE.search(cell)
    if not match:
        return None
    target = match.group(1).strip()
    return target.split("#", 1)[0].split("?", 1)[0]


def github_repo_from_url(url: str) -> str | None:
    match = GITHUB_REPO_RE.search(url)
    if not match:
        return None
    owner = match.group(1)
    repo = match.group(2).removesuffix(".git")
    if owner.startswith(".") or repo.startswith("."):
        return None
    return f"{owner}/{repo}"


def extract_github_repos(text: str) -> set[str]:
    found: set[str] = set()
    for owner, repo in GITHUB_REPO_RE.findall(text):
        repo = repo.removesuffix(".git")
        found.add(f"{owner}/{repo}")
    return found


def in_code_or_table(line: str, in_fence: bool) -> tuple[bool, bool]:
    stripped = line.lstrip()
    if stripped.startswith("```"):
        return True, not in_fence
    if in_fence or stripped.startswith("|"):
        return True, in_fence
    return False, in_fence


def check_required_files(errors: list[str]) -> None:
    for name in REQUIRED_FILES:
        path = ROOT / name
        if not path.is_file():
            errors.append(f"missing required file: {name}")
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8") if (
        ROOT / "LICENSE"
    ).is_file() else ""
    if "Apache License" not in license_text or "Version 2.0" not in license_text:
        errors.append("LICENSE is not Apache License Version 2.0 text")


def check_final_newlines(errors: list[str]) -> None:
    for path in iter_text_files():
        data = path.read_bytes()
        if not data:
            errors.append(f"{rel(path)}: empty file")
            continue
        if not data.endswith(b"\n"):
            errors.append(f"{rel(path)}: missing final newline")
        if data.endswith(b"\n\n"):
            errors.append(f"{rel(path)}: trailing extra blank line")


def check_line_length(errors: list[str]) -> None:
    for path in iter_text_files():
        name = rel(path)
        if name in LINE_LENGTH_EXEMPT or path.suffix != ".md":
            continue
        in_fence = False
        for number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            skip, in_fence = in_code_or_table(line, in_fence)
            if skip:
                continue
            if len(line) > PROSE_LINE_LENGTH:
                errors.append(
                    f"{name}:{number}: line length {len(line)} exceeds "
                    f"{PROSE_LINE_LENGTH}"
                )


def check_currency_markers(errors: list[str]) -> None:
    """Markdown must not assert its own currency with a commit hash.

    GitHub Actions pin SHAs are dependency pins, not self-currency claims,
    so workflow files are out of scope.
    """
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        name = rel(path)
        text = path.read_text(encoding="utf-8")
        for match in SHA_RE.finditer(text):
            errors.append(
                f"{name}: self-currency SHA {match.group(0)} is forbidden "
                "(generate or omit moving state)"
            )
        for pattern in CURRENCY_RES:
            if pattern.search(text):
                errors.append(
                    f"{name}: stale/candidate/self-currency marker "
                    f"{pattern.pattern!r}"
                )


def check_internal_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in MD_LINK_RE.findall(text):
            href = target.strip()
            if href.startswith(("http://", "https://", "mailto:")):
                continue
            if href.startswith("#"):
                continue
            file_part = href.split("#", 1)[0].split("?", 1)[0]
            if not file_part:
                continue
            resolved = (path.parent / file_part).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{rel(path)}: link escapes repository: {href}")
                continue
            if not resolved.exists():
                errors.append(f"{rel(path)}: broken internal link {href}")


def check_governed_github_allowlist(errors: list[str]) -> None:
    for name in GOVERNED_ROUTING_FILES:
        path = ROOT / name
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for repo in sorted(extract_github_repos(text)):
            # Compare case-sensitively to the published public identifiers.
            if repo not in ALLOWED_GITHUB_REPOS:
                errors.append(
                    f"{name}: unrecognized GitHub route target {repo!r}. "
                    "Governed routing files may only link allowlisted public "
                    "repositories."
                )


def check_routes_table(errors: list[str]) -> None:
    path = ROOT / "ROUTES.md"
    tables = parse_tables(path.read_text(encoding="utf-8"))
    if not tables:
        errors.append("ROUTES.md: missing route table")
        return
    headers, body = normalize_table(tables[0])
    required_headers = ["Concern", "Public route", "Authority there", "Contribution"]
    if headers != required_headers:
        errors.append(
            "ROUTES.md: route table headers must be "
            + ", ".join(required_headers)
            + f" (got {headers})"
        )
        return
    if not body:
        errors.append("ROUTES.md: route table has no data rows")
        return

    seen_repos: set[str] = set()
    for index, row in enumerate(body, start=1):
        if len(row) != 4:
            errors.append(f"ROUTES.md: row {index} does not have 4 cells")
            continue
        concern, public_route, _authority, contribution = row
        if contribution not in CONTRIBUTION_KINDS:
            errors.append(
                f"ROUTES.md: row {index} has unrecognized Contribution "
                f"{contribution!r}; allowed: {sorted(CONTRIBUTION_KINDS)}"
            )
        target = first_link_target(public_route)
        if not target:
            errors.append(f"ROUTES.md: row {index} ({concern}) has no link")
            continue
        repo = github_repo_from_url(target)
        if repo:
            if repo == PARENT_REPO:
                errors.append(
                    "ROUTES.md: circular parent → parent route row is not "
                    "allowed"
                )
            elif repo not in PUBLIC_CHILD_REPOS:
                errors.append(
                    f"ROUTES.md: row {index} routes to unrecognized public "
                    f"identifier {repo!r}"
                )
            else:
                seen_repos.add(repo)
            continue
        if target not in INTERNAL_ROUTE_TARGETS:
            errors.append(
                f"ROUTES.md: row {index} has unrecognized internal route "
                f"target {target!r}"
            )

    missing = PUBLIC_CHILD_REPOS - seen_repos
    if missing:
        errors.append(
            "ROUTES.md: missing required public component route(s): "
            + ", ".join(sorted(missing))
        )


def check_readme_components(errors: list[str]) -> None:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    found = extract_github_repos(text)
    missing = PUBLIC_CHILD_REPOS - found
    if missing:
        errors.append(
            "README.md: missing required public component link(s): "
            + ", ".join(sorted(missing))
        )


def check_agents_pointer(errors: list[str]) -> None:
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8").strip()
    if "CONTEXT.md" not in text:
        errors.append("AGENTS.md must be a pointer to CONTEXT.md")
    if text.count("\n") > 4:
        errors.append("AGENTS.md must stay a one-line pointer to CONTEXT.md")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_final_newlines(errors)
    check_line_length(errors)
    check_currency_markers(errors)
    check_internal_links(errors)
    check_governed_github_allowlist(errors)
    check_routes_table(errors)
    check_readme_components(errors)
    check_agents_pointer(errors)

    if errors:
        print("parent validation failed:")
        for item in errors:
            print(f"  - {item}")
        return 1
    print("parent validation passed")
    print(
        "allowlist check: governed routing targets are restricted to known "
        "public identifiers; no private-name denylist is used."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
