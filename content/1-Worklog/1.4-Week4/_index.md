---
title: "Week 4 Worklog"
date: 2026-05-12
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

# Week 4 Worklog

## Work Completed

- Designed the first high-level AWS architecture.
- Mapped user actions to AWS components: upload, process, analyze, store, retrieve.
- Studied S3 private buckets, pre-signed URLs, object prefixes, and lifecycle cleanup.

## Results Achieved

- Chose Amazon S3 as the storage layer for audio, transcript, and report files.
- Defined a simple S3 prefix structure: `uploads/`, `transcripts/`, and `reports/`.
- Added S3 security requirements to the project proposal.

## Learning Outcomes

- A storage design should include access control and cleanup policy, not only bucket creation.
- Pre-signed URLs are useful for controlled upload without making a bucket public.
