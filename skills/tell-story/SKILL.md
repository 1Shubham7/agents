---
name: tell-story
description: Writes a new true story from tech, saved as one file in stories/ with a primer that teaches the user the story and its concepts with examples and code, an X post within 280 characters, a LinkedIn post, and an image prompt. Use when the user asks for a story, a tech story, or a story post for X/Twitter or LinkedIn, or asks for a primer to be added to an existing story file. Not for technical articles (write-article) or explanations (teacher).
argument-hint: [topic, person, or area] [number of stories] | [path to a story file that needs a primer]
---

Tell a story about: **$ARGUMENTS**

If nothing follows the colon, the agent picks the story. If what follows is a path to an existing file in `stories/`, the job is to add a primer to that story, and the agent is told so in place of a topic.

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

Pass on the agent's report: the file path, the story in one line, the concepts the primer teaches and whether its code was run, the X post with the character counts, and any notes about facts to double-check before posting. Tell the user to read the primer at the top of the file before posting. The posts are finished work, so relay them as written.
