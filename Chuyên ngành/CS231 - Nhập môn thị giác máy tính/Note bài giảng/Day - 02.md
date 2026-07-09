Nếu hình chữ nhật có kích thước 1284x2778. Với 1284 là chiều rộng, 2778 là chiều cao.
Nên là ma trận có kích thước 2778x1284.

Ví dụ ảnh ma trận có kích thước HxW thì sẽ có ảnh kích thước WxH vì ảnh là chiều rộng trước chiều cao sau.

pixel: sử dụng 1 bit thì chấm đen, sử dụng 24 bit RGB.

Ảnh trong điện thoại chứa dữ liệu đã được nén của ảnh số chứ không phải ảnh số.

Phương pháp nén. PNG, JPG. nén mất thông tin.
Nó nằm ở image processor.

môn này ta làm trên ảnh số.

jpg, png là ảnh được nén, ỉmreal để giải nén. 

Nếu để ảnh số phải hiểu là ma trận lưu các giá trị số chứ không phải ảnh jpg hay png. 

Video số: có nhiều chuẩn để lưu.

ma trận a[2][2].

Tính giá trị a[0][1] tính ra được 1.2 -> như vậy là sai. 
Vì Nếu ảnh xám là từ phạm vi giá trị [0, 256).


Ảnh màu 24-bit , mỗi pixel đựo được biểu diễn bằng 3 byte, thượng đại diện  cho 3 thành phần RGB. 
Do 256x256x256 nên có 16 triệu màu.


mỗi ảnh số là 1 ma trận, mỗi phần tử của ma trận gồm 3 kênh màu.
Ảnh số đó là ảnh màu có phạm vi là 1 ma trận.

Còn Ma trận không có độ sâu.

Khi nói đến tensor thì ms có độ sâu.

Matrix lập trình trên CPU.
Còn Tensor lập trình trên GPU.

Tensor có thể chạy được trên CPU nhưng chậm.

Các thư viện phát triển trên ma trận. convert từ matrix sang tensor để chạy trên gpu chứ ko sẽ vẫn chạy trên cpu.

Số đằng trước là kích thước. số đăng sau laf độ sau.
ví dụ 244x244x64. 244x244 là kích thước ảnh còn 64 là độ sau.

input thường là ma trận.

Biểu diễn là WxH, nhưng khi lập trình là ma trận HxW.

Resolution thể hiện mức độ chi tiết.

pixel count đếm số lượng điểm ảnh.


Có nhiều hệ màu khác nhau hổ trợ mục đích khác nhau.

Nếu kích thước khác nhau thì resize cái lớp hơn. 

Histogram là thống kê số lượng. -> mỗi phần tử là 1 bin. 1 bin sẽ gộm các phần tử lại. 

color histogram là thống kê số lượng màu. 

Làm việc trên ảnh số, xong chuyển về vector để xử lý.

vector là đoạn thẳng có hướng. 
Độ đo: 
+ khoảng cách: khoách cách giữa 2 điểm đang xét, xét trên điểm. kkhông thể đo khoảng cách vector.

+ sim (độ đo tương đồng), độ đo cosin, so theo góc cosin.
+ jaccard: set

Có rất nhiều độ đo khoảng cách.
Có bao nhiêu độ đo tương đồng:
+ cosin
+ jaccard 
2 vector A(3, 4), B(6, 8). 
Khoảng cách d(A, B) = 5.
Độ tương đồng: sim(A, B) = ... 1.

Thêm nước Norm (chuẩn hóa ) trước khi đo khoảng cách.

Khi chuyển ảnh số qua vector nhớ chuẩn hóa (norm) chứ không sẽ dễ bị cút.

dựa vào ý nghĩa để biết nó là feature hay embeding.
feature vector: nếu biết được ý nghĩa của từng cái.
embedding vector: mình sẽ ko bt được ý nghĩa từng cái.