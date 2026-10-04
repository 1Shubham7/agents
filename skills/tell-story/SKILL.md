---
name: tell-story
description: Writes a new true story from tech as an X post within 280 characters, a LinkedIn post, and an image prompt, saved as one file in stories/. Use when the user asks for a story, a tech story, or a story post for X/Twitter or LinkedIn. Not for technical articles (write-article) or explanations (teacher).
argument-hint: [topic, person, or area] [number of stories]
---

Tell a story about: **$ARGUMENTS**

If nothing follows the colon, the agent picks the story.

You are the dispatcher. The `story-teller` agent chooses, researches, and writes; you hand it what it needs and relay what it returns. When installed as a plugin the agent appears as `agents:story-teller`; use whichever name is listed.

## 1. Find the guide

`guide.md` and `check_story.py` sit next to this file, in this skill's base directory. Work out their absolute paths.

## 2. Run the agent

Invoke **story-teller** with:

- the absolute paths to `guide.md` and `check_story.py`
- the folder to write into: `stories/` under the current working directory
- the user's topic, person, or area in their own words, or a statement that the choice is open
- any experience of their own the user offered for the story, verbatim

Send nothing else. A story idea from you narrows the agent to the first thing you thought of, which is the story everyone has already posted.

When the user asks for several stories, run the agent once per story, one after another. Each run reads the files already in `stories/` to avoid repeating a subject, an opening, or an image style, so parallel runs would collide.

## 3. Relay

Pass on the agent's report: the file path, the story in one line, the X post with the character counts, and any notes about facts to double-check before posting. The posts are finished work, so relay them as written.
