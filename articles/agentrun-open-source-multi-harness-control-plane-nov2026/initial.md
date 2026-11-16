# AgentRun mở mã nguồn control plane cho Claude Code, Codex, Pi và OpenCode

- **story_id:** `agentrun-open-source-multi-harness-control-plane-nov2026`
- **update_id:** `initial`
- **Ngày sự kiện:** 2026-11-12
- **Ngày digest:** 2026-11-16 (Asia/Singapore)
- **Created/updated UTC:** 2026-11-16T00:21:16Z
- **Loại bằng chứng:** source chính thức của dự án; các đánh giá kỹ thuật được ghi rõ là suy luận

## Tổng quan
AgentRun là lớp quản lý runs và learning đặt bên ngoài coding harness; mã nguồn công khai theo Apache-2.0. Thông tin ra mắt open-source được ghi nhận ngày 12/11, đây là mục BACKFILL.

## Điều gì mới và chi tiết kỹ thuật
Theo [repository gốc](https://github.com/Parcha-ai/agentrun) và [tài liệu nhà phát triển](https://agentrun.ai/), nền tảng cung cấp API thống nhất cho Pi, Claude Code, Codex và OpenCode. Control plane quản lý revisions, logs, human approvals, chi phí và durable execution. Compute được tách khỏi agent loop, với tùy chọn Docker, Daytona hoặc Modal. Sau một run, lớp self-learning đề xuất notes, skills, workflows, kiểm tra và chấm điểm trước khi tái sử dụng; đây không phải cập nhật trọng số model. [Tài liệu learning](https://agentrun.ai/platform/self-improving) giải thích quy trình Reflect → Validate → Grade.

## Ý nghĩa kỹ thuật
Suy luận: AgentRun có thể giảm lock-in vào một harness và tạo điểm tích hợp cho checkpoint, resume, approval và ngân sách; thích hợp nghiên cứu agent workflows chạy dài ngày. Cần kiểm tra tính nhất quán khi tool có side effects, cô lập credentials và chất lượng skills tự sinh trước khi cho chạy production.

## Evidence, availability và giới hạn
Các tính năng là mô tả của tác giả, chưa phải đánh giá độc lập về tỷ lệ phục hồi, giảm token hoặc task success. Ví dụ chi phí trên website là minh họa, không phải benchmark chuẩn hóa. Có thể self-host; người dùng vẫn chịu model/infrastructure costs. Các integration phụ thuộc phiên bản harness và deployment configuration.

**Nguồn:** [GitHub](https://github.com/Parcha-ai/agentrun) · [Trang sản phẩm](https://agentrun.ai/) · [Learning docs](https://agentrun.ai/platform/self-improving).
