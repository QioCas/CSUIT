### Object localization
là một phần của object detection. 


Input: $D = \{(x_i, y_i, b_i)\}$

$x_i \rightarrow e_i \rightarrow \text{classifier}$

$b_i$ là Bounding Box = Hộp giới hạn. 
- Hộp là hình hộp chữ nhật 6 mặt -> Mỗi mặt là HCN.
- HCN là HBH có góc vuông. HBH là ...

**Đồ họa máy tính** mô tả đối tượng dưới dạng lưới các điểm trong không gian 3D.
3D phải render (with GPU) để display 2D.
6 giá trị.

**Thị gíac máy tính** dữ liệu là ảnh số, dưới dạng matrix 2D.

Để làm bounding box cho CV:
$x$ ngang, $y$ xuống.

(l, t, r, b) pascal VOC tính theo kích thước.
(l, t, W, H) CoCo tính theo kích thước.
(x_c, y_c, W, H) YoLo tính theo tỉ lệ.

Tính kiểu gì cũng sẽ có 4 giá trị.

Bài toán supervised.

Cho $D = \{(x_i, y_i, b_i)\}_{i=1}^{n}$.

Làm sao để tìm được idx của 4 gia tri? Sử dụng hồi quy.

classifier: Giá trị output rời rạc. 
regression: Giá trị output liên tục.


depend on instance ...

weakly sup

few shot
$\{C_0, C_1, C_2\}$
$C2 << C_0, C_1$ $\rightarrow$ ML $\rightarrow$  Ảnh hưởng bởi data.

one shot là mẫu.
zero shot là biết có $C_3$ nhưng 0 có mẫu.
$\rightarrow$ open_world.

Lớp base và lớp abc không được giao nhau.

30 điểm là xác định đúng bài toán.

MS COCO: Vì sao bbox lại có số thực vì làm nhiều người (lẻ người) để tìm trung bình.

Độ đo Jaccard 
Sim(A, B) = (A giao B) / (A hợp B)

IoU = C / (A + B - C)