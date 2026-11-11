# GitHub Secret Scanning mở rộng sang GitHub Actions workflow logs

- **story_id:** `github-actions-log-secret-scanning-nov2026`
- **update_id:** `initial`
- **Ngày công bố gốc:** 2026-11-09
- **Ngày digest (Asia/Singapore):** 2026-11-11
- **content_created_at (UTC):** 2026-11-11T00:26:12.217Z
- **content_updated_at (UTC):** 2026-11-11T00:26:12.217Z
- **Phân loại:** security

## Tổng quan
Public preview quét provider-pattern secrets trong logs của workflow hoàn thành; chỉ enterprise đủ license và bật policy, không backfill, không thông báo alerts trong preview.

## Điều gì xảy ra và điểm mới
**Thông tin do nhà cung cấp công bố:** GitHub quét logs khi workflow run kết thúc, tạo secret-scanning alert có liên kết về log. Có validity checks cho những loại secrets được hỗ trợ. Public preview dành cho GitHub Enterprise Cloud với Secret Protection hoặc Advanced Security; enterprise owner phải bật policy, mặc định tắt. Chỉ quét runs hoàn tất sau khi bật. ([nguồn chính thức](https://github.blog/changelog/2026-11-09-secret-scanning-detects-secrets-in-github-actions-workflow-logs/)).

## Chi tiết kỹ thuật và tác động thực tế
**Phân tích của người viết:** Coding agents chạy CI có thể vô tình ghi token vào stdout/stderr. Quét logs bổ sung lớp phát hiện nhưng vẫn cần masking, credential scoping, rotation và tránh xuất secrets từ đầu. Đây là suy luận về thiết kế hệ thống, không phải kết quả kiểm thử độc lập.

## Bằng chứng, giới hạn và availability
Không quét logs lịch sử, generic/custom patterns, AI-detected secrets hay secrets đã được Actions masking; alerts từ logs không gửi notifications trong preview. Không có số liệu precision/recall. **Đánh giá độc lập:** chưa được xác minh trong bản tin này. **Peer review:** không áp dụng cho thông báo sản phẩm/chính sách. Không suy diễn benchmark khi nguồn không cung cấp điều kiện đánh giá.

## Nguồn gốc
- [Thông báo chính thức ngày 2026-11-09](https://github.blog/changelog/2026-11-09-secret-scanning-detects-secrets-in-github-actions-workflow-logs/)
