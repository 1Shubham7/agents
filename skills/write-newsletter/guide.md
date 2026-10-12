# Writing the Obmondo newsletter

How a newsletter story is written so that someone who gets forty emails a day reads it to the end. The style comes from five newsletters that engineers keep opening, read in October 2026, and from the stories already published in the Obmondo newsletter. Only the writing is borrowed from the five; their length and their sections are theirs, and the Obmondo story keeps its own shape, which `agents/newsletter-writer.md` describes.

## Part 1: what the five newsletters teach

Read a recent free issue of each when you want to recalibrate; the lessons below are what they taught, with the trait each one is best at.

### The IPE newsletter (ipenewsletter.substack.com)

Independent reporting on open source, with "What happened" and "Our take" as separate blocks under every story.

- **Background before news.** A story about disposable infrastructure first explains what changed about servers and databases, then what SQLite is in one sentence ("a single file that is easy to create, move and delete"), then what checkpointed execution is, and only then the announcement. The reader is never told about a change to a thing they have not been introduced to.
- **Fact and opinion kept apart.** The news is attributed to people and sources, stated plainly. The judgement lives in its own block and is written as a confident claim: "Dots are exactly the kind of use-case that merit disposable infrastructure in the first place." For Obmondo the equivalent of "Our take" is the Maintenance part: what we did and why, stated as a decision.
- **Links on the thing, not on "here".** The linked words are the name of the tool, the release, or the claim, in the middle of the sentence.
- **Numbers make it concrete.** "3,700 agents", "$20M", "10,000". A version number and a date do the same work in ours.

### The Pragmatic Engineer (newsletter.pragmaticengineer.com)

Long-form analysis of engineering decisions at named companies, by a former engineering manager.

- **History before the reversal.** The Shopify piece describes the 2020 move to React Native and what it bought before it reaches the 2026 decision to leave it. Cause and effect are laid out as a chain: the capability changed, so the cost calculation changed, so the decision followed. The Obmondo story is that chain in miniature: upstream changed, so the platform would have broken, so we did this.
- **Specifics ground every claim.** A 2 to 6 hour outage window, "Google did not update the status page", a percentage, a count. When a sentence has no specific, it is usually a sentence that could be cut.
- **The reader is invited to think, not told what to conclude.** "It's fair to ask if ..." does more than "clearly ...".
- **Prose, not bullets, for the argument.** Lists are for the roundup at the top; the explanation runs in paragraphs.

### Platformer (platformer.news)

Casey Newton's reporting on platforms and AI. Mostly paywalled; the headlines and decks are the lesson.

- **The headline states the news; the deck states the tension.** "AI is solving math problems faster than humans can understand the solutions" and under it "may trigger an identity crisis for mathematicians". Our News headline names the upstream change; our Maintenance headline names what it meant for the reader.
- **Short, concrete headlines**, six to ten words, a verb in the middle, no colon stacking.
- **A question only when the story answers it.** "Does intelligence need a hard cap?" is followed by an argument. A question headline over a story that does not answer it is a trick.

### Bytes (bytes.dev)

A JavaScript newsletter that is funny on purpose.

- **One news item is one or two sentences.** "Vue Router is working on experimental scroll restoration. Better late than never." The name of the project, what changed, and at most one clause of context. When Obmondo adds a one-line item (a chart update, a small fix), this is its length.
- **The news first, the verdict last.** "Artem Zakharchenko released MSW v3, which is now pure ESM" and then the aside. Ours ends with the callout instead of a joke.
- **The joke is dry and short.** Obmondo does not joke, but the lesson transfers: the aside after a fact is one clause, never a paragraph.

### DevOps Weekly (devopsweeklyarchive.com)

Gareth Rushgrove's weekly list of links, run for over a decade.

- **A blurb describes the resource, not its argument.** "An introduction to the DORA metrics for measuring SDLC performance, with a focus on the challenges of collecting the data." Fifteen to thirty-five words: what it is, what it covers, who it is for. The one adjective allowed is "useful".
- **The intro is the table of contents in a sentence.** "Platform engineering, establishing a center of production excellence, measuring the DORA metrics ..." Our "In this edition" line is that sentence.
- **No marketing language anywhere**, in ten years of issues.

### The Obmondo stories already published

Read every story in the current edition before writing. They are the house examples of the shape: definition, change, link; why it could not wait, what was built, callout. Match their paragraph count and their register. The 2022 editions in `wiki/newsletters/` show the earlier voice: lists of improvements with a reason attached to each, no hype, open source contributions named with their pull request.
