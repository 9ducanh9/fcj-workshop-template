---
title: "Week 3 Worklog"
date: 2026-05-12
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

# Week 3 Worklog

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

  <!-- 01/05/2026 -->
  <div class="day-card" style="border-left: 4px solid #e2e8f0;">
    <div class="day-header" style="background: linear-gradient(135deg, #4a5568 0%, #2d3748 100%);">
      <div class="day-icon"><i class="fas fa-umbrella-beach"></i></div>
      <h4 class="day-title">01/05/2026 (Friday)</h4>
    </div>
    <div class="day-body" style="grid-template-columns: 1fr; padding: 25px;">
      <div style="background: #f7fafc; padding: 20px; border-radius: 8px; text-align: center; border: 1px dashed #cbd5e0;">
        <h5 style="color: #4a5568 !important; margin: 0 0 8px 0 !important; font-weight: bold;"><i class="fas fa-glass-cheers"></i> International Workers' Day Holiday (30/04 - 01/05)</h5>
        <p style="margin: 0; color: #718096; font-size: 0.95rem;">No learning or project activities carried out during the public holidays.</p>
      </div>
    </div>
  </div>

  <!-- 02/05/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">02/05/2026 (Saturday)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Work Completed</h5>
        <ul>
          <li>Discussed task management using GitHub Projects (Kanban).</li>
          <li>Prepared proposal content for the project.</li>
          <li>Evaluated ideas based on feasibility, AWS compatibility, and implementation capability.</li>
          <li>Planned the phase for system architecture design.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Results Achieved</h5>
        <ul>
          <li>Identified potential project directions.</li>
          <li>Prepared the foundation for selecting the main idea next week.</li>
          <li>Began building the deployment plan and task division.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 03/05/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">03/05/2026 (Sunday)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Work Completed</h5>
        <ul>
          <li>Studied fundamental concepts of AWS Networking: VPC, CIDR block, subnet, route table, Internet Gateway, NAT Gateway, Security Group, Network ACL, and Site-to-Site VPN.</li>
          <li>Created the main VPC for the lab using the public/private subnet pattern.</li>
          <li>Configured 2 public subnets and 2 private subnets across multiple Availability Zones.</li>
          <li>Created and attached an Internet Gateway to the main VPC.</li>
          <li>Created a route table for the public subnets with a route for 0.0.0.0/0 &rarr; Internet Gateway.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Results Achieved</h5>
        <ul>
          <li>Understood how to design a basic network architecture on AWS with public and private subnets.</li>
          <li>Understood the roles of Internet Gateway, route tables, and Security Groups in controlling traffic.</li>
          <li>Successfully set up the baseline network infrastructure for the lab.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 04/05/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">04/05/2026 (Monday)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Work Completed</h5>
        <ul>
          <li>Created security groups for the public and private EC2 instances.</li>
          <li>Launched public and private EC2 instances using Amazon Linux 2023.</li>
          <li>Connected to the public EC2 instance via MobaXterm using the SSH key.</li>
          <li>Tested Internet connectivity from the public EC2 instance using ping and curl.</li>
          <li>Uploaded the key to the public EC2 and SSHed from the public EC2 to the private EC2 via private IP.</li>
          <li>Created an Elastic IP and NAT Gateway for the private subnets.</li>
          <li>Configured the private route table with a route of 0.0.0.0/0 &rarr; NAT Gateway.</li>
          <li>Verified that the private EC2 could access the Internet through the NAT Gateway.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Results Achieved</h5>
        <ul>
          <li>Successfully configured the public EC2 to access the Internet.</li>
          <li>Successfully configured the private EC2 to connect outbound to the Internet through the NAT Gateway without having a public IP.</li>
          <li>Successfully practiced the SSH flow using a bastion host model: local machine &rarr; public EC2 &rarr; private EC2.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 05/05/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">05/05/2026 (Tuesday)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Work Completed</h5>
        <ul>
          <li>Created a VPC-OnPrem to simulate an on-premises environment.</li>
          <li>Created a public subnet, Internet Gateway, and route table for the VPC-OnPrem.</li>
          <li>Launched an EC2-CustomerGateway instance in the VPC-OnPrem.</li>
          <li>Assigned an Elastic IP to the EC2-CustomerGateway.</li>
          <li>Disabled Source/Destination Check on the EC2-CustomerGateway to allow it to function as a gateway/router.</li>
          <li>Created a Virtual Private Gateway and attached it to the main VPC.</li>
          <li>Created a Customer Gateway using the Elastic IP of the EC2-CustomerGateway.</li>
          <li>Created a Site-to-Site VPN Connection between the VGW and CGW.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Results Achieved</h5>
        <ul>
          <li>Successfully set up a VPC-OnPrem environment to simulate an on-premises network.</li>
          <li>Successfully initiated a Site-to-Site VPN connection between AWS VPC and the VPC-OnPrem.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 06/05/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">06/05/2026 (Wednesday)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Work Completed</h5>
        <ul>
          <li>Downloaded the VPN configuration from AWS.</li>
          <li>Installed Libreswan on the EC2-CustomerGateway to configure the IPSec VPN.</li>
          <li>Configured /etc/ipsec.conf and /etc/ipsec.secrets based on the tunnel details from AWS.</li>
          <li>Enabled IP forwarding on the EC2-CustomerGateway.</li>
          <li>Started the IPSec service and checked the tunnel status.</li>
          <li>Debugged an IPSec issue where the modp1024 algorithm was unsupported, shifting to modp2048.</li>
          <li>Checked the VPN tunnel using ipsec status and ipsec trafficstatus.</li>
          <li>Configured routing between the main VPC and VPC-OnPrem.</li>
          <li>Updated the Security Group to allow ICMP traffic between CIDRs 10.10.0.0/16 and 192.168.0.0/16.</li>
          <li>Debugged a one-way ping issue by checking routes, Security Groups, IPSec policies, and source IPs.</li>
          <li>Successfully verified bi-directional connectivity between the private EC2 in the main VPC and the EC2-CustomerGateway in VPC-OnPrem.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Results Achieved</h5>
        <ul>
          <li>The VPN tunnel reached the established state and bi-directional routing between AWS private network and simulated on-premises network was successful.</li>
          <li>Learned to debug real-world AWS networking issues like missing key pairs, SSH timeouts, incorrect security groups, missing routes, IPSec algorithm mismatches, and incorrect source IPs.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 07/05/2026 -->
  <div class="day-card">
    <div class="day-header">
      <div class="day-icon"><i class="fas fa-calendar-day"></i></div>
      <h4 class="day-title">07/05/2026 (Thursday)</h4>
    </div>
    <div class="day-body">
      <div class="section-work">
        <h5><i class="fas fa-tasks"></i> Work Completed</h5>
        <ul>
          <li>Cleaned up all resources after the lab to avoid charges: EC2 instances, NAT Gateway, Elastic IPs, VPN Connection, Virtual Private Gateway, Customer Gateway, Internet Gateways, subnets, route tables, security groups, and VPCs.</li>
          <li>Studied Infrastructure as Code (IaC) using AWS CloudFormation.</li>
          <li>Created a simple CloudFormation YAML template to deploy a VPC automatically.</li>
          <li>Deployed the stack using CloudFormation and verified auto-created resources.</li>
          <li>Deleted the CloudFormation stack to verify the automated cleanup process.</li>
        </ul>
      </div>
      <div class="section-result">
        <h5><i class="fas fa-trophy"></i> Results Achieved</h5>
        <ul>
          <li>Understood how CloudFormation uses YAML templates to automate infrastructure deployment.</li>
          <li>Recognized the distinction between manual console actions and deploying resources through Infrastructure as Code.</li>
          <li>Ensured complete resource cleanup to prevent unexpected billing.</li>
        </ul>
      </div>
    </div>
  </div>

</div>
