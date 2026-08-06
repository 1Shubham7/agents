# standup-gen

A Claude Code agent that generates a standup update — plain bullet points, in your own casual voice — from the real work done in your current Claude Code session.

It doesn't just list what shipped. It includes dead ends, wrong turns, and detours that ate time but didn't lead anywhere, because that's usually what you actually need to explain in standup.

It also tracks itself: ask for a standup twice in the same session, and the second run only covers what happened since the first one — no repeats.

## Install

```
/plugin marketplace add 1Shubham7/standup-gen
/plugin install standup-gen@standup-gen
```

Then reload if prompted:

```
/reload-plugins
```

## Usage

Just ask, in any Claude Code session:

```
generate my standup
```

or "give me a standup update", "what did I work on today", etc. Claude will invoke the `standup-gen` agent, which reads the current session's transcript and writes the update.

## Notes

- Only covers the current session's transcript — it can't see across separate sessions.
- The very first time you ask in a session, it covers everything so far. Ask again later in the same session and it only covers what's new since the last time.
