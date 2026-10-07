---
title: "The Clock Is Already Running: Will the CRA Block Your Product from Shipping to the EU?"
outcome: draft
conferences: [KubeCon + CloudNativeCon Europe 2027]
format: Session Presentation (30 minutes)
field: compliance
speaker: we
---

Draft for KubeCon + CloudNativeCon Europe 2027, revised by hand several times. The user's current preferred shape for a compliance talk aimed at platform and release engineers. Outcome unknown at the time of writing.

## Description

For as long as software has been sold, its security has been a promise in a contract, not a condition of sale. The EU Cyber Resilience Act, which entered into force in December 2024, changes that. From 11 December 2027, any software or hardware product that does not meet its requirements cannot be placed on the EU market, and authorities can order it withdrawn or recalled, with fines up to EUR 15 million or 2.5 percent of global turnover. And part of the law is already live.

This reaches most of the cloud native ecosystem: companies shipping Kubernetes distributions, operators, and Helm charts, companies selling products built on open source, and the platform and release engineers who will have to produce the evidence.

In this session we will explain what the CRA actually requires of a product, how to work out in a few minutes whether a product is in scope and which risk class it falls into, and what that means for how it is assessed. We will also cover what a release process must produce before the deadline. We maintain open source projects ourselves and help companies comply with standards such as ISO 27001, the CRA, GDPR and NIS2, and from that work we will walk through each requirement on a real Kubernetes setup using only open source tools.

This session will be a complete map of what the Cyber Resilience Act demands of a software product, and of how a cloud native release pipeline can meet it. Attendees will leave knowing whether their product is in scope, exactly what it must produce and by when, how far their current pipeline is from that, and a concrete checklist they can start working through the next morning.

## Benefits to the ecosystem

Software is at a turning point. For years, whether a product shipped with an SBOM, secure defaults or a way to receive updates was a matter of best practice and customer pressure. The Cyber Resilience Act makes those things a condition of selling in the EU at all. Product security is clearly moving from following best practices to complying with the law, and the CRA is only the first of these laws.

Most of the engineers who build and ship these products have not heard that this is happening, and almost all the guidance that exists is written by lawyers for lawyers. We believe everyone who ships software into the EU, from platform teams and release engineers to the companies selling products built on open source, needs to know what the CRA requires of them and how little time is left. Finding out from a customer's procurement questionnaire, or from a market surveillance authority, is the wrong way to learn it.

This talk gives the community that knowledge in engineering terms: the requirements translated into concrete outputs of a release pipeline, each produced with open source tools. Everything in it comes from reading all 71 articles of the regulation and applying them to an open source Kubernetes platform we maintain ourselves, and everything shown is open source.
