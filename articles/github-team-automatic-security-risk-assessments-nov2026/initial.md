# GitHub Team tự động chạy security risk assessments

- **story_id:** `github-team-automatic-security-risk-assessments-nov2026`
- **update_id:** `initial`
- **Original event/publication date:** 2026-11-18
- **Digest date (Asia/Singapore):** 2026-11-19
- **Content created/updated (UTC):** 2026-11-19T00:04:12Z
- **Category:** security

## Tổng quan
GitHub Team organizations được tự động chạy security risk assessments miễn phí; org admins/security managers xem exposed credentials, code vulnerabilities và mức rủi ro để ưu tiên xử lý.

## Điều gì đã xảy ra và điểm mới
**Sự kiện được nguồn chính thức xác nhận:** Thông báo ngày 18/11 xác nhận risk assessments chạy tự động cho organizations trên GitHub Team. Organization admins và security managers có thể xem findings về exposed credentials và code vulnerabilities, dùng làm risk overview và ưu tiên next steps.

## Chi tiết kỹ thuật và ý nghĩa đối với AI/agent engineering
**Phân tích và suy luận kỹ thuật của người viết, không phải kết quả kiểm thử độc lập:** Có thể dùng kết quả như một tín hiệu đầu vào cho security triage, nhưng cần correlate với deployed software inventory, CVE/KEV và exposure thực tế trước khi ưu tiên remediation. Không thay thế secret rotation, SAST hoặc full vulnerability assessment.

## Evidence, availability và giới hạn
Thông báo không nêu lịch chạy, mức coverage, detection rates, thời gian giữ findings hoặc khả năng tự động remediation. Không nên khẳng định continuous monitoring với SLA cụ thể hay benchmark precision/recall.

Không có independent evaluation được tái lập trong bản tin này. Nếu nguồn nêu nhận định từ nhà cung cấp, chúng được xem là vendor claims, không phải bằng chứng benchmark độc lập. Không suy diễn thêm số liệu hay availability ngoài thông báo.

## Primary source
- [GitHub Changelog — GitHub Team tự động chạy security risk assessments](https://github.blog/changelog/2026-11-18-security-risk-assessments-run-automatically-on-github-team/) (ngày 2026-11-18).
