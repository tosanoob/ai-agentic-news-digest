# GitHub công bố kế hoạch ngừng sáu model Copilot ngày 14/12/2026

- **story_id:** `github-copilot-model-deprecations-dec2026`
- **update_id:** `initial`
- **Ngày sự kiện/công bố:** 2026-11-13
- **Ngày digest (Asia/Singapore):** 2026-11-14
- **Created/updated UTC:** 2026-11-14T00:44:16Z
- **Loại:** enterprise

## Tổng quan

GitHub lên lịch deprecate Fable 5, Haiku 4.5, Gemini 3.8 Flash, Gemini 4 Argon, Grok 4.6, Kimi K3 trên Copilot 14/12; nêu alternatives và ngoại lệ Haiku 4.5 annual individual.

## Điều gì xảy ra và điểm mới

Ngày 13/11 GitHub thông báo sẽ ngừng hỗ trợ trên mọi Copilot experiences vào 14/12/2026: Claude Fable 5 → Fable 5.2; Claude Haiku 4.5 → Haiku 5.5; Gemini 3.8 Flash → Gemini 4 Hydrogen; Gemini 4 Argon → Gemini 4 Carbon; Grok 4.6 → Grok 4.7; Kimi K3 chưa có replacement công bố. Ngoại lệ: Haiku 4.5 tiếp tục cho individual Copilot subscribers theo annual plans. Admin Business/Enterprise có thể cần bật model alternatives nếu đã tắt default enablement.

## Ý nghĩa thực tiễn với AI/agent engineering (phân tích, không phải vendor claim)

Model pinning là dependency quản trị trong coding agents: kiểm kê CLI/IDE configurations, workflow YAML, model allowlists, fallback chains và regression suites trước deadline. Đổi model có thể thay đổi tool-use behavior, latency, chi phí, safety/retention policy. Đề xuất chạy canary trên tập tasks cố định và lưu model ID, effort, harness version để so sánh.

## Bằng chứng, giới hạn và availability

Đây là thông báo kế hoạch, chưa phải sự kiện đã ngừng hoạt động. Không suy ra các API model ngoài GitHub Copilot cũng ngừng; không có benchmark mới.

## Nguồn chính thức

- [Nguồn công bố](https://github.blog/changelog/2026-11-13-upcoming-deprecation-of-selected-github-copilot-models-in-december/)

**Phân loại bằng chứng:** Ngày công bố, API/availability và tính năng là thông tin từ nhà cung cấp; các đánh giá kỹ thuật và đề xuất triển khai là suy luận của người viết. Không có benchmark độc lập mới được xác minh cho sự kiện này.
