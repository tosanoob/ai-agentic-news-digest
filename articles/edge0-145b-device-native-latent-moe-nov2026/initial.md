# Edge0-145B phát hành trọng số MoE cho inference cục bộ

- **story_id:** `edge0-145b-device-native-latent-moe-nov2026`
- **update_id:** `initial`
- **Ngày sự kiện:** 2026-11-13
- **Ngày digest:** 2026-11-16 (Asia/Singapore)
- **Created/updated UTC:** 2026-11-16T00:21:16Z
- **Loại bằng chứng:** source chính thức của dự án; các đánh giá kỹ thuật được ghi rõ là suy luận

## Tổng quan
Edge0 giới thiệu mô hình 145B latent mixture-of-experts cho inference trên thiết bị cá nhân; public artifacts được ghi nhận 12–13/11, chọn ngày sự kiện 13/11 theo thông tin phát hành được tổng hợp. Đây là mục BACKFILL.

## Điều gì mới và chi tiết kỹ thuật
Theo [repository](https://github.com/Edge0-AI/Edge0), Edge0-145B sử dụng 512 experts mỗi layer, chọn 10 routed experts cộng một shared expert cho mỗi token. Các artifacts Q3_K và NVFP4 được phát hành, có CLI/server inference và kiến trúc streaming weights từ storage. [Trọng số Q3_K](https://huggingface.co/Edge0/Edge0-145B-q3k) có thể tải để kiểm tra. Mô hình được phát triển dựa trên Qwen3.8-Flash-Next theo thông tin nhà phát triển.

## Ý nghĩa kỹ thuật
Suy luận: Mô hình lớn với active parameters thấp có thể mở hướng triển khai agent cục bộ, nhưng tổng trọng số vẫn chiếm nhiều dung lượng. Không thể suy ra toàn bộ 145B weights vừa trong VRAM 24 GB; SSD offloading có thể tạo bottleneck prefill/decode. Cần đo TTFT, tokens/s, RAM, VRAM, SSD throughput và agent task success trên cấu hình mục tiêu.

## Evidence, availability và giới hạn
Mã runtime và trọng số được công bố nhưng license model khác với license Apache-2.0 của phần mềm; phải kiểm tra điều kiện sử dụng thương mại. Chưa có báo cáo benchmark độc lập tái lập trong bản tin. Các demo và thông số tốc độ của tác giả không đủ để so sánh công bằng với Qwen hoặc các model khác.

**Nguồn:** [GitHub chính thức](https://github.com/Edge0-AI/Edge0) · [Model artifact](https://huggingface.co/Edge0/Edge0-145B-q3k).
