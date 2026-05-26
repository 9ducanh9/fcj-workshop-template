---
title: "Week 5 Worklog"
date: 2026-05-12
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

# Week 5 Worklog

## Work Completed

- Studied Lambda event handling and basic Python SDK usage with `boto3`.
- Designed backend functions for creating upload URLs, starting analysis jobs, and retrieving results.
- Studied DynamoDB partition keys and item design for job status tracking.

## Results Achieved

- Chose `jobId` as the DynamoDB partition key.
- Defined job states: `UPLOADED`, `TRANSCRIBING`, `ANALYZING`, `COMPLETED`, and `FAILED`.
- Created a simple API design for `/upload-url`, `/jobs`, and `/jobs/{jobId}`.

## Learning Outcomes

- DynamoDB is effective when access patterns are simple and known.
- API design should expose clear states so users can understand asynchronous processing.
