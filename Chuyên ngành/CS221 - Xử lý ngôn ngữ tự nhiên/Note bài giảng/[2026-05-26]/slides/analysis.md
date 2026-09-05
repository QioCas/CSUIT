# Phân tích MiniRAG trên OpenBookQA

## 1. Tổng quan

Mục tiêu của phần phân tích là đánh giá ưu và nhược điểm của MiniRAG khi áp dụng lên tập dữ liệu mới `OpenBookQA`.

Kết quả hiện có:

| Mô hình | NaiveRAG | MiniRAG |
| --- | ---: | ---: |
| GLM-Edge-1.5B-Chat | 67.60% | 57.80% |
| gemma-4-26b-a4b-it | - | 91.40% |

Điểm đáng chú ý là MiniRAG không luôn vượt baseline đơn giản. Với mô hình nhỏ `GLM-Edge-1.5B-Chat`, MiniRAG thấp hơn NaiveRAG gần 10 điểm phần trăm. Tuy nhiên, khi dùng mô hình lớn hơn, MiniRAG đạt kết quả cao hơn nhiều. Điều này cho thấy hiệu quả của MiniRAG trên OpenBookQA phụ thuộc mạnh vào cả chất lượng truy xuất và năng lực của mô hình sinh.

## 2. Ưu điểm của MiniRAG trên OpenBookQA

### 2.1 Kiến trúc đơn giản và tiết kiệm

MiniRAG được thiết kế để đơn giản hóa RAG cho các mô hình nhỏ. Thay vì dùng pipeline phức tạp, hệ thống tập trung vào hai thành phần chính:

- lập chỉ mục bằng đồ thị dị thể
- truy xuất tri thức nhẹ dựa trên cấu trúc graph

Cách này phù hợp với mục tiêu giảm chi phí tính toán nhưng vẫn giữ được khả năng khai thác quan hệ giữa các mảnh tri thức.

### 2.2 Không chỉ dựa vào so khớp văn bản

MiniRAG biểu diễn kho tri thức bằng:

- text chunks
- named entities
- relation edges

Nhờ đó, hệ thống có thể mở rộng từ thực thể trong câu hỏi sang các thực thể liên quan trong graph. Điều này hữu ích với những câu hỏi cần nối nhiều fact ngắn, vốn là đặc điểm phổ biến của OpenBookQA.

### 2.3 Vẫn tìm được một số bằng chứng liên quan

Trong failure case được phân tích, MiniRAG vẫn truy xuất được một vài fact có ích:

- `fact_1060.txt`: `some animals live in zoo exhibits`
- `fact_0622.txt`: `endangered means low in population`

Hai fact này không đủ mạnh để trực tiếp kết luận đáp án, nhưng chúng cho thấy pipeline không hoàn toàn bỏ qua vùng tri thức đúng. Vấn đề chính là các bằng chứng đúng xuất hiện quá muộn và bị bao quanh bởi nhiều bằng chứng nhiễu.

### 2.4 Có tiềm năng khi mô hình sinh đủ mạnh

Kết quả `91.40%` với `gemma-4-26b-a4b-it` cho thấy MiniRAG vẫn có thể hoạt động tốt nếu mô hình sinh đủ khả năng lọc nhiễu, nối bằng chứng và suy luận commonsense. Vì vậy, MiniRAG không thất bại tuyệt đối trên OpenBookQA; điểm yếu chủ yếu lộ rõ khi dùng mô hình nhỏ hoặc khi truy xuất bị lệch hướng.

## 3. Nhược điểm của MiniRAG trên OpenBookQA

### 3.1 Graph của OpenBookQA thưa hơn MultiHop-RAG

So sánh graph hiện tại:

| Chỉ số | OpenBookQA | MultiHop-RAG |
| --- | ---: | ---: |
| Entity nodes | 1,228 | 6,730 |
| Relation edges | 398 | 2,214 |
| Avg directly linked entities per linked chunk | 2.09 | 8.79 |
| Avg directly linked relations per linked chunk | 0.34 | 2.15 |
| Avg reachable entities within `<= 5` hops | 100.87 | 542.77 |
| Avg reachable entities within `<= 10` hops | 145.79 | 872.03 |

Các con số này cho thấy mỗi chunk của OpenBookQA có ít entity và relation trực tiếp hơn. Vùng tri thức có thể đi tới trong vài hop cũng nhỏ hơn nhiều. Khi truy xuất ban đầu chọn sai thực thể, graph thưa làm hệ thống khó phục hồi.

### 3.2 Câu hỏi trắc nghiệm làm tăng nhiễu từ distractor

Một failure case cụ thể:

- Failure ID: `120`
- Dataset: `OpenBookQA`
- Câu hỏi:

```text
Endangered pandas are sometimes
(A) accidentally dropped into volcanoes
(B) confined to enclosures to be viewed by the public
(C) found eating corn in the middle of North America
(D) made into delicious rare steaks
```

- Đáp án đúng: `B`
- MiniRAG dự đoán ban đầu: `A`
- Chạy lại dự đoán: `C`

MiniRAG trích xuất cả nội dung của các lựa chọn sai, ví dụ:

- `Volcanoes`
- `Corn`
- `Steaks`

Các distractor này có từ khóa rất rõ trong kho fact, nên chúng kéo truy xuất về các vùng tri thức sai.

### 3.3 Các phương án sai có anchor mạnh hơn phương án đúng

Các match quan trọng:

- `Corn` khớp mạnh với `CORN`, `CROPS`, `PLANTS`, `FOOD`
- `Volcanoes` khớp mạnh với `VOLCANOES`, `LAVA`, `TECTONIC PLATE`, `MAGMA`
- `Enclosures` không khớp sạch với vùng zoo/enclosure
- `Public Viewing` chỉ chạm yếu tới `ZOO EXHIBITS`

Kết quả là graph ưu tiên các vùng tri thức liên quan đến bắp và núi lửa, trong khi vùng tri thức cần cho đáp án đúng lại yếu hơn.

### 3.4 Ngữ cảnh cuối bị lệch chủ đề

Các entity được ưu tiên cao gồm:

1. `CORN`
2. `VOLCANOES`
3. `CROPS`
4. `LAVA`
5. `TECTONIC PLATE`
6. `TECTONIC PLATES`
7. `MAGMA`
8. `PLANTS`
9. `ENDANGERED`
10. `FOOD`

Trong khi đó, `ZOO EXHIBITS` chỉ xuất hiện ở hạng thấp hơn nhiều. Các chunk đầu tiên cũng tập trung vào:

- predator
- herbivore
- habitat
- volcano
- corn

Những bằng chứng này không giúp phân biệt đáp án đúng `B` với các distractor.

### 3.5 Bằng chứng đúng bị chôn trong nhiễu

Hai fact liên quan nhất:

- `some animals live in zoo exhibits`
- `endangered means low in population`

Các fact này vẫn thiếu các cầu nối quan trọng:

- pandas được giữ trong zoo/enclosure
- zoo exhibits là enclosure
- zoo exhibits phục vụ public viewing

Do đó, mô hình phải dựa vào commonsense để nối các bước còn thiếu. Nếu mô hình nhỏ hoặc ngữ cảnh quá nhiễu, khả năng chọn sai tăng lên.

### 3.6 Câu trả lời không ổn định

Việc lần đầu dự đoán `A` nhưng lần chạy lại dự đoán `C` là dấu hiệu grounding yếu:

- ngữ cảnh không ép mô hình về một đáp án rõ ràng
- nhiều distractor vẫn có tín hiệu truy xuất mạnh
- mô hình đang đoán trong một vùng bằng chứng nhiễu

Nếu MiniRAG truy xuất được chuỗi bằng chứng rõ quanh `pandas -> endangered -> zoo exhibits -> public viewing`, kết quả đáng lẽ phải ổn định hơn.

## 4. Diễn giải chính

MiniRAG có lợi khi:

- graph giàu liên kết
- entity mapping chính xác
- câu hỏi cần suy luận nhiều bước
- mô hình sinh đủ mạnh để lọc và nối bằng chứng

MiniRAG bất lợi khi:

- fact ngắn và rời rạc
- graph thưa
- distractor có từ khóa mạnh
- đáp án đúng cần commonsense bridge không có sẵn trong graph

Với OpenBookQA, graph expansion đôi khi không bổ sung tri thức hữu ích mà lại khuếch đại nhiễu. Đây là lý do MiniRAG có thể kém hơn NaiveRAG với mô hình nhỏ.

## 5. Hướng cải thiện

Một số hướng cải thiện phù hợp cho OpenBookQA:

- tách subject chính của câu hỏi khỏi nội dung các lựa chọn
- giảm trọng số truy xuất của distractor
- rerank evidence theo từng đáp án thay vì gom tất cả vào một context chung
- ưu tiên các fact giúp phân biệt giữa các lựa chọn
- lọc context cuối để loại các vùng tri thức lệch chủ đề
- thêm bước kiểm tra tính ổn định khi mô hình chọn đáp án

## 6. Kết luận

MiniRAG trên OpenBookQA cho thấy một trade-off rõ ràng. Graph retrieval giúp hệ thống có khả năng nối tri thức và khai thác quan hệ, nhưng nếu graph thưa và truy vấn bị distractor chi phối, chính bước mở rộng graph có thể đưa thêm nhiều nhiễu vào context.

Vì vậy, MiniRAG phù hợp hơn với những tập dữ liệu có cấu trúc tri thức giàu liên kết. Với OpenBookQA, cần cơ chế kiểm soát distractor và rerank evidence tốt hơn để graph retrieval thật sự tạo lợi thế so với retrieval đơn giản.
