---
name: write-newsletter
description: Writes one story for the Obmondo customer newsletter about a feature the user names, from the feature's Mattermost thread and Gitea time registrations, verified against the KubeAid and LinuxAid repositories and rendered into the edition's PDF. Use when the user asks for a newsletter story, post or item about a feature, or to add a feature to the newsletter. Not for blog posts (write-article) or talk proposals (write-cfp).
argument-hint: <feature name> [material: Mattermost thread, time registrations, notes, PR links]
---

Write a newsletter story for: **$ARGUMENTS**

You are the dispatcher. The `newsletter-writer` agent reads, verifies and writes; you collect what it needs and relay what it returns. When installed as a plugin the agent appears as `agents:newsletter-writer`; use whichever name is listed.

## 1. Find the agent's material

Two things, and the agent will not run without both:

- **The guide.** `guide.md` sits next to this file, in this skill's base directory. Work out its absolute path.
- **The outreach repository**, which holds the newsletter at `newsletter/`. Look for it at `~/Code/EnableIT/outreach`, then at `outreach/` under the current working directory, and confirm with `git -C <path> remote get-url origin`. If it is not there, ask where it is.

## 2. Collect the assignment

Pin down, from the user's message and one round of questions at most:

- **The feature**, by its title as the portal shows it, and its milestone ID if the user has it. One feature per run.
- **The material.** The Mattermost thread, pasted or as a file; the time registration comments from the Gitea issue; any notes; pull request links. Pass all of it through verbatim. The agent decides what is noise, and it cannot decide that from a summary.
- **The edition**, if not the newest one in `newsletter/`.
- **The topic**, if the user already knows which heading the story belongs under.

Do not ask a second round. Material the user does not have becomes a `[NEED: ...]` in the story, which is the right outcome.

## 3. Run the agent

Invoke **newsletter-writer** with:

- the absolute path to `guide.md`
- the absolute path to the outreach repository
- everything from step 2, in the user's words and the material verbatim

Send nothing else. Do not summarise the thread and do not propose an angle; the agent reads the raw material and the repositories and works out the story from them.

## 4. Relay

Pass on the agent's report: the files it changed, the topic, the upstream source for each date and version, what it left out as internal or noise, every `[NEED: ...]`, and the one thing the story teaches. The story is in the rendered PDF at `newsletter/newsletter-<year>-<month>/newsletter-<year>-<month>.pdf`; point the user at it, since that is what they review. Nothing is committed; the user commits after reading the PDF.
