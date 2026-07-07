---
title: "Nhật ký tuần 11"
date: 2026-06-26
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

# Nhật ký tuần 11

## 26/06/2026

### Công việc đã thực hiện

- Review lại phiên bản MVP của LiveCap sau khi đã tích hợp các thành phần chính.
- Kiểm tra các luồng chính của hệ thống: bắt đầu phiên, nhận caption, dịch nội dung, kết thúc phiên và export transcript.
- Ghi nhận các vấn đề cần cải thiện: độ ổn định WebSocket, xử lý lỗi, độ trễ realtime, microphone permission và trải nghiệm người dùng khi mất kết nối.

### Kết quả đạt được

- Xác định được các hạng mục cần tối ưu trước khi hoàn thiện demo.
- Có danh sách lỗi và cải tiến cần xử lý trong giai đoạn production-readiness.
- Nhóm thống nhất tập trung vào độ ổn định, bảo mật, monitoring và trải nghiệm người dùng thay vì thêm nhiều tính năng mới.

---

## 27/06/2026

### Công việc đã thực hiện

- Cải thiện cơ chế quản lý session trong backend.
- Bổ sung logic kiểm soát số lượng phiên đang hoạt động để tránh hệ thống bị sử dụng quá mức.
- Xem xét session timeout để giới hạn thời gian phiên và giảm rủi ro phát sinh chi phí không kiểm soát.
- Kiểm tra cách cleanup tài nguyên sau khi người dùng kết thúc hoặc mất kết nối phiên.

### Kết quả đạt được

- Backend quản lý caption session rõ ràng và an toàn hơn.
- Giảm rủi ro session bị treo hoặc tiếp tục chạy sau khi người dùng rời khỏi hệ thống.
- Hệ thống có nền tảng tốt hơn để kiểm soát tài nguyên và chi phí khi chạy trên AWS.

---

## 28/06/2026

### Công việc đã thực hiện

- Cải thiện trải nghiệm frontend khi kết nối realtime.
- Bổ sung các trạng thái: connecting, connected, reconnecting, error và microphone permission denied.
- Kiểm tra lại cách hiển thị caption và bản dịch để nội dung rõ ràng hơn trong quá trình sử dụng.
- Review lại flow người dùng theo các use case đã thiết kế ở giai đoạn phân tích hệ thống.

### Kết quả đạt được

- Giao diện phản hồi tốt hơn với các trạng thái thực tế của hệ thống.
- Người dùng dễ hiểu hơn khi hệ thống đang kết nối, mất kết nối hoặc gặp lỗi microphone.
- Các luồng chính trên giao diện bám sát hơn với tài liệu yêu cầu và UAT.

---

## 29/06/2026

### Công việc đã thực hiện

- Rà soát các cấu hình bảo mật cơ bản cho hệ thống.
- Kiểm tra lại IAM permission cho các dịch vụ: Transcribe, Translate, S3 và CloudWatch.
- Xem xét cấu hình CORS, security group, HTTPS/WSS và quyền truy cập vào S3 bucket.
- Thảo luận hướng bảo vệ hệ thống khi public demo: giới hạn truy cập, firewall và WAF ở mức định hướng.

### Kết quả đạt được

- Hệ thống có định hướng bảo mật rõ ràng hơn.
- Quyền truy cập AWS được rà soát theo hướng chỉ cấp quyền cần thiết.
- Nhóm hiểu rõ hơn tầm quan trọng của security khi triển khai ứng dụng realtime lên cloud.

---

## 30/06/2026

### Công việc đã thực hiện

- Tập trung vào monitoring và cost optimization cho hệ thống.
- Kiểm tra CloudWatch logs để theo dõi lỗi backend, trạng thái session và lỗi khi gọi AWS services.
- Xem xét chính sách lưu log và transcript để tránh lưu dữ liệu quá lâu.
- Thảo luận cách giảm chi phí khi hệ thống không có người dùng, đặc biệt với backend và các dịch vụ chạy liên tục.

### Kết quả đạt được

- Có cơ chế quan sát hệ thống rõ ràng hơn thông qua log.
- Nhóm xác định được các loại log quan trọng cần theo dõi khi demo và debug.
- Có định hướng tối ưu chi phí: kiểm soát session, giới hạn thời gian sử dụng và tránh để tài nguyên chạy không cần thiết.

---

## 01/07/2026

### Công việc đã thực hiện

- Thiết lập và kiểm tra các bước kiểm thử tự động cho project.
- Kiểm tra backend test, frontend build và các bước validate cấu hình hạ tầng.
- Thực hiện rà soát secret/configuration để tránh đưa thông tin nhạy cảm lên source code.
- Cập nhật tài liệu kỹ thuật liên quan đến testing, deployment và security notes.

### Kết quả đạt được

- Project có quy trình kiểm tra chất lượng rõ ràng hơn trước khi demo.
- Giảm rủi ro lỗi phát sinh do thay đổi code không được kiểm tra.
- Tài liệu kỹ thuật đầy đủ hơn về cách kiểm thử, build và triển khai hệ thống.

---

## 02/07/2026

### Công việc đã thực hiện

- Review toàn bộ hệ thống sau giai đoạn tối ưu trong tuần.
- Kiểm tra lại các thành phần chính: frontend, backend, WebSocket, Transcribe, Translate, S3, CloudWatch, IAM và deployment.
- Cập nhật issue list, test result, UAT checklist và các điểm cần hoàn thiện trước final submission.
- Chuẩn bị nội dung cho tuần cuối: báo cáo, tài liệu hệ thống, demo flow và tổng kết project.

### Kết quả đạt được

- LiveCap ổn định hơn so với bản prototype ban đầu.
- Các vấn đề quan trọng về session, error handling, monitoring, security và cost đã được xem xét.
- Nhóm sẵn sàng chuyển sang giai đoạn hoàn thiện tài liệu, demo và báo cáo cuối kỳ.

---

## Tổng kết tuần

Trong tuần này, nhóm tập trung cải thiện độ ổn định và khả năng vận hành của LiveCap. Sau khi MVP đã có các chức năng chính, nhóm ưu tiên xử lý các vấn đề quan trọng như session lifecycle, WebSocket reconnect, error handling, IAM permission, monitoring, logging và cost optimization, thay vì tiếp tục mở rộng tính năng. Em học được rằng một hệ thống chạy được chưa đủ để xem là hoàn chỉnh — khi triển khai trên cloud, cần kiểm tra thêm về bảo mật, khả năng phục hồi, khả năng quan sát lỗi và kiểm soát chi phí. Sau tuần này, LiveCap có nền tảng ổn định hơn để bước vào giai đoạn cuối: hoàn thiện tài liệu, kiểm thử UAT, chuẩn bị demo và tổng kết project.
