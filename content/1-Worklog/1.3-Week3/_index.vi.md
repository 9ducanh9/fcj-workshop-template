---
title: "Nhật ký tuần 3"
date: 2026-05-12
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

# Nhật ký tuần 3

<style>
.worklog-timeline {
  display: flex;
  flex-direction: column;
  gap: 24px;
  margin: 30px 0;
}

.day-card {
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  border: 1px solid #eef2f5;
  transition: all 0.3s ease;
  overflow: hidden;
}

.day-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
  border-color: #4881cd;
}

.day-header {
  background: linear-gradient(135deg, #283e5b 0%, #1c222a 100%);
  color: #ffffff;
  padding: 14px 20px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.day-icon {
  background: rgba(255, 255, 255, 0.2);
  width: 32px;
  height: 32px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.95rem;
}

.day-title {
  font-size: 1.1rem;
  font-weight: 600;
  letter-spacing: 0.5px;
  color: #ffffff !important;
  margin: 0 !important;
}

.day-body {
  padding: 20px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

@media (max-width: 768px) {
  .day-body {
    grid-template-columns: 1fr;
    gap: 15px;
  }
}

.section-work, .section-result {
  background: #f8fafc;
  padding: 16px;
  border-radius: 8px;
  border-left: 4px solid #4881cd;
  height: 100%;
}

.section-result {
  border-left-color: #fd9827;
  background: #fffcf8;
}

.section-work h5, .section-result h5 {
  margin-top: 0 !important;
  margin-bottom: 12px !important;
  font-size: 0.95rem !important;
  font-weight: bold !important;
  display: flex;
  align-items: center;
  gap: 8px;
}

.section-work h5 {
  color: #283e5b !important;
}

.section-result h5 {
  color: #d97706 !important;
}

.day-body ul {
  margin: 0 !important;
  padding-left: 20px !important;
}

.day-body li {
  margin-bottom: 8px !important;
  font-size: 0.9rem !important;
  line-height: 1.6 !important;
  color: #4a5568 !important;
  list-style-type: disc !important;
}

.day-body li:last-child {
  margin-bottom: 0 !important;
}

/* Styles for Screenshot Gallery */
.card-screenshots {
  display: flex;
  gap: 12px;
  margin-top: 16px;
  grid-column: span 2;
  overflow-x: auto;
  padding: 8px 4px;
}

@media (max-width: 768px) {
  .card-screenshots {
    grid-column: span 1;
  }
}

.screenshot-item {
  flex: 0 0 220px;
  border: 1px solid #eef2f5;
  border-radius: 8px;
  overflow: hidden;
  background: #ffffff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  display: flex;
  flex-direction: column;
  transition: all 0.2s ease;
}

.screenshot-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  border-color: #4881cd;
}

.screenshot-item img {
  width: 100%;
  height: 130px;
  object-fit: cover;
  border-bottom: 1px solid #eef2f5;
  cursor: zoom-in;
}

.screenshot-item span {
  padding: 8px;
  font-size: 0.75rem;
  color: #4a5568;
  text-align: center;
  font-weight: 500;
  line-height: 1.4;
  background: #fafbfe;
}

/* Lightbox Modal CSS */
.lightbox-modal {
  display: none;
  position: fixed;
  z-index: 9999;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(15, 23, 42, 0.9);
  backdrop-filter: blur(8px);
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.lightbox-modal.show {
  display: flex;
  opacity: 1;
}

.lightbox-content {
  max-width: 90%;
  max-height: 80%;
  border-radius: 12px;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
  transform: scale(0.95);
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  border: 4px solid rgba(255, 255, 255, 0.1);
}

.lightbox-modal.show .lightbox-content {
  transform: scale(1);
}

.lightbox-close {
  position: absolute;
  top: 25px;
  right: 35px;
  color: #ffffff;
  font-size: 35px;
  font-weight: 300;
  cursor: pointer;
  width: 44px;
  height: 44px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.lightbox-close:hover {
  background: rgba(255, 255, 255, 0.25);
  color: #fd9827;
  transform: rotate(90deg);
}

.lightbox-caption {
  position: absolute;
  bottom: 30px;
  color: #ffffff;
  font-size: 0.95rem;
  font-weight: 500;
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(4px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 10px 24px;
  border-radius: 30px;
  text-align: center;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
  letter-spacing: 0.5px;
}

</style>

<div class="worklog-timeline">

  <!-- 01/05/2026 -->
  <div class="day-card" style="border-left: 4px solid #e2e8f0;">
    <div class="day-header" style="background: linear-gradient(135deg, #4a5568 0%, #2d3748 100%);">
      <div class="day-icon"><i class="fas fa-umbrella-beach"></i></div>
      <h4 class="day-title">01/05/2026 (Thứ Sáu)</h4>
    </div>
    <div class="day-body" style="grid-template-columns: 1fr; padding: 25px;">
      <div style="background: #f7fafc; padding: 20px; border-radius: 8px; text-align: center; border: 1px dashed #cbd5e0;">
        <h5 style="color: #4a5568 !important; margin: 0 0 8px 0 !important; font-weight: bold;"><i class="fas fa-glass-cheers"></i> Nghỉ Lễ Quốc Tế Lao Động (30/04 - 01/05)</h5>
        <p style="margin: 0; color: #718096; font-size: 0.95rem;">Không phát sinh hoạt động học tập và dự án trong kỳ nghỉ lễ.</p>
      </div>
    </div>
  </div>

  <!-- 02/05/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">02/05/2026 (Thứ Bảy)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Công việc đã làm</h5>
        <ul>
          <li>Thảo luận cách quản lý công việc bằng GitHub Projects (Kanban).</li>
          <li>Chuẩn bị nội dung proposal cho dự án.</li>
          <li>Đánh giá các ý tưởng theo tiêu chí tính thực tế, mức độ phù hợp với AWS và khả năng triển khai.</li>
          <li>Lên kế hoạch cho giai đoạn thiết kế kiến trúc hệ thống.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Kết quả đạt được</h5>
        <ul>
          <li>Xác định được các hướng dự án tiềm năng.</li>
          <li>Chuẩn bị cơ sở cho việc lựa chọn ý tưởng chính ở tuần tiếp theo.</li>
          <li>Bắt đầu xây dựng kế hoạch triển khai và phân chia công việc.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 03/05/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">03/05/2026 (Chủ Nhật)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Công việc đã làm</h5>
        <ul>
          <li>Tìm hiểu các khái niệm cơ bản về AWS Networking: VPC, CIDR block, subnet, route table, Internet Gateway, NAT Gateway, Security Group, Network ACL và Site-to-Site VPN.</li>
          <li>Tạo VPC chính cho lab với mô hình public/private subnet.</li>
          <li>Cấu hình 2 public subnet và 2 private subnet trong nhiều Availability Zone.</li>
          <li>Tạo và attach Internet Gateway cho VPC chính.</li>
          <li>Tạo route table cho public subnet với route 0.0.0.0/0 &rarr; Internet Gateway.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Kết quả đạt được</h5>
        <ul>
          <li>Hiểu rõ cách thiết kế kiến trúc mạng cơ bản trên AWS với public subnet và private subnet.</li>
          <li>Hiểu vai trò của Internet Gateway, route table và Security Group trong việc kiểm soát traffic.</li>
          <li>Thiết lập thành công hạ tầng mạng cơ bản cho lab.</li>
        </ul>
      </div>
      <!-- Screenshots -->
      <div class="card-screenshots">
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/1-create-vpc-main.png" alt="Create VPC main" />
          <span>Thiết lập VPC chính 10.10.0.0/16</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/2-vpc-created-successfully.png" alt="VPC created successfully" />
          <span>VPC VPC-Lab03-ASG tạo thành công</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/3-public-subnet-1a.png" alt="Public Subnet 1A" />
          <span>Cấu hình Public-Subnet-1A</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/4-public-subnet-1b.png" alt="Public Subnet 1B" />
          <span>Cấu hình Public-Subnet-1B</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/5-private-subnet-1a.png" alt="Private Subnet 1A" />
          <span>Cấu hình Private-Subnet-1A</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/6-private-subnet-1b.png" alt="Private Subnet 1B" />
          <span>Cấu hình Private-Subnet-1B</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/7-subnets-list.png" alt="Subnets created list" />
          <span>Danh sách subnets tạo thành công</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/8-create-igw.png" alt="Create IGW" />
          <span>Tạo Internet Gateway (IGW-Lab03)</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/9-attach-igw.png" alt="Attach IGW" />
          <span>Attach Internet Gateway vào VPC</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/10-create-route-table.png" alt="Create RT" />
          <span>Tạo Route Table cho Public Subnet</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/11-associate-subnet.png" alt="Public Subnet association" />
          <span>Liên kết subnet vào Route Table</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/12-add-route-igw.png" alt="Edit routes IGW" />
          <span>Thêm Route 0.0.0.0/0 qua IGW</span>
        </div>
      </div>
    </div>
  </div>

  <!-- 04/05/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">04/05/2026 (Thứ Hai)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Công việc đã làm</h5>
        <ul>
          <li>Tạo security group cho public EC2 và private EC2.</li>
          <li>Launch EC2 public và EC2 private bằng Amazon Linux 2023.</li>
          <li>Kết nối vào EC2 public bằng MobaXterm thông qua SSH key.</li>
          <li>Kiểm tra kết nối Internet từ EC2 public bằng ping và curl.</li>
          <li>Upload key lên EC2 public và SSH từ EC2 public sang EC2 private bằng private IP.</li>
          <li>Tạo Elastic IP và NAT Gateway cho private subnet.</li>
          <li>Cấu hình private route table với route 0.0.0.0/0 &rarr; NAT Gateway.</li>
          <li>Kiểm tra private EC2 có thể truy cập Internet thông qua NAT Gateway.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Kết quả đạt được</h5>
        <ul>
          <li>Thiết lập thành công public EC2 có thể truy cập Internet.</li>
          <li>Thiết lập thành công private EC2 không có public IP nhưng vẫn có thể outbound Internet thông qua NAT Gateway.</li>
          <li>Thực hành thành công SSH flow theo mô hình bastion host: local machine &rarr; public EC2 &rarr; private EC2.</li>
        </ul>
      </div>
      <!-- Screenshots -->
      <div class="card-screenshots">
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/13-create-sg-public.png" alt="Create SG Public" />
          <span>Tạo Security Group cho Public EC2</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/14-launch-public-ec2.png" alt="Launch public EC2" />
          <span>Launch EC2 Public (Amazon Linux 2023)</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/15-network-settings-public.png" alt="Network settings public EC2" />
          <span>Cấu hình Network cho Public EC2</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/16-public-ec2-details.png" alt="Public EC2 detailed info" />
          <span>Thông tin chi tiết Public EC2 đã chạy</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/17-ssh-mobaxterm.png" alt="MobaXterm setting SSH" />
          <span>Cấu hình kết nối SSH trong MobaXterm</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/18-ssh-terminal-public.png" alt="SSH terminal successful" />
          <span>Kết nối thành công vào Public EC2</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/19-ping-curl-test.png" alt="Ping test from EC2" />
          <span>Kiểm tra Ping và Curl ra Internet</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/20-create-sg-private.png" alt="Create SG Private" />
          <span>Tạo Security Group cho Private EC2</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/21-launch-private-ec2.png" alt="Launch private EC2" />
          <span>Launch EC2 Private</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/22-network-settings-private.png" alt="Network settings private EC2" />
          <span>Cấu hình Network cho Private EC2</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/23-ec2-instances-list.png" alt="EC2 Instance list status" />
          <span>Trạng thái 2 EC2 hoạt động đồng thời</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/24-allocate-eip.png" alt="Allocate Elastic IP" />
          <span>Cấu hình Elastic IP cho NAT Gateway</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/25-eip-allocated.png" alt="EIP allocated successful" />
          <span>Elastic IP được cấp phát thành công</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/26-create-nat-gateway.png" alt="Create NAT Gateway" />
          <span>Tạo NAT Gateway (NAT-Lab03)</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/27-private-subnet-rt-association.png" alt="Private Subnet RT Association" />
          <span>Liên kết Subnet Private với Route Table</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/28-add-route-nat-gateway.png" alt="Edit routes for NAT Gateway" />
          <span>Thêm Route 0.0.0.0/0 qua NAT Gateway</span>
        </div>
      </div>
    </div>
  </div>

  <!-- 05/05/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">05/05/2026 (Thứ Ba)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Công việc đã làm</h5>
        <ul>
          <li>Tạo VPC-OnPrem để giả lập môi trường on-premises.</li>
          <li>Tạo public subnet, Internet Gateway và route table cho VPC-OnPrem.</li>
          <li>Launch EC2-CustomerGateway trong VPC-OnPrem.</li>
          <li>Gán Elastic IP cho EC2-CustomerGateway.</li>
          <li>Disable Source/Destination Check cho EC2-CustomerGateway để instance có thể đóng vai trò gateway/router.</li>
          <li>Tạo Virtual Private Gateway và attach vào VPC chính.</li>
          <li>Tạo Customer Gateway sử dụng Elastic IP của EC2-CustomerGateway.</li>
          <li>Tạo Site-to-Site VPN Connection giữa VGW và CGW.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Kết quả đạt được</h5>
        <ul>
          <li>Thiết lập thành công môi trường VPC-OnPrem để giả lập hệ thống on-premises.</li>
          <li>Tạo thành công kết nối Site-to-Site VPN giữa AWS VPC và VPC-OnPrem.</li>
        </ul>
      </div>
      <!-- Screenshots -->
      <div class="card-screenshots">
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/29-create-vpc-onprem.png" alt="Create VPC OnPrem" />
          <span>Tạo VPC-OnPrem 192.168.0.0/16</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/30-create-subnet-onprem.png" alt="Create Subnet OnPrem" />
          <span>Tạo Subnet cho VPC-OnPrem</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/31-route-table-onprem.png" alt="Route Table OnPrem" />
          <span>Cấu hình Route Table cho OnPrem</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/32-create-vgw.png" alt="Create VGW" />
          <span>Tạo Virtual Private Gateway (VGW)</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/33-create-cgw.png" alt="Create CGW" />
          <span>Tạo Customer Gateway (CGW-OnPrem)</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/34-vgw-routing-config.png" alt="VGW Routing configuration" />
          <span>Cấu hình Route qua VGW trong VPC chính</span>
        </div>
      </div>
    </div>
  </div>

  <!-- 06/05/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">06/05/2026 (Thứ Tư)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Công việc đã làm</h5>
        <ul>
          <li>Download VPN configuration từ AWS.</li>
          <li>Cài đặt Libreswan trên EC2-CustomerGateway để cấu hình IPSec VPN.</li>
          <li>Cấu hình /etc/ipsec.conf và /etc/ipsec.secrets dựa trên thông tin tunnel từ AWS.</li>
          <li>Bật IP forwarding trên EC2-CustomerGateway.</li>
          <li>Khởi động IPSec service và kiểm tra trạng thái tunnel.</li>
          <li>Debug lỗi IPSec do thuật toán modp1024 không được hỗ trợ, sau đó chuyển sang modp2048.</li>
          <li>Kiểm tra VPN tunnel bằng ipsec status và ipsec trafficstatus.</li>
          <li>Cấu hình route giữa VPC chính và VPC-OnPrem.</li>
          <li>Cập nhật Security Group để cho phép ICMP traffic giữa 2 CIDR 10.10.0.0/16 và 192.168.0.0/16.</li>
          <li>Debug lỗi ping một chiều bằng cách kiểm tra route, Security Group, IPSec policy và source IP.</li>
          <li>Kiểm tra thành công kết nối hai chiều giữa EC2 private trong VPC chính và EC2-CustomerGateway trong VPC-OnPrem.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Kết quả đạt được</h5>
        <ul>
          <li>VPN tunnel đạt trạng thái established và kết nối hai chiều giữa AWS private network và simulated on-premises network hoạt động thành công.</li>
          <li>Nắm được cách debug các lỗi thực tế trong AWS networking như mất key pair, SSH timeout, sai security group, thiếu route, lỗi IPSec algorithm, sai source IP.</li>
        </ul>
      </div>
      <!-- Screenshots -->
      <div class="card-screenshots">
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/35-download-vpn-config.png" alt="Download VPN config" />
          <span>Tải file cấu hình VPN từ AWS</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/36-install-libreswan.png" alt="Install Libreswan" />
          <span>Cài đặt Libreswan trên OnPrem Gateway</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/37-config-ipsec-conf.png" alt="Config ipsec.conf" />
          <span>Cấu hình IPSec bằng nano editor</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/38-ipsec-connection-established.png" alt="IPSec connection established" />
          <span>Thiết lập thành công IPSec Tunnel</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/39-ping-ec2-to-onprem.png" alt="Ping EC2 to OnPrem" />
          <span>Ping kiểm tra Private EC2 &rarr; OnPrem</span>
        </div>
        <div class="screenshot-item">
          <img src="/images/1-Worklog/Lab3%20-B%E1%BA%AFt%20%C4%91%E1%BA%A7u%20v%E1%BB%9Bi%20Amazon%20Virtual%20Private%20Cloud%20(VPC)%20v%C3%A0%20AWS%20Site-to-Site%20VPN/40-ping-onprem-to-ec2.png" alt="Ping OnPrem to EC2" />
          <span>Ping kiểm tra OnPrem &rarr; Private EC2</span>
        </div>
      </div>
    </div>
  </div>

  <!-- 07/05/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">07/05/2026 (Thứ Năm)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Công việc đã làm</h5>
        <ul>
          <li>Cleanup toàn bộ tài nguyên sau lab để tránh phát sinh chi phí: EC2, NAT Gateway, Elastic IP, VPN Connection, Virtual Private Gateway, Customer Gateway, Internet Gateway, subnet, route table, security group và VPC.</li>
          <li>Tìm hiểu Infrastructure as Code bằng AWS CloudFormation.</li>
          <li>Tạo CloudFormation YAML template đơn giản để deploy VPC tự động.</li>
          <li>Deploy stack bằng CloudFormation và kiểm tra resource được tạo tự động.</li>
          <li>Delete CloudFormation stack để kiểm tra cơ chế cleanup tự động.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Kết quả đạt được</h5>
        <ul>
          <li>Hiểu được cách CloudFormation dùng template YAML để tự động hóa việc tạo hạ tầng.</li>
          <li>Nhận thức rõ sự khác nhau giữa thao tác thủ công trên AWS Console và triển khai hạ tầng theo hướng Infrastructure as Code.</li>
          <li>Bảo đảm dọn dẹp sạch tài nguyên (cleanup) tránh phát sinh chi phí phát sinh ngoài ý muốn.</li>
        </ul>
      </div>
    </div>
  </div>

</div>


<!-- Lightbox Modal DOM -->
<div id="lightbox" class="lightbox-modal">
  <span class="lightbox-close">&times;</span>
  <img class="lightbox-content" id="lightbox-img" src="" alt="" />
  <div class="lightbox-caption" id="lightbox-caption"></div>
</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
  const lightbox = document.getElementById("lightbox");
  const lightboxImg = document.getElementById("lightbox-img");
  const lightboxCaption = document.getElementById("lightbox-caption");
  const closeBtn = document.querySelector(".lightbox-close");

  document.querySelectorAll(".screenshot-item img").forEach(img => {
    img.addEventListener("click", function() {
      lightboxImg.src = this.src;
      lightboxCaption.textContent = this.nextElementSibling ? this.nextElementSibling.textContent : "";
      lightbox.classList.add("show");
    });
  });

  closeBtn.addEventListener("click", function() {
    lightbox.classList.remove("show");
  });

  lightbox.addEventListener("click", function(e) {
    if (e.target === lightbox || e.target === closeBtn) {
      lightbox.classList.remove("show");
    }
  });

  // Close with Esc key
  document.addEventListener("keydown", function(e) {
    if (e.key === "Escape" && lightbox.classList.contains("show")) {
      lightbox.classList.remove("show");
    }
  });
});
</script>
