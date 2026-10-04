#!/usr/bin/env python3
"""Mechanical checks for a story file written by the story-teller agent.

Usage: check_story.py stories/<file>.md

Counting characters and spotting stock phrases is exactly what a language
model is bad at, so this script does it instead. ERROR lines must be fixed.
WARN lines must each be fixed or kept on purpose. Exit code is 1 when there
is at least one ERROR.
"""

import re
import sys
import unicodedata

X_LIMIT = 280
LINKEDIN_LIMIT = 3000
LINKEDIN_LONG = 2200  # past this a story post is usually padded
LINKEDIN_FOLD = 140  # roughly what shows before "see more" on a phone
LINKEDIN_MAX_HASHTAGS = 3
IMAGE_MIN_WORDS = 40

REQUIRED_FRONTMATTER = ("title", "date", "subject", "area")
SECTIONS = ("X", "LinkedIn", "Image prompt", "Sources")

# X counts these code point ranges as 1 character and everything else as 2
# (twitter-text v3 config).
X_SINGLE_WEIGHT = ((0, 4351), (8192, 8205), (8208, 8223), (8242, 8247))

DASHES = ("—", "–", " -- ")

VOCABULARY = (
    "delve", "leverage", "utilize", "robust", "seamless", "landscape", "realm",
    "elevate", "unlock", "unleash", "game-changer", "game changer", "tapestry",
    "testament", "pivotal", "crucial", "foster", "navigate", "journey",
    "embark", "harness", "revolutionize", "groundbreaking", "cutting-edge",
    "ever-evolving", "fast-paced", "transformative", "paradigm", "synergy",
    "underscore", "intricate", "meticulous", "vibrant", "bustling", "beacon",
    "treasure trove", "double-edged sword", "supercharge", "deep dive",
)

PHRASES = (
    "in today's", "in the world of", "in a world where", "it's important to",
    "it's worth noting", "it is worth noting", "at the end of the day",
    "let that sink in", "read that again", "here's the thing",
    "here's the kicker", "here's why", "here's what", "the lesson?",
    "the result?", "the takeaway", "key takeaway", "moral of the story",
    "little did", "the rest is history", "fast forward", "plot twist",
    "spoiler", "buckle up", "let me tell you a story", "picture this",
    "imagine this", "what do you think", "thoughts?", "agree?",
    "additionally", "furthermore", "moreover", "in conclusion",
    "needless to say", "changed everything", "changed the world forever",
    "story time", "a thread", "but here's", "and honestly",
)

# Sentence shapes that give a model away, whatever words fill them.
SHAPES = (
    (r"\b(?:isn't|wasn't|is not|was not|aren't|weren't) (?:just |only |merely )?"
     r"(?:about )?[^.?!\n]{1,60}[.,;:] (?:it|he|she|they|this|that)(?:'s| is| was|'re| were) ",
     'the "it wasn\'t X, it was Y" reversal'),
    (r"\bnot (?:just|only) [^.?!\n]{1,60}\bbut\b", 'the "not just X but Y" frame'),
    (r"(?:^|\n)[^\n.?!]{1,40}\?\s*\n+[^\n]{1,60}[.!]\s*(?:\n|$)",
     "a rhetorical question answered in the next line"),
)

EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U00002B00-\U00002BFF\U0000FE0F]"
)
URL = re.compile(r"https?://\S+|\bwww\.\S+")
HASHTAG = re.compile(r"(?<!\w)#\w+")


def x_length(text):
    total = 0
    for ch in unicodedata.normalize("NFC", text):
        cp = ord(ch)
        total += 1 if any(lo <= cp <= hi for lo, hi in X_SINGLE_WEIGHT) else 2
    return total


def parse(raw):
    """Return (frontmatter dict, {section name: body text})."""
    front = {}
    body = raw
    match = re.match(r"---\n(.*?)\n---\n", raw, re.S)
    if match:
        body = raw[match.end():]
        for line in match.group(1).splitlines():
            key, sep, value = line.partition(":")
            if sep and not key.startswith((" ", "-")):
                front[key.strip()] = value.strip()

    sections = {}
    parts = re.split(r"^## +(.+?)\s*$", body, flags=re.M)
    for name, text in zip(parts[1::2], parts[2::2]):
        fence = re.search(r"```[^\n]*\n(.*?)\n```", text, re.S)
        sections[name.strip()] = (fence.group(1) if fence else text).strip()
    return front, sections


def scan_style(name, text, errors, warnings):
    lowered = text.lower().replace("’", "'")
    for dash in DASHES:
        if dash in text:
            label = "double hyphen" if dash == " -- " else "em or en dash"
            errors.append(f"{name}: {label} used as punctuation ({text.count(dash)}x)")
    for word in VOCABULARY:
        if re.search(rf"\b{re.escape(word)}", lowered):
            warnings.append(f'{name}: stock vocabulary "{word}"')
    for phrase in PHRASES:
        if phrase in lowered:
            warnings.append(f'{name}: stock phrase "{phrase}"')
    for pattern, label in SHAPES:
        found = re.search(pattern, lowered)
        if found:
            snippet = " ".join(found.group(0).split())[:70]
            warnings.append(f'{name}: {label}: "{snippet}"')


def scan_rhythm(name, text, warnings):
    lines = [line for line in text.splitlines() if line.strip()]
    if len(lines) >= 8:
        short = sum(1 for line in lines if len(line.split()) <= 8)
        if short / len(lines) > 0.7:
            warnings.append(
                f"{name}: {short} of {len(lines)} lines are 8 words or fewer. "
                "One sentence per line is the LinkedIn-bro cadence; write paragraphs."
            )
    sentences = [s for s in re.split(r"(?<=[.?!])\s+", text) if s.strip()]
    lengths = [len(s.split()) for s in sentences]
    if len(lengths) >= 6 and max(lengths) - min(lengths) < 8:
        warnings.append(
            f"{name}: every sentence is {min(lengths)} to {max(lengths)} words. Vary the length."
        )


def check(path):
    errors, warnings, info = [], [], []
    with open(path, encoding="utf-8") as handle:
        front, sections = parse(handle.read())

    for key in REQUIRED_FRONTMATTER:
        if not front.get(key):
            errors.append(f"frontmatter: missing `{key}`")
    for name in SECTIONS:
        if not sections.get(name):
            errors.append(f"missing or empty section `## {name}`")

    x = sections.get("X", "")
    if x:
        length = x_length(x)
        info.append(f"X: {length}/{X_LIMIT} characters")
        if length > X_LIMIT:
            errors.append(f"X: {length} characters, {length - X_LIMIT} over the limit")
        if URL.search(x):
            errors.append("X: contains a link (links belong in a reply, not the post)")
        if HASHTAG.search(x):
            errors.append("X: contains a hashtag")
        if EMOJI.search(x):
            warnings.append("X: contains emoji")
        scan_style("X", x, errors, warnings)

    linkedin = sections.get("LinkedIn", "")
    if linkedin:
        length = len(linkedin)
        info.append(f"LinkedIn: {length}/{LINKEDIN_LIMIT} characters, {len(linkedin.split())} words")
        if length > LINKEDIN_LIMIT:
            errors.append(f"LinkedIn: {length} characters, {length - LINKEDIN_LIMIT} over the limit")
        elif length > LINKEDIN_LONG:
            warnings.append(f"LinkedIn: {length} characters. Check for padding.")
        hook = linkedin.splitlines()[0]
        if len(hook) > LINKEDIN_FOLD:
            warnings.append(
                f"LinkedIn: first line is {len(hook)} characters, the fold is near {LINKEDIN_FOLD}"
            )
        tags = HASHTAG.findall(linkedin)
        if len(tags) > LINKEDIN_MAX_HASHTAGS:
            errors.append(f"LinkedIn: {len(tags)} hashtags, the maximum is {LINKEDIN_MAX_HASHTAGS}")
        if URL.search(linkedin):
            warnings.append("LinkedIn: contains a link (put links in the first comment)")
        if EMOJI.search(linkedin):
            warnings.append("LinkedIn: contains emoji")
        if re.search(r"^\s*(?:[-*•]|\d+[.)])\s", linkedin, re.M):
            warnings.append("LinkedIn: contains a bullet or numbered list. A story is prose.")
        scan_style("LinkedIn", linkedin, errors, warnings)
        scan_rhythm("LinkedIn", linkedin, warnings)

    image = sections.get("Image prompt", "")
    if image:
        words = len(image.split())
        info.append(f"Image prompt: {words} words")
        if words < IMAGE_MIN_WORDS:
            warnings.append(f"Image prompt: only {words} words, too thin to steer an image model")
        for dash in DASHES[:2]:
            if dash in image:
                errors.append("Image prompt: em or en dash used as punctuation")

    sources = sections.get("Sources", "")
    if sources and not URL.search(sources):
        errors.append("Sources: no URL listed. Every story needs a source that was actually fetched.")

    return errors, warnings, info


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    errors, warnings, info = check(sys.argv[1])
    for line in info:
        print(f"INFO  {line}")
    for line in warnings:
        print(f"WARN  {line}")
    for line in errors:
        print(f"ERROR {line}")
    if not errors and not warnings:
        print("OK    clean")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
