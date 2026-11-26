# Tone drift: preregistration

Written before any scoring. Thresholds are proposed by Claude and are open to your veto until Checkpoint A. After that they're locked.

## Scope right now
- **H2 (your writing), run on the Adventure Capital Substack** (88 public posts, 2020-2026) because the X archive hasn't arrived. Same test gets rerun on tweets when it does.
- **H1 (Sharp Tech): not started.** Transcripts need your Passport login, and this cloud container has no access to it. Needs your saved pages or your machine.

## Measures
Each ~150-word passage gets 1-5 ratings: `arrogance`, `righteousness` (moralizing / "people who disagree are wrong or bad"), `heat` (outrage), and `nuance` (acknowledges tradeoffs / uncertainty). Scored by Haiku subagents against a written rubric. Stored: labels, counts, hashes. Not stored: text.

## What counts as "no, this isn't happening"
**H2: writing got more arrogant/righteous after you started using AI agents heavily.**
- Primary test: mean arrogance+righteousness per passage (post-level means, so long posts don't dominate), before vs after the exposure-start date. Bootstrap over posts, 95% CI.
- **No effect** if the CI for the post-minus-pre difference includes 0, OR the point estimate is under **0.3 points on the 5-point scale** (about 0.4 SD, assumed).
- **Not credited to agents** even if the difference is real if: placebo split dates (every other 6-month boundary with enough posts on each side) produce differences as large as the real one in 1 of 5 or more cases; or the effect vanishes after controlling for topic (politics/culture-war vs. tech/product vs. personal).
- **Dose-response** (needs your agent-use series): no support if monthly dose vs. tone correlation at lag 1-3 months has a CI including 0, or tone-leads-dose correlation is as large as dose-leads-tone.
- With 88 posts and a thin 2021-2024, a null here means **low power**, not proof of no change. I'll report the minimum detectable effect next to every null.

**H1: Sharp Tech drifted from nuance toward moralizing/outrage.**
- Count it as **no drift** if the yearly trend in LLM `heat` and `righteousness` has a slope CI (episode-level, clustered by year) including 0, or the standardized change from first to last year is under **0.3 SD**, or the word-list and LLM trends disagree in sign.
- Run on `tech_only` segments too. If drift appears only in all-segments, it's topic mix (China/geopolitics/NBA), not tone.

## Known alternative explanations (to be checked, not assumed away)
Topic mix shifting; the 2020 cluster (11 posts in one month) being a different genre; the model's own rating bias (scored in random order, rubric fixed, 25-passage human audit); platform and role changes for tweets.
