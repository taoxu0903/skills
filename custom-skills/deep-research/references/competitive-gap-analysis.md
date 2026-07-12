# Competitive Gap Analysis & Enhancement Recommendations

This is the **judgment-quality** file: how to make sure a gap/enhancement CONCLUSION is sound.
Load it ONLY when the user asks a gaps / enhancement / "what should we build" / "confirm my
conclusion" follow-up after a Compare run — it is NOT part of a normal descriptive run.

For **fact-quality** (is the datum true, fresh, officially sourced?), see the always-on
`verification-and-recency.md`. Clean split: **that file = is the FACT true and current?** ·
**this file = is the CONCLUSION sound?** The disprove-your-own-gap pass below depends on the
recency/primary-source discipline in that file — run both together on a gap analysis.

The pattern was learned from a Foundry token-feature analysis where 3 of 6 claimed gaps turned
out to be false.

## 1. The descriptive → prescriptive transition (sanctioned, on explicit request only)

- Compare stays DESCRIPTIVE by default (see the main Compare pitfall).
- BUT when the user EXPLICITLY asks for gaps / enhancements / "what's missing in X"
  as a distinct follow-up, prescriptive recommendations ARE the requested deliverable.
  Provide them — do not refuse by citing the descriptive-only rule.
- Flag the transition out loud ("this crosses from comparison into recommendation,
  which is what you asked for").
- Stay grounded: every recommended gap must trace to a specific matrix cell + the
  competitor that beats it. The thing to avoid is strategy that floats free of the
  comparison data, not strategy per se.

## 2. Claiming a competitor LACKS a feature is the highest-risk claim in the report

Absence / negative claims ("Foundry has no X") are exactly what stale secondary
sources get wrong. In the motivating session, 3 of 6 "gaps" were false — the product
already had anomaly detection, cross-vendor routing, and cache-hit metrics; the
"gap" came from outdated blogs.

Rule: before asserting any gap, actively try to DISPROVE it.
- Run a search whose goal is to find the feature EXISTS ("X does have Y",
  "X Y generally available <year>"), not one that only confirms absence.
- Resolve every gap against a PRIMARY source (vendor docs / Learn / release notes),
  never a secondary blog.
- For GA-vs-preview / "just shipped" status, read the vendor's own doc page — that
  status flips fast and secondary recaps lie. When a blog and the vendor doc
  disagree, the vendor doc wins.
- CHECK THE DOC'S LAST-UPDATED DATE, not just that it's a primary source. A vendor
  doc can be primary AND stale. Read the "last updated" / publish date on the page and
  prefer the freshest authoritative page (the vendor's GA-status overview and "What's
  New" index both carry dates). In the motivating run, the claim that flipped Gap 1 came
  from a Learn page dated 2026-04-13 that an earlier pass had missed — and the GA-status
  table dated 06/02/2026 was the tiebreaker on preview-vs-GA. When the user says "check
  with the LATEST date," they mean exactly this: sort for freshness, read the date, cite it.

## 3. Triple-confirm volatile maturity claims when the user pushes

When the user says "double check" / "confirm with latest", escalate verification:
1. Time-filtered search (last month) + the vendor's "What's New" / release post.
2. Read the authoritative doc page directly (web_extract / reader) — do not trust
   the search snippet alone.
3. Separate VISIBILITY features from ENFORCEMENT/CONTROL features. A shipped
   "see cost per agent" does NOT close a "cap cost per agent" gap.

## 4. Don't shrink a gap with an unrelated feature

A precisely-scoped gap (e.g. "no per-agent token CONTROL") is not narrowed by a
different feature (e.g. "per-agent cost VISIBILITY shipped"). Keep the gap's scope
exactly as originally stated; credit the competitor only for the exact thing the
gap named. Resisting the urge to claim a "partial closure" keeps the analysis honest.

## 5. When a BROAD gap is disproven, re-scope it to the precise surviving dimension — don't just drop it

Distinct from #4. There, an unrelated feature can't shrink a precise gap. HERE, the
gap as originally stated turns out FALSE, but a narrower true gap survives inside it —
keep that, re-scoped, rather than deleting the whole entry.

Motivating case (this session): "Foundry has no hard spend cap" was disproven — Foundry
DOES hard-block on a cumulative token quota (403 Forbidden). But the survivor is real and
sharper: the cap is denominated in TOKENS not DOLLARS, and it's at PROJECT scope not
PER-AGENT. So the gap became "no dollar-denominated, per-agent hard cap" — narrower, fully
defensible, and it folds cleanly into the per-agent-governance thesis.

Why it matters: an overstated gap ("no hard cap at all") is instantly rebuttable by a
product expert who knows the 403 quota exists — it destroys your credibility. The precise
survivor ("caps tokens not dollars, not per agent") holds up in front of someone who knows
the product. When freshness-checking flips a gap:
1. Don't binary-drop it. Ask what EXACTLY still doesn't exist.
2. Re-scope the gap title and body to that exact surviving dimension.
3. Log the correction visibly in the doc's evidence note (what was claimed, what the
   primary source showed, the date) so the change is traceable.
4. Re-grade status honestly: "Open (narrowed)" beats both "Open" (overstated) and
   "Closed" (overcorrected).

## 6a. Classify every gap as CATCH-UP vs GREENFIELD — it changes the whole framing

The most useful thing gap analysis produces is not the gap list, it's the TYPE of each gap.
Two kinds, and they demand opposite treatment:

- **Catch-up gap:** a rival already ships it, you're behind. Urgent, defensive, match-the-rival.
  "Plug the hole before you lose deals."
- **Greenfield gap:** the capability is missing from YOUR product AND from every competitor.
  Not urgent (nobody's winning deals on it yet), offensive, define-the-category. "An early
  forward bet, not a fire to put out."

How to tell them apart: when you assert "X lacks feature F," also check whether the RIVALS have
F. If none do, F is greenfield, not a Foundry-specific hole — and saying "Foundry is behind on F"
would be wrong.

> ⚠️ **The GREENFIELD verdict is ITSELF an absence claim — disprove it per-rival, against PRIMARY
> docs, with the SAME rigor as the original gap (this is the #1 way greenfield gets mis-called).**
> "No rival has F" feels safe to assert because it flatters your product (first-mover!), so it's the
> claim least likely to get the disprove pass from §2 — and that's exactly the trap. Before declaring
> greenfield, open EACH named rival's own primary doc for the feature class (for agent runtime limits:
> the rival's agent-runtime quota / "control cost with limits" / service-limits page) and confirm
> absence there, not from a blog or from memory.
>
> **Motivating case — the verdict that flipped THREE times (June 2026, Foundry):** "no per-agent
> token CONTROL" was first called a Foundry gap, then "corrected" to GREENFIELD on the belief that
> AWS and GCP don't have it either, then "re-corrected" on secondary sources to "both AWS and GCP
> enforce per-agent (GCP = 30 requests/min per agent)." A final pass against PRIMARY docs settled it
> and showed that third version was ALSO wrong on GCP:
> - **AWS AgentCore — genuinely per-agent:** `maxTokens` / `maxIterations` / `timeoutSeconds` per
>   invocation, plus a 25 TPS rate limit "per agent, per account" (the quotas page says exactly that).
>   → Foundry is behind AWS here.
> - **GCP Agent Engine — NOT per-agent:** its real limit is **90 `Query`/min scoped per project /
>   per region** (the primary `cloud.google.com` quotas page), the SAME shape as Foundry's
>   model-deployment quota — not the "30/min per agent" a secondary aggregator and a Tavily synthesized
>   `answer` had claimed. → Foundry is LEVEL with GCP, not behind.
> - **Net verdict:** catch-up versus AWS only; level with GCP; and a per-agent CUMULATIVE dollar
>   budget remains a genuine greenfield slice nobody ships.
>
> **The meta-lesson: a CORRECTION is itself an absence/scope claim — source it to a primary page, not
> to the secondary aggregator or the Tavily `answer` field that produced the previous wrong version.**
> Each flip here came from trusting a synthesized number; only opening the vendor's own quotas page
> (and reading whether the limit is scoped per-agent vs per-project/region) ended the thrash. When you
> "fix" a verdict, hold the fix to the §2 disprove-pass bar too.
>
> **Decompose the capability before you classify it — the unit was too coarse.** "Per-agent control"
> hid things with opposite verdicts: (a) per-invocation caps + a per-agent rate limit — AWS ships this
> (GCP does not, it's per-project) → catch-up vs AWS; (b) a per-agent CUMULATIVE, dollar-denominated
> budget ("spend $500/mo then stop") — nobody ships this cleanly → the real, narrow greenfield slice.
> A coarse feature label gets one verdict for the whole thing; split it into the enforcement primitives
> and classify each. Also watch the per-agent-vs-per-project SCOPE axis: a limit can exist but be
> project-scoped (shared pool), which is NOT the same as a true per-agent dial — don't let a
> project-scoped quota count as per-agent enforcement. If the whole "gap" sat in your own prior doc
> with the wrong verdict, fix that doc too and log the correction in its evidence note.

A greenfield bet still needs a "why this player": strategic fit (does it serve their stated bet?),
groundwork already laid (is the precursor shipped?), and an ownable message. State the honest caveat
too — greenfield means no proven customer pull yet, so it competes against urgent work.

> Triage is THREE-WAY, not two-way: catch-up, greenfield, and STRUCTURAL NON-GAP (6d below).
> Before you file a "trails here" axis as catch-up, run it past the 6d test — a lot of "gaps"
> are really non-gaps the vendor should be told NOT to chase.

## 6d. The structural NON-GAP — "trails here" is not the same as "should invest here"

The weak gap analysis lists EVERY axis where the vendor isn't #1 and says "invest in all of them."
That is bad product advice. Some axes a vendor trails on are not product holes at all — they are
**market-access realities** the vendor cannot and should not try to close. Filing them as gaps points
investment at markets the vendor can't win, and it buries the one or two real gaps in noise.

**The test (run it on every "trails here" axis before calling it a gap):** ask *"could this vendor
win here if it invested?"* If the barrier is a MISSING FEATURE → real gap (catch-up or greenfield).
If the barrier is one of these, it's a structural non-gap — carve it out:
- **National / regulatory mandate** you're on the wrong side of (e.g. China 信创 domestic-stack
  requirement — no Western platform can play inside China; it's sovereignty, not a feature).
- **Geography / platform you don't own** (e.g. super-app distribution — Foundry owns the Teams/M365
  seat where its users live; it cannot acquire WeChat/DingTalk reach. The market is structurally closed,
  not under-served).
- **A different buyer segment / market** (e.g. China live-commerce digital-human livestreaming — not
  the enterprise buyer; the enterprise slice of it, real-time voice, the vendor already covers).
- **A business-model / go-to-market choice** (e.g. full-service "sit with you and run it" ToB delivery
  vs self-serve SaaS + partners — changing this is a GTM decision, not a product build).

**Carve them out EXPLICITLY, with the reason — never silently omit.** A dedicated "Where NOT to invest
(structural non-gaps)" section (a small table: axis | who owns it | why the vendor shouldn't chase it)
does two jobs: it proves you SAW the axis (silent omission reads as "you missed it"), and it protects the
real investment list from dilution. The honest one-liner: *these aren't weaknesses to fix; they're the
home-market structure of the regional players that an outside vendor can't and shouldn't try to match.*

Motivating case (Foundry platform analysis, June 2026): Foundry trailed on ~7 axes (verticals,
real-time multimodal, channel distribution, plus four China axes — 信创 sovereignty, super-app reach,
live-commerce digital humans, full-service delivery). Naive output: "invest in all 7." Correct triage:
ONE catch-up (verticals — and even that was "repackage existing Dynamics 365 / industry-cloud assets
into Foundry," not net-new build), ONE greenfield (govern the multi-agent mesh), one minor (developer
funnel / free tier), and FOUR structural non-gaps deliberately carved out as "do not chase." Out of
seven "trails here" axes, only one was a true catch-up. That filtering IS the value of the analysis.

## 6e. Mirroring an existing doc's structure when the user names one as the template

When the user says "referring to the doc structure of <file>" (or "same shape as X"), they want the
NEW doc to reuse the skeleton of the named one, adapted to the new subject — not a fresh structure.
Read the template doc first, lift its section skeleton verbatim (e.g. Takeaway → Section 1: position
table → Section 2: gaps one-by-one with the catch-up/greenfield split + the green honest-caveat callout
→ evidence & confidence notes → open questions), then pour the new analysis into it. Keep the same
heading names, the same ordering, the same callout conventions. You MAY add one section if the new
subject needs it (this session added a "Where NOT to invest" section, see 6d) — but flag the addition
rather than silently restructuring. Mirroring the structure is what makes the doc set feel like one
coherent body of work instead of a pile of one-offs.

## 6b. "Ahead" vs "parity/complete" — claim the defensible one

When the user asks you to double-check your OWN conclusion, audit superiority claims hardest.
"X is AHEAD on these three aspects" is rebuttable the instant one rival turns out to have the same
thing — and it usually does. "X is COMPLETE / at parity (no competitor offers something it lacks)"
is the stronger AND more defensible claim, and it's usually the true one.

Motivating case: an early draft claimed Foundry was "ahead on three" (anomaly detection, cache-hit
visibility, cross-vendor routing). On audit all three were parity — AWS has ML anomaly bands, AWS/GCP
expose cache token counts, the clouds all route. Downgrading "ahead" → "complete/parity" lost nothing
real and removed three easy rebuttals. Rule: prefer "complete / nothing missing vs rivals" over
"ahead / beats rivals" unless you can cite the exact thing a named rival cannot do. Better packaging
of a feature everyone has is parity, not a lead.

## 6c. Tier your "why invest" evidence — developer-layer signal ≠ enterprise demand

When justifying an investment, separate evidence of "the problem is REAL" from evidence of
"ENTERPRISES will pay to solve it." They are different altitudes and a low-altitude signal does not
prove the high-altitude claim.

- Bottom-up / developer-layer signals (a hobbyist harness telling users "keep memory small," a CLI
  showing a context-pressure meter) prove the problem is FELT and name the direction of travel
  (e.g. market moving from "display tokens" to "manage tokens"). They support the WHY-NOW.
- They do NOT prove enterprises will buy an enterprise-grade version. The examples are the LEAST
  enterprise players in the matrix; "keep my memory file small" is self-discipline, not demand for
  a platform-enforced control.

So cite such signals as CORROBORATING ("the problem is becoming named, bottom-up"), never as
load-bearing demand. The load-bearing pillars stay: strategic fit + groundwork laid. If you want
real demand evidence, find the enterprise version of the signal (a platform customer asking for the
exact feature), and say plainly when you only have the developer-layer version.

## 6 — Scope axes must all be covered by the locked dimension set

When the user defines explicit scope axes up front (e.g. visibility / management /
cost-reduction / observability), map every comparison COLUMN back to an axis BEFORE
locking the dimension set at the checkpoint. A dimension set frozen too early
under-builds the axes you hadn't explored yet — one run shipped 9 columns that
covered 2 axes richly and 2 barely. If understanding deepens mid-run, re-open the
column set rather than leaving an axis thin.

## 7 — When asked to confirm a conclusion, JUDGE — do not rubber-stamp
The user said it directly: *"don't just follow what I said... I need your help to judge together."*
When asked "do you agree?", actively try to BREAK the conclusion, then report honest agreement AND
disagreement: which sub-claims hold, which are overstated. Separate the defensible **spine** from
the overstated **support**. (Observed: agreed the spine — "Foundry is complete + the one bet is a
greenfield" — but corrected "ahead on three aspects" down to "parity," and split a conflated gap
into present-maturity vs future-greenfield.) Agreeing too fast on an overstated claim is a failure
mode — the weakest link gets rebutted by a domain expert (a vendor PM, a rival).

## 8 — Separate a PRESENT gap from a FUTURE gap
A capability blank and a maturity lag are different gaps and get different treatment:
- **Present gap (self-closing):** the feature EXISTS but is still in preview while rivals shipped
  general availability. Real today (enterprises won't build on preview), but it closes itself on
  the GA timeline — nothing to build, only to graduate. Frame it as a maturity item, not a
  capability hole.
- **Future gap (a true blank):** the capability does not exist at all. This is the one to actually
  build. (Observed: Foundry's per-agent monitor was a present gap — preview, self-closing — while a
per-agent cumulative budget was a future gap — genuinely missing.) Don't let a self-closing
preview-vs-GA item read as if it were a capability investment.

## 9 — The "who wins" evidence must be COMPLETE per rival, not a sample — and completing it can resize the gap

When you credit a rival with beating you on a gap, list that rival's FULL capability set for the
dimension, not a few examples. "Salesforce wins on channels — Slack + WhatsApp + telephony" is a
SAMPLE. The real evidence is the rival's complete list (website, mobile, WhatsApp, Facebook
Messenger, Apple Messages, LINE, SMS, voice). A sampled "who wins" cell reads as thin evidence and
hides how big the gap actually is. The user will catch it: *"you must provide the full list per
winner, instead of just naming some of the whole."*

Three rules:
1. **Enumerate every filler with what each provides, from its OWN doc.** For each rival that beats
   you, pull its primary page and list the complete set (the full channel list, the full connector
   catalog, the full modality set), each backed by that vendor's URL. Same disprove / primary-source
   bar as §2. Quote the line that proves the list (e.g. the vendor's "Messaging supports A, B, C, D,
   and E" sentence).
2. **Completing the evidence can resize the gap — then propagate it.** A sampled gap usually
   understates itself. When the full list shows the gap is wider (or narrower) than the sample
   implied, update the gap's severity AND any downstream prescriptive note ("what to build") to
   match — never leave the build note describing the old sampled scope. (Observed June 2026: a
   Foundry channel gap was first written as "add native Slack/WhatsApp." The full lists showed
   Foundry was native ONLY on Teams/M365 + custom web/app + voice and missing the WHOLE
   customer-messaging surface — WhatsApp, Facebook, SMS, Apple Messages, LINE. The "what to build"
   note had to widen from "Slack/WhatsApp" to the full surface, and the value re-tagged
   buyer-conditional — home turf of customer-facing / B2C agents, not internal Teams agents. The one
   downstream takeaway bullet that still said "Slack/WhatsApp" had to be fixed too, so the doc didn't
   contradict itself.)
3. **Stay honest while completing — don't pad the winner list (ties back to §6b / §7).** A rival
   that only PARTIALLY fills the gap, with the same indirection you have, is NOT a clean win — mark
   it partial and say why (Observed: AWS takes video only as grounding via Nova embeddings, the same
   indirection as Foundry — listed as "partial, not a clean win," not a winner). And an object with
   NO confirmed filler gets that stated explicitly ("no confirmed list in public docs"), never
   silently dropped — silent omission reads as "you missed it." Completeness means the COMPLETE true
   picture, including partials and blanks, not a longer list of clean wins.
