---
title: "Nhật ký tuần 2"
date: 2026-05-12
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

# Nhật ký tuần 2

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

  <!-- 24/04/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">24/04/2026 (Thứ Sáu)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Công việc đã làm</h5>
        <ul>
          <li>Tham gia họp nhóm đầu tiên để trao đổi về định hướng project Bootcamp.</li>
          <li>Thảo luận mục tiêu dự án, yêu cầu chương trình và tiêu chí đánh giá.</li>
          <li>Trao đổi về định hướng chuyên môn của từng thành viên (AI, Web, Security, System).</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Kết quả đạt được</h5>
        <ul>
          <li>Các thành viên hiểu rõ vai trò và định hướng cá nhân.</li>
          <li>Thống nhất bắt đầu giai đoạn khảo sát và lựa chọn ý tưởng dự án.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 25/04/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">25/04/2026 (Thứ Bảy)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Công việc đã làm</h5>
        <ul>
          <li>Đọc và nghiên cứu tài liệu FCAJ Project Guidelines.</li>
          <li>Tìm hiểu AWS Well-Architected Framework.</li>
          <li>Xem xét các yêu cầu về kiến trúc, bảo mật, hiệu năng và khả năng mở rộng của hệ thống cloud.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Kết quả đạt được</h5>
        <ul>
          <li>Nắm được các tiêu chí đánh giá dự án.</li>
          <li>Hiểu các nguyên tắc thiết kế hệ thống trên AWS.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 26/04/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">26/04/2026 (Chủ Nhật)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Công việc đã làm</h5>
        <ul>
          <li>Brainstorm các ý tưởng dự án tiềm năng.</li>
          <li>Đề xuất ý tưởng ứng dụng liên quan đến Crypto và dữ liệu thời gian thực.</li>
          <li>Thảo luận khả năng xây dựng hệ thống automation và nền tảng trung gian.</li>
          <li>Trao đổi về việc kết hợp AI vào web application.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Kết quả đạt được</h5>
        <ul>
          <li>Hình thành nhiều hướng triển khai khác nhau.</li>
          <li>Xác định các nhóm ý tưởng có tiềm năng phát triển thành project chính.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 27/04/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">27/04/2026 (Thứ Hai)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Công việc đã làm</h5>
        <ul>
          <li>Thảo luận các yêu cầu kỹ thuật cho dự án.</li>
          <li>Tìm hiểu khả năng áp dụng Real-time Data Processing.</li>
          <li>Trao đổi về cơ chế phân quyền, bảo mật hệ thống.</li>
          <li>Thảo luận các giải pháp hạn chế bot và DDoS.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Kết quả đạt được</h5>
        <ul>
          <li>Xác định các yêu cầu phi chức năng quan trọng cho hệ thống.</li>
          <li>Bắt đầu hình thành tư duy kiến trúc thay vì chỉ tập trung vào tính năng.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 28/04/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">28/04/2026 (Thứ Ba)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Công việc đã làm</h5>
        <ul>
          <li>Hoàn thành AWS Lab 1.</li>
          <li>Tìm hiểu chương trình AWS Free Tier 2025 và cơ chế cấp AWS Credit.</li>
          <li>Nghiên cứu sự khác biệt giữa Free Plan và Paid Plan trên AWS.</li>
          <li>Nghiên cứu các dịch vụ có nguy cơ phát sinh chi phí và các biện pháp kiểm soát ngân sách.</li>
          <li>Tìm hiểu các phương pháp monitoring và cost optimization trên AWS.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Kết quả đạt được</h5>
        <ul>
          <li>Hiểu cách sử dụng AWS Free Tier và AWS Credit hiệu quả.</li>
          <li>Nắm được các nguyên tắc cơ bản về quản lý chi phí trên nền tảng AWS.</li>
          <li>Nhận thức được các rủi ro thường gặp dẫn đến phát sinh chi phí ngoài ý muốn.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 29/04/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">29/04/2026 (Thứ Tư)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Công việc đã làm</h5>
        <ul>
          <li>Tìm hiểu quy trình Spec Driven Development.</li>
          <li>Làm quen với Kiro IDE và Kiro CI.</li>
          <li>Thực hành xây dựng prototype ứng dụng theo hướng tiếp cận của Kiro.</li>
          <li>Nghiên cứu cách AI hỗ trợ DevOps, Monitoring và Automation.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Kết quả đạt được</h5>
        <ul>
          <li>Hiểu quy trình xây dựng sản phẩm theo Spec Driven Development.</li>
          <li>Nắm được vai trò của Kiro trong phát triển và quản lý dự án.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 30/04/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">30/04/2026 (Thứ Năm)</h4>
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

</div>
