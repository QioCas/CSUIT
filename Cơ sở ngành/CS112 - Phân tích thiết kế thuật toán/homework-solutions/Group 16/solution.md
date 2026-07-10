# Group 16's homework solution


## Mô tả thuật toán

Ý tưởng chính của thuật toán sẽ bao gồm 3 giai đoạn:
- Quét xoáy quanh địa điểm ban đầu
- Quét quanh viền bao lồi
- Quét xoáy quanh địa điểm vùng đặc biệt, khi ta đã tìm được một boss từ vùng đó

### Giai đoạn 1: Vòng xoáy ban đầu

Ban đầu, khi số lượng điểm chưa đủ, ta sẽ quét quanh điểm khởi đầu theo hình dạng xoáy, khi thu thập đủ điểm để tạo được bao lồi thì mới bắt đầu vào giai đoạn chính để tìm vùng đặc biệt 

### Giai đoạn 2: Quét quanh viền bao lồi

Khi ta đã đánh đủ boss để tạo bao lồi, ta sẽ chuyển sang giai đoạn quét quanh viền của bao lồi

Mục tiêu của phương pháp này là tiết kiệm một phần lượng tính toán so với việc quét vòng xoáy, trong quá trình quét quanh viền đượcc mở rộng của convex hull thì ta sẽ có tỉ lệ gặp dungeon mới cao hơn 

Quá trình quét của ta có 2 cơ chế cần chú ý:
- Cơ chế mở rộng bao lồi:
    - Ta sẽ tìm bao lồi của các con boss đã từng đánh qua hàm `convexHull()`
    - Từ bao lồi đó, tạo thêm các điểm nằm ở cách viền bao lồi khoảng 80 đơn vị qua hàm `expandHull()`
    - Ta sẽ đi dò thêm boss trên đường viền này theo chiều xoáy, các điểm trên đường viền nằm ở trong `patrolPath`
- Cơ chế update bao lồi
    - cứ mỗi 5 điểm đi qua, ta sẽ update danh sách các điểm viền để tiếp tục đi -> tiết kiếm chi phí tính toán hơn là update với mỗi bước đi


### Giai đoạn 3: Quét quanh vùng đặc biệt

Khi ta tìm được vùng đặc biệt, mục tiêu bây giờ là giết được nhiều boss nhất trong vùng này, nên ta đơn giản là quét đường xoáy, tương tự như giai đoạn 1

Quét đường xoáy sẽ cần lượng tính toán cao hơn, nhưng vì mục tiêu của ta là quét kĩ càng vùng đặc biệt, nên chi phí này có thể chấp nhận được, việc quét bằng convex hull có thể nhanh hơn nhưng có thể không đưa lại chính xác tốt