Thuật toán loại bỏ các hộp giới hạn dư thừa NMS

loại bỏ ancher box

Không phải dựa vào mỗi độ tin cậy mới quyết định bb.

Thuật toán NMS


Phương pháp sử dụng mạng học sâu.

`fit`: 

Trong qúa trình huấn luyện:
- train 90%, val: 70% giải quyết sao

under, fit, over.

Lưu ý nhớ sau khi có mô hình best, sau khi test thử.
Chịu khó xem nó sai ở đâu.

Sai từ lúc train rồi.

Khó qúa bỏ qua.

Bài toán phát hiện đối tượng.

object localization, 

D/CAT/M: multi class classification
D, C: multi label.


Sử dụng hàm có sẵn hay tự code.


haar-like features

mAP -> AP -> P = TP / (TP + FP).

mAP, AP theo VOC và COCO.

what is TP, FP.


AP dựa vào VOC: trung bình của 11 giá trị
AP theo COCO liên tục -> tích phân.

mAP VOC trung bình của 11 giá trị AP.
$mAP_{COCO} = \frac{mAP_{0.50} + mAP_{0.55} + \ldots + mAP_{0.95}}{10}$

kiểm tra cận trên cận dưới.



| P1  | A   | 0.95 | 0.83 | 0.30 |
| --- | --- | ---- | ---- | ---- |
| P2  | A   | 0.87 | 0.42 | 0.75 |
| P3  | A   | 0.85 | 0.75 | 0.55 |
|     |     |      |      |      |
