# The story-teller's guide

This is the craft reference for the `story-teller` agent. Read all of it before writing a story, every run. It is distilled from the twelve books on storytelling, persuasion, and why ideas spread that are listed at the end, and bent toward one job: a true story from the world of tech, told twice, once in 280 characters and once as a LinkedIn post, with one image to carry both.

Two things about the examples in here. They were checked against their sources when this was written, but they are in the guide to show craft, so re-verify any fact before you reuse it. And their shapes are illustrations. A story that copies the outline of an example is a template with new nouns in it, and readers can feel that.

## Part 1: What a story is

Most posts that call themselves stories are opinions in costume. Shawn Callahan, in *Putting Stories to Work*, gives the plainest test for the real thing: a story describes what happened. It has a time and a place, people who do and say things, events that follow one another, and something the listener did not see coming. He calls a story a promise to tell people something they do not already know. If you cannot answer "when and where was this, and who was there?", you are holding a viewpoint.

Three statements about the same event:

- A fact: left-pad was an eleven-line npm package that thousands of projects depended on.
- An opinion: the JavaScript ecosystem leans too hard on tiny dependencies.
- A story: in March 2016 Azer Koçulu lost an argument with npm over the name of one of his packages, and in protest he unpublished all of his modules, more than 250 of them. One was eleven lines long. It padded strings with spaces. Within hours, builds were failing across the industry.

Only the third can be pictured, and only the third gets retold. Notice that it also delivers the fact and makes the opinion without stating it.

Lisa Cron's definition in *Wired for Story* says what the account has to contain: a story is how what happens affects someone who is trying to achieve what turns out to be a difficult goal, and how they change as a result. Take it one clause at a time.

- **Someone.** A person, or a team small enough to picture. A technology cannot be a protagonist and neither can a company. Git is a setting. The man who wrote it in a hurry because his version control had just been taken away is a protagonist.
- **Trying to achieve a goal.** They want something specific: ship before the launch window, find the bug, keep the project alive.
- **That turns out to be difficult.** Jonathan Gottschall, in *The Storytelling Animal*, boils every story down to a character, a predicament, and an attempt to get out of it. Trouble is the one ingredient no story does without. A tale where a smart team builds a good product and it succeeds is a press release.
- **How they change.** By the end someone believes something they did not believe at the start, or the world works differently. The plot is the events. The story is what the events did to the person.

Cron adds that a reader's brain asks three questions from the first sentence, and keeps reading only while they are being answered: whose story is this, what is happening, and what is at stake. An opening that answers none of them is asking the reader for patience they have not agreed to give.

Gottschall also explains why any of this works on engineers in particular. Stories are flight simulators. We are drawn to accounts of trouble because they let us rehearse problems we may face without paying for them. An outage story is a simulation of the reader's own next bad night, which is why they will read it to the end.

One warning comes with that. Gottschall shows that the mind is a compulsive storyteller. It is, he writes, "allergic to uncertainty, randomness, and coincidence", a factory that turns out true stories when it can and manufactures lies when it cannot. You will feel that pull when the record is incomplete. The neat motive, the perfect last line someone must have said, the cause that makes the ending click. If a source does not give it, it is your brain confabulating, and it stays out.

The books on this shelf are not immune. Sinek's best-known story has Samuel Langley giving up on powered flight the day the Wright brothers flew. The record says Langley's last attempt had crashed into the Potomac nine days earlier. The version in the book is the better story, which is exactly how it got there. A lesson will bend a fact to fit if you let it, so check the legend against the record every time, including the legends in this guide.

## Part 2: Choosing the story

Before writing anything, run the candidate through these. A story that fails the first two is the wrong story, and polish will not save it.

**Is there something unexpected?** The Heaths' second principle and Callahan's last story marker are the same thing. A story exists because a pattern broke: the absurd bug report was accurate, the eleven-line package was holding up the industry, the backdoor was caught by a man who noticed half a second. State the break in one sentence. If you cannot, there is no story yet. Jonah Berger's version of the test, from *Contagious*: is it remarkable, literally worth a remark? Would an engineer bring it up at lunch?

**Is there a person with something to lose?** Find whose story it is and what they stood to lose: money, data, a launch, a reputation, years of work. If the record names nobody, look for another story.

**Does the record hold a scene?** You need at least one moment that can be shown with real detail: what was typed, what was said, what the screen showed, what time it was. Without it you can only summarise, and a summary is a fact with a longer word count.

**What is the one sentence?** Four of the books make the same demand under different names. Chris Anderson calls it the throughline, the idea every part of a talk must connect to, and wants it in fifteen words or fewer. The Heaths call it the core, and borrow the army's Commander's Intent: the single thing that must survive when everything else goes wrong. Cron calls it the story's point, and Walsh the central truth. Write it down before you write the story. For the 500-mile email it might be: *the bug report that sounds insane may simply be precise.*

That sentence does not appear in the post. It is a ruler. Every detail that does not serve it gets cut, however good it is. Anderson is blunt that this is where most talks fail: the speaker tries to cover ground when they should go deep on one idea. His phrase for it is "overstuffed equals underexplained".

**Why does it matter?** Simon Sinek's argument in *Start With Why* is that people respond to the belief behind a thing before they care about the thing. A story chosen only because it is odd is trivia. A story that carries a belief the reader shares (that curiosity is a professional skill, that the boring maintenance work holds everything up, that the user is sometimes right) feels like it was told to them on purpose. Know the why. Let the story carry it without saying it. Gottschall gives the reason: we read argument with our shields up, and we lower them when we are absorbed in a story. A stated moral turns the post back into an argument and the shields come up again.

**Which plot is it?** The Heaths found that inspiring stories fall into three plots. Naming yours tells you where to spend the words.

- *Challenge*: someone outmatched gets through by persistence. Spend the words on the obstacle and the cost.
- *Connection*: people reach across a gap of status, team, company, or rivalry. Spend them on the gap and the gesture.
- *Creativity*: someone cracks a puzzle in a way nobody expected. Most debugging stories live here. Spend them on the puzzle, so that the answer lands as a click.

**What will the reader feel?** Berger's research on what gets shared found that it is driven by arousal more than by whether the emotion is pleasant. Awe, amusement, anxiety, and anger make people pass things on. Sadness and contentment make them close the tab. Name the feeling you are after. For tech stories awe (at ingenuity, at scale, at how thin the margin was) and amusement are the dependable ones.

**Is the idea load-bearing?** Berger's last principle is the Trojan horse: people share stories, and whatever is packed inside goes along for the ride, but only if the story cannot be told without it. The technical idea in your story should sit at the hinge of the plot. Nobody can retell the 500-mile email without explaining the timeout. That is the standard.

## Part 3: Building it

### The spine

Joseph Campbell laid out the pattern under the world's myths in *The Hero with a Thousand Faces*: a hero leaves the ordinary world, crosses into a place of trials, wins something, and comes home changed. He divided it into Departure, Initiation, and Return. A 200-word post cannot visit all seventeen of his stages and should not try. What survives compression is the three movements, and each maps onto a tech story without forcing.

1. **Departure.** The ordinary world, briefly, and then the call: the page at 3 a.m., the licence revoked, the ticket that makes no sense. Campbell's "refusal of the call" is worth keeping when the record has it, because it is so human. Harris's first response to the 500-mile report was that email does not work that way.
2. **Initiation.** The road of trials. What they tried, what failed, the point where it looked worst. This is the part writers skip and readers want. The struggle is the story.
3. **Return.** They come back with what Campbell calls the boon: the fix, the tool, the piece of knowledge. And something is different afterwards. Say what.

Treat this as a map of where stories tend to go. The Joseph Campbell Foundation itself says only the three phases are essential and the rest are variations, and that a tale containing every stage turns clumsy and bloated. Callahan goes further and tells business storytellers to throw the Hero's Journey away as far too complicated for the small stories people actually tell. Take his advice about the seventeen stages. The three movements are what is left.

Callahan offers a simpler frame for stories that explain why something exists, which he calls a clarity story: *in the past* things were one way, *then something happened*, *so now* we do this, and *in the future* it leads here. The origin of nearly any tool fits it.

### Cause, then effect

Cron's rule for what holds a story together: every event is caused by the one before it and causes the one after. Test your draft by reading the joins between sentences. If they are all "and then", you have a timeline. If they are "so" and "but" and "because", you have a story.

> A consultant patched the server. The patch swapped in an older Sendmail. The older Sendmail could not read the config, *so* the timeout became zero, *so* any connection that took longer than three milliseconds died.

The joining words do not need to appear on the page. The logic does.

### Start where the trouble starts

Open at the call. The ordinary world gets a clause, at most a sentence, placed after the reader is already curious. Cron's question for every piece of background is: what does the reader need to know right now to understand what is happening? Anything else waits, or goes. John Walsh's *The Art of Storytelling* builds a story in fourteen steps, and two of them are "plan your first words" and "know how the story ends". Those are the two places a story is won or lost. Settle both before you fill in the middle.

Callahan's advice on first words: begin with a time marker or a place marker ("In March 2016", "At 2:14 on a Tuesday morning", "In a lab at Harvard"), which signals to a listener that an account of something real is coming. And never announce the story. The phrase "let me tell you a story" puts the reader on guard and delays the thing it promises.

Anderson lists four ways to open that hold an audience: drama, a spark of curiosity, a compelling image, or a tease of what is coming. On a feed, the first two do nearly all the work.

### See it before you write it

Walsh titles one chapter "You Have to See It". The teller pictures each scene and then describes what is there, and the audience experiences the story where it would otherwise only hear about it. It works on the page too. Before drafting, pick the three or four pictures the story is made of. For the 500-mile email: a phone call with a statistician; a terminal with test messages going out; a config file full of zeros; a number on the screen. Then write what is in each picture.

Another of his steps is to tell the story from the view of someone at the scene. Choose where the camera stands. The same outage is a different story from the on-call engineer's chair, from the desk of the customer whose checkout stopped working, and from the seat of the person who merged the change. Pick one and stay there for as long as the record lets you. If the only recorded scene belongs to a different seat, move the camera once, at a paragraph break.

Scenes are built from things a camera or a microphone could pick up. Cron's chapter title says it: the story is in the specifics. "He tested it" is a summary. "Mail to Princeton, 400 miles away, went through" is a scene. One sensory detail per scene is enough in a post this short, and it must be one a trusted source records. If the record offers none, the scene is built from actions and numbers alone, which is still a scene. Cron's caution applies here: sensory details clog a story's arteries unless they tell the reader something they need. The detail has to do work.

Give at least one person a line in their own words, spoken or written. Callahan counts dialogue among the things that make a listener feel they are inside an event, and a verbatim quote is also the strongest proof that the event happened.

### The stakes, early

The reader should know by the second paragraph what could be lost. Put a number or a name on it. "A trading firm had a bad deploy" has no stakes. "It was losing roughly ten million dollars a minute" does.

### What to cut

Two more of Walsh's steps come as a pair: eliminate needless detail, then add description. The order matters. Clear out what the story does not need, and spend the space you won on making the remaining scenes visible. Cron's version is to ask "and so?" of every sentence. In practice, cut:

- Background the reader did not need in order to follow the turn.
- The second example of anything.
- Every name after the second or third. A post can hold one protagonist and one or two others.
- Explanations of things your reader already knows. See the curse of knowledge in Part 4, which cuts both ways.
- Identifiers the reader will never use: internal task names, ticket numbers, hostnames, the second version string. Keep one if it has flavour.
- All but one paragraph of mechanism. Even a niche post holds a single technical idea, explained once, in the plainest words that are still correct. When the explanation runs longer than the events, you have written a postmortem with a person in the first line.
- Your favourite fact, if it does not serve the one sentence.

### Endings

Anderson's list of how talks die is a list of how posts die: running out of time, apologising for what was left out, a vague platitude, a request for money. His better endings include two that work in a short piece. One is the camera pull-back, where the last lines show the wider meaning of what just happened. The other is narrative symmetry, where the ending returns to the image you opened with and it now means something else. The 500-mile post does the second: it opens with a bug report and closes on the same report, now accurate to within forty miles.

Stop on the strongest thing. Readers remember the last line longest.

## Part 4: Making it stick, making it travel

A story can be well built and still be forgotten by the next scroll. Two books are about exactly that problem. *Made to Stick* asks why some ideas are remembered. *Contagious* asks why some get passed on. Use them as two editing passes over a finished draft.

### The stick pass

The Heaths' six principles spell SUCCESs. Read the draft once for each.

| Principle | The question to ask of the draft |
| :-- | :-- |
| **Simple** | Is there one core, and is it compact? "Simple" means prioritised, the way a proverb is. If the draft has two points, one of them is a different post. |
| **Unexpected** | Where does the pattern break, and does the draft open a gap before it closes it? Surprise gets attention. Curiosity holds it. |
| **Concrete** | Could a reader draw it? The Heaths compare memory to Velcro: the more hooks an idea has, the better it holds, and sensory detail is hooks. Swap every abstraction for the thing itself. |
| **Credible** | Does the story prove itself from the inside? Vivid, checkable details do this better than any appeal to authority. So does one example strong enough to settle the matter alone, which the Heaths call the Sinatra test. |
| **Emotional** | Is it about one person? People feel for an individual and go numb at a crowd. One named engineer at 3 a.m. outweighs "millions of users affected". |
| **Stories** | Does it let the reader simulate being there, and want to act? This is the principle the other five serve. |

Two tools from the same book deserve their own notes.

**Human-scale numbers.** A statistic means nothing until the reader can feel its size. Translate it into a unit a person lives in. A trading firm that lost about $440 million in 45 minutes was losing close to ten million dollars a minute. A timeout of three milliseconds is 558 miles of light. Do the arithmetic yourself, check it, and give the reader the version they can hold.

**The curse of knowledge.** In the Heaths' best-known example, people asked to tap out a famous song on a table predicted that listeners would name it half the time. Listeners managed about one song in forty. The tapper hears the tune in their head and cannot imagine not hearing it. After researching a story you are the tapper: you know the postmortem, the acronyms, who everyone is. The reader has only the page.

For this audience the curse cuts both ways. The reader is an engineer, so explaining what DNS is insults them and reads like filler. But they were not in the room, so they do not know that "the Power Peg flag" was dead code, or who Jia Tan was. Assume the craft. Supply the incident.

### The travel pass

Berger's six principles spell STEPPS. Not every story needs all of them, and two or three done well is plenty.

- **Social currency.** People share what makes them look sharp. A story that gives the reader a piece of inside knowledge ("that's why the default is 1500") is a gift they can re-gift.
- **Triggers.** Berger's phrase is "top of mind, tip of tongue". Things get talked about when something in the environment keeps reminding people of them. A story hooked to something engineers touch daily, a command, an error message, a default port, gets recalled every time they touch it. Favour stories with a trigger built in, and make sure the trigger is named in the telling.
- **Emotion.** High arousal, as covered in Part 2.
- **Public.** Mostly a matter for the image, which is the part of the post visible at a glance.
- **Practical value.** News a reader can use. If the story leaves them with a check they will run on their own system tomorrow, they will send it to their team.
- **Stories.** The Trojan horse from Part 2. The idea rides inside the narrative, and the narrative cannot be told without it.

### Persuasion, used honestly

Robert Cialdini's *Influence* catalogues the shortcuts people use to decide: reciprocity, commitment and consistency, social proof, liking, authority, scarcity, and in later editions unity. He wrote it largely so that readers could defend themselves, and the feed is full of the tactics he warns about: invented urgency, borrowed authority, "everyone is talking about this". A true story has no need of them. It can earn the same principles legitimately.

- *Reciprocity*: give the reader something complete and ask for nothing. That is the whole reason the post ends without a request.
- *Authority*: comes from precision. A date, a version number, and a verbatim quote make a writer credible in a way that claiming expertise never does.
- *Liking and unity*: we listen to people who are like us. Write as one engineer to another, in the vocabulary of the trade, with no explaining down.
- *Scarcity*: a story few people know is worth more than one everybody has heard. That is a reason to dig for the uncommon story, and never a reason to dress up a common one as a secret.
- *Social proof and commitment*: leave these alone. In a post they only show up as bait.

Cialdini also reports Ellen Langer's photocopier experiment: people let a stranger cut in line far more often when the request came with a reason, even an empty one, because the word "because" itself triggers agreement. Stories run on the honest form of that reflex. A reader who is given the cause of each event keeps nodding. This is Cron's cause and effect again, arrived at from the other side.

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
