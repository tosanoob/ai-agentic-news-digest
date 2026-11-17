# VS Code 1.146 bổ sung agent Inbox và experimental model comparisons

- **story_id:** `vscode-copilot-1-146-agent-inbox-model-comparison-nov2026`
- **update_id:** `initial`
- **Original event/publication date:** 2026-11-16
- **Digest date (Asia/Singapore):** 2026-11-17
- **Content created (UTC):** 2026-11-17T00:40:52Z
- **Content updated (UTC):** 2026-11-17T00:40:52Z
- **Type:** Initial event

## Tổng quan
GitHub công bố bản tổng hợp Copilot Weekly Releases ngày 16/11, bao gồm các tính năng mới trong **VS Code 1.146** dành cho quản lý nhiều agent sessions và đánh giá model. Ngày 16/11 là ngày bản tổng hợp; không mặc định là ngày từng feature được phát hành lần đầu.

## Điều gì mới
**Theo GitHub:** Inbox mode trong Agents window gom sessions từ nhiều workspaces và ưu tiên những phiên cần người dùng xử lý, hỗ trợ dismiss, hold và snooze; hiện **experimental**. Với Compare Models, khi bật setting và agent tools, agent có thể tìm models khả dụng, chạy comparisons và đọc kết quả để tóm tắt; cũng **experimental**. Chat có thể tách thành cửa sổ riêng (**preview**). Tích hợp extensions trong Agents window đang experimental.

GitHub còn thông báo **Local harness sẽ bị loại bỏ vào tháng 02/2027**; Copilot harness là mặc định cho phiên mới. Các cập nhật Fable 5.2, Gemini 4 Carbon và GHES trong cùng weekly roundup đã được lưu ở digest trước, không phải sự kiện mới của mục này.

## Chi tiết kỹ thuật
Agent Inbox là lớp attention management cho nhiều sessions, không phải một hệ thống bảo đảm durable execution. Compare Models hỗ trợ workflow đánh giá nhưng thông báo không nêu dataset, sampling, judge calibration hay thống kê variance; không thể suy ra model ranking đáng tin cậy chỉ từ việc có công cụ so sánh.

## Ý nghĩa thực tiễn
Với multi-agent coding, Inbox giúp phân loại human approvals và blocked sessions, giảm context switching. Model comparisons có thể được kết hợp với test suites có ground truth và cost tracking để tạo routing policy. Việc deprecate Local harness đòi hỏi audit các cấu hình hoặc custom workflows trước 02/2027.

## Evidence limitations
Đây là release notes do GitHub công bố, không có benchmark độc lập về giảm thời gian hoặc tăng task success. Các tính năng experimental/preview có thể thay đổi hoặc chưa có cho mọi người dùng. Không suy diễn Local harness đã bị gỡ ngay ngày 16/11.

## Nguồn
- [GitHub Changelog, 16/11/2026 — Copilot weekly releases](https://github.blog/changelog/2026-11-16-github-copilot-weekly-releases-november-9/)
