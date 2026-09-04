# Contributing

Thank you for helping keep this public parent useful and safe.

This repository is the **router and public front door** for Sovereign AI
OS. It is not a monorepo, not a second implementation authority, and not
a planning database. Implementation belongs in the owning public child
repository named by [`ROUTES.md`](ROUTES.md).

By contributing, you agree that your contributions are licensed under
the Apache License 2.0. See [`LICENSE`](LICENSE). Child repositories may
use different licenses.

## Read first

1. [`README.md`](README.md) — what this parent is and is not.
2. [`ROUTES.md`](ROUTES.md) — which public component owns the concern.
3. [`CONTEXT.md`](CONTEXT.md) — cold-start order for agents.
4. [`SECURITY.md`](SECURITY.md) — what must never appear in public
   issues or pull requests.
5. [`THESIS.md`](THESIS.md) — only when mission or invariant principles
   are needed.
6. [`HORIZON.md`](HORIZON.md) — only when future direction matters.

Agents should follow `CONTEXT.md` before ingesting thesis or horizon
payload.

## Downstream dogfood to generic upstream

Wirespeed and other deployments may observe real defects while dogfooding
the architecture. Those observations do not become upstream truth by
being true downstream.

```text
downstream dogfood observation
        ↓
genericize / remove private payload
        ↓
issue or PR to the owning upstream public repo
        ↓
normal review / evidence / acceptance
        ↓
optional downstream adoption
```

Clarifications:

- Downstream evidence does **not** self-promote upstream.
- Upstream acceptance does **not** force downstream parity.
- Business-specific policy, private data, topology, credentials, and
  deployment-only behavior stay in the authorized business deployment.
- A generic lesson may enter the owning **public** repository only after
  private payload is removed.

If the owning public route is unclear, open an issue on this parent that
asks for a route, not for an implementation change.

## What belongs here

Good parent contributions are small and routing-shaped:

- broken public links or missing required files;
- ambiguous routes that send a cold reader to the wrong public repo;
- CONTRIBUTING / SECURITY / LICENSE corrections for this parent;
- public decision-pointer wording that no longer matches an accepted
  ruling.

Do not add:

- a hand-maintained current-state, effort, or provenance chronicle;
- private names, locators, or denylist patterns;
- a machine-readable program manifest without a demonstrated second
  consumer;
- implementation, schema, or deployment changes that belong in a child
  repository.

## Pull requests

Keep pull requests small enough to review as one coherent change.

A pull request should:

- explain the routing or documentation defect;
- name the owning surface (`ROUTES.md`, this parent, or a child repo);
- avoid unrelated doctrine rewrites;
- pass Tier-1 CI;
- omit private payload.

Use a topic branch. Do not merge without human approval.

## Validation

From the repository root:

```text
python3 scripts/validate_parent.py
```

GitHub Actions also run Markdown structural checks and internal/external
link validation. The public-boundary check is an **allowlist** of known
public routes; it is not a denylist of private names.

## Acceptance

This parent uses two meanings of “accepted.” See the Acceptance section
in [`README.md`](README.md):

- the per-change merit test for ordinary later work;
- the one-time parent acceptance milestone, declared by Jesse at an
  exact head.

This file does not record whether that milestone has been declared.
