# BACKFILL: GitHub và Microsoft công bố kết quả pilot Codename MDASH

- **story_id:** `github-microsoft-mdash-ai-vuln-fix-pilot-nov2026`
- **update_id:** `initial`
- **Ngày công bố gốc:** 2026-11-17
- **Ngày digest (Asia/Singapore):** 2026-11-21
- **Tạo/cập nhật nội dung (UTC):** 2026-11-21T00:34:17Z
- **Loại:** security
- **Nhãn:** BACKFILL (công bố cũ chưa ghi ledger)

## Tổng quan

GitHub và Microsoft trình bày pilot security-agent pipeline tập trung vào báo cáo lỗ hổng đã kiểm chứng kèm bản vá, thay vì gửi thẳng hàng nghìn cảnh báo thô cho maintainers.

## Điều gì xảy ra và điểm mới

Codename MDASH với MAI Cyber model quét sáu dự án AutoGPT, Caddy, Express, FastMCP, ImageMagick và Netty. GitHub Security Lab triage bằng Copilot skills để loại duplicates và kiểm tra tính hợp lệ, sau đó bảy nhà nghiên cứu Microsoft FORGE Lab xác minh thủ công. Theo GitHub, 9.791 candidate issues dẫn tới 99 private reports; đến 15/11 có 55 vấn đề được maintainers sửa và 14 bản vá đã có trong releases. Mỗi báo cáo có proof of concept và suggested fix; các maintainers đồng ý tham gia.

Nguồn chính thức: [GitHub — BACKFILL: GitHub và Microsoft công bố kết quả pilot Codename MDASH](https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/).

## Chi tiết kỹ thuật và tác động đến AI/agent engineering

Pipeline cho security agents nên tách detection → deduplication → validation → private disclosure → suggested fix → maintainer approval. Với MCP server như FastMCP, các security findings phải xét threat model và side effects. Human verification vẫn là nút thắt quan trọng khi scale.

## Bằng chứng, khả dụng và giới hạn

Đây là vendor-reported pilot trên sáu dự án chọn trước, không phải controlled independent benchmark; không suy ra precision = 99/9791 vì triage loại nhiều loại findings và chưa biết ground-truth false negatives. Số 55 fixes phản ánh tiến độ đến 15/11, không phải tỷ lệ thành công phổ quát.

**Phân loại bằng chứng:** Các khả năng, phạm vi triển khai và số liệu được ghi nhận từ công bố GitHub (vendor-reported facts/claims). Những khuyến nghị kiến trúc ở phần tác động là suy luận kỹ thuật của bài viết, không phải kết quả thử nghiệm độc lập. Không có peer-reviewed benchmark cho sự kiện này.

## Nguồn gốc

- [Thông báo và dữ liệu chính thức của GitHub](https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/)
