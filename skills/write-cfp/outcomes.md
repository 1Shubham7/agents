# Outcomes

The agent's memory across runs. One entry per submission, newest first, kept by the user. The agent reads all of it before writing, so the "why" line is the part that matters: it is how the next proposal learns from this one.

Add an entry when a proposal is submitted, and update it when the result comes in. A rejection with a reason is worth more here than an acceptance without one.

Format:

```
## <Conference Name Year>
- **<title>** (<format>, <track>): <accepted | rejected | waitlisted | pending>. Why: <the user's view, one or two lines>. Sample: <file in samples/, if any>.
```

## Patterns so far

- An engineering talk with a first-person story, three named symptoms in the first sentence, and two numbers in the benefits (three months, 100+ users) was accepted at four events as a lightning talk.
- A session proposal promising four things in one slot (enable, policy, ship, alert) has not been accepted so far. Hypothesis: one point made well beats a tutorial.
- Compliance drafts were cut by the user to name areas rather than list every item, and to remove asides, self-praise and digs at other guidance. That is the house style.

## Cloud Native Summit Kerala 2026
- **Cilium Network Policy Anti-Patterns I Learned the Hard Way** (Lightning talk, Security): accepted. Why: [user to fill in]. Sample: `samples/cilium-network-policy-anti-patterns.md`.

## KCD Gujarat 2026
- **Cilium Network Policy Anti-Patterns I Learned the Hard Way** (Lightning talk, Security): waitlisted. Why: [user to fill in]. Sample: `samples/cilium-network-policy-anti-patterns.md`.

## KubeCon + CloudNativeCon Europe 2027
- **The Clock Is Already Running: Will the CRA Block Your Product from Shipping to the EU?** (Session, Security): pending. Sample: `samples/cra-clock-is-already-running.md`.
- **Open Source Is Not Exempt: What the CRA Really Asks of Open Source Projects and Vendors** (Session, Security): pending. Sample: `samples/cra-open-source-is-not-exempt.md`.

## Other events, to be filled in by the user
- **Cilium Network Policy Anti-Patterns I Learned the Hard Way**: accepted at two further events in 2026. Why: [user to fill in].
- **Building Your Cluster's Memory for the Worst Day: Audit -> Detect -> Alert**: not accepted so far. Events: [user to fill in]. Why: [user to fill in]. Sample: `samples/kubernetes-audit-logging-detect-alert.md`.
