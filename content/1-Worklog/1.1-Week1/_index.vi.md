---
title: "Nhật ký tuần 1"
date: 2026-05-12
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---

# Nhật ký tuần 1

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
</style>

<div class="worklog-timeline">

  <!-- 17/04/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">17/04/2026 (Thứ Sáu)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Công việc đã làm</h5>
        <ul>
          <li>Tham gia lễ khai mạc chương trình thực tập First Cloud AI Journey (FCAJ).</li>
          <li>Tìm hiểu tổng quan về lộ trình Bootcamp, yêu cầu dự án và các hoạt động trong chương trình.</li>
          <li>Hoàn tất các bước xác nhận tài khoản và truy cập các nền tảng học tập.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Kết quả đạt được</h5>
        <ul>
          <li>Nắm được mục tiêu chương trình và kế hoạch học tập.</li>
          <li>Sẵn sàng tham gia các hoạt động trong Bootcamp.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 18/04/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">18/04/2026 (Thứ Bảy)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Công việc đã làm</h5>
        <ul>
          <li>Truy cập và làm quen với AWS Management Console.</li>
          <li>Khám phá giao diện AWS và các dịch vụ phổ biến.</li>
          <li>Tìm hiểu cấu trúc tài khoản AWS và cơ chế quản lý tài nguyên trên Cloud.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Kết quả đạt được</h5>
        <ul>
          <li>Hiểu cách điều hướng trong AWS Console.</li>
          <li>Nắm được vị trí và chức năng cơ bản của các dịch vụ AWS.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 19/04/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">19/04/2026 (Chủ Nhật)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Công việc đã làm</h5>
        <ul>
          <li>Tiếp tục khám phá các chức năng cơ bản trong giao diện AWS.</li>
          <li>Tìm hiểu Dashboard, Billing, Region và các thành phần quản trị tài khoản.</li>
          <li>Thực hành các thao tác quản lý cơ bản trên AWS Console.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Kết quả đạt được</h5>
        <ul>
          <li>Thành thạo hơn trong việc sử dụng giao diện AWS.</li>
          <li>Hiểu các thành phần quan trọng phục vụ quá trình học tập và triển khai dự án.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 20/04/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">20/04/2026 (Thứ Hai)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Công việc đã làm</h5>
        <ul>
          <li>Thiết lập môi trường làm việc phục vụ Bootcamp.</li>
          <li>Cài đặt và cấu hình các công cụ phát triển cần thiết.</li>
          <li>Chuẩn bị môi trường cho dự án cá nhân.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Kết quả đạt được</h5>
        <ul>
          <li>Hoàn thiện môi trường làm việc ban đầu.</li>
          <li>Sẵn sàng cho các bài lab và hoạt động thực hành tiếp theo.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 21/04/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">21/04/2026 (Thứ Ba)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Công việc đã làm</h5>
        <ul>
          <li>Thực hiện các nhiệm vụ cơ bản trong chương trình AWS để nhận AWS Credit.</li>
          <li>Hoàn thành các bài tập và yêu cầu onboarding ban đầu.</li>
          <li>Kiểm tra trạng thái tài khoản AWS sau khi hoàn thành nhiệm vụ.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Kết quả đạt được</h5>
        <ul>
          <li>Hoàn thành 5 nhiệm vụ cơ bản theo yêu cầu chương trình.</li>
          <li>Đủ điều kiện nhận 100 USD AWS Credit phục vụ học tập và phát triển dự án.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 22/04/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">22/04/2026 (Thứ Tư)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Công việc đã làm</h5>
        <ul>
          <li>Tìm hiểu phương pháp Spec Driven Development.</li>
          <li>Nghiên cứu quy trình phát triển phần mềm dựa trên đặc tả yêu cầu.</li>
          <li>Tìm hiểu Kiro IDE và Kiro CI, vai trò của AI trong hỗ trợ phát triển phần mềm.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Kết quả đạt được</h5>
        <ul>
          <li>Hiểu quy trình phát triển dự án theo hướng Spec Driven Development.</li>
          <li>Nắm được các tính năng chính của Kiro IDE và Kiro CI.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 23/04/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">23/04/2026 (Thứ Năm)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Công việc đã làm</h5>
        <ul>
          <li>Thử nghiệm các tutorial được cung cấp trong chương trình.</li>
          <li>Thực hành các thao tác cơ bản trên AWS theo hướng dẫn.</li>
          <li>Kiểm tra khả năng sử dụng môi trường đã thiết lập.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Kết quả đạt được</h5>
        <ul>
          <li>Hoàn thành các bài tutorial cơ bản.</li>
          <li>Củng cố kiến thức về AWS Console và quy trình thực hành trên Cloud.</li>
          <li>Sẵn sàng bước sang giai đoạn học tập và triển khai dự án ở tuần tiếp theo.</li>
        </ul>
      </div>
    </div>
  </div>

</div>
