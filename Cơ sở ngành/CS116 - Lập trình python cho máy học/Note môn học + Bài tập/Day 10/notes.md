
### TASK 1: persional item recommendation, 

- Train dataset: Time dữ liệu của năm 2025 (full năm)
- Test dataset: Tháng 1 năm 2026 (blind) -> chỉ tính event "purchased"

Input: 
- dữ liệu mua hàng (trans) (event "purchased") 
- event data: 'view_item', "add_to_cart" (ATC) # <--- new 

Output:
- 1 dictionary mapping từ customer_id
$user_id: [item_1, item_2, \ldots, item_N]$ (có thứ tự) $\rightarrow$ recommend on web
Tính metric đánh giá trên những khách hàng có phát sinh giao dịch.


view_item > atc > event
xác định weight của 3 thằng.

metrics:
- IoU của tập recommend
- 1 / rank(first hit item)
- precision@10 -> recommend ở Kiosk (chính)
- MAP


Dữ liệu có xét những khách hàng ms tạo tài khoảng từ tháng 1/2026
cold start user (user mới trong tập test)
- Thống kê polular item (ko ổn).
- khách hàng mới có dữ liệu ngày tạo tải khoảng, thường là mới sinh con nên ms có nhu cầu mua.


### TASK 2: Sale Forcasting

- Train dataset: Time dữ liệu của năm 2025 (full năm)
- Test dataset: Tháng 1 năm 2026 (blind) -> chỉ tính event "purchased"

Input: 
- dữ liệu mua hàng (trans) (event "purchased") 
- event data: 'view_item', "add_to_cart" (ATC) # <--- new 

Output:
Bảng dữ liệu bao gồm 3 cột location, item_id và prediction.
Tính metric đánh giá trên nhwxng cửa hàng (location) có phát sinh giao dịch. Không tính những mặt hàng có sale_status = 0.
Metrics:
- MAE trên doanh số (số lượng) $leftrightarrow$ RMSE (tham khảo)
- MAE trên doanh thu (tham khảo) (doanh thu số lượng + tiền)
- MAPE trên doanh thu (tham khảo)
- MAPE trên doanh số (chính)

---

thực tế: 100 hộp 
kho: 70 hộp $\rightarrow$ mất 30 hộp chi phí "cơ hội"
kho: 130 hộp $\rightarrow$ mất "chi phí vốn"

upd file -> file pickle (pkl)

Tuần cuối cùng: 30/5 (Tuần tới).

1 ngày nộp 5 lần

Cách tính điểm cho từng đồ án:
top 1: 10
top 2-3: 9
top 4-7: 8
top 8-10: 7

Nếu chọn 2 đồ án, điểm sẽ là điểm cao nhất trong từng đồ án.
