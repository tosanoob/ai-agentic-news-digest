# Copilot code review: Adaptive effort, cross-repo context và secret detection

- **story_id:** `github-copilot-code-review-adaptive-security-nov2026`
- **update_id:** `initial`
- **Ngày công bố gốc:** 2026-11-17
- **Ngày digest (Asia/Singapore):** 2026-11-18
- **Tạo/cập nhật nội dung (UTC):** 2026-11-18T00:36:53Z
- **Loại:** security

## Tổng quan
Adaptive tự chọn Lite/Balanced/Max theo PR risk; cross-repository context preview trên public repos; secret scanning kết hợp deterministic patterns và AI; Azure Repos code review đạt GA.

## Sự kiện và điểm mới
Theo [thông báo chính thức của GitHub](https://github.blog/changelog/2026-11-17-copilot-code-review-adaptive-effort-secret-detection-and-more/), Adaptive tôn trọng mức effort tối đa do admin cấu hình. Secret detection kiểm tra thay đổi PR, hơn 500 loại secret từ 150+ partners cùng AI/ML detector; review Azure Repos có branch policy và Azure AI credit billing.

## Chi tiết kỹ thuật và giới hạn triển khai
Adaptive tôn trọng mức effort tối đa do admin cấu hình. Secret detection kiểm tra thay đổi PR, hơn 500 loại secret từ 150+ partners cùng AI/ML detector; review Azure Repos có branch policy và Azure AI credit billing. Đây là mô tả tính năng hoặc kết quả do nhà cung cấp công bố, không mặc định chứng minh năng lực vận hành trong mọi môi trường. Việc sử dụng thực tế cần kiểm tra quyền truy cập, trạng thái preview/GA, cấu hình agent harness và khả năng đo lường.

## Ý nghĩa thực tiễn cho AI/agent engineering
**Phân tích và khuyến nghị của tác giả:** Dùng risk-based review budgets và secret detection trước merge; cần tách static detectors khỏi LLM judgment, audit findings và bắt buộc human review cho code nhạy cảm.

## Bằng chứng, độ tin cậy và tính khả dụng
**Sự kiện được xác minh:** GitHub công bố ngày 17/11/2026 tại URL gốc bên dưới. **Tuyên bố của nhà cung cấp / giới hạn:** Nhiều tính năng vẫn public preview. Chưa có independent recall/precision hoặc controlled cost study; scanning changes không thay thế history scan. **Đánh giá độc lập:** chưa được xác minh trong lần nghiên cứu này; không coi vendor claims là independent evaluation.

## Nguồn chính
- [GitHub Changelog — Copilot code review: Adaptive effort, cross-repo context và secret detection](https://github.blog/changelog/2026-11-17-copilot-code-review-adaptive-effort-secret-detection-and-more/)
