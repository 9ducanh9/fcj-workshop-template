---
title: "Blog 2 - Attack Flow Logs"
date: 2026-07-05
weight: 2
chapter: false
pre: " <b> 3.2 </b> "
---

# Phân tích tính năng Attack Flow Logs trong AWS Shield Advanced

Gần đây tôi có đọc một bài viết trên AWS Security Blog giới thiệu về tính năng Attack Flow Logs của Shield Advanced. Trước đây, khi bị tấn công DDoS, quản trị viên thường chỉ biết "hệ thống đang bị tấn công" thông qua một vài metric chung chung trên CloudWatch, chứ không thể nhìn thấy chi tiết của từng luồng dữ liệu (traffic flow) — việc tái hiện lại cuộc tấn công đồng nghĩa với việc phải chắp vá dữ liệu từ nhiều nguồn khác nhau. Tính năng mới này đã lấp đầy điểm mù đó: nó ghi lại các thông tin thiết yếu của lưu lượng tấn công như IP nguồn/đích, port, protocol, và quốc gia ngay trong lúc sự cố đang diễn ra.

## Cách hoạt động

Ngay trong quá trình bị tấn công, Shield sẽ ghi lại metadata của từng luồng dữ liệu: IP nguồn/đích, port, protocol, các TCP flag, số lượng gói tin/byte — cùng với 3 trường đáng chú ý:

- **srccountry:** Quốc gia xuất phát của cuộc tấn công
- **location:** AWS edge location nơi lưu lượng đi vào mạng
- **action:** Cách Shield xử lý luồng dữ liệu đó — đây là bằng chứng giảm nhẹ (mitigation) cụ thể thay vì chỉ là phỏng đoán.

Logs được xuất ra theo chu kỳ 5 phút (cả trong và sau khi tấn công), mỗi file có dung lượng tối đa 75 MB, hỗ trợ các định dạng JSON / plain text / W3C / Parquet.

## Log được lưu trữ ở đâu?

Khi được tạo ra, log không tự động chạy về máy của bạn — chúng phải đi qua một "pipeline" gồm 3 thành phần cấu trúc:

- **DeliverySource** — Nơi gửi: khai báo "log này đến từ tài nguyên nào đang được Shield bảo vệ".
- **DeliveryDestination** — Nơi nhận: khai báo "log sẽ đi đến đâu" (S3, CloudWatch Logs, hoặc Firehose).
- **Delivery** — Người vận chuyển: kết nối nơi gửi và nơi nhận. Chỉ sau khi tạo thành phần này, log mới bắt đầu được truyền đi.

Việc chọn nơi lưu trữ phụ thuộc vào nhu cầu thực tế của bạn:

- **S3** → Lưu trữ dài hạn, có thể truy vấn bằng Athena để điều tra sau khi cuộc tấn công kết thúc.
- **CloudWatch Logs** → Quan sát nhanh ngay trong lúc cuộc tấn công đang diễn ra (sử dụng Logs Insights).
- **Data Firehose** → Stream log trực tiếp tới một giải pháp SIEM của bên thứ ba (ví dụ: Splunk, Elastic…).

Điểm thú vị của việc chia nhỏ thành 3 thành phần này là sự linh hoạt khi kết hợp chúng: nhiều Source có thể trỏ đến cùng một Destination, cho phép một tổ chức có nhiều AWS account có thể gom tất cả log DDoS về chung một bucket duy nhất (thông qua cấu hình cross-account).

## Hai hạn chế cần lưu ý trước khi sử dụng

- **Về phạm vi hỗ trợ:** Hiện tại tính năng này chỉ hỗ trợ các tài nguyên được bảo vệ thông qua Elastic IP. Các điểm vào web phổ biến như CloudFront hay ALB vẫn chưa được hỗ trợ. Nói cách khác, các hệ thống nằm sau CloudFront/ALB tạm thời chưa thể sử dụng tính năng này.
- **Về chi phí:** Bên cạnh phí đăng ký Shield Advanced, việc bật flow logs sẽ phát sinh thêm chi phí vended logs của CloudWatch Logs và chi phí cho các tài nguyên đích (lưu trữ S3/log group, hoặc xử lý bằng Firehose).

![Sơ đồ luồng hoạt động của attack flow logs](/images/3-BlogsPosted/blog2-1.png)
*(Lưu ý: Sơ đồ trên là sơ đồ luồng do tôi tự vẽ để minh họa luồng hoạt động, không phải là kiến trúc tham chiếu để triển khai)*

## Tóm lại

Attack Flow Logs không giúp Shield chặn tấn công tốt hơn — nhưng nó giải quyết bài toán cốt lõi là giúp bạn có thể nhìn thấy và chứng minh được cuộc tấn công.

**Nguồn tham khảo:** [Gain visibility into DDoS attacks with flow logs in AWS Shield Advanced](https://aws.amazon.com/blogs/security/gain-visibility-into-ddos-attacks-with-flow-logs-in-aws-shield-advanced/)
