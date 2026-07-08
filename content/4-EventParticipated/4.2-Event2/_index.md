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

FCAJ Community Day 2026 gave me a more practical view of AI. AI is no longer only a standalone chatbot; it is becoming a component of software systems with architecture, workflows, data, security, operating costs, and accountability. The sessions moved from career preparation and context design to AI Agent automation, CloudFront infrastructure, LLM control, and enterprise multi-agent systems.

## Opening – Nguyen Gia Hung: AI and changes in the job market

![Nguyen Gia Hung giving the opening remarks about AI and the job market](/images/4-EventParticipated/Event2/nguyen-gia-hung-opening.png)

*Nguyen Gia Hung briefly discusses AI's impact on the job market and how students should prepare.*

Nguyen Gia Hung opened the event by explaining how AI is reducing the time and cost required to develop software. As prototyping, coding, debugging, and MVP creation become faster, the number of software products may increase significantly. This does not necessarily remove the demand for IT professionals. People who can identify the right problem, build systems, operate them, resolve failures, optimize performance, and scale solutions may become even more important.

A university degree or familiarity with several tools is no longer enough to create a strong advantage. Students need to understand business operations, build real products rather than isolated demos, connect technology to business use cases, and develop communication and language skills. Continuous learning is also necessary because both technology and market requirements keep changing.

My takeaway was that AI can help me write code faster, but it cannot take responsibility for deciding which problem is worth solving. An engineer's value comes from understanding users, clarifying requirements, and designing a solution that produces a real outcome.

## Topic 1 – Tinh Truong: Context Is Everything

**Context Is Everything** explained that model capability alone does not guarantee a useful result. When context is unclear or overloaded with irrelevant information, AI can misunderstand the objective, produce unfocused answers, or generate results that are difficult to use.

![The components of effective context for AI](/images/4-EventParticipated/Event2/context-is-everything-details.png)

*A goal, situation, constraints, and relevant evidence turn a vague request into a solvable task.*

Effective context should establish at least four elements:

* **Goal:** The final outcome that must be achieved.
* **Persona:** The intended reader, such as a beginner, developer, architect, or business user.
* **Format:** The expected output structure, such as a table, checklist, technical document, or JSON.
* **Related data:** Evidence and information that are genuinely relevant to the problem.

The speaker also warned about the “Internet Builder” mindset: adding every interesting framework, template, prompt, or library without reading or understanding it. This approach fills a system with unnecessary components, overloads the AI context, and eventually produces low-quality code that is difficult to control.

A stronger approach is to develop an AI mindset and an organized “Second Brain.” A knowledge tool such as Obsidian can preserve notes, connect concepts, and record decision-making. Organized knowledge helps a person construct better prompts and explain how information was learned, verified, and used.

My lesson was that **Prompt Engineering is fundamentally Context Engineering**. More capable AI requires users to provide better direction, boundaries, and relevant evidence—not simply more data.

## Topic 2 – Anh Pham Nguyen Hai: Friendly AI Assistant with Amazon Quick

![Anh Pham Nguyen Hai presenting Friendly AI Assistant with Amazon Quick](/images/4-EventParticipated/Event2/friendly-ai-amazon-quick.png)

*[Anh Pham Nguyen Hai](https://www.linkedin.com/in/anhpnh/) introduces a practical approach to building a friendly AI assistant with Amazon Quick.*

**Friendly AI Assistant with Amazon Quick** presented a common enterprise problem: automating the preparation of management reports. Data can be distributed across spreadsheets, email, meeting notes, Jira, Google Workspace, and Microsoft Teams. A person preparing a report must collect the data, understand it, identify trends, create charts, summarize key points, and deliver the result to the correct stakeholder.

The proposed solution used an AI Agent as the “brain” that interprets requests and external tools connected through MCP as its extended “arms.” This allows AI to do more than generate text. It can read files, analyze data, create dashboards, summarize meetings, and support report delivery through an existing workflow.

Managers do not necessarily need deep BI expertise to benefit from this approach. They can provide a raw spreadsheet and request trend analysis, charts, or a list of anomalies in natural language. However, the system still needs data access controls, clear sources, and confirmation before actions that affect other people.

I learned that a chatbot creates greater value when it is placed inside a specific process. **An AI Agent is most valuable when it is connected to real enterprise workflows and tools**, with clear inputs, outputs, and ownership.

## Topic 3 – Thinh Nguyen: From Edge To Origin – CloudFront as Your Foundation

![Thinh Nguyen presenting Amazon CloudFront architecture from edge to origin](/images/4-EventParticipated/Event2/cloudfront-thinh-nguyen.png)

*[Thinh Nguyen](https://www.linkedin.com/in/thinhnguyen1211/) explains how CloudFront connects edge locations with the origin.*

**From Edge To Origin: CloudFront as Your Foundation** examined CloudFront through three concerns: cost control, security, and performance.

For cost, a common cloud risk is bill shock caused by unusual traffic, an attack, or an inefficient configuration. Flat-rate pricing can make costs more predictable because bandwidth can be limited after an allowance is exceeded instead of creating uncontrolled usage charges.

For security, CloudFront operates at the edge in front of the origin. Its network of points of presence can absorb or reject malicious traffic earlier, support DDoS protection and geographic restrictions, and reduce direct exposure of the backend. VPC Origin can keep the origin inside a private network without making it publicly reachable, reducing the attack surface.

For performance, CloudFront supports caching, HTTP/3, and TLS/TCP processing close to users. Static assets can be served from the edge rather than returning to the origin for every request, reducing latency and backend CPU load. Cache policies must still be designed carefully because dynamic content, personal data, and real-time flows cannot be treated like static assets.

My takeaway was that **CloudFront is not only a CDN for faster websites; it is also a layer for controlling security, cost, and performance**. A system design should explain how requests move from users through the edge to the origin, what can be cached, and which traffic must reach the backend directly.

## Topic 4 – Uyen Le Pham Ngoc, Nguyen Ngoc Quynh Mai, and Thao Nguyen Phuong: 36 hrs with LotusHacks

![The UTMorpho team sharing its journey from idea to product at LotusHacks](/images/4-EventParticipated/Event2/utmorpho-team.png)

*[Uyen Le Pham Ngoc](https://www.linkedin.com/in/lephamngocuyen/), [Nguyen Ngoc Quynh Mai](https://www.linkedin.com/in/nnquynhmai/), and [Thao Nguyen Phuong](https://www.linkedin.com/in/thao-ngph/) share how they built UTMorpho in 36 hours.*

**36 hrs with LotusHacks – Building UTMorpho from Idea to Reality** was a practical case study in building an AI product under severe time constraints. UTMorpho used AI to generate interfaces from sketches or user descriptions while also allowing users to edit the generated result directly. Editing was a key capability because an AI-generated first version rarely matches the final requirement perfectly.

The team used a serverless approach and divided responsibilities among agents, such as an image-reading agent, a layout/CSS agent, and a code-generation agent. Specialization allowed each agent to focus on one task instead of requiring a single model to process an entire workflow in a large context.

The team encountered familiar limitations, including token constraints and over-generation. AI can add unnecessary details or features, making the product more complex and increasing review time. This is especially risky during a hackathon when time is limited.

My main lesson was to protect the product's core value. A strong AI product is not the product with the most AI features; it is the product that **uses AI in the right place to solve a clearly defined problem**. A narrow scope, rapid feedback, and editable results can be more useful than a long list of incomplete capabilities.

## Topic 5 – Duc Dao Minh: Non-Determinism of “Deterministic” LLM Settings

![Duc Dao Minh explaining the roles of Temperature, Top-P, and Top-K](/images/4-EventParticipated/Event2/duc-dao-minh.png)

*[Duc Dao Minh](https://www.linkedin.com/in/itsdmd/) explains how Temperature, Top-P, and Top-K affect the consistency of LLM outputs.*

In **Non-Determinism of “Deterministic” LLM Settings**, [Duc Dao Minh](https://www.linkedin.com/in/itsdmd/) explained that an LLM can still produce different outputs when Temperature is set to zero. LLMs are probabilistic by nature. In addition to sampling parameters, numerical precision, rounding, and parallel GPU execution can introduce small variations. In cloud environments, providers may also batch requests to optimize infrastructure usage, which can affect outputs.

This has important production implications. A correct result in one demonstration does not prove that the system will behave consistently across repeated runs. High-reliability tasks require additional control layers:

* Run several agents or attempts and compare or vote on results.
* Use JSON mode or schemas to constrain output structure.
* Add validation, error handling, and fallback paths.
* Test with multiple datasets and edge cases.
* Consider self-hosting when greater control is required.
* Measure trade-offs among accuracy, cost, and latency.

My lesson was that **LLM-based systems must be designed to tolerate variation** instead of assuming that a model will always return the same answer.

## Topic 6 – Lam Hoang Cat Vy: Enterprise-Grade Multi-Agent System

![Lam Hoang Cat Vy presenting a multi-agent architecture for startup credit scoring](/images/4-EventParticipated/Event2/lam-hoang-cat-vy.png)

*[Lam Hoang Cat Vy](https://www.linkedin.com/in/lam-hoang-cat-vy/) presents the Enterprise-Grade Multi-Agent System case study for startup credit scoring.*

**Enterprise-Grade Multi-Agent System: The Case of Startup Credit Scoring** presented a complex use case: evaluating credit for startups. Startups often lack the collateral and long financial histories available for traditional businesses, so the decision requires multiple data types and expert perspectives.

The multi-agent architecture divided responsibility among roles such as a financial analysis agent, market research agent, risk evaluation agent, and manager agent that combined the findings. This resembles a group of specialists, reducing the context load for each agent and increasing specialization.

The hardest enterprise concerns were not limited to the model. The system needs strict access control, guardrails against prompt injection, an audit trail for decisions, and clear accountability when an output is wrong. Financial data also requires careful security and authorization.

The session also emphasized Knowledge Transfer and Context Engineering. An organization cannot upload hundreds of PDF pages and expect AI to become a domain expert automatically. Subject-matter experts must identify important evidence, explain evaluation methods, and design the context used by each agent.

My takeaway was that **enterprise AI is a complete software engineering problem**, including architecture, security, permissions, auditing, guardrails, infrastructure, and domain knowledge. Adding agents is useful only when each agent has a clear responsibility and the coordination process remains controllable.

## Synthesis

Event 2 showed me that AI is changing software development without removing the engineer's role. AI accelerates implementation, while people must still understand the problem, design context, control data, and remain responsible for results.

My main lessons were:

* AI increases development speed, but people must identify the correct problem.
* Prompt Engineering is fundamentally context design.
* AI Agents create value when connected to real workflows and tools.
* CloudFront supports performance, security, and cost control.
* AI products should prioritize core value instead of accumulating features.
* Probabilistic LLMs require validation, error handling, and serious testing.
* Enterprise AI requires permissions, audit trails, guardrails, and domain knowledge.

The event aligned closely with my interest in Business System Analyst and Solution Architect roles. A BSA must understand business use cases, ask the right questions, and translate needs into system requirements. A Solution Architect must evaluate architecture, security, cost, scalability, and trade-offs. The real advantage is not using the largest number of AI tools, but designing and controlling a system that solves the right problem.
