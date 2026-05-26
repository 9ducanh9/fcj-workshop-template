---
title : "Create Storage and Job Foundation"
date : 2026-05-12
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

# Create Storage and Job Foundation

This section creates the foundation used by the AI workflow:

- A private S3 bucket for uploaded files and reports.
- A DynamoDB table for job status.
- IAM roles and policies for Lambda and Step Functions.

The goal is to keep the data model simple and easy to validate during the final demo.
