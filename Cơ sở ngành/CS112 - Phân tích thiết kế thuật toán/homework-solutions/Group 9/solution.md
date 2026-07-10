# Bài 1
Độ phức tạp được sắp xếp theo thứ tự tăng dần khi $n \to \infty$ (từ nhanh nhất đến chậm nhất):

$O(1) \subset O(logn) \subset O(n) \subset O(nlogn) \subset O(n^2) \subset O(n^3) \subset O(2^n) \subset O(n!) $

# Bài 2

Với $n \ge 1$, ta có: $5n^2 + 3n + 1 \le 5n^2 + 3n^2 + 1n^2 = 9n^2$\
=> nên ta chọn $c_2 = 9$ và $n_0 = 1$.

Với $n \ge 1$, ta có: $5n^2 \le 5n^2 + 3n + 1$.\
=> nên ta chọn $c_1 = 5$ và $n_0 = 1$.

Vậy ta có: $5n^2 + 3n + 1 = \Theta(n^2)$.

# Bài 3

Ta Thấy vòng lặp ngoài lặp theo cấp số nhân mũ $2$, nên số lần lặp sẽ là $k \approx log_2{n}$

Vòng lặp ở trong lặp từ $1$ đến giá trị $i$ hiện tại

Nên ta có thể tính số lần thực thi của lệnh theo công thức:

$T(n) = 1 + 2 + 4 + \ldots + 2^k = 2^{k + 1} - 1$

vì $k \approx log_2{n}$ nên $2^{k + 1} - 1 \approx 2 * n - 1$

Vậy độ phức tạp thuật toán là $T(n) = O(n)$


# Bài 4

Ta áp dụng 4 quy tắc phân tích:
- Bỏ qua hằng số nhân -> $T(n) = n^2 + n + logn + 20$
- Bỏ qua hằng số cộng -> $T(n) = n^2 + n + logn$
- Bỏ qua các số hạng bậc thấp -> sau so sánh thì ta thấy $n^2$ có độ tăng trưởng cao nhất nên bỏ $n$ và $logn$
- Giữ lại phần có độ tăng trưởng cao nhất -> $T(n) = O(n^2)$

Vậy độ phức tạp tiệm cận của $T(n)$ là $O(n^2)$


