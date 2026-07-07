---
title: "Nhật ký tuần 3"
date: 2026-05-01
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

# Nhật ký tuần 3

## 01/05/2026

### Công việc đã thực hiện


### Kết quả đạt được


---

## 02/05/2026

### Công việc đã thực hiện

- Thảo luận cách quản lý công việc bằng GitHub Projects (Kanban).
- Chuẩn bị nội dung proposal cho dự án.
- Đánh giá các ý tưởng theo tiêu chí tính thực tế, mức độ phù hợp với AWS và khả năng triển khai.
- Lên kế hoạch cho giai đoạn thiết kế kiến trúc hệ thống.

### Kết quả đạt được

- Xác định được các hướng dự án tiềm năng.
- Chuẩn bị cơ sở cho việc lựa chọn ý tưởng chính ở tuần tiếp theo.
- Bắt đầu xây dựng kế hoạch triển khai và phân chia công việc.

---

## 03/05/2026

### Công việc đã thực hiện

- Tìm hiểu các khái niệm cơ bản về AWS Networking: VPC, CIDR block, subnet, route table, Internet Gateway, NAT Gateway, Security Group, Network ACL và Site-to-Site VPN.
- Tạo VPC chính cho lab với mô hình public/private subnet.
- Cấu hình 2 public subnet và 2 private subnet trong nhiều Availability Zone.
- Tạo và attach Internet Gateway cho VPC chính.
- Tạo route table cho public subnet với route 0.0.0.0/0 → Internet Gateway.

### Kết quả đạt được

- Hiểu rõ cách thiết kế kiến trúc mạng cơ bản trên AWS với public subnet và private subnet.
- Hiểu vai trò của Internet Gateway, route table và Security Group trong việc kiểm soát traffic.
- Thiết lập thành công hạ tầng mạng cơ bản cho lab.

![Create VPC main](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/1-create-vpc-main.png)

*Thiết lập VPC chính 10.10.0.0/16*

![VPC created successfully](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/2-vpc-created-successfully.png)

*VPC VPC-Lab03-ASG tạo thành công*

![Public Subnet 1A](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/3-public-subnet-1a.png)

*Cấu hình Public-Subnet-1A*

![Public Subnet 1B](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/4-public-subnet-1b.png)

*Cấu hình Public-Subnet-1B*

![Private Subnet 1A](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/5-private-subnet-1a.png)

*Cấu hình Private-Subnet-1A*

![Private Subnet 1B](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/6-private-subnet-1b.png)

*Cấu hình Private-Subnet-1B*

![Subnets created list](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/7-subnets-list.png)

*Danh sách subnets tạo thành công*

![Create IGW](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/8-create-igw.png)

*Tạo Internet Gateway (IGW-Lab03)*

![Attach IGW](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/9-attach-igw.png)

*Attach Internet Gateway vào VPC*

![Create RT](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/10-create-route-table.png)

*Tạo Route Table cho Public Subnet*

![Public Subnet association](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/11-associate-subnet.png)

*Liên kết subnet vào Route Table*

![Edit routes IGW](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/12-add-route-igw.png)

*Thêm Route 0.0.0.0/0 qua IGW*

---

## 04/05/2026

### Công việc đã thực hiện

- Tạo security group cho public EC2 và private EC2.
- Launch EC2 public và EC2 private bằng Amazon Linux 2023.
- Kết nối vào EC2 public bằng MobaXterm thông qua SSH key.
- Kiểm tra kết nối Internet từ EC2 public bằng ping và curl.
- Upload key lên EC2 public và SSH từ EC2 public sang EC2 private bằng private IP.
- Tạo Elastic IP và NAT Gateway cho private subnet.
- Cấu hình private route table với route 0.0.0.0/0 → NAT Gateway.
- Kiểm tra private EC2 có thể truy cập Internet thông qua NAT Gateway.

### Kết quả đạt được

- Thiết lập thành công public EC2 có thể truy cập Internet.
- Thiết lập thành công private EC2 không có public IP nhưng vẫn có thể outbound Internet thông qua NAT Gateway.
- Thực hành thành công SSH flow theo mô hình bastion host: local machine → public EC2 → private EC2.

![Create SG Public](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/13-create-sg-public.png)

*Tạo Security Group cho Public EC2*

![Launch public EC2](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/14-launch-public-ec2.png)

*Launch EC2 Public (Amazon Linux 2023)*

![Network settings public EC2](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/15-network-settings-public.png)

*Cấu hình Network cho Public EC2*

![Public EC2 detailed info](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/16-public-ec2-details.png)

*Thông tin chi tiết Public EC2 đã chạy*

![MobaXterm setting SSH](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/17-ssh-mobaxterm.png)

*Cấu hình kết nối SSH trong MobaXterm*

![SSH terminal successful](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/18-ssh-terminal-public.png)

*Kết nối thành công vào Public EC2*

![Ping test from EC2](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/19-ping-curl-test.png)

*Kiểm tra Ping và Curl ra Internet*

![Create SG Private](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/20-create-sg-private.png)

*Tạo Security Group cho Private EC2*

![Launch private EC2](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/21-launch-private-ec2.png)

*Launch EC2 Private*

![Network settings private EC2](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/22-network-settings-private.png)

*Cấu hình Network cho Private EC2*

![EC2 Instance list status](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/23-ec2-instances-list.png)

*Trạng thái 2 EC2 hoạt động đồng thời*

![Allocate Elastic IP](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/24-allocate-eip.png)

*Cấu hình Elastic IP cho NAT Gateway*

![EIP allocated successful](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/25-eip-allocated.png)

*Elastic IP được cấp phát thành công*

![Create NAT Gateway](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/26-create-nat-gateway.png)

*Tạo NAT Gateway (NAT-Lab03)*

![Private Subnet RT Association](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/27-private-subnet-rt-association.png)

*Liên kết Subnet Private với Route Table*

![Edit routes for NAT Gateway](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/28-add-route-nat-gateway.png)

*Thêm Route 0.0.0.0/0 qua NAT Gateway*

---

## 05/05/2026

### Công việc đã thực hiện

- Tạo VPC-OnPrem để giả lập môi trường on-premises.
- Tạo public subnet, Internet Gateway và route table cho VPC-OnPrem.
- Launch EC2-CustomerGateway trong VPC-OnPrem.
- Gán Elastic IP cho EC2-CustomerGateway.
- Disable Source/Destination Check cho EC2-CustomerGateway để instance có thể đóng vai trò gateway/router.
- Tạo Virtual Private Gateway và attach vào VPC chính.
- Tạo Customer Gateway sử dụng Elastic IP của EC2-CustomerGateway.
- Tạo Site-to-Site VPN Connection giữa VGW và CGW.

### Kết quả đạt được

- Thiết lập thành công môi trường VPC-OnPrem để giả lập hệ thống on-premises.
- Tạo thành công kết nối Site-to-Site VPN giữa AWS VPC và VPC-OnPrem.

![Create VPC OnPrem](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/29-create-vpc-onprem.png)

*Tạo VPC-OnPrem 192.168.0.0/16*

![Create Subnet OnPrem](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/30-create-subnet-onprem.png)

*Tạo Subnet cho VPC-OnPrem*

![Route Table OnPrem](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/31-route-table-onprem.png)

*Cấu hình Route Table cho OnPrem*

![Create VGW](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/32-create-vgw.png)

*Tạo Virtual Private Gateway (VGW)*

![Create CGW](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/33-create-cgw.png)

*Tạo Customer Gateway (CGW-OnPrem)*

![VGW Routing configuration](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/34-vgw-routing-config.png)

*Cấu hình Route qua VGW trong VPC chính*

---

## 06/05/2026

### Công việc đã thực hiện

- Download VPN configuration từ AWS.
- Cài đặt Libreswan trên EC2-CustomerGateway để cấu hình IPSec VPN.
- Cấu hình /etc/ipsec.conf và /etc/ipsec.secrets dựa trên thông tin tunnel từ AWS.
- Bật IP forwarding trên EC2-CustomerGateway.
- Khởi động IPSec service và kiểm tra trạng thái tunnel.
- Debug lỗi IPSec do thuật toán modp1024 không được hỗ trợ, sau đó chuyển sang modp2048.
- Kiểm tra VPN tunnel bằng ipsec status và ipsec trafficstatus.
- Cấu hình route giữa VPC chính và VPC-OnPrem.
- Cập nhật Security Group để cho phép ICMP traffic giữa 2 CIDR 10.10.0.0/16 và 192.168.0.0/16.
- Debug lỗi ping một chiều bằng cách kiểm tra route, Security Group, IPSec policy và source IP.
- Kiểm tra thành công kết nối hai chiều giữa EC2 private trong VPC chính và EC2-CustomerGateway trong VPC-OnPrem.

### Kết quả đạt được

- VPN tunnel đạt trạng thái established và kết nối hai chiều giữa AWS private network và simulated on-premises network hoạt động thành công.
- Nắm được cách debug các lỗi thực tế trong AWS networking như mất key pair, SSH timeout, sai security group, thiếu route, lỗi IPSec algorithm, sai source IP.

![Download VPN config](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/35-download-vpn-config.png)

*Tải file cấu hình VPN từ AWS*

![Install Libreswan](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/36-install-libreswan.png)

*Cài đặt Libreswan trên OnPrem Gateway*

![Config ipsec.conf](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/37-config-ipsec-conf.png)

*Cấu hình IPSec bằng nano editor*

![IPSec connection established](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/38-ipsec-connection-established.png)

*Thiết lập thành công IPSec Tunnel*

![Ping EC2 to OnPrem](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/39-ping-ec2-to-onprem.png)

*Ping kiểm tra Private EC2 → OnPrem*

![Ping OnPrem to EC2](/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/40-ping-onprem-to-ec2.png)

*Ping kiểm tra OnPrem → Private EC2*

---

## 07/05/2026

### Công việc đã thực hiện

- Cleanup toàn bộ tài nguyên sau lab để tránh phát sinh chi phí: EC2, NAT Gateway, Elastic IP, VPN Connection, Virtual Private Gateway, Customer Gateway, Internet Gateway, subnet, route table, security group và VPC.
- Tìm hiểu Infrastructure as Code bằng AWS CloudFormation.
- Tạo CloudFormation YAML template đơn giản để deploy VPC tự động.
- Deploy stack bằng CloudFormation và kiểm tra resource được tạo tự động.
- Delete CloudFormation stack để kiểm tra cơ chế cleanup tự động.

### Kết quả đạt được

- Hiểu được cách CloudFormation dùng template YAML để tự động hóa việc tạo hạ tầng.
- Nhận thức rõ sự khác nhau giữa thao tác thủ công trên AWS Console và triển khai hạ tầng theo hướng Infrastructure as Code.
- Bảo đảm dọn dẹp sạch tài nguyên (cleanup) tránh phát sinh chi phí phát sinh ngoài ý muốn.

---

## Tổng kết tuần

Trong tuần này, em mở rộng các bài thực hành VPC bằng cách triển khai AWS Site-to-Site VPN với môi trường on-premises mô phỏng. Em cấu hình các thành phần VPN và IPSec tunnel, xử lý các lỗi routing và kết nối, kiểm tra giao tiếp hai chiều, cleanup tài nguyên sau lab và bước đầu tìm hiểu Infrastructure as Code với AWS CloudFormation.
