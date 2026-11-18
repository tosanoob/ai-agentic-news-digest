# UPDATE Copilot Fusion: Terminal-Bench 4.1, mở rộng surfaces và model routing

- **story_id:** `github-copilot-fusion-benchmark-expansion-nov2026`
- **update_id:** `initial`
- **Ngày công bố gốc:** 2026-11-17
- **Ngày digest (Asia/Singapore):** 2026-11-18
- **Tạo/cập nhật nội dung (UTC):** 2026-11-18T00:36:53Z
- **Loại:** benchmark

## Tổng quan
GitHub báo cáo Fusion Max 71.2% Terminal-Bench 4.1, hơn Opus 5.5/Fable 5.2 5.4 điểm phần trăm; công bố chi phí thấp hơn 57%/88% theo điều kiện bảng xếp hạng; mở rộng web/mobile/Visual Studio và models.

## Sự kiện và điểm mới
Theo [thông báo chính thức của GitHub](https://github.blog/changelog/2026-11-17-github-copilot-fusion-updates-more-availability-benchmarks-and-models/), Fusion chọn/điều phối model theo effort; Max thêm Sonnet 5.5, High thêm GPT-6.1 Terra, Standard thêm MAI-Code-2. Kết quả được liệt kê trên public leaderboard Terminal-Bench 4.1.

## Chi tiết kỹ thuật và giới hạn triển khai
Fusion chọn/điều phối model theo effort; Max thêm Sonnet 5.5, High thêm GPT-6.1 Terra, Standard thêm MAI-Code-2. Kết quả được liệt kê trên public leaderboard Terminal-Bench 4.1. Đây là mô tả tính năng hoặc kết quả do nhà cung cấp công bố, không mặc định chứng minh năng lực vận hành trong mọi môi trường. Việc sử dụng thực tế cần kiểm tra quyền truy cập, trạng thái preview/GA, cấu hình agent harness và khả năng đo lường.

## Ý nghĩa thực tiễn cho AI/agent engineering
**Phân tích và khuyến nghị của tác giả:** Đánh giá model router theo cost per solved task và matched harness settings; không đồng nhất model-only với router multi-model. Thử nghiệm nội bộ phải phản ánh workload thật.

## Bằng chứng, độ tin cậy và tính khả dụng
**Sự kiện được xác minh:** GitHub công bố ngày 17/11/2026 tại URL gốc bên dưới. **Tuyên bố của nhà cung cấp / giới hạn:** 71.2% và so sánh chi phí là số GitHub trích từ public leaderboard, chưa tự tái lập; cần xem sampling, hardware, token pricing và confidence intervals. **Đánh giá độc lập:** chưa được xác minh trong lần nghiên cứu này; không coi vendor claims là independent evaluation.

## Nguồn chính
- [GitHub Changelog — UPDATE Copilot Fusion: Terminal-Bench 4.1, mở rộng surfaces và model routing](https://github.blog/changelog/2026-11-17-github-copilot-fusion-updates-more-availability-benchmarks-and-models/)
