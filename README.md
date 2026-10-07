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

**write-article** is the skill that orchestrates. It collects the assignment into `articles/<slug>/brief.md` (topic, angle, audience, voice samples, and the facts you're supplying, recorded verbatim), runs the writer, runs the critic, and if the verdict isn't PUBLISH sends the review back to the writer and reviews again, for as many rounds as it takes. The writer doesn't have to accept every finding: it can dispute one with evidence (the number is in the brief, here's the primary source, the voice sample uses the same construction), and the critic has to rule on the dispute by checking that evidence, withdrawing the finding if the writer is right. If the two genuinely deadlock on a judgment call, it's escalated to you to rule on rather than looping forever. All handoffs go through files (`review-N.md`, `response-N.md`), so neither agent ever works from a summary.

Usage: `/write-article <topic>` or just "write an article about X". Have a topic, a rough angle, any real numbers or incidents you want in it, and ideally a sample of your own writing. Output lands in `articles/<slug>/`: `brief.md`, `article.md`, and one `review-N.md` and `response-N.md` per round.

You can still call `tech-writer` alone for a draft with no review, or point `article-critic` at any existing draft to get it judged.

### story-teller (and the tell-story skill)

Finds a true story from tech and writes it up for posting: one file in `stories/` with an X post inside the 280-character limit, a LinkedIn post, and a prompt you can hand to an image model for the picture that goes with both.

The file opens with a primer written for you and never posted. It tells the story in plain words, teaches each concept the story stands on (what it is, what problem it solves, the smallest example, then the same example broken the way the story breaks it), walks through how those concepts play out in the incident, and lists what the posts leave out, including the objection a sharp commenter is most likely to raise. Code in the primer is run before it is shown, and the output is the output it printed. The agent writes the primer before the posts, because a post is a compression and it cannot compress what it does not understand.

The stories come from anywhere in tech: languages, tools, hardware, security, the people behind them. In DevOps and programming it is allowed to go niche, down to a flag, a default, or a line in a postmortem. Each run reads what is already in `stories/` and picks something new, with a different opening and a different image style from the recent ones.

Two rules shape everything it writes. The story has to be true: it fetches at least two sources per run, every name, date, number, and quote has to appear in one of them, and the file ends with a `Sources` section so you can check before you post. It never writes in the first person about things you did not do. And it has to read like a writer wrote it, which is what `skills/tell-story/guide.md` is for. The guide distills twelve books on storytelling and why ideas spread (*Made to Stick*, *Contagious*, *Wired for Story*, *Putting Stories to Work*, *The Storytelling Animal*, Campbell's monomyth, *TED Talks*, *Influence*, *Start With Why*, *Ego Is the Enemy*, and others) into working instructions: what counts as a story, how to choose one, how to build it, how to make it stick and travel, what human prose is made of, how to teach a concept in the primer, and how to write each of the outputs. The agent reads it in full on every run.

`skills/tell-story/check_story.py` does what a model cannot do reliably. It counts the X post with X's own character weighting, checks the LinkedIn post against the 3,000 limit and the mobile fold, checks that the primer is present, comes first, and has code where the story is about code, and scans for em-dashes, stock vocabulary, the "it wasn't X, it was Y" reversal, one-sentence-per-line cadence, and flat sentence rhythm. The agent runs it and fixes what it flags before reporting back.

`stories/` is in `.gitignore`. In any other repository the agent adds it to `.git/info/exclude`, so drafts never get pushed.

Usage: `/tell-story` for a story of its choosing, `/tell-story the history of grep` or `/tell-story something about Kubernetes networking` to steer it, or just "tell me a tech story". Stories written before the primer existed can get one added: `/tell-story stories/<file>.md`.

### cfp-writer (and the write-cfp skill)

Writes conference talk proposals that get accepted, or at least do not get rejected for the reasons most proposals do.

It works from three things that live in `skills/write-cfp/`. `guide.md` is the craft: how a tired reviewer reads a proposal in ninety seconds, what the accepted and rejected samples taught, the house style learned from hand edits to earlier drafts (name the areas and save the list for the talk, no asides written for effect, no praise for the talk in place of a description of it, "attendees" never "you", speak as the person who will stand on the stage), how to write the title, the description and the benefits section, how to sound like an experienced speaker in the talk's own field, and the tells that give a machine away. `samples/` holds real proposals the user has submitted, each with its outcome in the frontmatter, so the agent sees what worked and what did not. `outcomes.md` is the memory: one line per submission with the result and the user's own view of why, updated as results come in, so every later proposal knows more than the last.

It writes for one conference at a time and will not write without one. Given the conference, it fetches the CFP page for the form fields and their character limits, then reads the programme from the last one or two editions and writes down what the accepted talks have in common: title length and shape, whether they are first person, what they name, what is absent. Those notes land in `skills/write-cfp/conferences/<slug>.md` for the next run. The proposal is then written to fit that conference, in the voice of a working engineer, a maintainer, or a compliance practitioner depending on the talk, with every specific traced to something the user supplied and anything missing left as a visible `[NEED: ...]` rather than invented.

Drafts go to `cfps/<conference>/<talk>.md`, which is in `.gitignore`; in any other repository the agent adds it to `.git/info/exclude`.

Usage: `/write-cfp <talk idea> for <conference>`, or just "write a CFP for X". Have the conference name, the idea, who is speaking, and any real numbers or incidents you want in it. When the result comes in, add a line to `outcomes.md` saying what happened and why; that is how the agent gets better.

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

All agents install together as one plugin. Check `/context` under Custom Agents, or just ask for a standup, an article, a story, or a lesson, to confirm they loaded.

To register the agents and skills locally without going through the plugin, copy `agents/*.md` into `~/.claude/agents/` and symlink `skills/write-article` and `skills/tell-story` into `~/.claude/skills/`.
