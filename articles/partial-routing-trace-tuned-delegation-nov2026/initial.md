# Partial Routing: giao từng việc con cho model rẻ hơn thay vì route cả task

- story_id: partial-routing-trace-tuned-delegation-nov2026
- update_id: initial
- Ngày nguồn (UTC): 2026-11-24. Digest: 2026-11-27. Biên tập: 2026-11-27T06:31:54.509Z.

## Có gì mới?
Preprint báo cáo ViBench 70,2 → 78,5 với chi phí thấp hơn 19%; Terminal-Bench 54,3% → 60,9% với chi phí gần như ngang nhau.

## Cơ chế
Nhóm tác giả đối chiếu trace của lead và worker để tìm các bước lặp lại mà worker làm đủ tốt với chi phí thấp. Lead dùng dữ liệu đó để tự chọn phần việc giao đi khi chạy, không cần huấn luyện lại model. Baseline chỉ cung cấp bản chia việc cũng giúp giảm chi phí trên cả hai bộ test; trên Terminal-Bench nó đạt 58,7%, so với 54,3% của lead chạy một mình.

## Việc đáng thử
Thử ba nhánh trên cùng bộ fixture: lead chạy như cũ; lead nhận bản chia việc nhưng không delegate; và cùng bản chia việc nhưng delegating tác vụ trích xuất bằng chứng. So chi phí, lỗi trích dẫn và số mâu thuẫn được giữ lại, không chỉ số token.

## Giới hạn
Đây là preprint với 10 ứng dụng ViBench và 23 tác vụ Terminal-Bench holdout trong kết quả chính. ViBench là điểm trên thang 100, không phải pass rate. Kết quả phụ thuộc cặp model và harness; không suy rộng mức tiết kiệm 19% sang pipeline khác. arXiv ghi ngày nộp 24/11 UTC; feed ghi 27/11.

[Nguồn gốc 1](https://arxiv.org/abs/2611.33402) · [Nguồn gốc 2](https://arxiv.org/html/2611.33402v1)
