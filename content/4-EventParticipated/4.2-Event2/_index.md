---
title: "Event 2: FCAJ Community Day 2026"
date: 2026-05-23
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---

# Event 2: FCAJ Community Day 2026

| Field | Detail |
| --- | --- |
| Event name | FCAJ Community Day 2026 |
| Date/time | 23 May 2026 |
| Location | AWS Event Hall, Floor 26, Bitexco Financial Tower, Ho Chi Minh City |
| Role | Participant |

![Group photo at FCAJ Community Day 2026](/images/4-EventParticipated/Event2/group-photo.png)

*Speakers, organizers, and participants at FCAJ Community Day 2026.*

FCAJ Community Day 2026 provided practical perspectives on AI, cloud architecture, content delivery, and the process of turning an idea into a product. The sessions showed not only what each technology can do, but also how to place it in the right context, recognize its limitations, and design systems that can operate in practice.

## Opening – Nguyen Gia Hung: AI and changes in the job market

![Nguyen Gia Hung giving the opening remarks about AI and the job market](/images/4-EventParticipated/Event2/nguyen-gia-hung-opening.png)

*Nguyen Gia Hung briefly discusses AI's impact on the job market and how students should prepare.*

Nguyen Gia Hung opened the event with an approximately ten-minute overview of AI's impact on the job market and the preparation students need to adapt. This was a short orientation rather than one of the event's main technical topics. My main takeaway was that students need strong foundations, continuous learning, and problem-solving ability instead of depending only on AI tools.

## Topic 1 – Tinh Truong: Context Is Everything

**Context Is Everything** explained that a powerful model is not enough when the context is unclear. A goal, situation, constraints, and relevant evidence help AI understand the real task instead of responding to a vague request. The insight I retained was that **context quality matters more than context quantity**.

![The components of effective context for AI](/images/4-EventParticipated/Event2/context-is-everything-details.png)

*A goal, situation, constraints, and relevant evidence turn a vague request into a solvable task.*

For LiveCap, this means that any AI feature applied to transcripts or post-session content should receive structured objectives, conversation context, and relevant evidence. Supplying more data does not guarantee a better result when that data is irrelevant or fails to clarify the requirement.

## Topic 2 – Anh Pham Nguyen Hai: Friendly AI Assistant with Amazon Quick

![Anh Pham Nguyen Hai presenting Friendly AI Assistant with Amazon Quick](/images/4-EventParticipated/Event2/friendly-ai-amazon-quick.png)

*[Anh Pham Nguyen Hai](https://www.linkedin.com/in/anhpnh/) introduces a practical approach to building a friendly AI assistant with Amazon Quick.*

**Friendly AI Assistant with Amazon Quick** introduced a practical way to apply AI to work support and business process automation. The important point for me was not only response generation, but the need to place an assistant inside a process with a clear objective, appropriate inputs, and identified users.

For LiveCap, this extends the view beyond real-time transcripts. Post-session results can be organized for review and reuse, but any additional AI capability should address a specific user need rather than being added simply because the technology is available.

## Topic 3 – Thinh Nguyen: From Edge To Origin – CloudFront as Your Foundation

![Thinh Nguyen presenting Amazon CloudFront architecture from edge to origin](/images/4-EventParticipated/Event2/cloudfront-thinh-nguyen.png)

*[Thinh Nguyen](https://www.linkedin.com/in/thinhnguyen1211/) explains how CloudFront connects edge locations with the origin.*

**From Edge To Origin: CloudFront as Your Foundation** clarified CloudFront's role in delivering content between edge locations and an origin. CloudFront affects not only access speed but also scalability, reliability, and user experience for an application serving distributed users.

In LiveCap, CloudFront should be explained through the actual request flow rather than appearing only as an icon in an architecture diagram. I need to identify which content is delivered through the edge, where the origin is located, what can be cached, and which real-time flows cannot be handled like static assets.

## Topic 4 – Uyen Le Pham Ngoc, Nguyen Ngoc Quynh Mai, and Thao Nguyen Phuong: 36 hrs with LotusHacks

![The UTMorpho team sharing its journey from idea to product at LotusHacks](/images/4-EventParticipated/Event2/utmorpho-team.png)

*[Uyen Le Pham Ngoc](https://www.linkedin.com/in/lephamngocuyen/), [Nguyen Ngoc Quynh Mai](https://www.linkedin.com/in/nnquynhmai/), and [Thao Nguyen Phuong](https://www.linkedin.com/in/thao-ngph/) share how they built UTMorpho in 36 hours.*

**36 hrs with LotusHacks – Building UTMorpho from Idea to Reality** described how the team began with an incomplete idea, identified a problem from daily work, and developed UTMorpho within a limited hackathon window. AI accelerated brainstorming, prototyping, and UI development, but the team still had to define the problem and prioritize the most important work.

I learned that clear scope and fast feedback matter more than attempting every feature at once. For LiveCap, I need to protect the core objective, validate progress in small steps, and use AI as an accelerator without allowing it to shift the project away from the real problem.

## Topic 5 – Duc Dao Minh: Non-Determinism of “Deterministic” LLM Settings

![Duc Dao Minh explaining the roles of Temperature, Top-P, and Top-K](/images/4-EventParticipated/Event2/duc-dao-minh.png)

*[Duc Dao Minh](https://www.linkedin.com/in/itsdmd/) explains how Temperature, Top-P, and Top-K affect the consistency of LLM outputs.*

In **Non-Determinism of “Deterministic” LLM Settings**, [Duc Dao Minh](https://www.linkedin.com/in/itsdmd/) explained that LLM systems may still produce different outputs even when some parameters appear deterministic. A fixed-looking configuration does not guarantee identical behavior on every run.

This makes me more careful when evaluating AI in production. If LiveCap uses AI for summaries or other post-session processing, I need test criteria, observable results, and ways to handle variation. A successful output from one demo run does not prove reliability.

## Topic 6 – Lam Hoang Cat Vy: Enterprise-Grade Multi-Agent System

![Lam Hoang Cat Vy presenting a multi-agent architecture for startup credit scoring](/images/4-EventParticipated/Event2/lam-hoang-cat-vy.png)

*[Lam Hoang Cat Vy](https://www.linkedin.com/in/lam-hoang-cat-vy/) presents the Enterprise-Grade Multi-Agent System case study for startup credit scoring.*

**Enterprise-Grade Multi-Agent System: The Case of Startup Credit Scoring** provided an enterprise view of AI architecture. A multi-agent system needs more than agents performing tasks; it also requires a coherent structure, coordination, governance, security, and evaluation.

The case study taught me that splitting a system into many agents does not automatically improve it. Each agent needs a clear responsibility, appropriate data, and control mechanisms. LiveCap should adopt more complex AI workflows only when the problem genuinely requires them, rather than adding complexity to follow a trend.

## Synthesis

The event connected several layers of modern systems: context determines the quality of AI interaction; Amazon Quick demonstrates AI inside a workflow; CloudFront provides a content-delivery foundation; UTMorpho illustrates rapid prototyping; LLM non-determinism highlights production limitations; and multi-agent credit scoring demonstrates enterprise architecture and governance.

For LiveCap, I can turn these lessons into concrete actions: explain the architecture from edge to backend, design structured context for AI features, test outputs instead of trusting a single run, keep the product scope realistic, and introduce complexity only when it serves a clear user requirement.
