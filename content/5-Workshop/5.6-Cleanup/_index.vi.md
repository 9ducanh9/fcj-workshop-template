---
title: "An toàn release và phần việc còn lại"
date: 2026-07-05
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---

# An toàn release và phần việc còn lại

## Baseline đã hoàn thành

- Landing page và caption dashboard công khai qua CloudFront.
- Backend ECS Fargate sau ALB multi-AZ.
- Luồng WebSocket Transcribe/Translate song ngữ thật.
- Heartbeat, reconnect có giới hạn, timeout và abuse guard.
- Export TXT private, retention 14 ngày và không lưu raw audio.
- CloudWatch logging với retention 14 ngày.
- Terraform source cho remote state, target network, WAF, dashboard, budget,
  wake-on-demand, idle scaling và blue/green cutover.
- GitHub Actions validation và secret scanning.

## Quy trình thay đổi an toàn

1. Làm việc trên branch và chia frontend/backend/infra thành batch dễ review.
2. Chạy gate backend, frontend, Terraform và Gitleaks.
3. Review `git diff` rồi mở pull request.
4. Chỉ merge sau khi CI của PR và post-merge main đều pass.
5. Build image bằng immutable SHA tag.
6. Reconcile Terraform state và review plan trước mọi infrastructure apply.

## Phần còn lại sau cutover

1. Theo dõi target trong rollback window tối thiểu 24 giờ.
2. Bật automatic idle scale-down và xác minh grace period 300 giây.
3. Kiểm tra reconnect khi cold start và task replacement đang diễn ra.
4. Review CloudWatch dashboard, WAF logs, ALB 5XX và chi phí NAT/ALB/WAF.
5. Chỉ lập destroy plan legacy sau khi xác nhận ownership và rollback window.
6. Không xóa EC2 stopped, EBS, security group cũ hoặc bucket legacy nếu chưa có
   approval riêng.

## Ranh giới kiến trúc

Target là self-healing, chưa phải active-active HA. ECS max vẫn là một đến khi
active-session registry chuyển sang shared store. NAT Gateway thứ hai và service
hai task chỉ nên xét khi yêu cầu availability đủ để biện minh recurring cost.

Không chạy `terraform destroy` như một bước cleanup workshop. Xóa tài nguyên là
operation riêng, cần review theo state ownership và bằng chứng chi phí.
