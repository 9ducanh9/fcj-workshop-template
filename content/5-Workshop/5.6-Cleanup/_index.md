---
title: "Release Safety and Remaining Work"
date: 2026-07-05
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---

# Release Safety and Remaining Work

## Completed Baseline

- Public CloudFront landing page and caption dashboard.
- ECS Fargate backend behind a multi-AZ ALB.
- Real bilingual Transcribe/Translate WebSocket flow.
- Heartbeat, bounded reconnect, timeout, and abuse guards.
- Private TXT transcript export with 14-day retention and no raw audio storage.
- CloudWatch logging with 14-day retention.
- Terraform source for remote state, target networking, WAF, dashboard, budget,
  wake-on-demand, idle scaling, and blue/green cutover.
- GitHub Actions validation and secret scanning.

## Safe Change Process

1. Work on a branch and keep changes in reviewable frontend/backend/infra batches.
2. Run backend, frontend, Terraform, and Gitleaks gates.
3. Review `git diff` and open a pull request.
4. Merge only after both PR and post-merge main CI pass.
5. Build images with immutable SHA tags.
6. Reconcile Terraform state and review the plan before any infrastructure apply.

## Remaining Work After Cutover

1. Observe the target for at least the 24-hour rollback window.
2. Enable automatic idle scale-down and verify the 300-second grace period.
3. Test reconnect behavior during cold start and task replacement.
4. Review the CloudWatch dashboard, WAF logs, ALB 5XX, and NAT/ALB/WAF cost.
5. Prepare a legacy destroy plan only after ownership and rollback approval.
6. Do not delete stopped EC2, EBS, old security groups, or legacy buckets
   without a separate approval.

## Architecture Boundary

The target is self-healing, not active-active HA. Maximum ECS capacity remains
one until the active-session registry moves to a shared store. A second NAT
Gateway and two-task service can be evaluated later when availability needs
justify their recurring cost.

Do not run `terraform destroy` as workshop cleanup. Resource deletion is a
separate, reviewed operation based on state ownership and cost evidence.
