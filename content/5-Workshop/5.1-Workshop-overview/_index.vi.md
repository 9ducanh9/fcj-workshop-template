---
title: "Tổng quan workshop"
date: 2026-07-05
weight: 1
chapter: false
pre: " <b> 5.1. </b> "
---

# Tổng quan workshop

## Vấn đề và mục tiêu

Rào cản ngôn ngữ và tốc độ nói nhanh khiến người tham gia khó theo dõi cuộc họp
song ngữ. LiveCap cung cấp phụ đề gần thời gian thực mà không cần tích hợp trực
tiếp với nền tảng họp và không lưu bản ghi microphone.

MVP đã triển khai có thể:

- thu âm từ trình duyệt dưới dạng PCM mono 16 kHz, 16-bit;
- stream audio qua WebSocket bảo mật;
- nhận dạng tiếng Việt và tiếng Anh bằng hai Transcribe stream song song;
- chỉ dịch segment đã finalized và chỉ thêm caption finalized vào giao diện;
- giữ caption finalized khi WebSocket reconnect có giới hạn;
- giới hạn session 30 phút và giới hạn abuse theo process; và
- export transcript song ngữ dạng TXT qua presigned URL của S3.

## Kiến trúc đang chạy đã xác minh

```mermaid
flowchart LR
  Browser["Trình duyệt"] -->|HTTPS và WSS| CF["Amazon CloudFront"]
  WAF["CloudFront WAF - BLOCK"] -.-> CF
  CF -->|OAC origin fetch| Frontend["S3 frontend private"]
  CF -->|/api/wake| Wake["Wake Lambda"]
  Wake -->|desired_count=1| ECS["Amazon ECS"]
  CF -->|/api/* và /ws/*| ALB["ALB public multi-AZ"]
  ALBWAF["ALB WAF - BLOCK"] -.-> ALB
  ALB -->|HTTPS origin, HTTP 8000 target| Task["Một ECS Fargate task private"]
  ECR["Amazon ECR - image immutable"] -.-> Task
  Task -->|PCM stream| Transcribe["Amazon Transcribe Streaming"]
  Task -->|finalized text| Translate["Amazon Translate"]
  Task -->|chỉ TXT export| Transcript["S3 transcript private"]
  Task -.->|log| CW["Amazon CloudWatch"]
```

Backend chạy tại `ap-southeast-1` trong custom VPC `10.20.0.0/16`. ALB trải
trên public subnet thuộc `ap-southeast-1a` và `ap-southeast-1b`; ECS task nằm ở
private subnet, không có public IP, và outbound qua một NAT Gateway tại `1a`.
ECS có thể thay task lỗi, nhưng đây không phải active-active; WebSocket đang
chạy sẽ mất khi task bị thay thế.

## Dịch vụ và trách nhiệm

| Dịch vụ | Vai trò trong LiveCap |
| --- | --- |
| CloudFront | Entry point HTTPS/WSS công khai và định tuyến theo path |
| AWS WAF | Block managed threats và rate abuse ở CloudFront và ALB |
| Lambda | Wake target ECS service từ 0 lên 1 trước khi capture |
| Amazon S3 | Origin frontend private và nơi lưu transcript TXT private |
| ALB | Health check và forward API/WebSocket đến port 8000 |
| ECS Fargate | Chạy backend FastAPI dạng container |
| Amazon ECR | Lưu backend image bằng tag immutable từ Git SHA |
| Amazon Transcribe | Chuyển PCM stream thành partial/final text |
| Amazon Translate | Dịch finalized text giữa tiếng Anh và tiếng Việt |
| CloudWatch | Nhận application log và metric dịch vụ AWS |
| GitHub Actions | Chạy CI kiểm tra, không tự deploy |

## Luồng runtime chính

1. CloudFront phục vụ frontend React/Vite từ S3 private qua OAC.
2. Người dùng bấm Start; frontend gọi `/api/wake` qua CloudFront OAC đến Lambda.
3. Frontend poll `/api/health`, rồi cấp quyền microphone và mở `/ws/transcribe`.
4. FastAPI kiểm tra giới hạn session toàn hệ thống và theo IP trước khi mở AWS stream.
5. PCM chunk chỉ được gửi khi WebSocket đang mở.
6. Transcribe trả partial/final text; chỉ finalized segment được dịch và thêm vào transcript.
7. Caption song ngữ trả về theo Fargate -> ALB -> CloudFront -> browser.
8. Export ghi object TXT vào S3 private và trả URL tải có thời hạn.

## Trạng thái sau cutover

Custom VPC, private Fargate, target ALB HTTPS, NAT Gateway, hai WAF BLOCK, wake
Lambda, CloudWatch dashboard và AWS Budget đã deploy. CloudFront đã route API
và WebSocket sang target stack. Controlled `0 -> 1` wake test đã pass; automatic
idle scale-down vẫn tắt trong rollback window. Legacy stack chưa bị xóa.

![Kiến trúc target đã dùng cho blue/green cutover](/images/3-Project/livecap-target-architecture.png)
