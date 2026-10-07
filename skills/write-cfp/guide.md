# The CFP writer's guide

A talk proposal is not an article and not a sales page. It is a bet placed with a stranger who has ninety seconds and a stack of two hundred others. This guide is what the proposals in `samples/` taught, what the user's own edits taught, and what programme committees say they look for. Read all of it before writing.

## Part 1: How a reviewer reads

Reviewers at community conferences are volunteers. They review in batches, late, and they are tired. They read the title, then the first two sentences of the description, and they have usually decided by then. The rest of the text either confirms the decision or, rarely, reverses it.

They are asking three questions, in this order:

1. **Is this a real talk?** A real talk has one thing the room will leave with, and the proposal can say what it is. A proposal that promises to "explore", "dive into", or "discuss" a topic is describing a reading list, not a talk.
2. **Does this person know?** Reviewers look for signs of first-hand experience: a number, an incident, a decision that went wrong, a detail only someone who did the work would know. One such detail is worth three paragraphs of context.
3. **Why this, here?** The talk has to fit the conference and the track, and it has to offer something attendees cannot get from the documentation or a blog post. Conference programmes are built to balance topics, so a proposal that lands in an empty slot beats a better one that lands in a crowded one. That is why Step 2 of the agent researches what the conference accepted last time.

Two things end a proposal early. The first is a vendor pitch: a product name in the title, a description that is a feature list, "benefits" that are benefits to the company. Open source projects are welcome when the talk is about the problem and the project is one of the tools. The second is a proposal that could have been written without doing the work: generic, correct, and empty.

## Part 2: What the samples taught

Read `samples/` before this section makes sense. Each file carries its outcome.

**The accepted one**, the Cilium anti-patterns lightning talk, was accepted at four events. What it does:

- The first sentence states the problem in the words an engineer would use at a desk: "looks straightforward - until traffic starts getting blocked for reasons that aren't obvious, policies silently match nothing, or things work in staging but fail in production." Three real symptoms, no abstraction.
- The second sentence establishes the speaker's standing with a fact, not a claim: "writing and designing Network Policies used by multiple teams across multiple Kubernetes clusters, and debugging policy failures in real production environments."
- It promises a shape the reviewer can picture: real examples that look correct but are wrong, each paired with the corrected approach.
- The benefits section has numbers: three months, 100+ users. It names the exact failure that costs people hours: "a policy that reads correctly, applies without error, and silently drops traffic." And it says what the talk hands over that documentation does not: "the parts of the enforcement model that actually explain the failures", named precisely.
- The title names the tool, the form (anti-patterns), and the price paid ("I Learned the Hard Way"). It is a story in nine words.
- It is first person throughout, and it is honest that most of the knowledge came from things going wrong.

**The not-yet-accepted one**, the audit logging talk, has the same bones and has not been picked up. The user's own view of why lives in `outcomes.md`; treat the following as hypotheses to test against the target conference, not rules:

- The opener is a scene, which is good, but the talk then promises four things (enable, write policies, ship logs, alert with Falco) for a single slot. Reviewers may read that as a tutorial rather than a talk with a point.
- The title carries an arrow diagram, which some forms strip and some reviewers find gimmicky.
- The credibility line ("a team of 20 SREs") is a team size, not an incident. The Cilium talk's "three months" and "100+ users" are outcomes.
- The talk covers upstream features that are well documented, so the "what you cannot get from a blog post" question is harder to answer. The benefits section does answer it, in the second paragraph, but the reviewer may not reach it.

**The two CRA drafts** are the user's current preferred shape for a compliance talk, revised several times by hand. Their structure is the template for any regulation or compliance proposal:

1. Open on the change itself, in plain words, with the dates in the sentence that first names the law. Stakes in the first paragraph: what happens to a product or a company that does not comply.
2. Name who this affects, as a list of roles.
3. "In this session we will explain ... We will cover ... We will also talk about ..." for the content, followed by one credibility sentence: "We maintain open source projects ourselves and at work, we help companies comply with standards such as ISO 27001, the CRA, GDPR and NIS2."
4. Close with the formula: "This session will be a complete map of ... Attendees will leave with ..."
5. Benefits open on the turning point ("Open source is at a turning point. For years its security has been a matter of best practice."), then "Most of the engineers who actually maintain this code have not heard that this is happening", then "We believe ... needs to know", then "Our aim with this talk is to give the community ...", and end with where the knowledge comes from: "Everything in it comes from applying the regulation to open source projects we maintain ourselves."

## Part 3: What the user's edits taught

The user rewrote the CRA drafts by hand several times. The pattern in what they cut and kept is the house style:

- **Name the areas, save the list for the talk.** A sentence enumerating every sub-item ("a software bill of materials for every release, a working vulnerability handling process, secure defaults, a supported update path, a declared support period, and the documentation that proves all of it") was cut to "what a release process must produce before the deadline." The proposal says what the talk covers, the talk shows the detail.
- **Cut the illustrative aside.** "For many of them the first sign of the deadline will be a customer asking for an SBOM" was cut. Clever asides read as written for effect.
- **Cut self-praise.** "It is honest about what the law does not require, so teams do not over-build" was cut. The proposal describes the talk; it does not review it.
- **Cut digs at others.** "most of what circulates is either alarmist or wrong on the details" was replaced with "Most of the engineers who actually maintain this code have not heard that this is happening." State the gap, not the competitors.
- **Cut sales negatives.** "without buying a compliance product" was cut.
- **Speak as the speaker.** "This talk gives the community ..." became "Our aim with this talk is to give the community ...". "It covers" became "We will cover". The speaker is a person who will stand on the stage, and the proposal sounds like them.
- **Attendees, never "you".** A proposal is read by a reviewer, not the audience.
- **Hyphens, not em dashes.** The user writes "straightforward - until". An em dash is the single clearest sign that a machine wrote the text.
- **Dates and numbers stay.** Every date, deadline and figure was kept. They are the specifics.

## Part 4: Title

The title is written last and read first. Patterns from the accepted sample and from conference programmes:

- Name the thing: the tool, the law, the failure. "Cilium Network Policy Anti-Patterns" tells a reviewer what track, what level, and what the room will see.
- A hook, then a plain second half. "Open Source Is Not Exempt: What the CRA Really Asks of Open Source Projects and Vendors." "The Clock Is Already Running: Will the CRA Block Your Product from Shipping to the EU?" The first half earns the click, the second half says what the talk is.
- The price paid is a credential: "I Learned the Hard Way", "What Broke", "The Parts Nobody Writes Down".
- Questions work when the talk answers them. A question the talk cannot answer is a trick.
- Check the conference's length limit and its last programme. If no accepted title had a colon, do not be the first.
- Avoid: "A Journey", "Unlocking", "Demystifying", "Deep Dive" with nothing after it, "101" unless the track is for beginners, the product name as the first word, and anything a reviewer could not tell apart from last year's rejected pile.

## Part 5: Description

The description is the talk, compressed. Its job is to let the reviewer see the session.

- **Open on the problem or the change**, in the words a practitioner would use. The accepted sample opens on three symptoms. The CRA drafts open on the law and its dates. Both put the stakes in the first two sentences.
- **Establish standing with a fact.** Where the speaker has done this, say so with the specific: clusters, teams, months, users, incidents. One fact beats any adjective.
- **Say what the session covers, as the speaker.** "In this session we will ..." or "In this talk I'll ...". Name the areas. The detail belongs in the talk.
- **Promise a shape the reviewer can picture.** Real examples paired with corrections. A walkthrough on a real setup. A test the audience can apply in minutes.
- **Close on what attendees leave with.** One sentence, concrete. The CRA formula works for compliance talks: "This session will be a complete map of ... Attendees will leave with ..." An engineering talk can be plainer: "Attendees leave able to write an audit policy that fits their environment and to know within minutes, not days, when something happens that shouldn't have."
- **Length**: fit the form. If the form allows 1,000 characters, the description is 900 to 1,000. A short description in a long field reads as a thin talk; an over-limit one cannot be submitted.

## Part 6: Benefits to the ecosystem

This field is where most proposals go generic, because the writer has run out of things to say. Reviewers read it to answer the third question: why this talk, here, now.

- **Open on why now.** Adoption outrunning knowledge ("Cilium adoption is growing faster than the operational knowledge around it"). A turning point ("Open source is at a turning point"). A gap between what the docs say and what teams decide under time pressure.
- **Name the gap precisely.** Not "there is a lack of awareness" but "a policy that reads correctly, applies without error, and silently drops traffic. There is no obvious place to start debugging that, so people lose hours to it."
- **Say what the talk hands over, and what it cost to learn.** "In this talk I want to hand over what took me three months to work out." Then name the pieces.
- **For a community or cause talk**, state the belief: "We believe the whole open source world ... needs to know what the CRA is and what it requires of them."
- **End on the source of the knowledge.** "Everything shown is upstream Kubernetes, Falco, and standard log aggregation." "Everything in it comes from applying the regulation to open source projects we maintain ourselves." This is the sentence that tells a reviewer the talk is not a pitch.

## Part 7: The voice

The proposal reads as written by an experienced speaker in the talk's own field. Calibrate to the field:

- **Engineering talk**: a working engineer. Short sentences, concrete nouns, the failure named before the fix, opinions stated flat ("That reflex was wrong"). Assumes the room knows what a pod and a rollback are.
- **Compliance or regulation talk**: a practitioner who has read the text and done the mapping. Dates and article numbers used naturally, never as decoration. Plain words for legal concepts ("a condition of selling in the EU at all"). Calm about consequences; the facts carry the fear.
- **Open source or community talk**: a maintainer. Speaks about the project's users and contributors as people they owe something to. Honest about what the project does not do.
- **Platform or product talk**: an operator who runs it. Numbers about scale and time. The product is one of the tools, never the subject.

Read the user's samples for their own cadence and match it: how long their sentences run, how often they state an opinion, how they refer to their own work.

## Part 8: What gives a machine away

Reviewers now see hundreds of generated proposals and reject them on sight. Each of these is a tell:

- Em dashes, or `--` used as a dash. Use a comma, a colon, or a hyphen with spaces as the user does.
- "Additionally", "Furthermore", "Moreover", "It's important to note", "In today's fast-paced", "at the end of the day".
- "leverage", "utilize", "robust", "seamless", "delve", "landscape", "realm", "journey", "unlock", "empower", "game-changer", "cutting-edge", "best-in-class".
- Three of everything: three adjectives, three bullets, three benefits. Real proposals are lopsided.
- "In this talk, we'll explore/dive into/unpack ..." with no object the reviewer can picture.
- A paragraph that would fit any other talk on the topic. Apply the substitution test to every paragraph: if a different speaker on the same topic could have written it, it is not pulling weight.
- Praise for the talk ("insightful", "comprehensive", "actionable insights", "practical takeaways") in place of a description of it.
- Perfect symmetry: every paragraph the same length, every sentence the same shape.
- A closing line that summarises the proposal.
- Invented specifics. A number the user did not supply is a `[NEED: ...]`, never a guess.

## Part 9: Fitting the form

Every conference's form is different, and the differences are enforced:

- Fields and their names. Write to the fields the form has, under the names it uses. KubeCon-style forms want a description and "benefits to the ecosystem"; others want "value to the community", "takeaways", "outline", or a bio.
- Character limits. Count. Over-limit text is silently truncated or rejected by the form.
- Tracks and formats. Pick from the conference's own list. A lightning talk proposal promises less and is held to less; a 30-minute session proposal that promises four tutorials will lose to one that promises one point made well.
- Audience level. Say who the talk is for in the proposal itself, not only in the dropdown.
- What the organisers say they want. The CFP page usually says. Read it and match the words they use for what they are looking for.
