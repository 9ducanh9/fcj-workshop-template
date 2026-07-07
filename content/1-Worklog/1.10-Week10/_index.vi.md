---
title: "Nhật ký tuần 10"
date: 2026-06-19
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

# Nhật ký tuần 10

## 19/06/2026

### Công việc đã thực hiện

- Tiếp tục hoàn thiện prototype LiveCap sau tuần trước.
- Cải thiện luồng xử lý caption và translation trên frontend.
- Kiểm tra lại cách hiển thị transcript để nội dung dễ đọc hơn trong quá trình sử dụng realtime.
- Thành viên Hệ thống thông tin review lại giao diện theo các use case chính đã thiết kế.

### Kết quả đạt được

- Giao diện hiển thị caption và bản dịch rõ ràng hơn.
- User flow của hệ thống ổn định hơn so với phiên bản prototype ban đầu.
- Các chức năng chính tiếp tục bám sát phạm vi MVP đã xác định.

---

## 20/06/2026

### Công việc đã thực hiện

- Xây dựng chức năng export transcript sau khi phiên kết thúc.
- Thiết kế format transcript gồm timestamp, speaker, nội dung gốc và bản dịch.
- Kiểm tra cách lưu trữ transcript để có thể tải về hoặc lưu lên Amazon S3.
- Thành viên Hệ thống thông tin cập nhật mô hình dữ liệu liên quan đến session, transcript segment, speaker và translation.

### Kết quả đạt được

- Có chức năng export transcript ở mức ban đầu.
- Format transcript rõ ràng hơn và phù hợp với mục tiêu hỗ trợ người dùng xem lại nội dung workshop/meeting.
- Mô hình dữ liệu được cập nhật sát hơn với chức năng thực tế của hệ thống.

---

## 21/06/2026

### Công việc đã thực hiện

- Tích hợp lưu trữ transcript với Amazon S3.
- Kiểm tra quyền truy cập cần thiết để backend có thể ghi file transcript vào S3.
- Thảo luận cách đặt tên file, tổ chức dữ liệu theo session và kiểm soát quyền truy cập.
- Thành viên Mạng kiểm tra các cấu hình IAM liên quan đến S3, Transcribe, Translate và CloudWatch.

### Kết quả đạt được

- Xác định được cách lưu transcript export lên Amazon S3.
- Hiểu rõ hơn vai trò của IAM trong việc cấp quyền cho backend truy cập các AWS services.
- Bổ sung được yêu cầu bảo mật dữ liệu transcript trong tài liệu hệ thống.

---

## 22/06/2026

### Công việc đã thực hiện

- Chuẩn bị triển khai thử backend FastAPI lên môi trường cloud.
- Thành viên Mạng cấu hình EC2, security group, port, domain/reverse proxy ở mức thử nghiệm.
- Kiểm tra kết nối giữa frontend và backend thông qua HTTPS/WSS.
- Ghi nhận các vấn đề kỹ thuật liên quan đến WebSocket Secure, CORS và firewall.

### Kết quả đạt được

- Có môi trường triển khai thử cho backend.
- Nhóm hiểu rõ hơn các vấn đề khi đưa ứng dụng realtime từ local lên cloud.
- Xác định được HTTPS/WSS là yêu cầu quan trọng để frontend có thể giao tiếp an toàn với backend.

---

## 23/06/2026

### Công việc đã thực hiện

- Cấu hình logging và monitoring cơ bản bằng Amazon CloudWatch.
- Theo dõi log của backend, lỗi kết nối, lỗi AWS service và trạng thái xử lý session.
- Xác định các loại log cần quan sát trong quá trình demo: start session, stop session, transcript received, translation completed và export completed.
- Thành viên Hệ thống thông tin liên kết các log này với KPI đã xác định trước đó.

### Kết quả đạt được

- Hệ thống có logging cơ bản để phục vụ debug và monitoring.
- Nhóm có thể quan sát tốt hơn các lỗi phát sinh trong quá trình chạy thử.
- KPI như độ trễ, tỷ lệ lỗi và trạng thái phiên có cơ sở để theo dõi rõ hơn.

---

## 24/06/2026

### Công việc đã thực hiện

- Thực hiện kiểm thử end-to-end cho các luồng chính của LiveCap.
- Kiểm thử luồng người dùng: mở ứng dụng → cấp quyền microphone → bắt đầu phiên → nhận caption → nhận bản dịch → kết thúc phiên → export transcript.
- Ghi nhận các lỗi về microphone permission, mất kết nối WebSocket, độ trễ caption và trạng thái loading/error.
- Cập nhật test case và tài liệu UAT dựa trên kết quả kiểm thử.

### Kết quả đạt được

- Xác định được các lỗi quan trọng cần xử lý trước khi hoàn thiện demo.
- Bộ test case/UAT đầy đủ hơn cho các chức năng chính.
- Nhóm hiểu rõ hơn cách đánh giá hệ thống theo trải nghiệm người dùng thực tế, không chỉ theo việc code chạy được.

---

## 25/06/2026

### Công việc đã thực hiện

- Review toàn bộ tiến độ triển khai trong tuần.
- Tổng hợp các phần đã hoàn thành: frontend, backend, WebSocket, Transcribe, Translate, S3 export, CloudWatch logging và deployment thử.
- Ghi nhận các điểm cần cải thiện trong tuần tiếp theo: tối ưu độ trễ, xử lý reconnect, cải thiện UI, kiểm soát chi phí và hoàn thiện documentation.
- Cập nhật báo cáo hệ thống: architecture, data flow, test result, issue list và kế hoạch hoàn thiện.

### Kết quả đạt được

- LiveCap đã có phiên bản prototype có thể kiểm thử theo luồng end-to-end.
- Các thành phần chính của MVP đã được tích hợp ở mức cơ bản.
- Nhóm xác định được các hạng mục cần tối ưu trước khi chuẩn bị final demo và submission.

---

## Tổng kết tuần

Trong tuần này, nhóm tập trung hoàn thiện các chức năng chính của LiveCap và đưa hệ thống từ prototype local sang giai đoạn tích hợp và triển khai thử trên cloud. Các công việc quan trọng bao gồm xây dựng export transcript, lưu transcript lên Amazon S3, cấu hình IAM, triển khai backend thử nghiệm, thiết lập HTTPS/WSS, cấu hình CloudWatch logging và kiểm thử end-to-end. Em học được rằng triển khai hệ thống cloud không chỉ là viết code, mà còn bao gồm quyền truy cập IAM, bảo mật kết nối, cấu hình mạng, logging, monitoring, xử lý lỗi và kiểm thử thực tế. Sau tuần này, LiveCap đã có phiên bản MVP tích hợp đầy đủ các thành phần chính — frontend, backend, Amazon Transcribe Streaming, Amazon Translate, Amazon S3 và Amazon CloudWatch — làm nền tảng để tối ưu, kiểm thử và hoàn thiện tài liệu ở các tuần cuối.
