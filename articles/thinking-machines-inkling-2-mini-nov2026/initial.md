# Thinking Machines phát hành Inkling 2 Mini: Looped MoE 26,4B cho local coding agents

- **story_id:** `thinking-machines-inkling-2-mini-nov2026`
- **update_id:** `initial`
- **Ngày công bố gốc:** 2026-11-20
- **Ngày digest (Asia/Singapore):** 2026-11-22
- **Tạo/cập nhật nội dung (UTC):** 2026-11-22T00:24:00Z
- **Loại:** model_release

## Tổng quan

Thinking Machines Lab phát hành Inkling 2 Mini, model multimodal open-weights Apache-2.0, nhận text/image và sinh text, nhắm tới local inference và agentic coding. Bản phát hành có ngày gốc 20/11/2026; được bổ sung vào digest 22/11 dưới nhãn BACKFILL vì chưa có trong ledger trước đó.

## Điều gì xảy ra và điểm mới

Model dùng kiến trúc looped transformer kết hợp sparse mixture-of-experts: 24 decoder layers vật lý, trong đó 12 layers giữa chạy lặp ba lần, tương đương 48 lượt áp dụng layers nhưng dùng lại weights. Tổng cộng 26,4B parameters, 3,4B active; tính thêm repeated passes thành khoảng 5,4B effective active parameters/token. Mỗi layer chọn 8/128 experts. Context tối đa được công bố 1 triệu tokens; không có nghĩa máy 32GB có thể chạy 1M context với latency hoặc memory thấp.

Checkpoint hỗn hợp NVFP4/MXFP8 khoảng 20GB. Nhà phát triển liệt kê hỗ trợ Apple Silicon 32GB+, NVIDIA DGX Spark và các GPU khoảng 32GB+ VRAM, cùng các runtime như Transformers, SGLang, vLLM, llama.cpp/GGUF và Ollama (tùy nền tảng). Việc triển khai trên phần cứng cụ thể cần kiểm tra runtime/quantization tương thích.

## Kỹ thuật và benchmark

Việc lặp layers giảm lượng trọng số phải lưu nhưng không loại bỏ compute: mỗi token vẫn trải qua 48 lượt layers, có thể tăng compute và KV/cache pressure so với số lớp vật lý. Kiến trúc này tạo ra một trade-off giữa model capacity, memory footprint và inference latency.

Thinking Machines tự báo cáo DeepSWE v1.1 đạt 48,2% và Vals Index v2.2 đạt 46,5%, đồng thời mô tả hiệu quả trong nhóm open-weight models dưới 100B parameters. Hugging Face trình bày các so sánh với Qwen3.8-27B và các model khác, nhưng evaluation setup có thể khác nhau; các số liệu này chưa được tái lập độc lập trong bản tin. Hugging Face cũng mô tả bản research variant cho phép số lượt loop biến đổi, song chưa được đánh giá đầy đủ. Không có paper peer-reviewed mới được xác minh cho release này.

## Ý nghĩa thực tiễn cho AI/agent engineering

Đối với local coding agents, kích thước checkpoint ~20GB có thể phù hợp máy Apple Silicon 32GB hoặc GPU có đủ VRAM; tuy nhiên nên đo throughput, TTFT, RAM/VRAM, KV-cache khi tăng context, tool-call correctness, task success và cost/energy per successful task. Với GPU 24GB, không nên suy ra sẽ chạy full precision/long context chỉ từ kích thước weights. So sánh công bằng cần cùng agent harness, task suite, inference settings và context.

## Bằng chứng, khả dụng và bất định

**Sự kiện xác minh:** Model card của nhà phát triển ghi release 20/11, Apache-2.0 và artifacts trên Hugging Face. **Vendor claims:** Benchmark scores, hardware recommendations và throughput/efficiency. **Independent evidence:** Bài kỹ thuật Hugging Face có ví dụ inference và nhận định ban đầu, nhưng không thay thế benchmark tái lập có kiểm soát. **Suy luận của bài:** Lựa chọn model cần được xác nhận bằng local evaluation. Không khẳng định 1M context khả dụng thực tế trên mọi thiết bị.

## Nguồn chính

- [Thinking Machines Lab — Introducing Inkling 2 Mini (20/11/2026)](https://thinkingmachines.ai/news/inkling-2-mini/)
- [Thinking Machines Lab — Official model card](https://thinkingmachines.ai/model-card/inkling-2-mini/)
- [Official weights and model card — Hugging Face](https://huggingface.co/thinkingmachines/Inkling-2-Mini)
- [Hugging Face technical launch analysis (20/11/2026)](https://huggingface.co/blog/inkling2mini)
