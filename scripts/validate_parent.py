#!/usr/bin/env python3
"""Tier-1 validation for the public parent routing surface.

ALLOWLIST DESIGN
----------------
This checker asserts known-good public routes and identifiers. It does
**not** encode private repository names, private locators, or other
forbidden strings as a denylist.

A denylist would publish the inventory the public/private boundary exists
to protect. An allowlist fails closed: unrecognized GitHub repository
targets in public Markdown are defects. Absence from this public router
is not evidence that a private component does not exist.

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

# CONTEXT.md is the original self-citation home. A router file cannot pin
# the commit that contains it. Other Markdown may cite a historical SHA
# when the line does not claim that the containing artifact is current.
ROUTER_NO_SHA_FILES = frozenset({"CONTEXT.md"})
LINE_LENGTH_EXEMPT = frozenset({"THESIS.md", "HORIZON.md", "LICENSE"})
PROSE_LINE_LENGTH = 120

SHA_RE = re.compile(r"\b[0-9a-f]{40}\b", re.IGNORECASE)
# Locator forms compared against the allowlist. Matching only https would
# let http, schemeless, or SSH GitHub locators through. Do not treat bare
# owner/repo prose as a locator.
GITHUB_HTTP_RE = re.compile(
    r"(?:https?:)?//(?:www\.)?github\.com/([^/\s)#?]+)(?:/([^/\s)#?]+))?",
    re.IGNORECASE,
)
GITHUB_SCHEMELESS_RE = re.compile(
    r"(?<![\w@])(?:www\.)?github\.com/([^/\s)`\"'<>?#]+)/([^/\s)`\"'<>?#]+)",
    re.IGNORECASE,
)
GITHUB_SSH_RE = re.compile(
    r"(?:git@|ssh://git@)github\.com[:/]([^/\s)`\"'<>?#]+)/([^/\s)`\"'<>?#]+)",
    re.IGNORECASE,
)
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
CURRENCY_RES = (
    re.compile(r"source baseline", re.IGNORECASE),
    re.compile(r"\b(?:main|head)\s+at\b", re.IGNORECASE),
    re.compile(r"as of commit", re.IGNORECASE),
    re.compile(r"this (?:file|document) is current", re.IGNORECASE),
    re.compile(r"v0\.1 candidate", re.IGNORECASE),
)
SHA_CURRENCY_LINE_RE = re.compile(
    r"(source baseline|current(?:\s+\w+){0,3}\s+(?:main|head)|"
    r"as of commit|this (?:file|document|repository) is current|"
    r"v0\.1 candidate|\b(?:main|head)\s+at\b)",
    re.IGNORECASE,
)
# Profile URLs have no repository path. Advisory URLs are paths under an
# allowlisted public repository and are compared as owner/repo only.
ALLOWED_GITHUB_PROFILES = frozenset({"jryski"})

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


def _clean_github_segment(value: str) -> str:
    value = value.split("?", 1)[0].split("#", 1)[0]
    value = value.rstrip(".,);:'\"")
    if value.lower().endswith(".git"):
        value = value[:-4]
    return value.rstrip(".,);:'\"")


def _record_github_pair(
    owner: str, repo: str | None, repos: set[str], profiles: set[str]
) -> None:
    owner = _clean_github_segment(owner)
    if not owner or owner.startswith("."):
        return
    if repo:
        repo = _clean_github_segment(repo)
        if not repo or repo.startswith("."):
            return
        repos.add(f"{owner}/{repo}")
        return
    profiles.add(owner)


def parse_github_url(url: str) -> tuple[str, str | None] | None:
    """Return (owner, repo_or_None) for a GitHub locator."""
    repos, profiles = extract_github_targets(url)
    if len(repos) == 1:
        owner, repo = next(iter(repos)).split("/", 1)
        return owner, repo
    if len(profiles) == 1 and not repos:
        return next(iter(profiles)), None
    match = GITHUB_HTTP_RE.search(url)
    if not match:
        return None
    owner = _clean_github_segment(match.group(1))
    repo = match.group(2)
    if not owner or owner.startswith("."):
        return None
    if repo:
        repo = _clean_github_segment(repo)
        if not repo or repo.startswith("."):
            return None
        return owner, repo
    return owner, None


def github_repo_from_url(url: str) -> str | None:
    parsed = parse_github_url(url)
    if not parsed or parsed[1] is None:
        return None
    return f"{parsed[0]}/{parsed[1]}"


def extract_github_targets(text: str) -> tuple[set[str], set[str]]:
    """Return (repos as owner/repo, profile logins) from GitHub locators."""
    repos: set[str] = set()
    profiles: set[str] = set()
    for match in GITHUB_HTTP_RE.finditer(text):
        _record_github_pair(match.group(1), match.group(2), repos, profiles)
    for match in GITHUB_SCHEMELESS_RE.finditer(text):
        _record_github_pair(match.group(1), match.group(2), repos, profiles)
    for match in GITHUB_SSH_RE.finditer(text):
        _record_github_pair(match.group(1), match.group(2), repos, profiles)
    return repos, profiles


def allowlist_rejected_repos(text: str) -> set[str]:
    repos, _profiles = extract_github_targets(text)
    return {repo for repo in repos if repo not in ALLOWED_GITHUB_REPOS}


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


def line_has_currency_claim(line: str) -> bool:
    return bool(SHA_CURRENCY_LINE_RE.search(line))


def currency_sha_hits(name: str, text: str) -> list[tuple[int, str]]:
    """Return (line, sha) pairs treated as self-currency claims.

    A SHA is a defect in CONTEXT.md, on the same line as a currency
    claim, or on a line adjacent to a currency claim (for example
    ``Current head:`` followed by a 40-character SHA). Historical
    exact-head citations without that claim are retained.
    """
    hits: list[tuple[int, str]] = []
    lines = text.splitlines()
    for number, line in enumerate(lines, start=1):
        prev_line = lines[number - 2] if number >= 2 else ""
        next_line = lines[number] if number < len(lines) else ""
        adjacent = line_has_currency_claim(prev_line) or line_has_currency_claim(
            next_line
        )
        in_currency = line_has_currency_claim(line) or adjacent
        in_router = name in ROUTER_NO_SHA_FILES
        if not (in_router or in_currency):
            continue
        for match in SHA_RE.finditer(line):
            hits.append((number, match.group(0)))
    return hits


def check_currency_markers(errors: list[str]) -> None:
    """Reject self-currency claims, not every historical commit identifier.

    Workflow pin SHAs are out of scope because they are dependency pins,
    not document currency.
    """
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        name = rel(path)
        text = path.read_text(encoding="utf-8")
        for number, sha in currency_sha_hits(name, text):
            errors.append(
                f"{name}:{number}: self-currency SHA {sha} is forbidden "
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


def check_github_allowlist(errors: list[str]) -> None:
    """Allowlist GitHub repository links across every public Markdown file.

    Reachability (lychee) is not membership. A live but unapproved
    repository URL in CONTRIBUTING.md, SECURITY.md, or a decision pointer
    is still an unrecognized public-boundary target. Profile URLs are
    compared against ALLOWED_GITHUB_PROFILES; advisory URLs are compared
    as their owner/repo prefix.
    """
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        name = rel(path)
        text = path.read_text(encoding="utf-8")
        repos, profiles = extract_github_targets(text)
        for repo in sorted(repos):
            if repo not in ALLOWED_GITHUB_REPOS:
                errors.append(
                    f"{name}: unrecognized GitHub route target {repo!r}. "
                    "Public Markdown may only link allowlisted public "
                    "repositories."
                )
        for profile in sorted(profiles):
            if profile not in ALLOWED_GITHUB_PROFILES:
                errors.append(
                    f"{name}: unrecognized GitHub profile {profile!r}. "
                    "Public Markdown may only link the allowlisted maintainer "
                    "profile."
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
    found, _profiles = extract_github_targets(text)
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


def _self_check() -> None:
    sample_sha = "0123456789abcdef0123456789abcdef01234567"
    pointer = "decisions/SAOS-ADR-001.md"

    assert github_repo_from_url("http://github.com/evil/private") == "evil/private"
    assert (
        github_repo_from_url("https://www.github.com/jryski/Household-OS")
        == "jryski/Household-OS"
    )
    repos, profiles = extract_github_targets(
        "see https://github.com/jryski and http://github.com/acme/secret"
    )
    assert profiles == {"jryski"}
    assert repos == {"acme/secret"}

    same_line = f"Current head: `{sample_sha}`"
    assert currency_sha_hits(pointer, same_line) == [(1, sample_sha)]

    adjacent = f"Current head:\n{sample_sha}\n"
    assert currency_sha_hits(pointer, adjacent) == [(2, sample_sha)]

    historical = f"Accepted at exact head `{sample_sha}`."
    assert SHA_RE.search(historical)
    assert not SHA_CURRENCY_LINE_RE.search(historical)
    assert currency_sha_hits(pointer, historical) == []

    historical_wrap = f"Accepted at exact head\n`{sample_sha}`."
    assert currency_sha_hits(pointer, historical_wrap) == []

    current = f"Source baseline: main at `{sample_sha}`"
    assert SHA_CURRENCY_LINE_RE.search(current)
    assert currency_sha_hits(pointer, current) == [(1, sample_sha)]

    unrecognized = "example-not-allowlisted/example-repo"
    allowlisted = "jryski/sovereign-memory-core"
    parent = "jryski/sovereign-ai-os"
    assert allowlist_rejected_repos(
        f"github.com/{unrecognized}"
    ) == {unrecognized}
    assert allowlist_rejected_repos(
        f"git@github.com:{unrecognized}.git"
    ) == {unrecognized}
    assert allowlist_rejected_repos(f"github.com/{allowlisted}") == set()
    assert allowlist_rejected_repos(
        f"git@github.com:{allowlisted}.git"
    ) == set()
    assert allowlist_rejected_repos(
        f"https://github.com/{allowlisted}"
    ) == set()
    assert "owner/repo" not in extract_github_targets(
        "see owner/repo in prose"
    )[0]

    assert allowlist_rejected_repos(
        f"//github.com/{unrecognized}"
    ) == {unrecognized}
    assert allowlist_rejected_repos(
        f"www.github.com/{unrecognized}"
    ) == {unrecognized}
    assert extract_github_targets(
        f"git@github.com:{parent}.git."
    )[0] == {parent}
    assert allowlist_rejected_repos(f"git@github.com:{parent}.git.") == set()
    assert extract_github_targets(
        f"github.com/{parent}?tab=readme-ov-file"
    )[0] == {parent}
    assert allowlist_rejected_repos(
        f"github.com/{parent}?tab=readme-ov-file"
    ) == set()
    assert allowlist_rejected_repos(f"//github.com/{parent}") == set()
    assert allowlist_rejected_repos(f"www.github.com/{parent}") == set()
    assert allowlist_rejected_repos(
        f"www.github.com/{unrecognized}?tab=readme-ov-file"
    ) == {unrecognized}
    assert allowlist_rejected_repos(
        f"git@github.com:{unrecognized}.git."
    ) == {unrecognized}


def main() -> int:
    _self_check()
    errors: list[str] = []
    check_required_files(errors)
    check_final_newlines(errors)
    check_line_length(errors)
    check_currency_markers(errors)
    check_internal_links(errors)
    check_github_allowlist(errors)
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
        "allowlist check: public Markdown GitHub targets are restricted to "
        "known public identifiers; no private-name denylist is used."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
