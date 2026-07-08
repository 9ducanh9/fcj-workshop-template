---
title: "Security, Observability, Testing, and Cost"
date: 2026-07-05
weight: 5
chapter: false
pre: " <b> 5.5. </b> "
---

# Security, Observability, Testing, and Cost

## Security Controls Already Implemented

- IAM roles replace static AWS credentials in containers and source code.
- Frontend and transcript S3 buckets are private; frontend access uses OAC.
- Transcript downloads use expiring presigned URLs.
- Raw audio is not stored; transcript objects expire after 14 days.
- CORS restricts the accepted frontend origin.
- Global/per-IP session limits and a 30-minute timeout reduce abuse exposure.
- Gitleaks runs in CI, while tfstate, tfvars, plans, and real `.env` files remain untracked.
- ECR images use immutable SHA-derived tags and scanning results are reviewed.

## WAF and Network Status

Two Web ACLs are deployed: CloudFront (`CLOUDFRONT`) and ALB (`REGIONAL`).
Managed and rate-based rules are in BLOCK mode; production XSS and Log4J probes
returned HTTP 403. The ALB accepts traffic only from the CloudFront
origin-facing managed prefix list.

The dedicated VPC `10.20.0.0/16` has two public and two private subnets across
two AZs. The ALB uses public subnets while Fargate tasks use private subnets
without public IPs. One NAT Gateway in `1a` is the cost-sensitive, single-AZ
outbound tradeoff.

## Observability

- FastAPI emits structured session and integration logs to CloudWatch when the
  handler is available, with stdout fallback.
- Backend log retention is 14 days.
- ALB, ECS, and Lambda expose standard CloudWatch metrics.
- A dashboard for ECS CPU/memory, ALB traffic/health, wake Lambda, and WAF is
  defined in target Terraform without enabling paid Container Insights.

The CloudWatch dashboard, WAF logging, Budget, and 14-day retention are now
applied. Container Insights remains disabled to avoid extra cost.

## CI and Verification

GitHub Actions validates every pull request and main push:

1. Gitleaks secret scan with full Git history.
2. Python 3.11 backend compile and pytest.
3. Node 20 frontend install, tests, and production build.
4. Terraform 1.10.5 format and validation with `-backend=false`.

CI deliberately performs no production deployment, Terraform apply, destroy,
or state migration.

## Cost Controls

- Transcribe and Translate are usage-based and run mainly during active sessions.
- Session duration/concurrency limits bound accidental AI usage.
- Transcript and log retention are both 14 days.
- A configurable `$50/month` AWS Budget exists in target Terraform; alerts are
  delayed billing signals, not real-time enforcement.
- Wake Lambda passed a controlled `0 -> 1` test. Automatic idle scale-down
  remains disabled until the rollback window and grace-period test complete.

ALB, NAT Gateway, and WAF have fixed or baseline charges while provisioned.
Scaling ECS to zero does not remove those costs.

## Residual Risks

- One NAT Gateway creates a single-AZ outbound dependency.
- One in-memory session registry prevents safe multi-task scaling.
- One active task means replacement interrupts live WebSocket sessions.
- The legacy stack remains during the rollback window and temporarily adds cost.
- ECR base-image package findings remain tracked until compatible fixes exist.
