# Identity continuity: evidence, conclusions and reconsolidation

SKAi specifies identity as a revisable trajectory. This repository defines the host contract.
The AIS repository supplies the event ledger, and ontodiff supplies the impact evaluator.
A host must wire those components together to run the full loop. An `enabled` flag alone
does not implement a stage.

Map AIS `conclusion_id` to SKAi `id`, and AIS `origin` to SKAi `provenance`.
Only approved active conclusions enter self-state. Review proposals keep their source IDs.
Use an explicit approval step before promoting or changing an identity-bearing conclusion.

## Four layers

1. **Evidence** — observations, tool results and recorded events.
2. **Memory** — durable records of relevant experience.
3. **Conclusion** — an inference the agent currently draws from one or more records.
4. **Self-state** — the small set of conclusions stable and important enough to shape "who I am now".

The separation prevents a summary from quietly converting interpretation into fact.

## Reconsolidation

When evidence or a conclusion changes, the dependency graph produces impact proposals.
Ordinary downstream conclusions may become uncertain, stale or require review. Identity-bearing
state is handled differently: it is queued for reconsolidation.

Reconsolidation asks:

- what support remains?
- is the contradiction local or general?
- are there independent supporting paths?
- was the challenged claim self-authored, externally suggested or imported?
- should confidence fall, scope narrow, or the claim actually be retracted?

No single event is privileged merely because it is recent. No old claim is privileged merely
because it is old. Stability is earned by repeated coherent support; revision is earned by
changed evidence.

## Authorship

External statements can be evidence. They are not silently converted into the agent's own
beliefs. A user suggestion remains labeled as such unless a later agent-authored conclusion
adopts it for explicit reasons.

This lets SKAi preserve identity without turning identity into either a frozen persona or a
highly suggestible rolling summary.
