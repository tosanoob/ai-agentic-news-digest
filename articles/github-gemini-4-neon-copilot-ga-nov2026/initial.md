# Gemini 4 Neon GA trong GitHub Copilot

- **story_id:** `github-gemini-4-neon-copilot-ga-nov2026`
- **update_id:** `initial`
- **Original event/publication date:** 2026-11-18
- **Digest date (Asia/Singapore):** 2026-11-19
- **Content created/updated (UTC):** 2026-11-19T00:04:12Z
- **Category:** model_release

## Tổng quan
GitHub đưa Gemini 4 Neon GA vào Copilot Pro+/Max/Business/Enterprise, rollout dần; Google claim chất lượng gần Carbon với chi phí token thấp hơn, phản hồi nhanh và ít sửa code ngoài yêu cầu hơn; chưa có independent benchmark.

## Điều gì đã xảy ra và điểm mới
**Sự kiện được nguồn chính thức xác nhận:** Model được cung cấp trong VS Code, Visual Studio, Copilot CLI, coding agent, Copilot app, github.com, mobile, JetBrains, Xcode và Eclipse. GitHub dùng usage-based billing theo provider list pricing; Business/Enterprise có model policy. GitHub trích dẫn Google về response onset nhanh hơn và ít unsupported claims hơn so với Carbon.

## Chi tiết kỹ thuật và ý nghĩa đối với AI/agent engineering
**Phân tích và suy luận kỹ thuật của người viết, không phải kết quả kiểm thử độc lập:** Có thể thử Neon như middle tier giữa Flash và frontier models cho coding agents. Đánh giá trên cùng bộ tasks với Carbon/Hydrogen: success rate, unwanted edits, hallucinated tool results, latency và cost per resolved task; cố định harness/effort để so sánh.

## Evidence, availability và giới hạn
Thông báo là GA trong Copilot, không chứng minh model lần đầu phát hành ngày này. Không có con số benchmark hoặc giá token cụ thể trong nguồn; các tuyên bố chất lượng là vendor claims, không phải independent evaluation. Rollout dần.

Không có independent evaluation được tái lập trong bản tin này. Nếu nguồn nêu nhận định từ nhà cung cấp, chúng được xem là vendor claims, không phải bằng chứng benchmark độc lập. Không suy diễn thêm số liệu hay availability ngoài thông báo.

## Primary source
- [GitHub Changelog — Gemini 4 Neon GA trong GitHub Copilot](https://github.blog/changelog/2026-11-18-gemini-4-neon-in-github-copilot/) (ngày 2026-11-18).
