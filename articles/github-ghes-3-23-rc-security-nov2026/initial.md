# GitHub Enterprise Server 3.23 RC: offline AI secret detection và supply-chain controls

- **story_id:** `github-ghes-3-23-rc-security-nov2026`
- **update_id:** `initial`
- **Ngày công bố gốc:** 2026-11-20
- **Ngày digest (Asia/Singapore):** 2026-11-21
- **Tạo/cập nhật nội dung (UTC):** 2026-11-21T00:34:17Z
- **Loại:** security

## Tổng quan

GitHub phát hành release candidate GHES 3.23 với các thay đổi đáng chú ý cho môi trường doanh nghiệp và air-gapped.

## Điều gì xảy ra và điểm mới

AI secret detection có thể nhận diện unstructured secrets ngay trong mạng nội bộ bằng model fine-tuned chạy trên CPU của appliance, không cần GPU, hosted LLM hay outbound connection; đây là public preview. GitHub Advisory Database mở rộng malware advisories sang PyPI, Maven, RubyGems, NuGet, Go, Rust và Composer ngoài npm, sử dụng nguồn OpenSSF malicious-packages. Dependabot mặc định chờ phiên bản package tồn tại ít nhất ba ngày trước khi tạo version-update PR. OAuth access tokens có thể hết hạn sau tám giờ kèm refresh tokens; preview, opt-in cho apps cũ.

Nguồn chính thức: [GitHub — GitHub Enterprise Server 3.23 RC: offline AI secret detection và supply-chain controls](https://github.blog/changelog/2026-11-20-github-enterprise-server-3-23-release-candidate/).

## Chi tiết kỹ thuật và tác động đến AI/agent engineering

Với enterprise agents, offline scanning giúp giảm dữ liệu rời khỏi mạng; package cooldown giảm rủi ro hấp thụ ngay bản phát hành độc hại nhưng đánh đổi độ mới của dependencies. Token expiry cần quản lý refresh và rotation. Trước khi nâng cấp production, thử nghiệm trong staging và kiểm tra tương thích CI, IAM, package ecosystems.

## Bằng chứng, khả dụng và giới hạn

Đây là release candidate, không phải GA. AI detector và OAuth expiry là preview; chưa có independent precision/recall hoặc CPU throughput benchmark. Cooldown không phải biện pháp bảo đảm package an toàn.

**Phân loại bằng chứng:** Các khả năng, phạm vi triển khai và số liệu được ghi nhận từ công bố GitHub (vendor-reported facts/claims). Những khuyến nghị kiến trúc ở phần tác động là suy luận kỹ thuật của bài viết, không phải kết quả thử nghiệm độc lập. Không có peer-reviewed benchmark cho sự kiện này.

## Nguồn gốc

- [Thông báo và dữ liệu chính thức của GitHub](https://github.blog/changelog/2026-11-20-github-enterprise-server-3-23-release-candidate/)
