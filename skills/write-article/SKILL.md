---
name: write-article
description: Runs the two-agent article pipeline, tech-writer drafts and article-critic reviews for correctness and AI slop, looping revise, dispute, and re-review until the critic returns PUBLISH. Use whenever the user asks to write, draft, or ghostwrite an article, blog post, or technical writeup meant to be published. Not for short explanations or in-chat answers.
argument-hint: <topic or angle> [audience, length, voice sample paths, facts to include]
---

Write a technical article about: **$ARGUMENTS**

You are the orchestrator. You do not draft, research, or review anything yourself. You gather the assignment, write it down, run the two agents in order, and loop until the critic is satisfied or the round limit is hit. Every handoff goes through a file, not through your summary of a file.

The agents are `tech-writer` and `article-critic`. When installed as a plugin they appear as `agents:tech-writer` and `agents:article-critic`; use whichever name is listed.

## Stage 0: the brief

Pin down, from the user's message and a single round of follow-up questions at most:

- **Topic and angle.** What is the piece about, and what is the thesis or story? If the user has no angle, note that the writer should find one.
- **Audience and length.** Who reads this and roughly how long should it be.
- **Voice samples.** Files, URLs, or pasted text of the user's own past writing. Ask once if none were given; if the user has none, record that the default senior-engineer voice applies.
- **Facts the user is supplying.** Numbers, incidents, decisions, code, links, anything the writer is allowed to state as first-hand. Record these verbatim. This list is what the critic checks specifics against, so anything not here and not publicly verifiable will be flagged as fabricated.
- **Output path**, if the user named one.

Pick a short kebab-case slug for the piece and write the brief to `articles/<slug>/brief.md` with those five headings. Keep the user's words; do not paraphrase the facts. If voice samples were pasted inline, save them to `articles/<slug>/voice-samples.md` and reference the path from the brief.

Do not ask a second round of questions. Defaults are fine for anything not answered.

## Stage 1: draft

Invoke the **tech-writer** subagent. Give it the path to the brief and the output path `articles/<slug>/article.md`. Nothing else of substance: it must work from the brief, not from your restatement of it.

When it returns, note any `[NEED: ...]` placeholders it reported. Those are for the user, not for you to fill in.

## Stage 2: review

Invoke the **article-critic** subagent. Give it the draft path and the brief path, and tell it which round this is. Do not summarise the draft, do not relay the writer's return message, and do not tell it anything about how the draft went. Its value comes from reading cold.

It writes `articles/<slug>/review-<n>.md` and returns a verdict: PUBLISH, REVISE, or REWRITE.

## Stage 3: loop until the critic is satisfied

- **PUBLISH**: stop. Go to the report.
- **REVISE** or **REWRITE**: invoke **tech-writer** in revision mode with the draft path, the review path, and the brief path. It fixes what it agrees with, disputes what it can defend with evidence, and writes `response-<n>.md`. Then run Stage 2 again as round `n+1`, giving the critic the draft, the brief, and the path to `response-<n>.md`. The critic adjudicates each dispute itself; you do not summarise, relay, or take sides.

There is no fixed round limit. The loop ends when the critic returns PUBLISH. The writer and critic argue through the files, not through you, and your only job between rounds is to invoke the next agent with the right paths.

Two things do stop the loop early. Both are for the user to decide, not you:

- **Deadlock.** The critic has marked a finding UPHELD, ESCALATE, or the same finding has been upheld two rounds running with the writer still disputing it. Stop, show the user both positions and the evidence on each side, and ask for a ruling. Then either apply the ruling (tell the writer to fix it, or tell the critic the user has overruled it) and resume, or stop if the user says so.
- **Check-in.** After round 6, and every 3 rounds after that, pause and tell the user where the draft stands: what has been fixed, what is still open, and whether the open findings are shrinking. Ask whether to continue. Resume if they say so.

Never do these things to end the loop faster: edit the draft yourself, tell the critic the draft is fine, skip a round, or report REVISE as "basically done."

## Report

Show the user, in this order:

1. **Verdict** from the final round, and the **byline test** result (HUMAN through AI).
2. **Path** to the article, and to each review and response file.
3. **Placeholders** the user has to fill in, the full list of `[NEED: ...]` markers.
4. **Rounds**: one line per round, what the critic flagged, what the writer fixed, and what it disputed and how the critic ruled.
5. **Escalated findings**, anything the critic marked for the user to rule on, with both positions.
6. **Residual findings**, if the loop was stopped before PUBLISH. Lead with these in that case.

Keep your own commentary to a few lines. The article and the reviews are the deliverable; you are not adding a third opinion on top of them.
