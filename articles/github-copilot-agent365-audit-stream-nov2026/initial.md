# GitHub Copilot activity streaming vào Microsoft Agent 365

- **story_id:** `github-copilot-agent365-audit-stream-nov2026`
- **update_id:** `initial`
- **Ngày công bố gốc:** 2026-11-17
- **Ngày digest (Asia/Singapore):** 2026-11-18
- **Tạo/cập nhật nội dung (UTC):** 2026-11-18T00:36:53Z
- **Loại:** enterprise

## Tổng quan
Enterprise Managed Users trên GitHub Enterprise Cloud có thể stream Copilot agent activity sang Microsoft Agent 365 để quan sát sessions, prompts, responses, tool calls và risk signals.

## Sự kiện và điểm mới
Theo [thông báo chính thức của GitHub](https://github.blog/changelog/2026-11-17-monitor-github-copilot-activity-through-microsoft-agent-365/), Nguồn bao gồm GitHub cloud agent, CLI, VS Code, Visual Studio và partner IDEs; dữ liệu kết hợp Microsoft Purview và Defender phục vụ audit và investigation.

## Chi tiết kỹ thuật và giới hạn triển khai
Nguồn bao gồm GitHub cloud agent, CLI, VS Code, Visual Studio và partner IDEs; dữ liệu kết hợp Microsoft Purview và Defender phục vụ audit và investigation. Đây là mô tả tính năng hoặc kết quả do nhà cung cấp công bố, không mặc định chứng minh năng lực vận hành trong mọi môi trường. Việc sử dụng thực tế cần kiểm tra quyền truy cập, trạng thái preview/GA, cấu hình agent harness và khả năng đo lường.

## Ý nghĩa thực tiễn cho AI/agent engineering
**Phân tích và khuyến nghị của tác giả:** Đưa observability multi-agent vào enterprise control plane; cần RBAC, data retention, privacy controls, SIEM correlation và incident response playbooks.

## Bằng chứng, độ tin cậy và tính khả dụng
**Sự kiện được xác minh:** GitHub công bố ngày 17/11/2026 tại URL gốc bên dưới. **Tuyên bố của nhà cung cấp / giới hạn:** Giới hạn ở GHEC Enterprise Managed Users; chưa có SLA, coverage guarantee hay benchmark detection efficacy trong thông báo. **Đánh giá độc lập:** chưa được xác minh trong lần nghiên cứu này; không coi vendor claims là independent evaluation.

## Nguồn chính
- [GitHub Changelog — GitHub Copilot activity streaming vào Microsoft Agent 365](https://github.blog/changelog/2026-11-17-monitor-github-copilot-activity-through-microsoft-agent-365/)
