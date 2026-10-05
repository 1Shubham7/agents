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

## Part 5: The prose

Everything so far decides what goes in the story. This part is about the sentences, which is where a reader decides in a few seconds whether a person wrote this.

### Three models from the shelf

**Ryan Holiday** is the closest model for a short true story. A chapter of *Ego Is the Enemy* typically drops you into a historical life already under way, a general or an athlete or an inventor at a moment of decision, and tells it in short declarative sentences with plain words and no hedging. The point comes after the story, never before it. Take from him: start inside the event, prefer the short sentence, use the plain word, and let the long sentence be the exception that carries a chain of events. Leave one of his habits on the shelf. His chapters end by turning to "you" with a run of instructions, which suits a book the reader chose to pick up. In a feed it is a sermon.

Take his subject too. The book's argument is that ego, the need to be seen as important, ruins the work. On the page, a writer's ego shows up as cleverness on display, hype, and the urge to tell the reader what to think. The story belongs to its subject. The narrator who performs insight ("and that's when it hit me") is making it about themselves. One chapter, "Talk, Talk, Talk", warns against talking about the work in place of doing it, and the writing equivalent is announcing that something is fascinating when you could be showing the fascinating thing.

Anderson makes the same point from the stage. He names four kinds of talk nobody wants: the sales pitch, the ramble, the org bore (an organisation's inner workings are dull to everyone outside it), and the inspiration performance. "Inspiration can't be performed," he writes. It is a response the audience has to a real story, and a speaker who reaches for it directly gets the opposite. LinkedIn is where all four live. A true story told straight is the alternative to each of them.

**Sejal Badani's** *The Storyteller's Secret* is a novel, and what it teaches is texture and withholding. The book plants its questions early (why did the narrator's mother leave India and never go back?) and makes the reader wait for the answers, telling a past story inside a present-day frame: a granddaughter in the present, listening as her grandmother's old servant recounts the grandmother's life in instalments. Three things carry over. First, the frame. A story from 1975 can open in the present ("Every time you type `grep`, you are using a name that began as an editor command") and then step back, which gives the reader a reason to care before the history starts. Second, withhold the answer and never the question. The reader of the novel knows from the start what the mystery is. Cron warns that hiding information to set up a big reveal usually robs a story of its hooks, because a reader who does not know what is at stake has nothing to wonder about. Tell them early what is strange. Make them wait for why.

Third, the senses. Readers praise the book's food, fabric, and festival colour, and its sharper critics complain that the dishes go unnamed. That complaint is the lesson: a sensory detail works when it is the specific thing. A server room has its own versions: the fan noise, the cold aisle, the amber cursor, the pager on the nightstand. One such detail, if the record supports it, moves a paragraph from report to scene.

**Simon Sinek** writes the way he speaks: common words, one idea, said plainly enough to be repeated by someone who heard it once. His test is worth stealing. Could a reader pass your story on from memory? If it takes notes to retell, it is too complicated.

### What a human voice is made of

Callahan warns about "the storytelling voice": telling that has been crafted and performed until it lands in an uncanny valley, close to natural and therefore off. The stories that work at work, he says, are small ones told the way you would tell a colleague. Cron puts the priority bluntly. Storytelling beats beautiful writing every time, and a beautifully written piece with no story earns a "who cares?". Write the way a good engineer talks when they are telling you about the worst bug they ever chased.

- **Nouns and verbs with addresses.** "Sendmail 5" and "Sun's patch", where a vaguer writer would put "an older version" and "an update". The specific word is nearly always shorter than the general one plus its adjectives.
- **Uneven sentences.** Length follows thought. A long sentence carries a chain of events, and the short one after it lands. If you read a paragraph aloud and it has a beat you could clap to, break it.
- **A temperature.** The narrator has an attitude toward the events: dry, amused, quietly impressed. Engineers write and read understatement fluently. "This was a problem" does more than three exclamation marks.
- **Trust.** The reader is told what happened and left to do the last step themselves. A writer who explains the joke, or the moral, does not believe in the story.
- **Real units.** Dates, durations, dollars, version numbers, line counts.
- **Small liberties.** A sentence that starts with "So" or "And". A fragment, once. A paragraph much shorter than its neighbours. Polish applied evenly to every sentence is itself a tell.

### What gives a machine away

The checker carries the word list. These are the habits behind the words, each with what to write in its place.

| The habit | What it looks like | Write this |
| :-- | :-- | :-- |
| The reversal | "It wasn't a bug. It was a warning." | Say what it was. Drop the thing it wasn't. |
| The self-answered question | "The cause? One missing server." | The statement, with no question in front of it. |
| The announcer | "Here's the thing." "Let that sink in." | Nothing. Go straight to the fact. |
| Triplets | "fast, simple, and reliable" | The one that matters to this story. |
| Stacked one-liners | Eight paragraphs, eight sentences | Paragraphs of uneven length. |
| The bolted-on moral | "The lesson? Always test your backups." | End on the fact that implies it. |
| Hype | "legendary", "mind-blowing", "changed everything" | The number or the consequence. |
| The generic actor | "One day, a developer noticed..." | The name, the date, the place. |
| Abstractions that act | "Curiosity saved the internet." | A person doing a specific thing. |
| The exit question | "What would you have done?" | Stop writing. |
| The dash aside | An em-dash carrying an afterthought | A comma, a colon, or a new sentence. Never an em-dash. |

One test catches most of what the table misses. Take any sentence and ask whether it could be moved, unchanged, into a post about a different story. "Sometimes the smallest details matter most" fits under any story ever told, so it is filler here. "Three millilightseconds came out as 558 miles" fits under exactly one.

## Part 6: The primer

The first section of the story file is for one reader, the user, and it never gets posted. It explains the story and teaches whatever is needed to understand it. The user is going to put their name on these posts. When someone replies "wait, why would a zero timeout take three milliseconds?", they have to be able to answer.

It is also for you. Write it before the posts. A post is a compression, and you cannot compress what you do not understand. If you cannot show the mechanism with an example that fits on one screen, you are not ready to put it in 280 characters, and the primer is where you find that out.

### Who you are teaching

The curse of knowledge rule from Part 4 flips here. In the posts, assume the craft and supply the incident. In the primer, assume a capable programmer who has never touched this particular language, tool, protocol, or era. They know what a loop, a pointer, a process, and a socket are. They may never have written Go, configured Sendmail, or heard of a certificate authority. Every term that belongs to the story's own corner of tech gets a sentence of definition the first time it appears.

### The four parts

Use `###` subsections, in this order.

**The story in plain words.** One to three paragraphs. What happened, to whom, when, and why anyone cares, told in order, with no hook, nothing withheld, and nothing left for the reader to infer. It is the answer you would give a colleague who asked "what's that one about?".

**The concepts.** One subsection for each concept the story stands on, titled with the concept's name. To find them, go through the story's turn and mark everything a reader must already understand for it to land. There are usually one to three. Put them in an order where each rests on the one before. Teach only as much of each as the story uses: a story about Go's loop variable needs the loop variable, and the rest of Go can wait.

**How it plays out.** Walk through the hinge of the story again, this time with the concepts in hand. Use the actual line of code, config, or command from the incident when a source has it, quoted and linked, with the line that matters pointed out. This is where the reader should think "so that's why".

**What the posts leave out.** The caveats, the simplifications, the details the sources dispute, and the objection a sharp reader is most likely to raise, with its answer. A post has no room for these. The user needs them before a commenter supplies them.

A story with no technical concept in it (a licensing fight, an argument over a name, an obituary) keeps the first and last parts. Its middle teaches context where another story would teach code: who these people were, what the field looked like at the time, what was at stake.

### How to teach one concept

Anderson's chapter on explanation gives the order, and it is the right one for a primer: start where the listener is, light a spark of curiosity, bring in concepts one at a time, use a metaphor, use examples. In practice:

1. **Say what it is in one sentence**, in words the reader already owns.
2. **Say what problem it exists to solve.** A thing with no purpose attached is a definition, and definitions do not stick.
3. **Show the smallest example that exhibits it.** Code, a command with its output, a config stanza, a worked number. The Heaths' point about concreteness matters more in teaching than anywhere else: an abstraction means something different to every reader, and an example means the same thing to all of them.
4. **Break it.** Show the failure the story turns on by changing the example as little as possible, and show what comes out. A before and after pair, a few lines each, teaches more than a page of description.
5. **Offer one comparison to something familiar, and say where it stops being true.** An analogy pushed past its limit teaches something false.

A small diagram in a `text` fence earns its place when the concept has a shape: two names pointing at one address in memory, a timeline of which task held which lock, the hops a packet takes.

### Code in the primer

- **Small and whole.** A complete file of ten to twenty-five lines that the user can paste and run beats a fragment with `...` in it. Give every fence its language.
- **Run it.** When the toolchain is on the machine, run every snippet and paste the real output beneath it in a `text` fence. The truth rule covers code: an example that does not do what the primer says it does is a fabrication. Anything you could not run gets a line under `Notes` saying so.
- **Name the version when the behaviour depends on it.** Many stories are about behaviour that was later changed, so the same code prints different things before and after. Say which version produced each output.
- **Point at the line.** One short comment on the line that matters. The rest stays uncommented.
- **Code from the incident is quoted as it was.** If you trim it, say that you trimmed it, and link the source.

### Voice and length

Plain second person, the way you would explain it at a whiteboard. Everything in Part 5 about human prose holds here, including the rule against dashes as punctuation. Leave out the encouragement and the recap.

The primer runs as long as the teaching needs, usually 400 to 900 words of prose plus code. Past that, check whether you have started teaching the subject and stopped teaching the story.

### A whole primer

This is the primer for the 500-mile email, the story whose posts appear in Parts 7 and 8. The Python was run, and the outputs are what it printed.

````markdown
## Primer

### The story in plain words

Some time between 1994 and 1997, Trey Harris was running the campus email system at the University of North Carolina at Chapel Hill. The chairman of the statistics department reported that their mail server could not deliver to anywhere more than about 500 miles away. Harris tested it and found it was true.

The cause was a server upgrade that had swapped the mail software, Sendmail, for an older version while leaving the newer version's config file in place. The old software did not understand some of the settings and treated them as zero. One of those was how long to wait when connecting to another mail server. With a wait that short, only nearby servers could answer in time. Harris wrote the story up in 2002 for a sysadmin mailing list, and it has been passed around ever since.

### Connect timeouts

Before a mail server can hand a message to another server, it opens a TCP connection to it. Opening a connection means sending a packet and waiting for the reply. A connect timeout is how long the sender will wait for that reply before giving up. It exists so that one dead server cannot stall the whole mail queue.

Here is a connect with a timeout of three thousandths of a second, to an address that never answers:

```python
import socket
import time

start = time.perf_counter()
try:
    # 192.0.2.1 is reserved for documentation and never answers
    socket.create_connection(("192.0.2.1", 25), timeout=0.003)
except OSError as err:
    waited = (time.perf_counter() - start) * 1000
    print(f"{type(err).__name__} after {waited:.1f} ms")
```

```text
TimeoutError after 5.7 ms
```

Two things to notice. The program gave up far sooner than a person could perceive. And it asked for 3 ms but waited 5.7, because a timeout is a request to the operating system's timer, which fires when it gets around to it. That second point is why "zero" in the story did not mean "fail instantly". On Harris's machine a timeout of zero came out as slightly over three milliseconds.

### Distance as time

Nothing travels faster than light, so every mile between two machines adds a delay that no hardware can remove. Light covers about 186 miles in a millisecond.

```python
c = 299_792_458              # metres per second
print(c * 0.003 / 1609.344)  # distance covered in 3 ms, in miles
```

```text
558.8471911536626
```

Normally this delay is buried under bigger ones, such as routers queueing packets and servers being busy. Harris's campus network was unusually fast, so for a nearby and lightly loaded server, distance was most of the wait.

### How it plays out

Put the two together. Every outgoing message got about three milliseconds to reach the remote server and hear back. A server close by answered inside that window, and the mail went through. A server far enough away could not answer in time however fast it was, so the connect was abandoned and the mail failed. The line between the two was a distance, which is why a statistician could draw it on a map.

Harris's own description of the cause: "a zero timeout would abort a connect call in slightly over three milliseconds".

### What the posts leave out

The arithmetic is tidier than the physics, and Harris says so in the FAQ he wrote afterwards. The reply has to travel back, so three milliseconds has to cover a round trip. Asked whether the figure should be six milliseconds, he answers: "Of course. This is one of the details I skipped in the story." Signals in copper and fibre also move well below the speed of light in a vacuum. On why he told it so vividly: "I took license. It made a better story that way."

He no longer has his notes, and can date the events only to somewhere between 1994 and 1997. What he stands by is the behaviour: nearby mail was delivered, distant mail was not, and a zeroed timeout was the cause. If a commenter says the numbers do not quite add up, they are right, and the author agrees with them.
````

What to notice: the plain account has no hook and holds nothing back. Each concept gets one sentence of definition, one reason to exist, and one example small enough to run. The example's surprising output (5.7 where 3 was asked for) is used to explain the story's own oddity. The last part hands the user the weakest point of the story before a stranger can.

## Part 7: The X post

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

## Part 8: The LinkedIn post

LinkedIn renders plain text. No Markdown, so no asterisks, no headers, no bullets. The ceiling is 3,000 characters and a story never needs it: write 150 to 300 words, and treat 300 as a wall. If the story is done at 160 words, it is done. When a draft runs over, cut a whole beat or a whole detail. Squeezing every sentence a little is how accurate statements turn into inaccurate ones.

### The first line

On a phone the feed shows roughly the first 140 characters and then a "see more" link. That first line is the only part most people will read, so it has to be the story already in motion: a person, a specific trouble, and a gap the reader wants closed. George Loewenstein's gap theory, which the Heaths lean on, says curiosity is the itch of knowing there is something you do not know. Open the gap with a fact, and let the fact be strange enough that the reader needs the explanation.

> The chairman of the statistics department called to say the mail server could not send email farther than 500 miles.

That line is the first beat of the story, and it is also the hook. Those should be the same sentence. A line that advertises the post ("I came across a fascinating story this week") spends the fold on nothing. A speaker on a stage gets a little goodwill before the audience drifts. A feed gives you one line.

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

## Part 9: The image prompt

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

### Imagined, but never false

The image is an illustration, so it may show things no source describes: what the room looked like, where the lamp stood. It may not contradict the record (the wrong decade of hardware, a crowd where there was one person), and it should not be mistakable for a documentary photograph of a real event. When the record gives you nothing to see, take the object or the metaphor route.

### Real people

When the story is about a real person, describe the figure and leave the name out of the prompt: approximate age, build, hair, clothing of the period, posture. Many image models refuse named likenesses or get them wrong, and a photorealistic fake portrait of a real person is not something to post beside a true story. Better options: show them from behind or in silhouette, show only their hands and their tools, or pick an illustrated medium that nobody could mistake for a photograph.

### Example

> A paper road map of the eastern United States pinned to a corkboard in a cramped university server room in the mid 1990s, a wobbly red circle drawn by hand around North Carolina. In the foreground, slightly out of focus, a beige terminal glows green and a man's hand rests on the keyboard, a mug of cold coffee beside it. Seen from over his shoulder. Warm tungsten light from a desk lamp, deep shadows, muted palette of beige, green and red. 35mm film photograph, shallow depth of field, visible grain. Square 1:1 composition with the map at the centre. No text, no lettering, no logos, no watermark.

## Part 10: The last read

Read the finished file as someone who has never heard of the subject and owes you nothing, with your sources open beside it. For each question below, find the sentence that proves the answer. This is a read, so nothing gets written down except the fixes.

1. **Two sentences.** Tell the story aloud, to nobody, in two sentences. If you cannot, the spine is missing, and no edit below will supply it.
2. **The first line.** Does it carry at least two of these: a person, a time or place, trouble? Would it make sense if it were the only line a reader saw?
3. **The break.** Point to the sentence where the unexpected thing happens. It should be in both posts.
4. **The person.** Is one human being named and doing something by the second paragraph?
5. **The cause.** Read only the joins between events. Each should be a "so" or a "but".
6. **The stranger.** Is there a name, an acronym, or a piece of the incident that the reader needs and was never given? Is there an explanation of something any engineer knows?
7. **The move test.** Could any sentence be moved into a post about a different story? Cut it or make it specific.
8. **The ending.** Is the final sentence a fact or an image from this story?
9. **The record.** Is every name, number, date, and quote backed by a line in `Sources`?
10. **The X post alone.** Read it without the LinkedIn post. Does it stand?
11. **The image.** Can the idea be said in one sentence, and is it something the reader has not seen before?
12. **The rotation.** Does the opening differ from the last few stories in `stories/`? Is the image in a different medium from the last one?

Last, the question that outranks the rest: if someone who was there read this, would they say that is what happened?

## The books

What each one gave this guide.

| Book | Used for |
| :-- | :-- |
| *Putting Stories to Work*, Shawn Callahan | The test for whether something is a story at all. Time and place markers. The clarity story. Never announcing a story. Small stories over epics, and the warning about the storytelling voice. |
| *Wired for Story*, Lisa Cron | The definition of story. The three questions a reader asks. Cause and effect. Need-to-know background. Specifics over generalities. Story over pretty sentences. |
| *The Storytelling Animal*, Jonathan Gottschall | Trouble as the engine. Story as simulation. The warning about the mind's habit of inventing tidy causes. |
| *The Hero's Journey*, Joseph Campbell | The three movements: departure, initiation, return. The refusal of the call. The boon. The stages themselves are set out in his earlier *The Hero with a Thousand Faces*. |
| *The Art of Storytelling*, John Walsh | Seeing the story as scenes. Telling it from the view of someone who was there. The central truth. Planning the first words and the ending. Cutting needless detail, then adding description. |
| *TED Talks*, Chris Anderson | The throughline. Ways to open. Ways to end, and ways endings fail. |
| *Made to Stick*, Chip and Dan Heath | SUCCESs. The curiosity gap. The curse of knowledge. Human-scale numbers. The three plots. Core plus compact, for the X post. |
| *Contagious*, Jonah Berger | STEPPS. High-arousal emotion. Triggers. The Trojan horse. |
| *Influence*, Robert Cialdini | Which persuasion principles a true story may earn, and which are bait. The power of "because". |
| *Start With Why*, Simon Sinek | Knowing the belief behind the story before telling it. Plain, repeatable language. |
| *Ego Is the Enemy*, Ryan Holiday | The prose model: start inside the event, short declarative sentences, the idea stated once. Keeping the narrator out of the way. |
| *The Storyteller's Secret*, Sejal Badani | The present-day frame around a past story. Withholding the answer, never the question. Naming the specific sensory detail. |

*Contagious* appeared on the reading list under two subtitles. It is one book. Badani's *The Storyteller's Secret* is a novel, so it is here as a model of craft. Carmine Gallo wrote a business book with the same title, which is not used.
