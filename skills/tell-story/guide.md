# The story-teller's guide

This is the craft reference for the `story-teller` agent. Read all of it before writing a story, every run. It is distilled from thirteen books on storytelling, persuasion, and why ideas spread (listed at the end), and bent toward one job: a true story from the world of tech, told twice, once in 280 characters and once as a LinkedIn post, with one image to carry both.

Two things about the examples in here. They are true as far as I could verify, but they are in the guide to show craft, so re-verify any fact before you reuse it. And their shapes are illustrations. A story that copies the outline of an example is a template with new nouns in it, and readers can feel that.

## Part 6: The X post

One post. 280 characters, which is about 45 words. `check_story.py` does the counting, because you cannot.

The X post is a different cut of the story, written on its own terms. Compressing the LinkedIn post into a summary gives you an abstract, and an abstract is the opposite of a story. Ask the Heaths' question from *Made to Stick* instead: if the reader remembers one thing, what is it? Find that core, then make it compact. In a story the core is nearly always the moment the expected thing failed to happen.

So the X post is that moment, with the least setup that lets it land:

- One sentence of normal world, so the reader has an expectation to break.
- The break, stated as plain fact.
- The last sentence holds the strongest fact or image in the post. The reader supplies the meaning.

Keep the proper nouns and the numbers. They are what make a reader believe you, and they are what a compressing writer cuts first. Cut the adjectives, then the scene-setting, then the second-best fact. Use full sentences. The post must make complete sense to someone who will never see the LinkedIn version.

Leave out hashtags, links, emoji, and thread markers. The post is the whole thing.

Weak, and typical:

> The xz backdoor is a reminder that open source security matters. One engineer's curiosity saved the internet. Here's what we can learn.

It is a claim about a story, with the story removed. Nothing in it could be pictured. Compare:

> In 2024 a Postgres developer noticed his SSH logins were taking half a second longer than they should. He went looking for the reason. He found a backdoor that someone had spent two years patiently planting in a library that ships with nearly every Linux system.

A normal world (logins should be fast), a break (half a second), and an ending that hands the reader the scale of it without commenting on it.

A second shape, where the numbers do the work:

> A statistics department reported that its mail server could not send email farther than 500 miles. The sysadmin tested it anyway. Princeton, 400 miles: delivered. Memphis, 600 miles: failed. A bad config had set a timeout so short that light ran out of time.

Other shapes that fit in 280: a real line someone said, with just enough context to make it sting; a single object and what it cost; a date, a decision, and the thing nobody knew yet. Rotate. If the last three stories in `stories/` all open the same way, open this one differently.

## Part 7: The LinkedIn post

LinkedIn renders plain text. No Markdown, so no asterisks, no headers, no bullets. The ceiling is 3,000 characters and a story rarely needs half of it: aim for 150 to 300 words. If the story is done at 160 words, it is done.

### The first line

On a phone the feed shows roughly the first 140 characters and then a "see more" link. That first line is the only part most people will read, so it has to be the story already in motion: a person, a specific trouble, and a gap the reader wants closed. George Loewenstein's gap theory, which the Heaths lean on, says curiosity is the itch of knowing there is something you do not know. Open the gap with a fact, and let the fact be strange enough that the reader needs the explanation.

> The chairman of the statistics department called to say the mail server could not send email farther than 500 miles.

That line is the first beat of the story, and it is also the hook. Those should be the same sentence. A line that advertises the post ("I came across a fascinating story this week") spends the fold on nothing. Chris Anderson gives speakers about a minute to earn attention before the audience drifts; a feed gives you one line.

### The body

Write paragraphs. Two to four sentences each, a blank line between them, lengths uneven. A one-sentence paragraph is a spotlight and works at most twice in a post. The feed is full of posts where every sentence stands alone on its own line with air around it, and that cadence now reads as either a growth hacker or a machine.

The beats, in whatever proportion the story needs: the person and their normal world, the trouble, what they tried, the turn, what it cost or changed. Part 3 covers how to build these. On LinkedIn each beat gets room for one or two concrete details the X post had to drop: the exact command, what the room was like, the line someone said.

### The close

End on the last fact or image of the story, chosen because the meaning is already inside it. If you add a line of meaning after that, it gets one or two sentences, it says something a working engineer would nod at, and it is tied to this story so tightly that it could not be pasted under another one.

The post stops there. The reader's comment is theirs to offer. A closing question asking for it, or a call to follow, turns a story into a pitch after the fact and the reader feels the switch.

Hashtags: none, unless the user asked, and then three at most on the final line. Links: none in the body. Sources live in the story file's `Sources` section, and the user can drop one in the first comment.

### A whole post

> The chairman of the statistics department called to say the mail server could not send email farther than 500 miles.
>
> Trey Harris ran the campus email system at a university in North Carolina, and he knew that was not how email worked. He said so. The chairman had come prepared. The department had waited a few days before calling, he explained, until they had collected enough data to be sure. "A little bit more, actually. Call it 520 miles. But no farther."
>
> So Harris tested it. Mail to Princeton, 400 miles away, went through. New York, 420 miles: delivered. Providence, 580 miles: failed. Memphis, 600 miles: failed.
>
> A consultant had patched the server a few days earlier, and the patch had quietly swapped in an older Sendmail that could not read the newer config file. Settings it did not understand became zero, including the timeout for connecting to a remote server. In practice zero meant about three milliseconds. On a fast campus network, the only delay left to measure was the speed of light.
>
> Harris opened a terminal and asked the units program to convert three millilightseconds into miles. It answered 558.84719.
>
> The bug report that sounded like a joke had been accurate to within forty miles.

What to notice: the hook is the first beat. The person has a name and a job by the second paragraph. The chairman speaks in his own words, once. The test results are real place names and distances, and their rhythm (delivered, delivered, failed, failed) is the turn. The explanation takes one paragraph and assumes the reader knows what Sendmail and a timeout are. The ending is a number, and the final line states the meaning as a fact about this bug report. The general lesson (take the absurd report seriously) is never written down, and the reader arrives at it anyway.

Sentence lengths in that post run from three words to thirty. No paragraph has the same shape as the one before it.

## Part 8: The image prompt

One image goes out with both posts. Its job is to stop a thumb, and then to add something the text did not say. The prompt is read by an image model that knows nothing about the story, so it has to be complete on its own.

### Pick the idea first

There are three routes, and the story usually favours one.

**The moment.** The scene at the turn of the story, as a photograph nobody took. A man at a beige terminal at night, looking at a paper map with a circle drawn on it.

**The object.** The one concrete thing the story hangs on, shot as a still life. A moth taped into a logbook. An eleven-line file printed on a single sheet of paper, sitting alone on an enormous empty desk.

**The metaphor.** A picture of the mechanism. A cathedral with one small brick at the base painted a different colour. A lighthouse whose beam stops short of the ship.

Whichever route, apply the Heaths' test for a sticky idea: is it concrete, and is it unexpected? A good image idea can be described in one sentence that makes someone say "oh, that's good." The stock pictures of tech fail both tests: the hooded figure at a keyboard, green code raining down a screen, a glowing brain, a robot hand reaching for a human one, blue circuit-board backgrounds. An image the reader has seen a hundred times is invisible.

### Then write the prompt

One paragraph of plain description, 60 to 120 words, covering:

- **Subject and action.** Who or what, doing what, with the two or three details that make it this story: period hardware, clothing, the thing on the desk.
- **Setting.** Place and era. "A university server room in the mid 1990s" gets you beige plastic and CRT glow for free.
- **Composition.** Framing and angle, what is in focus, where the eye lands first. Ask for a square 1:1 frame with the subject near the centre and some margin, so the crops on both platforms survive.
- **Light and colour.** Time of day, source, palette. Two or three colours named is plenty.
- **Medium.** 35mm film photograph, editorial ink illustration, linocut print, gouache, risograph, oil painting, technical blueprint, claymation still. Choose for the mood of the story and change it between stories. A feed where every image is the same glossy digital render looks generated.
- **Exclusions.** End with "no text, no lettering, no logos, no watermark." Image models garble words, and a picture with misspelled signage is the visual version of an em-dash.

### Real people

When the story is about a real person, describe the figure and leave the name out of the prompt: approximate age, build, hair, clothing of the period, posture. Many image models refuse named likenesses or get them wrong, and a photorealistic fake portrait of a real person is not something to post beside a true story. Better options: show them from behind or in silhouette, show only their hands and their tools, or pick an illustrated medium that nobody could mistake for a photograph.

### Example

> A paper road map of the eastern United States pinned to a corkboard in a cramped university server room in the mid 1990s, a wobbly red circle drawn by hand around North Carolina. In the foreground, slightly out of focus, a beige terminal glows green and a man's hand rests on the keyboard, a mug of cold coffee beside it. Seen from over his shoulder. Warm tungsten light from a desk lamp, deep shadows, muted palette of beige, green and red. 35mm film photograph, shallow depth of field, visible grain. Square 1:1 composition with the map at the centre. No text, no lettering, no logos, no watermark.
