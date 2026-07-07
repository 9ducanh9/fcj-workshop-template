---
title: "Nhật ký tuần 7"
date: 2026-05-29
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

# Nhật ký tuần 7

## 29/05/2026

### Công việc đã thực hiện

- Tổng hợp lại các kiến thức đã tự học trong 6 tuần đầu về AWS services, cloud computing và các use case thực tế.
- Bắt đầu suy nghĩ về hướng final project có thể áp dụng các dịch vụ AWS đã học.
- Liệt kê một số vấn đề thực tế có thể giải quyết bằng cloud services.

### Kết quả đạt được

- Xác định được cần chọn một project có tính thực tế, có thể demo được và có sử dụng nhiều AWS services.
- Có định hướng chuyển từ giai đoạn tự học sang giai đoạn xây dựng project thực tế.
- Bắt đầu hình thành ý tưởng làm một ứng dụng hỗ trợ người dùng trong workshop/meeting.

---

## 30/05/2026

### Công việc đã thực hiện

- Brainstorm các ý tưởng project liên quan đến xử lý giọng nói, transcript, translation và hỗ trợ người học trong workshop.
- Phân tích các khó khăn thường gặp khi tham gia workshop kỹ thuật: khó theo dõi nội dung dài, khó ghi chú đầy đủ và rào cản ngôn ngữ.
- So sánh một số hướng project dựa trên tính khả thi, giá trị thực tế và khả năng áp dụng AWS services.

### Kết quả đạt được

- Xác định được problem statement ban đầu: người tham gia workshop/meeting có thể gặp khó khăn trong việc theo dõi, ghi nhớ và hiểu đầy đủ nội dung.
- Chọn được hướng project ban đầu là xây dựng một ứng dụng hỗ trợ realtime caption, translation và transcript.
- Có cơ sở để phát triển ý tưởng thành project LiveCap.

---

## 31/05/2026

### Công việc đã thực hiện

- Đặt tên và định hình concept ban đầu cho project **LiveCap**.
- Xác định mục tiêu chính của project: hỗ trợ người dùng hiểu nội dung workshop/meeting tốt hơn thông qua caption realtime và transcript.
- Viết nháp phần giới thiệu project, problem statement và expected outcome.

### Kết quả đạt được

- Hình thành concept chính của LiveCap.
- Xác định được target users gồm sinh viên, người tham gia workshop, người học technical content và người cần hỗ trợ theo dõi nội dung song ngữ.
- Có bản nháp đầu tiên cho phần mô tả project.

---

## 01/06/2026

### Công việc đã thực hiện

- Research các AWS services có thể sử dụng cho LiveCap.
- Tìm hiểu vai trò của **Amazon Transcribe Streaming** trong việc chuyển giọng nói thành văn bản theo thời gian thực.
- Tìm hiểu thêm về **Amazon Translate**, **Amazon S3** và **Amazon CloudWatch** trong bối cảnh project.

### Kết quả đạt được

- Xác định được các AWS services chính cho MVP: Amazon Transcribe Streaming cho speech-to-text realtime, Amazon Translate cho dịch nội dung giữa tiếng Việt và tiếng Anh, Amazon S3 để lưu transcript export và Amazon CloudWatch để theo dõi log cơ bản.
- Hiểu rõ hơn cách các dịch vụ AWS có thể kết hợp để tạo thành một solution hoàn chỉnh.

---

## 02/06/2026

### Công việc đã thực hiện

- Phác thảo user flow ban đầu của LiveCap.
- Xác định các bước chính của người dùng: mở ứng dụng, bắt đầu session, xem caption realtime, xem bản dịch và export transcript sau khi kết thúc.
- Làm rõ phạm vi MVP để tránh project bị mở rộng quá nhiều.

### Kết quả đạt được

- Hoàn thành user flow ban đầu cho LiveCap.
- Xác định được các tính năng cốt lõi của MVP: Start/Stop caption session, hiển thị realtime transcript, dịch nội dung song ngữ và export transcript sau session.
- Có định hướng rõ hơn cho giai đoạn thiết kế kiến trúc và implementation.

---

## 03/06/2026

### Công việc đã thực hiện

- Phác thảo kiến trúc high-level đầu tiên cho LiveCap.
- Xác định các thành phần chính gồm frontend, backend realtime, Amazon Transcribe Streaming, Amazon Translate, Amazon S3 và CloudWatch.
- Mô tả luồng dữ liệu từ microphone input đến caption/translation hiển thị trên giao diện.

### Kết quả đạt được

- Có bản kiến trúc tổng quan ban đầu cho project.
- Hiểu rõ hơn vai trò của backend WebSocket trong việc xử lý audio realtime.
- Xác định được runtime flow cơ bản: microphone input → frontend → backend → AWS Transcribe → Translate → frontend display → transcript storage.

---

## 04/06/2026

### Công việc đã thực hiện

- Review lại toàn bộ ý tưởng, user flow và kiến trúc ban đầu của LiveCap.
- Điều chỉnh phạm vi project để tập trung vào các chức năng quan trọng nhất.
- Chuẩn bị kế hoạch triển khai prototype trong các tuần tiếp theo.

### Kết quả đạt được

- Chốt được hướng đi chính cho project LiveCap.
- Hoàn thiện phạm vi MVP ở mức ban đầu.
- Xác định bước tiếp theo là bắt đầu triển khai backend/frontend prototype và kiểm thử luồng realtime caption.

---

## Tổng kết tuần

Trong tuần này, em bắt đầu chuyển từ giai đoạn tự học AWS sang giai đoạn xây dựng final project thực tế. Từ việc phân tích vấn đề thực tế của người dùng trong workshop — khó theo dõi nội dung dài, khó ghi chú và rào cản ngôn ngữ — em hình thành ý tưởng **LiveCap**, một ứng dụng hỗ trợ realtime caption, translation và transcript export. Em học được rằng một project tốt nên bắt đầu từ vấn đề của người dùng, sau đó mới lựa chọn AWS services phù hợp. Sau tuần này, project đã có problem statement, user flow, phạm vi MVP và kiến trúc high-level ban đầu — đủ nền tảng để bắt đầu triển khai prototype trong các tuần tiếp theo.
