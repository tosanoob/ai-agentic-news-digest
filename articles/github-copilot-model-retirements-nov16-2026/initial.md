# GitHub Copilot chính thức ngừng Opus 4.8, Opus 5 và GPT-5.6 Terra

- **story_id:** `github-copilot-model-retirements-nov16-2026`
- **update_id:** `initial`
- **Original event/publication date:** 2026-11-16
- **Digest date (Asia/Singapore):** 2026-11-17
- **Content created (UTC):** 2026-11-17T00:40:52Z
- **Content updated (UTC):** 2026-11-17T00:40:52Z
- **Type:** Initial event

## Tổng quan
Ngày 16/11/2026, GitHub xác nhận **đã có hiệu lực** việc ngừng ba model trong đa số trải nghiệm GitHub Copilot. GitHub cho biết thay đổi này được thông báo trước vào 15/10. Đây là đợt retirements **khác** với sáu model dự kiến ngừng ngày 14/12, đã được ledger ghi riêng.

## Thay đổi đã xác nhận
- Claude Opus 4.8 → gợi ý Claude Opus 5.5; vẫn có ngoại lệ cho một số Copilot individual subscribers thanh toán hằng năm.
- Claude Opus 5 → gợi ý Claude Opus 5.5; đã rời model picker nhưng còn được dùng làm runtime refusal fallback khi quyền truy cập hiện tại cho phép.
- GPT-5.6 Terra → gợi ý GPT-6.1 Sol hoặc GPT-6 Luna.

Phạm vi GitHub công bố bao gồm Copilot Chat, inline edits, ask/agent modes và code completions trong đa số trải nghiệm Copilot. Đây **không phải** tuyên bố các model đã bị tắt ở mọi API của nhà cung cấp.

## Chi tiết vận hành
Với Copilot Business và Enterprise, alternatives được bật tự động theo default model enablement, trừ khi administrator đã tắt global default hoặc chặn model cụ thể. Cần kiểm tra policies trước khi thay đổi workflows.

## Ý nghĩa với coding agents
Model IDs và model-specific behavior là dependencies của harness. Nên chạy regression tests về tool calls, code changes, latency, task success và cost trước khi chuyển model. Fallback ở runtime không bảo đảm hành vi giống model đã retire; cần kiểm tra audit logs và policy compliance.

## Evidence và giới hạn
Đây là thông báo chính thức về availability; không có benchmark nào chứng minh model thay thế có hiệu năng tốt hơn trên workload riêng. Ngoại lệ Opus 5 là fallback nội bộ, không phải lựa chọn thông thường từ picker. Ngày retirements không được nhầm với đợt 14/12.

## Nguồn
- [GitHub Changelog, 16/11/2026 — Models deprecated](https://github.blog/changelog/2026-11-16-github-copilot-models-deprecated-on-november-16-2026/)
