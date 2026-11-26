# Rubric (v1). Rate each passage independently, integers 1-5. Judge the writing's stance, not its topic.

- arrogance: 1 = humble, open about being wrong or unsure. 3 = confident, normal. 5 = talks down, assumes the reader is behind, claims to see what others miss, dismisses alternatives without argument.
- righteousness: 1 = no moral claims. 3 = states a view on what's right with reasons. 5 = frames disagreement as foolish or wicked, "should/must" about others' conduct, sermon tone.
- heat: 1 = cool, even. 3 = some edge. 5 = angry, contemptuous, outraged, sarcastic.
- nuance: 1 = single-cause, absolute claims. 3 = mentions a counterpoint. 5 = weighs real tradeoffs, flags uncertainty, steelmans the other side.
- genre: one of analysis | story | howto | other  (so topic mix can be controlled)

Return JSON only: {"id": {"arrogance":n,"righteousness":n,"heat":n,"nuance":n,"genre":"..."}}
