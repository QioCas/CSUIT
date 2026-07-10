# Đề bài

Lại tới một mùa thi ICPC mới tại UIT, và các thí sinh đang xếp hàng để vào phòng thi.

Trước khi vào phòng thi, BTC ICPC thông báo một tin động trời, đó là một đội có thể có bao nhiêu bạn cũng được.

Để tiếp tục giữ học bổng và có tiền ăn sáng, các bạn KHTN2024 muốn tạo ra ít đội nhất có thể để thi ICPC, giúp giảm cạnh tranh giữa các đội.


Lớp KHTN2024 có $N$ học sinh, học sinh thứ $i$ của lớp đang đứng ở vị trí thứ $x_i$ trong hàng chờ, và có chỉ số rating Codeforces là $r_i$. 

Ban đầu sẽ không ai ở trong đội nào, mỗi bạn có thể tự tạo đội mới của mình, hoặc gia nhập đội của 1 bạn khác, bạn $j$ có thể gia nhập đội của bạn $i$ nếu $i$ đã có đội và $|x_i - x_j| \le r_i - r_j$.

Bạn hãy giúp tìm số đội tối thiếu cần phải được tạo ra để ai trong $N$ bạn cũng sẽ có đội nhé.

## Input

Dòng đầu tiên chứa một số nguyên dương N $(1 \le N \le 5.10^5)$ - Số học sinh trong lớp 

$N$ dòng tiếp theo, mỗi dòng chứa $2$ số nguyên $x_i, r_i, (1 \le x_i, r_i \le 10^9)$ - vị trí và rating Codeforces của học sinh thứ $i$ trong hàng 

## Output

In ra số lượng nhóm tối thiểu cần được tạo ra sao cho học sinh nào cũng ở trong một nhóm

## Subtasks

50% số test thỏa mãn: $n \le 1000$ \
50% số test còn lại không có ràng buộc gì thêm.


## Examples 
### Input 1
```
4
4 2
2 3
3 4
6 5
```
### Output 1
```
2
```

### Input 2
```
3
7 10
10 10
7 10
```
### Output 2
```
2
```

### Giải Thích Examples 1

Thành viên thứ 3 sẽ tạo nhóm 1 và thành viên thứ 4 sẽ tạo nhóm 2.

Thành viên 1 và thành viên 2 có thể tham gia vào nhóm 1.

Thế nên số nhóm tối thiểu cần được tạo ra là 2.

### Lưu ý khi nộp code bằng python

vì input lên đến $5.10^5$ nên code bằng python sẽ chạy rất chậm, bạn có thể dùng sys.stdin.readline để đọc nhanh hơn

# Các tiêu chí đánh giá BTVN 

## Mô tả thuật toán
**Với mỗi subtask**, sẽ có các tiêu chí đánh giá sau:
- Kỹ thuật bạn sử dụng là Decrease hay Divide hay Transform and Conquer ? và thuật toán được phân loại vào phương pháp nào trong kỹ thuật ấy ?
- bạn đã có những nhận xét gì cho bài toán để sử dụng được phương pháp ấy ?
- Mô tả thuật toán cho subtask 

## Cài đặt thuật toán
**Với mỗi subtask**, sẽ có các tiêu chí đánh giá sau:
- Mô tả cách thuật toán được cài đặt trong code 
- Code đơn giản, không rườm rà

## Phân tích độ phức tạp

**Với mỗi subtask**, sẽ có các tiêu chí đánh giá sau:
- Phân tích độ phức tạp thời gian thuật toán
- Phân tích độ phức tạp không gian thuật toán



## Phổ điểm

Với mỗi subtask, sẽ có 7 tiêu chí đánh giá, tổng cộng 14 tiêu chí cho 2 subtask của bài.

Những nhóm nào có nộp cả bài tập trên WeCode và file pdf thì sẽ được tặng tiêu chí thứ 15 :D

Cách tính điểm cho BTVN:
- Điểm chấm trên wecode: 70% 
- Điểm chấm các tiêu chí: 30%

Điểm chấm các tiêu chí là 30% số điểm, và có 15 tiêu chí, nên mỗi tiêu chí sẽ tương đương với 0.2đ tổng kết 

## Kết quả chấm điểm

[Bấm vào để dẫn tới link kết qủa chấm điểm](https://docs.google.com/spreadsheets/d/1SE-oroH1WxN_Zy-XRYTmP3nGbJYc2meeKAh_AAAo8Ok/edit?gid=0#gid=0)