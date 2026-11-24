# GitHub Code Quality phát hiện lỗi định dạng khi upload coverage

- **story_id:** `github-code-coverage-upload-validation-nov2026`
- **update_id:** `initial`
- **Original event/publication date:** 2026-11-23
- **Digest date (Asia/Singapore):** 2026-11-24
- **Content created/updated (UTC):** 2026-11-24T00:04:18Z

## Tổng quan
Ngày 23/11/2026, GitHub cải tiến action `upload-code-coverage` của GitHub Code Quality: workflow giờ báo lỗi rõ ràng khi file coverage không đúng định dạng **Cobertura XML**, thay vì báo upload thành công nhưng không hiển thị coverage trên PR.

## Điều gì mới
Nếu report không hợp lệ, bước upload thất bại và Actions log nêu rõ cần cung cấp Cobertura XML. Với report Cobertura hợp lệ, bộ xử lý trở nên khoan dung hơn với một số sai khác cấu trúc nhỏ; các dòng thiếu line number hoặc hit count hợp lệ được bỏ qua riêng thay vì loại cả báo cáo.

Phạm vi: repository đã bật GitHub Code Quality trên **GitHub Enterprise Cloud**, **GitHub Team** và Enterprise Cloud with data residency; **không hỗ trợ GitHub Enterprise Server** theo thông báo.

## Ý nghĩa kỹ thuật cho coding agents
**Suy luận kỹ thuật:** Trong vòng lặp agent implement → test → PR, upload có trạng thái thành công giả khiến agent hoặc reviewer hiểu nhầm thiếu coverage là lỗi hiển thị thay vì lỗi định dạng. Bước fail-fast mới giúp phát hiện vấn đề ở CI, nhưng workflow có thể bắt đầu fail sau thay đổi. Cần cấu hình test framework xuất Cobertura XML hoặc chuyển đổi định dạng trước upload. Không nên coi một report được chấp nhận là bảo đảm test coverage đầy đủ hay test quality tốt.

## Bằng chứng, giới hạn và availability
**Sự kiện đã xác nhận:** Changelog GitHub ngày 23/11 mô tả thay đổi. **Không có benchmark:** không có số liệu định lượng về false successes hoặc độ cải thiện chất lượng code. Đây là validation của coverage artifact, không phải model release hoặc tính năng AI scan.

## Nguồn chính
- [GitHub Changelog, 23/11/2026](https://github.blog/changelog/2026-11-23-code-coverage-uploads-now-flag-invalid-report-formats/)
