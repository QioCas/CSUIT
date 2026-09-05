# BÁO CÁO KẾT QUẢ TRIỂN KHAI MÔ HÌNH TRANSFORMER DECODER

## 1. Mục tiêu
File thực hành này trình bày cách xây dựng từ đầu (from scratch) kiến trúc của một mô hình ngôn ngữ dựa trên **Transformer Decoder** (tương tự kiến trúc cốt lõi của họ mô hình GPT) bằng cách sử dụng thư viện PyTorch. 

Mục tiêu chính là giúp hiểu rõ cách dòng dữ liệu (tensor) đi qua từng thành phần của mạng học sâu, từ đầu vào cho đến việc đưa ra dự đoán từ (token) tiếp theo.

## 2. Chi tiết các thành phần đã triển khai

Quá trình xây dựng được chia thành 5 bước tuần tự và logic:

### Bước 1: Khởi tạo môi trường và Siêu tham số (Hyperparameters)
 **Thư viện sử dụng:** Khai báo các module cần thiết của PyTorch (`torch`, `torch.nn`, `torch.nn.functional`) và thư viện toán học cơ bản (`math`).
 **Cấu hình tham số:** Thiết lập cấu hình cho một mô hình ngôn ngữ cỡ nhỏ (mô phỏng theo các cấu hình chuẩn):
     `batch_size = 4` và `context_length = 8` (kích thước chuỗi đầu vào).
     `d_model = 512` (số chiều của vector biểu diễn).
     `num_heads = 8` (số lượng attention heads), suy ra mỗi head có kích thước `d_k = 64`.
     `d_ff = 2048` (kích thước lớp ẩn trong mạng nơ-ron truyền thẳng).
     `num_layers = 6` (số lượng khối Transformer).
     `vocab_size = 1000` (kích thước tập từ vựng giả lập).

### Bước 2: Xây dựng cơ chế Multi-Head Attention với Masking
Đây là trái tim của mô hình, được gói gọn trong class `MultiHeadAttention`:
 **Q, K, V:** Tạo các ma trận trọng số tuyến tính để chiếu đầu vào thành các vector Query, Key, và Value.
 **Scaled Dot-Product Attention:** Tính toán điểm số chú ý (attention scores) bằng cách nhân ma trận Q và K, sau đó chia cho căn bậc hai của `d_k` để tránh giá trị quá lớn.
 **Causal Masking:** Áp dụng mặt nạ (mask) tam giác trên (upper triangular) chứa các giá trị âm vô cùng (`-inf`). Bước này cực kỳ quan trọng đối với Decoder để đảm bảo tại mỗi vị trí, mô hình chỉ "nhìn" thấy các từ trong quá khứ và hiện tại, không được "nhìn trộm" các từ ở tương lai.
 **Weighted Sum:** Đi qua hàm Softmax để tính trọng số và nhân với ma trận Value. Cuối cùng, gộp (concatenate) kết quả từ tất cả các heads và đưa qua một lớp tuyến tính đầu ra.

### Bước 3: Đóng gói Khối Transformer (Transformer Block)
Class `TransformerBlock` kết hợp Multi-Head Attention và mạng truyền thẳng (Feedforward Network) để tạo thành một khối hoàn chỉnh:
 **Kiến trúc Pre-norm:** Áp dụng Layer Normalization *trước* khi đưa qua khối Attention và khối Feedforward. Đây là phương pháp phổ biến trong các mô hình hiện đại giúp huấn luyện ổn định hơn.
 **Feedforward Network (FFN):** Gồm 2 lớp tuyến tính và hàm kích hoạt ReLU ở giữa để mở rộng không gian đặc trưng.
 **Residual Connections:** Sử dụng các kết nối tắt (cộng trực tiếp đầu vào với đầu ra của mạng: `x = x + Layer(x)`) giúp giải quyết vấn đề triệt tiêu đạo hàm khi huấn luyện mạng sâu (Residual Stream).

### Bước 4: Hoàn thiện Mô hình Transformer Decoder
Class `TransformerDecoder` là lớp ngoài cùng, kết nối tất cả các thành phần lại với nhau:
 **Embeddings:** Nhận vào các chỉ số (indices) của token và biến đổi chúng thông qua hai lớp: 
     `token_embedding`: Biểu diễn ý nghĩa của từ.
     `pos_embedding`: Biểu diễn vị trí của từ trong câu. Hai vector này được cộng lại với nhau (Composite Embeddings).
 **Xếp chồng các khối (Stacked Blocks):** Dữ liệu đi qua lần lượt 6 khối `TransformerBlock` đã định nghĩa ở bước 3.
 **Language Modeling Head (LM Head):** Lớp tuyến tính cuối cùng dùng để dự đoán xác suất của từ tiếp theo.
 **Weight Tying:** Mô hình áp dụng kỹ thuật chia sẻ trọng số (gắn trọng số của `lm_head` bằng với trọng số của `token_embedding`), giúp giảm thiểu lượng tham số đáng kể mà vẫn giữ được hiệu suất.

### Bước 5: Chạy Demo (Forward Pass)
Phần cuối của file dùng để kiểm tra tính đúng đắn của code bằng cách chạy thử một luồng dữ liệu giả lập:
 Khởi tạo một mô hình hoàn chỉnh dựa trên các siêu tham số ở Bước 1.
 Tạo một tensor ngẫu nhiên đóng vai trò là batch dữ liệu đầu vào (Kích thước: `4 x 8` - 4 câu, mỗi câu 8 từ).
 Đưa dữ liệu chạy qua mô hình (Forward pass) và trả về tensor `logits` có kích thước `[4, 8, 1000]` (tương ứng `[Batch_Size, Context_Length, Vocab_Size]`).
 Lấy vector ở vị trí cuối cùng của chuỗi, áp dụng hàm Softmax để tính toán phân bố xác suất và tìm ra token có khả năng xuất hiện cao nhất tiếp theo (ví dụ output trong demo trả về token có index là `85`).

## 3. Tổng kết
Bản thực hành đã thành công trong việc minh họa một luồng làm việc đầy đủ của kiến trúc Transformer Decoder dùng cho bài toán Language Modeling. Cấu trúc mã nguồn được tổ chức theo hướng đối tượng (OOP) rất rõ ràng, bám sát các khái niệm cốt lõi như Causal Masking, Residual Connections, Pre-norm và Weight Tying.