# agents

Personal Claude Code agents, packaged as a plugin so they're easy to install anywhere.

## What's in here

### standup-gen

Generates a standup update: plain bullet points, in your own casual voice, from the real work done in your current Claude Code session.

It doesn't just list what shipped. It includes dead ends, wrong turns, and detours that ate time but didn't lead anywhere, because that's usually what you actually need to explain in standup.

It also tracks itself: ask for a standup twice in the same session, and the second run only covers what happened since the first one. No repeats.

Usage: just ask, in any Claude Code session, "generate my standup" or "give me a standup update" or "what did I work on today." Claude routes this to the `standup-gen` agent, which reads the current session's transcript and writes the update.

Notes:
- Only covers the current session's transcript. It can't see across separate sessions.
- The first time you ask in a session, it covers everything so far. Ask again later in the same session and it only covers what's new since the last time.

### write-article (tech-writer + article-critic)

Writing a technical article is two jobs, so this is two agents and a skill that runs them in order.

**tech-writer** drafts. Before writing, it reads a handful of old (pre-2022) posts from Cloudflare's blog, the Netflix Tech Blog, and Stripe's engineering blog to study structure and rhythm from writing that predates LLM-assisted drafting. It writes in your voice if you give it samples, avoids the usual AI tells (em dashes as punctuation, stock transitions, the rule-of-three crutch, "leverage" and "delve" and friends, generic headers, canned intros and outros), and refuses to invent specifics: any number, incident, or decision you didn't supply becomes a visible `[NEED: ...]` placeholder instead of a plausible fabrication.

**article-critic** reviews the draft cold, without seeing anything the writer said about it. It judges two things:

- Is it correct? Every technical claim gets checked against a primary source (docs, source code, an RFC, or the repo itself if the article is about your code). Every code block gets checked for real APIs and flags. Every first-hand specific gets traced back to the brief you gave; anything that traces to nothing is flagged as fabricated.
- Does it read like a professional wrote it, or like AI slop? A mechanical grep for the tells above, then structural checks: are the sections suspiciously even, does every list have three items, could this paragraph be pasted into any other article on the topic (the substitution test), does the author ever actually take a position, do sentence lengths vary, is it explaining mutexes to backend engineers. It finishes with a byline test: would an experienced reader guess HUMAN or AI within two paragraphs, and which three quotes drove that call.

The verdict is PUBLISH, REVISE, or REWRITE, with every finding quoting the offending text and saying what the fix looks like. The critic doesn't rewrite the article; that would replace your voice with its own.

**write-article** is the skill that orchestrates. It collects the assignment into `articles/<slug>/brief.md` (topic, angle, audience, voice samples, and the facts you're supplying, recorded verbatim), runs the writer, runs the critic, and if the verdict isn't PUBLISH sends the review back to the writer for a revision pass and reviews again. Hard cap of three review rounds; if it still isn't there, you get told that rather than a softened verdict. All handoffs go through files, so the critic never reviews a summary.

Usage: `/write-article <topic>` or just "write an article about X". Have a topic, a rough angle, any real numbers or incidents you want in it, and ideally a sample of your own writing. Output lands in `articles/<slug>/`: `brief.md`, `article.md`, and one `review-N.md` per round.

You can still call `tech-writer` alone for a draft with no review, or point `article-critic` at any existing draft to get it judged.

### teacher

Teaches you concepts, tools, and code properly, assuming no prior knowledge. Builds explanations from the ground up (what the thing is, what problem it solves, how it works, then the details), uses concrete examples for anything abstract, and draws ASCII or Mermaid diagrams for anything with structure or flow.

When teaching a tool, it breaks the tool into its components first so you understand what the tool is actually doing, then connects the commands back to those components.

If you ask it to do a task and teach you at the same time, it does the task, narrates the why behind each step, then offers to create a `teach.md` file documenting what it did and the concepts involved.

You can also ask it to "double down" on any part you didn't get: it zooms in, goes one level deeper, and comes at it from a new angle with a fresh example or diagram instead of repeating itself.

Usage: "teach me how X works", "explain Y properly, don't assume I know it", "do this task and teach me what you did", or "double down on that part about Z".

## Install

```
/plugin marketplace add 1Shubham7/agents
/plugin install agents@agents
```

Then reload if prompted:

```
/reload-plugins
```

All agents install together as one plugin. Check `/context` under Custom Agents, or just ask for a standup, an article, or a lesson, to confirm they loaded.

To register the article pipeline locally without going through the plugin, copy `agents/*.md` into `~/.claude/agents/` and symlink `skills/write-article` into `~/.claude/skills/`.
