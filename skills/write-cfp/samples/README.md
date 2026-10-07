# Samples

Real proposals the user has submitted, one file each, with the outcome in the frontmatter. The `cfp-writer` agent reads every file here on every run, and `../outcomes.md` for what the user thinks made the difference.

Add a proposal here when its result is known, or when it is a shape worth copying. Keep the text exactly as submitted; this is the record of what reviewers saw. Frontmatter:

```yaml
---
title: "Exact title as submitted"
outcome: accepted | rejected | waitlisted | pending | draft
conferences: [Conference Name Year, ...]
format: Lightning talk (10 min)
field: engineering | compliance | open source | platform
speaker: I | we
---
```

Then the submission text under the headings the form used.
