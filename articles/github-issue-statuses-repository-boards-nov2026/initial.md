# GitHub Issue Statuses và Repository Boards: trạng thái công việc cho coding agents

- **story_id:** `github-issue-statuses-repository-boards-nov2026`
- **update_id:** `initial`
- **Original event/publication date:** 2026-11-23
- **Digest date (Asia/Singapore):** 2026-11-24
- **Content created/updated (UTC):** 2026-11-24T00:04:18Z

## Tổng quan
Ngày 23/11/2026, GitHub đưa issue statuses và repository boards vào **public preview**, cho phép cả con người và agents theo dõi công việc ở cấp issue chi tiết hơn trạng thái open/closed.

## Điều gì mới
Bảy trạng thái: Backlog, Todo, In progress, In review, Done, Not planned, Duplicate. Gán issue cho agent tự chuyển sang In progress; liên kết draft PR chuyển sang In progress; PR mở hoặc chuyển draft sang ready for review đưa issue sang In review; gán người dùng chuyển sang Todo. GitHub Projects có thể đồng bộ trạng thái trùng tên. Repository saved views hỗ trợ board layout, grouping, drag-and-drop. Issue fields không còn bắt buộc gắn với issue types.

GitHub nêu rõ **GraphQL, REST API và MCP server** có thể đọc/đặt trạng thái và đặt trạng thái khi tạo issue. Trạng thái thay đổi còn có thể kích hoạt Copilot automations. Đây là tích hợp vào MCP server hiện có, **không phải thay đổi MCP protocol**.

## Ý nghĩa kỹ thuật cho AI/agent engineering
**Suy luận kỹ thuật:** Agent điều phối có thể sử dụng trạng thái issue làm tín hiệu để chọn tác vụ, theo dõi tiến độ và bàn giao review. Tuy nhiên trạng thái issue chỉ là tín hiệu workflow, không chứng minh tác vụ đã thực thi thành công. Khi nhiều agents cập nhật cùng issue cần tránh race conditions, kiểm tra trạng thái PR/CI thực tế và duy trì idempotency. Với automation có side effects, phải giữ approval và quyền truy cập riêng.

## Bằng chứng, giới hạn và availability
**Sự kiện đã xác nhận:** Changelog chính thức ngày 23/11 mô tả chức năng và trạng thái public preview. **Vendor claim:** các thao tác tự động cập nhật trạng thái như mô tả của GitHub. **Chưa có đánh giá độc lập:** không có số liệu benchmark task success, latency hoặc hiệu quả điều phối; không nên khẳng định giảm chi phí. Availability có thể thay đổi trong preview.

## Nguồn chính
- [GitHub Changelog, 23/11/2026](https://github.blog/changelog/2026-11-23-issue-statuses-and-repository-boards-are-in-public-preview/)
