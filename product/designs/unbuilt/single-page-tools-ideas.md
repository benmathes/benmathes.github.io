# Single-Page Tools & Toys: 10 Ideas

Based on themes from [adventurecapital.substack.com](https://adventurecapital.substack.com): systems thinking, skepticism of complexity, semantic drift, consensus dynamics, Goodhart's Law, and cross-domain pattern recognition.

---

## 1. Goodhart's Gambler

**Concept:** Interactive simulation showing how optimizing for a single metric corrupts it over time.

**How it works:**
- User picks a "goal" (user engagement, revenue, test scores)
- Simulation runs showing actors gaming the metric
- Visual divergence between metric and original intent
- Reset and try different constraints

**Why it fits:** Direct extension of your Goodhart's Law piece. Makes abstract economic concepts tangible.

**Complexity:** Medium (JavaScript simulation, chart visualization)

---

## 2. Semantic Drift Detector

**Concept:** Paste two texts (or enter two terms) and see how the same words carry different meanings across contexts.

**How it works:**
- Enter a term like "agent", "model", "learning"
- Shows definitions/usage from: AI/ML, psychology, business, philosophy
- Highlights where meanings conflict or get confused
- Optional: LLM-powered examples of misunderstandings

**Why it fits:** Directly from "The Accidental Semiotics Shuffle" - making the semantic confusion visible.

**Complexity:** Medium (could be static definitions or LLM-powered)

---

## 3. Sticky Starter Visualizer

**Concept:** Interactive demo of how first impressions calcify in consensus cultures.

**How it works:**
- Simulated "team" rates a new idea/person
- First rater sets anchor
- Watch how subsequent ratings cluster around the anchor
- Toggle between "consensus culture" and "independent rating" modes
- Shows the statistical distribution difference

**Why it fits:** Makes "The Sticky Starter Shadow" thesis interactive and visceral.

**Complexity:** Medium (simulation + charting)

---

## 4. Complexity Tax Calculator

**Concept:** Estimate the hidden costs of over-engineering your dev environment or system.

**How it works:**
- Checklist of common over-complications (Docker, K8s for solo projects, custom build systems, etc.)
- Each adds "complexity debt" score
- Calculates: time to onboard new dev, context-switching cost, debugging overhead
- Compares to simpler alternatives
- Outputs a "complexity tax" as hours/week wasted

**Why it fits:** Your "Dev Environment Should Not Be Overcomplicated" piece as a tool.

**Complexity:** Low (questionnaire + scoring formula)

---

## 5. Systems Failure Pre-Mortem

**Concept:** Structured walkthrough to identify where a system/project will fail before it does.

**How it works:**
- User describes a system or project
- Tool prompts with questions from complexity theory (feedback loops, coupling, single points of failure)
- Generates a "failure map" with likely cascade paths
- Optional: LLM suggests interventions

**Why it fits:** "Systems Thinking and the Denial of Death" - practical application of accepting failures will come.

**Complexity:** Medium-High (structured prompts, optional LLM)

---

## 6. Keynes Quote Killer

**Concept:** Database of misused economics quotes with context and corrections.

**How it works:**
- Click to get a commonly misquoted econ maxim
- Shows: the quote, common misuse, actual context, what it really means
- "In the long run we are all dead" as the first card
- Shuffle through classics (invisible hand, creative destruction, etc.)

**Why it fits:** Your "I Hope One of Keynes's Memes Would Die" piece - a corrective database.

**Complexity:** Low (static content, card UI similar to Oblique Strategies)

---

## 7. Librarian or Butler?

**Concept:** Quiz/classifier to determine what kind of AI agent you actually need.

**How it works:**
- User describes their use case
- Series of questions about autonomy, verification needs, risk tolerance
- Outputs: "You need a Librarian" (retrieval/research) or "Butler" (execution) or hybrid
- Explains why and common mistakes of picking wrong type

**Why it fits:** Your "Agents: Librarians or Butlers?" piece as a practical decision tool.

**Complexity:** Low-Medium (questionnaire + logic tree)

---

## 8. Meta-Modernism Mood Board

**Concept:** Visual/interactive explainer that cuts through the bollocks of meta-modernism discourse.

**How it works:**
- Interactive timeline: Pre-modern → Modern → Post-modern → Meta-modern
- Click each era: see worldview, failure mode, what it was reacting against
- "Oscillation visualizer" showing the meta-modern both/and dynamic
- Counter-examples of what meta-modernism is NOT

**Why it fits:** Your "Meta-Modernism, from the word itself" piece - making the framework graspable.

**Complexity:** Medium (interactive visualization)

---

## 9. Dinner Party Fatalism Detector

**Concept:** Paste a take/opinion and get scored on how much it's cosplaying as wisdom vs. actual insight.

**How it works:**
- User pastes a hot take or received wisdom
- Tool checks for: vague timeframes, unfalsifiability, doom-as-sophistication, citation of authority without substance
- Outputs a "fatalism score" with breakdown
- Suggests how to make it more rigorous

**Why it fits:** Your "Keynes meme" piece's critique of dinner-party fatalism as pseudo-sophistication.

**Complexity:** Medium (could be rule-based or LLM-powered)

---

## 10. The Consensus Crusher

**Concept:** Anonymous voting tool that reveals opinions before showing the group consensus.

**How it works:**
- Create a room, share link
- Everyone submits their rating/opinion BLIND (can't see others)
- Only after everyone submits: reveal all votes simultaneously
- Shows: true distribution vs. what a serial voting would have produced
- Useful for team retros, design critiques, hiring decisions

**Why it fits:** Practical tool against "Lowest Common Consensus" and sticky-starter effects.

**Complexity:** Medium-High (needs backend for rooms/votes, or clever peer-to-peer approach)

---

## Prioritization Notes

**Lowest effort, high payoff:**
- #4 Complexity Tax Calculator (questionnaire)
- #6 Keynes Quote Killer (static content)
- #7 Librarian or Butler Quiz (logic tree)

**Medium effort, directly extends writing:**
- #2 Semantic Drift Detector
- #3 Sticky Starter Visualizer
- #1 Goodhart's Gambler

**Higher effort, most novel:**
- #10 Consensus Crusher (needs persistence)
- #5 Systems Failure Pre-Mortem (LLM integration)

All can be built as single HTML files using Tailwind + vanilla JS, consistent with your existing projects.
