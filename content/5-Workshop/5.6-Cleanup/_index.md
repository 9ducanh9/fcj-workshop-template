---
title: "Cleanup"
date: 2026-05-12
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---

# Cleanup

Clean up resources after testing to avoid unnecessary AWS charges.

## Cleanup Order

1. Stop active LiveCap sessions in the browser.
2. Stop the backend service:

```bash
sudo systemctl stop livecap
sudo systemctl disable livecap
```

3. Remove Nginx configuration if the instance will not be reused:

```bash
sudo rm /etc/nginx/conf.d/livecap.conf
sudo systemctl reload nginx
```

4. Delete CloudFront distribution after disabling it.
5. Delete frontend files from the S3 frontend bucket.
6. Delete transcript objects from the S3 transcript bucket.
7. Delete both S3 buckets if no longer needed.
8. Terminate the EC2 instance.
9. Delete the EC2 IAM role and custom policies.
10. Delete CloudWatch log groups created for LiveCap if logs are no longer needed.

## Verification

- CloudFront distribution no longer exists or is disabled.
- S3 buckets are empty or deleted.
- EC2 instance is terminated.
- IAM role is removed.
- CloudWatch log group is deleted if retention is not required.

