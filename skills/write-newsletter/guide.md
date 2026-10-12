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

## Part 2: how to write the story

### The reader

A CTO or an infrastructure lead at a customer, reading next to the invoice, or a subscriber who runs their own clusters and wants to know what changed upstream this month. Technical, busy, allergic to being sold to. They know what Kubernetes is; they may not know what Kyverno or Loki is. Every story is written for the second case and read by the first without annoyance.

### Opening a story

The first paragraph of the News part defines the project. Not its history, not its popularity: what it is and what it does in the cluster or on the server, in words a reader can repeat. Then one mechanism the story will turn on, in a sentence. The Loki story opens with "it does not index the text of every log line; it indexes a small set of labels", because the cost and the Grafana integration both follow from that. Find the one mechanism and put it first.

The change comes in the second paragraph, with its date and version, attributed: "Kyverno 1.19 was released on 20 August 2026". Deprecations and moves are stated as what they are, in the project's own words where possible. Then the link, alone on its line, as `[Read the <thing> →](url)`, naming what is behind it.

### Cause and effect

The Maintenance part opens with what would have happened to the reader's platform had nothing been done, in one or two sentences, stated as a fact about the software, not as a fear: "All of them would have stopped working at the next Kyverno upgrade." That sentence is why the invoice line exists; the reader must find it without searching.

The second paragraph says what was built, in nouns. Name the chart, the version, the component, the mode, the policy type. Say what each named thing does in a clause, so the paragraph teaches while it reports: "`GeneratingPolicy`: a new namespace triggers the creation of its secret, quota and limit range." Then that it was tested in an environment replicating production clusters, and that rollout happens in upcoming service windows. Those two sentences are the same in every story and belong at the end of the paragraph, not the start.

The callout is one or two sentences, the thing the reader must not miss. It is almost always "nothing to do on your side", with what stayed the same, or how to ask for the capability. It is never a summary of the story.

### Sentences

- Short paragraphs, three to five sentences. One idea per paragraph.
- Vary sentence length. A short sentence after a long one lands the point.
- Name the actor. "We rewrote every policy", "Grafana marked the chart deprecated". Passive voice hides who did what, and the whole point is who did what.
- Specifics over adjectives. A version number, a date, a count of policy types, a retention period. If a sentence has no specific and makes no claim, cut it.
- Technical terms are fine when the sentence says what they mean the first time. Code formatting for identifiers (`loki-stack`, `MutatingPolicy`), not for concepts.
- Hyphens, commas and colons for punctuation. No em-dashes, no `--`, no semicolon chains.
- No "we are excited", "robust", "seamless", "leverage", "cutting-edge", "best-in-class", "empower", "journey", "delve", "landscape", "game-changer", "ensure" as a verb of promise. No exclamation marks.
- No rule of three for its own sake: three adjectives, three examples, three clauses. Use the number of things there are.
- No rhetorical questions in a story. The deck of a Platformer piece can ask; an invoice explanation answers.
- No praise of the work. Describe it; the reader judges.

### Headlines

Written last. The News headline names the upstream change as a fact with a verb: "Kyverno 1.19 retires the old policy format", "Loki's old Helm chart is retired, and the chart itself has moved". The Maintenance headline names what Obmondo did and the deadline or reason in the same breath: "Every policy rewritten before the old format disappears", "Central logging in KubeAid rebuilt on the community chart". Six to twelve words, no colon, no question, no pun.

### What stays out

- Anything that identifies a customer: names, cluster names, "one of our customers in retail". Write about the capability.
- Counts of clusters, repositories, customers, hours, pull requests, review rounds.
- The debugging story. Dead ends, 429s, a stale PVC, a chart that pulled in a dependency, a reviewer's objection. The reader gets the result; the engineer keeps the war story for the blog.
- Internal names: kcm, kbm, kam, Artoo, opsmondo, the names of colleagues.
- The future tense about things not yet decided. "Will be rolled out in upcoming service windows" is a plan the user has confirmed; anything beyond it is a `[NEED: ...]`.

### The substitution test

Read each paragraph and ask whether it could be pasted into a different story about the same tool, or a story about a different tool, without changing a word. If it could, it says nothing about this feature. Replace it with the specific that makes it ours, or cut it.

### Length

A story is the length of the stories already in the edition: two headlines, four to six paragraphs, one callout, roughly 350 to 500 words. The five newsletters above run from one sentence per item to five thousand words per issue; none of that transfers. The reader is reading an invoice explanation, and it ends when the explanation does.
