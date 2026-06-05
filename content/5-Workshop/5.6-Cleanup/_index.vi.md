---
title: "Cleanup"
date: 2026-05-12
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---

# Cleanup

Dọn tài nguyên sau khi test để tránh phát sinh chi phí AWS không cần thiết.

## Thứ tự cleanup

1. Stop các LiveCap session đang chạy trong browser.
2. Stop backend service:

```bash
sudo systemctl stop livecap
sudo systemctl disable livecap
```

3. Xóa Nginx configuration nếu không dùng lại instance:

```bash
sudo rm /etc/nginx/conf.d/livecap.conf
sudo systemctl reload nginx
```

4. Disable rồi xóa CloudFront distribution.
5. Xóa frontend files trong S3 frontend bucket.
6. Xóa transcript objects trong S3 transcript bucket.
7. Xóa hai S3 bucket nếu không còn cần.
8. Terminate EC2 instance.
9. Xóa EC2 IAM role và custom policies.
10. Xóa CloudWatch log groups của LiveCap nếu không cần giữ logs.

## Kiểm tra

- CloudFront distribution không còn tồn tại hoặc đã disabled.
- S3 buckets đã rỗng hoặc đã bị xóa.
- EC2 instance đã terminated.
- IAM role đã được xóa.
- CloudWatch log group đã bị xóa nếu không cần retention.

