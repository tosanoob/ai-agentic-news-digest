# GitHub sẽ tạm dừng Dependabot alerts trên repositories không hoạt động

- **story_id:** `github-dependabot-inactive-repo-alert-pause-nov2026`
- **update_id:** `initial`
- **Ngày công bố gốc:** 2026-11-10
- **Ngày digest (Asia/Singapore):** 2026-11-11
- **content_created_at (UTC):** 2026-11-11T00:26:12.217Z
- **content_updated_at (UTC):** 2026-11-11T00:26:12.217Z
- **Phân loại:** security

## Tổng quan
Từ 08/12 GitHub dự kiến tắt Dependabot alerts trên đa số repos không có hoạt động một năm; alerts cũ được archive và khôi phục khi push hoặc bật lại, có ngoại lệ policy enterprise.

## Điều gì xảy ra và điểm mới
**Thông tin do nhà cung cấp công bố:** GitHub công bố kế hoạch áp dụng từ 08/12/2026 với repositories không hoạt động một năm. Hoạt động gồm push branch/tag, tạo repository hoặc bật Dependabot alerts. Push mới hoặc bật alerts sẽ khôi phục archived alerts. Enforced security configuration và một số enterprise policies được miễn; không áp dụng GHES. ([nguồn chính thức](https://github.blog/changelog/2026-11-10-dependabot-alerts-will-pause-on-inactive-repositories/)).

## Chi tiết kỹ thuật và tác động thực tế
**Phân tích của người viết:** Security inventory không nên mặc định coi thiếu alert là không có lỗ hổng. Repositories dormant nhưng vẫn được deploy có thể cần cấu hình enforced alerts hoặc quy trình kiểm tra độc lập. Đây là suy luận về thiết kế hệ thống, không phải kết quả kiểm thử độc lập.

## Bằng chứng, giới hạn và availability
Đây là thay đổi chính sách trong tương lai, chưa có hiệu lực ngày 11/11. Không có bằng chứng rằng vulnerabilities bị xóa; alerts được archive. **Đánh giá độc lập:** chưa được xác minh trong bản tin này. **Peer review:** không áp dụng cho thông báo sản phẩm/chính sách. Không suy diễn benchmark khi nguồn không cung cấp điều kiện đánh giá.

## Nguồn gốc
- [Thông báo chính thức ngày 2026-11-10](https://github.blog/changelog/2026-11-10-dependabot-alerts-will-pause-on-inactive-repositories/)
