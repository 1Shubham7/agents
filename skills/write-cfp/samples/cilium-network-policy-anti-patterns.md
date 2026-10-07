---
title: "Cilium Network Policy Anti-Patterns I Learned the Hard Way"
outcome: accepted
conferences: [Cloud Native Summit Kerala 2026, and three other events in 2026]
format: Lightning talk (10 min)
field: engineering
speaker: I
---

Accepted at four events. The user's reference for what a working engineering proposal looks like.

## Description

Writing Network Policies looks straightforward - until traffic starts getting blocked for reasons that aren't obvious, policies silently match nothing, or things work in staging but fail in production. I learned this the hard way while writing and designing Network Policies used by multiple teams across multiple Kubernetes clusters, and debugging policy failures in real production environments.

In this lightning talk, I'll share the most common Cilium Network Policy anti-patterns one can run into. We'll look at real examples of policies that look correct but are wrong, why certain design decisions matter, and how small mistakes can lead to confusing failures. Each example will be drawn from real world usage and paired with the corrected approach.

We will highlight practical tips and anti-patterns that are rarely documented, and brings together the key things you need to know to reliably firewall Kubernetes workloads using Cilium Network Policies.

## Benefits to the ecosystem

Cilium adoption is growing faster than the operational knowledge around it. I spent three months writing CiliumNetworkPolicies to firewall entire clusters, and built an OSS feature around it that is now used by 100+ users. Most of what I learned came from things going wrong first.

The failure I kept hitting, and have since watched other teams hit, is a policy that reads correctly, applies without error, and silently drops traffic. There is no obvious place to start debugging that, so people lose hours to it.

In this talk I want to hand over what took me three months to work out. That means the parts of the enforcement model that actually explain the failures: identity based enforcement, where in the datapath enforcement happens relative to DNAT and DNS, and additive composition with no precedence between policies. It also means the practical side that nobody writes down - how to stop CNPs turning into a mess once several teams are writing them, and a simple way to author them that still works at a large scale.
