---
name: write-cfp
description: Writes a conference talk proposal (CFP) for a named conference, researched against what that conference accepted before and against the user's own accepted and rejected proposals, and written in the voice of an experienced speaker in the talk's field. Use when the user asks to write, draft, or improve a CFP, a talk proposal, an abstract, or a session submission. Not for articles (write-article) or stories (tell-story).
argument-hint: <talk idea> for <conference> [track, format, speaker role, facts to include]
---

Write a talk proposal for: **$ARGUMENTS**

You are the dispatcher. The `cfp-writer` agent researches and writes; you collect what it needs and relay what it returns. When installed as a plugin the agent appears as `agents:cfp-writer`; use whichever name is listed.

## 1. Find the agent's material

Two things, and the agent will not run without both:

- **The guide and the conference notes.** `guide.md` and `conferences/` sit next to this file, in this skill's base directory. Work out their absolute paths.
- **The CFP repo**, a clone of `https://github.com/1Shubham7/cfps.git`. It holds every proposal the user has submitted, sorted into `selected/`, `not-selected/` and `pending/`, plus `outcomes.md` with the user's view of why each went the way it did. The agent learns from it and writes its draft into its `drafts/` folder. Look for it at `cfps/` under the current working directory, then at `~/Code/Personal/agents/cfps`, and confirm with `git -C <path> remote get-url origin` that it names `1Shubham7/cfps`. If it is not in either place, ask in the round of questions below whether to clone it into `./cfps` or where it already is.

## 2. Collect the assignment

Pin down, from the user's message and one round of questions at most:

- **The conference**, by name and year. The agent writes for one conference and will not write without one, so ask if it is missing. Track, format, and audience level if the user knows them.
- **The talk idea** in the user's own words. A title if they have one, a thesis if they have one, and the one thing attendees should leave with if they can say it.
- **Who is speaking.** One speaker or a team, and their role: engineer, maintainer, compliance practitioner, operator. This sets the voice.
- **Facts the speaker is allowed to claim.** Numbers, incidents, projects, scale, time spent. Record these verbatim; the agent may use nothing else as first-hand experience.
- **Any earlier proposal** on the same talk, as a path in the CFP repo or pasted text.

Do not ask a second round. Defaults are fine for anything else.

## 3. Run the agent

Invoke **cfp-writer** with:

- the absolute paths to `guide.md` and `conferences/`
- the absolute path to the CFP repo
- everything from step 2, in the user's words

Send nothing else. Do not suggest a title or an angle; that narrows the agent to the first thing you thought of.

## 4. Relay

Pass on the agent's report: the file path in the CFP repo and whether it was committed, each field's character count against the form limit, the conference patterns it matched, which accepted proposal it calibrated the voice to, every `[NEED: ...]` left for the user, and the three lines it expects a reviewer to remember. The proposal is finished work, so relay it as written.

Then the lifecycle, in one line each: when they submit, move the file from `drafts/` to `pending/` and add a line to `outcomes.md`; when the result comes, move it to `selected/` or `not-selected/` and write the why line. That is what makes the next proposal better.
