# Sovereign AI OS: project principles

Updated: 2026-09-07. This document preserves the program's earlier
data-sovereignty, mission and authority decisions in a shorter public guide.
Git history retains the earlier wording.

## Purpose

Keep a person's or organization's knowledge, evidence, decisions, permissions
and work history useful when models, applications and providers change.

WIRE SPEED COMPUTING LLC maintains the program, led by Jesse Ryski. The business
can track development costs and provide future support or licensing. Those
arrangements must preserve user control and interoperability. Company maintenance
does not change existing component licenses or contributors' rights.

This is a design statement, not a claim that the complete system exists.
[Component repositories](ROUTES.md) own implementation and acceptance evidence.
[HORIZON.md](HORIZON.md) describes longer-term possibilities.

## What must survive replacement

The durable record includes more than the text a model remembers:

- Original evidence and its source.
- The subject of a claim, what it says and what supports it.
- Whether it is an observation, inference, proposal, accepted decision or dispute.
- When it was observed, effective, recorded, accepted or superseded.
- Corrections, conflicting evidence and the history of changes.
- Who may read or change it, under which authority.
- Intended work, actions taken, outcomes and verification.

Models, interfaces, storage engines and integrations should be replaceable.
Indexes, embeddings, summaries, caches and model-specific context are rebuildable
views. They must not become the only copy of the evidence or its meaning.

## Accuracy requires evidence

A stronger model does not remove the need for provenance and review.

Preserve source material. Link derived claims to their evidence. Resolve entity
identity separately from attributes. Keep conflicting claims visible. Record
corrections as supersession rather than silently rewriting history.

Important rules need mechanical tests. Actions need receipts that distinguish
attempted, completed, failed and verified outcomes. Verified corrections should
improve later context assembly without turning model inference into fact.

When evidence is missing or stale, report that limit.

## Assemble only the context a task needs

Start with the authenticated principal, request, intent and available authority.
Resolve relevant subjects, retrieve permitted evidence, then attach provenance,
conflicts, policy and freshness. Give the worker a bounded context package.

Do not solve continuity by sending every model the entire archive. Retrieval
engines and ranking systems can help select context; they do not determine
canonical truth or access rights.

## Keep different kinds of state distinct

| Kind | What it records |
| --- | --- |
| Knowledge | Claims about the world and their history |
| Operational state | What is happening now |
| Planning | Intended work, dependencies, owners and approvals |
| Action | An authorized attempt to change something |
| Evidence and receipts | Support for claims about what occurred |

These records connect but have different lifetimes and authorities. Telemetry,
financial history, work queues and agent conversations should not become one
undifferentiated memory table.

## Enforce authority outside the model

Prompts are guidance, not security boundaries. Models and agents are workers;
they cannot grant themselves authority.

Use authenticated identity, scoped credentials, database permissions, bounded
tools, integration scopes, sandboxing, approval, revocation and audit where the
operation requires them. Caller-supplied identity labels are not proof.
Shared credentials cannot establish separate human and agent identities.

Build and administration access is different from ordinary runtime access.
A privileged construction tool must not become the permanent user-facing path.
Supabase User MCP is the intended principal-bound application-data component;
its repository states which profiles are currently accepted.

Merge, deployment, production access and publication remain separate decisions.
A document, public link or successful test does not grant any of them.

## Shared foundations, separate deployments

Household and business applications share provenance, authority, planning and
audit concepts. They do not need identical schemas, policies or product behavior.

Household workflows may cover events, chores, assets, maintenance and family
planning. Per-person private records remain separate from shared household
knowledge.

Business workflows may cover customers, suppliers, projects, incidents,
approvals and operations. Their data, credentials and operating authority stay
with that deployment.

Wirespeed maintains the shared program and can also use it in its own business.
That deployment is not the source of universal policy. A useful local finding
becomes a public contribution only after it is reduced to a generic example
and reviewed in the owning repository. Private records, customer information,
credentials and infrastructure details do not travel with it.

## Adapt and integrate

Use existing standards, models, memory engines and tools where they fit.
Translate between them when necessary, preserve provenance and disclose any
information lost in translation. Contribute generic improvements upstream
where useful.

Do not build a competing replacement merely because a capability belongs to
another project. Avoid intentional incompatibility and dependence on a single
vendor.

A frontend outside any single model provider is a future direction. It should
consume the same bounded access and durable records, not become another private
store of truth.

## Meet the user on the right surface

Choose the interface, timing and level of detail that fit the authorized task.
A concise answer, calendar item, shared task, dashboard, notification or no
interruption may each be appropriate.

Consider privacy, urgency, reversibility and the cost of interrupting the user.
Do not make the user translate the same intent across several applications.
Presentation consumes authority; it does not create it.

## Keep development useful and honest

Build small, useful capabilities while foundations are still changing.
Distinguish planned, implemented, tested, accepted and released states.
An experimental deployment can reveal a defect without proving readiness.

Use one implementation owner per task. Preserve independent review where
needed, explicit transition states and receipts for consequential actions.
Governance should protect useful work without consuming more effort than it saves.

A repository should have a clear reason to exist: a trust boundary, release
cycle, implementation lifecycle, licensing boundary or independent evidence
role. Consolidate weak boundaries when practical.

This parent repository explains purpose and routes readers to the right owner.
It is not a second task database, a private deployment map or a source of runtime
permission.

## Design test

Before a substantial addition, ask:

1. Does it improve a concrete task for a person or organization?
2. Can the current model, provider, interface or storage implementation be replaced?
3. Are source evidence, time, conflict and correction preserved?
4. Is authority explicit and enforced where consequences require it?
5. Does it have a clear source of truth and protect private deployment boundaries?
6. Can durable state be exported, restored and independently verified?
7. Are its claims supported by evidence for the relevant revision and environment?

Avoid an unrestricted agent, a monolithic everything-app, a vendor-owned memory
silo, a flat archive without provenance, or revenue-driven lock-in.

## Success and orientation

Success means an authorized replacement model can find relevant context,
understand its permissions, answer with evidence, perform bounded work and
leave useful receipts without the human rebuilding their history. That model
must itself remain replaceable.

Start here, then read [ROUTES.md](ROUTES.md), the owning component and the exact
issue or evidence needed for the task. Read [HORIZON.md](HORIZON.md) only when
future direction matters. Do not recursively load every repository.

When sources conflict, preserve the conflict and resolve the real authority.
When a task crosses personal, household, business or administrative boundaries,
resolve permission before combining context or acting.
