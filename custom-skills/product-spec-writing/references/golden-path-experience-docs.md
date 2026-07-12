# Authoring a golden-path / experience-design doc

For PM docs that define the "golden path" — the single opinionated end-to-end
route a product commits to for a common user task (e.g. "golden path for running
hosted agents on BYO-AKS"). Distinct from a feature spec: the deliverable is a
*paved-road walkthrough of the lifecycle*, not a scope/requirements list.

## Canonical definition (ground the doc in it — the user asks "what IS a golden path?")
A golden path (Spotify's coinage; see redhat.com/en/topics/platform-engineering/golden-paths)
is an **opinionated, well-documented, supported, end-to-end route** for a common
task — the paved road a team commits to so builders don't reinvent it. Two load-
bearing properties to preserve in the doc:
- **Opinionated + supported**, not exhaustive. One happy path, not every option.
- **Spans the FULL lifecycle**, create → operate → retire. This is the audit lens
  below — most draft golden paths cover the middle and silently drop the ends.

## Lifecycle audit checklist — run the draft against this, name what's missing
When the user's draft lists N steps, map them onto the canonical lifecycle and
report gaps as a table (in-path / implicit / missing / deliberate-non-goal):

| Lifecycle stage | Notes |
| --- | --- |
| Prereqs / access | permissions, capacity, networking to onboard |
| Scaffold from template | quickstart/init |
| **Build & test locally (inner loop)** | commonly MISSING — the author loop *before* deploy |
| Provision infra | |
| **Create the containing project/workspace** | commonly MISSING for platform products — the scoping container the artifact deploys *into* (carries the runtime identity, endpoint, linked resources like models/telemetry) |
| Deploy | |
| Invoke / run | |
| **Secure — grant the runtime identity access (RBAC)** | often buried inside Deploy; a canonical component |
| Monitor / observe | |
| Troubleshoot | |
| Update / version / rollback | |
| Scale / right-size | frequently a *deliberate* later-milestone non-goal — keep it out, but say so |
| Publish to channels (Teams/M365/etc.) | optional branch |
| **Decommission / offboard** | commonly MISSING — disable/enable, delete, tear-down |

The three usually-genuinely-missing (not deliberate) stages: **local build/test**,
**grant-identity/RBAC**, **decommission**. Surface them, recommend where they slot,
but DON'T silently add steps to the user's scoped path — offer and let them pick.

## Section skeleton that worked (BYO-AKS golden-path doc, leadership review)
1. **Goal** — one-sentence goal + a single "As a [persona], I want … so that …"
   scenario; then the scoped path as an ordered step list; then **Non-goals**
   (explicitly park scale/multi-X/behind-the-scenes-ops here).
2. **Responsibility split** (only for platform/shared-infra docs) — a compact
   "who owns what" table (provider vs customer) + one plain "impact on your
   environment" line. Ken forgot this in his own outline and wanted it added;
   for any BYO / shared-responsibility product it's a standard, expected section.
3. **Prerequisites** — what the customer must have in place to onboard.
4. **Step-by-step (GA)** — each step a bold header + tight bullets, with a
   one-line "(same as today; no change)" / "(today + a delta)" tag when the step
   reuses an existing experience. **Inline doc links at each point** (see below).
5. **Preview / next-milestone** — leave as a labelled TBD scaffold if the user
   will fill it; don't invent preview scope.
6. **Glossary at END** — spell out abbreviations once here, short form in body.

## Inline reference links (Ken's format preference — first-class)
When narrating "the current experience," put the official-doc link **right next
to the specific point it backs**, inline, using `→ [Label](url) · [Label2](url)`
after the sentence. Do NOT collect links in a footer/References section at the
end — he explicitly wants them adjacent so a reviewer can jump from any single
claim. Pull each link from the live doc (see SKILL.md "Naming … official doc"),
and tag GA vs (preview) per point. Verify every URL before shipping a leadership
doc — a quick HEAD/200 check on any link you inferred rather than opened; broken
links in a leader-facing doc read as sloppy.

## Condensed fact bank (verified this session — reuse, but re-confirm if load-bearing)
- **Golden-path stages / definition**: redhat.com golden-paths page; components =
  templates · infra provisioning · build&deploy · observability · security guardrails.
- **k8s permission to install a CRD + controller** (came up as a prereq): installing
  a CRD needs **cluster-admin-level** rights *at install time* — manage
  `customresourcedefinitions.apiextensions.k8s.io` **and** create the controller's
  own `ClusterRole`/`ClusterRoleBinding`. A CRD is cluster-scoped, so it's a
  `ClusterRole`, never a namespaced Role; cluster-admin is required because
  Kubernetes' privilege-escalation prevention blocks an installer from granting RBAC
  it doesn't already hold. On AKS with Azure RBAC for Kubernetes authorization this
  maps to the built-in "Azure Kubernetes Service RBAC Cluster Admin" role; the
  *running* controller then drops to its own least-privilege service account.
  (Sources: kubebuilder.io CRD-scope; learn.microsoft.com/azure/aks/manage-azure-rbac.)

## Deriving a PREVIEW scope from a settled GA scope (proposal + rationale)
When the user asks you to *propose* a private/public preview scope off the GA
golden path (and wants the rationale, not just a list), use this method — it
worked over several iterations for the BYO-AKS preview:
1. **State the lens first — it justifies every cut.** A preview exists to prove
   the *one genuinely new bet* end-to-end with a few named design partners and to
   *learn* the real onboarding/failure modes. It is **NOT a smaller GA.** Every
   scope call flows from that sentence, so lead with it.
2. **Write the goal so it does scope work.** "Partners try it end-to-end and give
   feedback — **explicitly not for production.**" Then make the organizing rule
   explicit: *anything whose purpose is production-readiness is out of scope by
   definition* (scale/NFR hardening, self-serve UX, full monitoring parity,
   production workloads) — decided by that rule, not case-by-case.
3. **Walk the GA steps and tag each** IN-as-is / IN-but-concierge-or-tooling /
   OUT-defer, with a one-line why per row. Pattern that recurred: the "same as
   today" happy-path steps ship unchanged; the *new/risky* steps ship
   **self-serve via tooling** (see next point) OR concierge; orthogonal/optional
   steps (publish-to-channels) and scale/polish defer.
4. **Prefer a self-serve TOOL over per-customer concierge for onboarding.** Ken
   explicitly rejected "ticket → Dev team onboards each customer": *don't bother
   the Dev team per customer.* The better answer for an infra/CLI-native audience
   is a **private CLI package** (e.g. a private Az CLI extension) distributed only
   to NDA partners — build once, every partner self-serves, zero marginal dev
   effort per onboarding, and it reads as native to AKS/`az`/IaC users. It runs as
   the customer's own logged-in identity, so it inherits their permissions exactly
   like the portal would (can list/validate *or* take an explicit resource ID),
   which also means the provider needs **no standing admin** on the customer env.
   Reserve concierge ONLY for the deliberate *learning loop* (debugging the new
   delta *with* partners to learn what to surface at GA), not for routine
   onboarding toil. Offboard should mirror provision (same tool).
5. **Cross-cutting scope block**: non-prod only · functional correctness not
   scale (answer any "do we support N-thousand concurrent?" with *no, that's a
   GA/Day-30 concern; preview proves the mechanism, not the magnitude*) · pricing
   · named partners.
6. **Exit bar** — close with "what we want to *know* by end of preview" (the path
   works on a real customer env; the true prereqs validated-not-assumed; which
   failure modes actually occur; does the core bet behave as designed). Ground
   the partner list + non-prod-CIDR call in the customer-research/context docs.
7. **Present for review first; don't write it into the doc's TBD section until
   the user signs off** — he iterates scope 3-4 rounds before it's settled.

## Scope-integrity corrections (Ken caught these — treat as invariants)
- **Never invent an asymmetric platform "delta" on a step he called "same as
   today."** When a lifecycle step is agent/artifact-level (offboard *an agent* =
   disable/delete that agent), keep it agent-level and worded like the other
   "(same as today)" steps. Do NOT bolt a made-up provider-side action
   ("platform tears down the whole cluster/instance") onto it — that conflates
   artifact-scope with instance/environment-scope. When unsure whether a step
   carries a BYO/platform delta, ask rather than manufacture one.
- **Don't restate a GA non-goal as a preview non-goal.** If ">1 cluster per
   instance" is already a GA non-goal, it's not a preview-specific exclusion —
   listing it again is noise. Preview non-goals = things GA *will* do that preview
   defers, not things nobody ever committed to.
- These are two faces of one rule Ken enforces: **every scope line must be true
   at the level and milestone it's stated for.** He'll challenge any line that
   isn't.

## Restructure/renumber pitfall (multi-step golden paths)
Inserting or removing a step (e.g. adding "Create a project" as step 2, shifting
3-9) via `patch` is error-prone:
- **A stale count reference hides elsewhere.** After changing an N-step list, grep
  the whole file for the old count ("six steps", "the 8 steps") — the intro
  sentence AND a later cross-ref (e.g. the Preview section's "which of the six
  steps change") both go stale. A regex may miss it; read the region to confirm.
- **`patch` can orphan a trailing bullet.** If your old_string didn't include a
  sub-bullet that belonged to the replaced step (e.g. a "*delta:*" line under the
  old final step), it survives as an orphan under the renumbered step. Re-read the
  edited region end-to-end after any renumber and delete leftovers.
- Update the step-role tag sentence too ("Steps 2,3,5,7 are same-as-today; Step 1
  is X; Step 6 adds a delta") — those index numbers shift with every insert.
