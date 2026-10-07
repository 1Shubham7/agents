---
title: "Building Your Cluster's Memory for the Worst Day: Audit -> Detect -> Alert"
outcome: rejected
conferences: [not accepted so far; events to be filled in by the user]
format: Session
field: engineering
speaker: we
---

Submitted and not accepted so far. Same author as the Cilium proposal, same bones, different result. The user's view of why is in `../outcomes.md`; the guide lists hypotheses.

## Description

A ClusterRoleBinding grants someone cluster-admin at AM. Three days later, someone asks who did it - and nobody can answer. This talk is about closing that gap. In this talk we will demonstrate how to enable audit logging, how to actually write audit policies specific to your needs along with best practices we follow as a team of 20 SREs, and how all of this changes depending on whether you're running prod, staging, or chasing a specific compliance requirement.

We'll cover shipping audit logs off the node and into a log aggregation platform (like Loki or Graylog) so you can query them during an investigation, and how to do all of this the GitOps way. Last, we'll build the part that actually answers "did anyone notice" - using Falco rules on the same audit stream to evaluate events in real time and set up alerting pipeline to Alertmanager or any webhook when something suspicious happens.

## Value to the community

Audit logging is one of the few Kubernetes features that is off by default, hard to turn on correctly, and invisible when it's misconfigured. Most teams either never enable it, or enable it with the sample policy from the docs and discover during an actual investigation that the event they needed wasn't recorded. There is no feedback loop: a bad audit policy looks exactly like a good one until the day you need it.

The gap is not in the API documentation, it's in the operational decisions around it. Which verbs and resources are worth recording at which level, what that costs in volume, where the logs go once they leave the node, and how any of it stays reviewable in Git rather than drifting on the control plane. Those choices get made once per team, usually under time pressure, and rarely get written down.

This talk brings together what a team of 20 SREs settled on after making those decisions across production clusters, and connects the last piece most setups are missing: turning a passive record into a live alert. Everything shown is upstream Kubernetes, Falco, and standard log aggregation, so it applies to any cluster regardless of distribution or cloud. Attendees leave able to write an audit policy that fits their environment and to know within minutes, not days, when something happens that shouldn't have.
