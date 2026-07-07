---
title: "Nhật ký tuần 5"
date: 2026-05-15
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

# Nhật ký tuần 5

## 15/05/2026

### Công việc đã thực hiện

- Bắt đầu học sâu hơn về các dịch vụ lưu trữ trên AWS.
- Tìm hiểu về Amazon S3, bucket, object, storage class và các khái niệm liên quan đến object storage.
- Đọc thêm tài liệu và blog để hiểu các use case phổ biến của S3 như lưu file tĩnh, backup, log và dữ liệu đầu ra của ứng dụng.

### Kết quả đạt được

- Hiểu được Amazon S3 là dịch vụ object storage dùng để lưu trữ dữ liệu dạng file/object.
- Nắm được khái niệm bucket, object key và storage class.
- Biết một số trường hợp sử dụng phổ biến của S3 trong hệ thống cloud.

---

## 16/05/2026

### Công việc đã thực hiện

- Tìm hiểu thêm về quyền truy cập và bảo mật dữ liệu trên Amazon S3.
- Học về bucket policy, access control, public access block và encryption.
- Ghi chú các rủi ro khi cấu hình bucket public không đúng cách.

### Kết quả đạt được

- Hiểu rõ hơn tầm quan trọng của việc bảo mật dữ liệu trên S3.
- Biết rằng không nên public bucket nếu không có nhu cầu rõ ràng.
- Nắm được các cơ chế cơ bản để kiểm soát quyền truy cập và mã hóa dữ liệu lưu trữ.

---

## 17/05/2026

### Công việc đã thực hiện

- Tìm hiểu về Amazon CloudFront và khái niệm Content Delivery Network.
- Đọc tài liệu/blog để hiểu cách CloudFront phân phối nội dung thông qua edge locations.
- So sánh việc truy cập trực tiếp vào S3 với việc phân phối nội dung qua CloudFront.

### Kết quả đạt được

- Hiểu CloudFront giúp tăng tốc độ truy cập nội dung thông qua CDN.
- Biết rằng CloudFront thường được dùng để phân phối static website, assets, video hoặc file download.
- Hiểu sơ bộ cách CloudFront kết hợp với S3 để phục vụ frontend hoặc nội dung tĩnh.

---

## 18/05/2026

### Công việc đã thực hiện

- Học về các khái niệm networking cơ bản trong AWS.
- Tìm hiểu về VPC, subnet, route table, internet gateway và security group.
- Ghi chú lại vai trò của từng thành phần trong việc kết nối và bảo vệ tài nguyên cloud.

### Kết quả đạt được

- Hiểu VPC là mạng riêng ảo dùng để triển khai tài nguyên AWS.
- Phân biệt được subnet public và subnet private ở mức cơ bản.
- Biết security group hoạt động như firewall ở cấp tài nguyên.

---

## 19/05/2026

### Công việc đã thực hiện

- Tiếp tục học về AWS networking và luồng truy cập vào hệ thống.
- Tìm hiểu khái niệm inbound rule, outbound rule, routing và kết nối từ internet vào tài nguyên AWS.
- Đọc thêm các ví dụ về cách triển khai ứng dụng web trên cloud.

### Kết quả đạt được

- Hiểu rõ hơn cách traffic đi vào và đi ra khỏi tài nguyên trong AWS.
- Biết rằng việc mở port cần được kiểm soát cẩn thận để giảm rủi ro bảo mật.
- Có kiến thức nền để hiểu các kiến trúc triển khai web application trên AWS.

---

## 20/05/2026

### Công việc đã thực hiện

- Tìm hiểu về Amazon CloudWatch và vai trò của monitoring trong hệ thống cloud.
- Học các khái niệm log, metric, alarm và dashboard.
- Đọc thêm các bài viết về việc theo dõi tài nguyên, phát hiện lỗi và kiểm soát vận hành hệ thống.

### Kết quả đạt được

- Hiểu CloudWatch giúp theo dõi tình trạng hoạt động của hệ thống.
- Biết rằng log và metric rất quan trọng để debug, kiểm tra hiệu năng và phát hiện lỗi.
- Nắm được vai trò của monitoring trong vận hành hệ thống thực tế.

---

## 21/05/2026

### Công việc đã thực hiện

- Review lại các nội dung đã học trong tuần về S3, CloudFront, networking và CloudWatch.
- Tổng hợp ghi chú thành các nhóm: storage, content delivery, network security và monitoring.
- Cập nhật worklog và tài liệu học tập cá nhân.

### Kết quả đạt được

- Hệ thống hóa được kiến thức về các dịch vụ AWS nền tảng.
- Hiểu cách storage, CDN, networking và monitoring có thể liên kết với nhau trong một hệ thống web.
- Chuẩn bị được nền tảng tốt hơn để học tiếp các dịch vụ AI/ML và architecture trong tuần sau.

---

## Tổng kết tuần

Trong tuần này, em tập trung học các dịch vụ AWS nền tảng phục vụ cho việc lưu trữ, phân phối nội dung, mạng và giám sát hệ thống. Em học được cách Amazon S3 được sử dụng để lưu trữ object, cách CloudFront hỗ trợ phân phối nội dung nhanh hơn, cách VPC và security group giúp kiểm soát mạng, cũng như cách CloudWatch hỗ trợ monitoring và logging. Sau tuần này, em hiểu rõ hơn rằng một hệ thống cloud thực tế không chỉ có phần ứng dụng, mà còn cần storage, networking, security và monitoring — đây là những kiến thức quan trọng để sau này có thể thiết kế và triển khai một ứng dụng hoàn chỉnh trên AWS.
