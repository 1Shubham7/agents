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

### tech-writer

Writes technical articles and blog posts that read as genuinely human-written, not AI-generated, in your own voice where you provide samples.

Before drafting, it reads a handful of old (pre-2022) posts from Cloudflare's blog, the Netflix Tech Blog, and Stripe's engineering blog, specifically to study structure and rhythm from writing that predates LLM-assisted drafting. It then writes while actively avoiding the usual AI tells: em dashes used as punctuation, stock transition phrases ("moreover," "it's important to note"), the rule-of-three adjective crutch, LLM-flavored vocabulary ("leverage," "delve," "seamless"), generic headers, and canned intros or outros. It self-reviews its own draft against that checklist before showing it to you.

Defaults to Markdown output, written to a file rather than left only in chat.

Usage: ask Claude to "write an article about X" or "draft a blog post on X." Have a topic, a rough angle, and ideally a sample of your own past writing ready if you want it calibrated to your specific voice rather than a generic senior-engineer voice.

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
