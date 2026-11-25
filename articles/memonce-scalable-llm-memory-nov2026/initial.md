# MemOnce: giảm active cache cho agent giữ context dài

- **story_id:** `memonce-scalable-llm-memory-nov2026`
- **update_id:** `initial`
- **Original event/publication date:** 2026-11-20
- **Digest date (Asia/Singapore):** 2026-11-25
- **Content created/updated (UTC):** 2026-11-25T08:08:04Z

## Tổng quan

MemOnce là preprint đề xuất một kiến trúc bộ nhớ ở tầng model. Thay vì giữ toàn bộ KV cache theo từng layer trên GPU, kiến trúc lưu biểu diễn nén vào một memory bank có thể đặt trên CPU hoặc SSD, chỉ truy xuất và khôi phục những trạng thái cần cho truy vấn hiện tại.

## Bằng chứng

Ở thí nghiệm 4B, context 1 triệu token, tác giả báo cáo **25 MB active cache trên GPU + 640 MB offload** so với **32,05 GB active cache** của Qwen3.5 baseline. Cùng bảng cho thấy prefill 41,36 giây so với 286,86 giây và decode 29,3 so với 8,4 token/giây. Ở 32K, baseline prefill lại nhanh hơn (0,87 so với 1,38 giây). Đây là số do tác giả đo trong thiết lập của paper; baseline không vừa GPU đơn 80 GB được đánh giá trên nhiều GPU. Không diễn giải cache thành tổng VRAM hoặc ngoại suy sang mọi model và workload.

## Ý nghĩa cho agent engineering

Kiến trúc này đáng thử khi context dài mới là nút thắt. Nó không thay thế checkpoint orchestration hoặc external RAG, và không phải cấu hình bật sẵn cho mọi model trong vLLM. Nếu đánh giá để dùng thật, nên đo tổng VRAM, I/O offload và latency dưới concurrency của workload, thay vì chỉ so cache ở một độ dài context. Chưa xác minh tái lập độc lập hoặc khả năng triển khai production.

## Nguồn chính

- [arXiv, ngày công bố và abstract](https://arxiv.org/abs/2611.27973)
- [Preprint, Phụ lục F.4, Bảng 14](https://arxiv.org/html/2611.27973v1#S14.T14)
