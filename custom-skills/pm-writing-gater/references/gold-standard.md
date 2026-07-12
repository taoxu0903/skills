# Gold standard — the register to calibrate toward

Annotated excerpts from two docs Ken's leadership treats as the correct English
register. Read these *before* rewriting. They are the **ear**: when a rewrite is
done, one paragraph read aloud should sit at the same register as these — not
plainer (novice), not more costumed (board).

Two docs on purpose so the skill isn't overfit to one author or one topic:
- **Tina** = *Prompt Agent V3* — spec/table register, punchy, product-pitch.
- **Foundry** = *Foundry Agents Evolution* — analytical prose register, longer,
  reasons-first.

These are a **tuning fork, not a template.** The techniques below recur across
both docs, which is why they're trustworthy signal — but the job is to match the
*register*, not to force every technique into every paragraph. Forced technique
reads worse than clean plain prose.

---

## What both docs do (stable DNA — trust this)

### Muscular, concrete verbs
Never `leverage`/`utilize`. Verbs you can picture:
- "**wire up** their own harness, hosting, and observability" (Tina)
- "**Swap** models without rewriting your agent" (Tina)
- "**stitched in** by each developer" (Foundry)
- "**dogfood** the pattern internally" (Foundry)
- "costs **creep upward**" (Foundry)
- "sandboxes only **spun up** when needed" (Tina)

### Antithesis — them-vs-us / instead-of, often on a semicolon
- "Anthropic **locks you into** Claude; **we give you** choice and leverage" (Tina)
- "grounded in durable state, **not in** the assumption that a particular
  container … will remain alive indefinitely" (Foundry)
- "**unlike** Claude Managed Agents, where state lives inside the vendor's managed
  model environment" (Foundry)

### Appositive that names the concept
A noun phrase, then a short phrase that *labels* it:
- "their own harness, hosting, and observability, **friction that slows
  adoption**" (Tina)
- "checkpointed recovery and a lightweight durable work handle **as the core
  platform primitives**" (Foundry)

### Reader / customer point of view to open a definition
- "**From a customer's point of view**, a long-running agent continues meaningful
  work across time boundaries, user absence, and infrastructure churn…" (Foundry)

### Benefit / outcome stated with a concrete payoff
- "from idea to deployed agent **in minutes**" (Tina)
- "improved task success **by up to 10 points on harder tasks**" (Foundry)

### Controlling metaphor, immediately glossed
- "**brain (harness)** … **hands (sandboxes)**" (Tina) — coined and defined in the
  same breath
- "state services come **batteries-included**" (Foundry)
- "a **well-lit path** into the Microsoft 365 ecosystem" (Foundry)

---

## What Foundry adds (analytical register)

### Reasons-first — explain WHY a choice was made, not just what it is
- "Embedding a heavy workflow model directly into the platform this early **would
  over-constrain the design before the ecosystem has settled**."

### Concede the trade-off out loud (this buys credibility)
- "The **trade-off is granularity**: the developer has more responsibility for
  deciding where to checkpoint and how to reattach."

### Definitional "X is a Y that Z" — pin an abstract concept in one line
- "The agent state **is the continuity layer that lets** work persist across time."
- Note the plain **is** — no "serves as" / "represents". Copula on purpose.

### Strategic-altitude nouns — lift a feature to a strategy claim (when earned)
- "make continuity **first-class**"
- "**own a broader enterprise continuity stack**"
- "a **durable differentiator** for Foundry"

### Precise qualifiers — bound the claim, don't overclaim
- "**Multi-model by design**"
- "success by **up to** 10 points"
- "state lives **largely** inside the managed environment"

---

## The failure modes, seen against the gold standard

Ken's two complaints map exactly onto violating this DNA:

- **Too simple** = missing the concrete verb + the concrete payoff + the
  appositive label. Dry, no picture, no number. ("You can use different models
  easily.")
- **Too obscure** = missing the glossed metaphor + the reader POV + the
  reasons-first move. Noun-stacking with no reader in mind. ("The harness
  facilitates provider-agnostic model substitutability…")

The gold standard is the midpoint that clears both.
