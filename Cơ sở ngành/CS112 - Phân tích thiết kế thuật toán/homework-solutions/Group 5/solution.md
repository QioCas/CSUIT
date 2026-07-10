
## Subtask 1 $(n, q \le 1000)$
### Mô tả Thuật Toán

> **Quan sát 1:**
> - Ta có thể biến đổi bài toán thành bài toán đồ thị

Cụ thể:
- Ta coi mỗi máy tính là một đỉnh của đồ thị. 
- Nếu có thể truyền dữ liệu trực tiếp giữa $2$ máy tính $u$ và $v$ thì tồn tại một cạnh ($u$ $v$) có trọng số $|u - v|$
- Lúc này, bài toán trở thành tìm kiếm đường đi có tổng trọng số nhỏ nhất (đường đi tối ưu) đi từ $s$ đến $t$.


Định nghĩa: 
+ Độ dài đường đi là số lượng cạnh đi qua của đường đi đó.
+ Gọi $E$ là tập cạnh của độ thị. Nếu cạnh $(u, v)$ thuộc đồ thị ta nói $(u, v) \in E$, ngược lại $(u, v) \not \in E$.

 
> **Nhận xét 1:**
> -  Nếu $s \not = t$ và $(s, t) \in E$ thì độ dài đường đi tối ưu bằng $1$.

Chứng minh:
- Xét đường đi trực tiếp đi từ $s$ đến $t$, thì chi phí bằng $|s - t|$.
- Xét đường đi thông qua một đỉnh trung gian $u$ ($(s, u)$, $(u, t)$ $\in E$ ), thì chi phí bằng $|s - u| + |u - t|$.
    + Đặt $a = s - u$, $b = u - t$.
    + Theo bất đẳng thức tam giác:
    + $|a + b| \le |a| + |b|$ 
    + $\Leftrightarrow$ $|s - u + u - t| \le |s - u| + |u - t|$ 
    + $\Leftrightarrow$ $|s - t| \le  |s - u| + |u - t|$ 
- Xét đường đi thông qua hai đỉnh trung gian $u$ $v$ (($s, u$), ($u, v$) và ($v, t$) $\in E$), thì chi phí bằng $|s - u| + |u - v| + |v - t|$.
    - Theo bất đẳng thức tam giác: $|s - t| \le |s - u| + |u - t| \le |s - u| + |u - v| + |v - t|$.
- Tương tự với mọi đường đi qua $k$ đỉnh trung gian $u_1 \ldots u_k$ (($s$ $u_1$) ($u_i$ $u_{i+1}$) ($u_k$ $t$) $\in E$) $\forall i < k$, 
    - Ta có công thức: $|s - t| \le \ldots \le |s - u_1| + \sum_{i=1}^{k-1}|u_i - u_{i+1}| + |u_k - t|$
Từ đó, ta kết luận đường đi tối ưu là đi trực tiếp từ $s$ đến $t$ với chi phí là $|s-t|$. Độ dài đường đi tối ưu bằng $1$.

 

> **Nhận xét 2:**
> - Độ dài đường đi có tổng trọng số nhỏ nhất đi từ $s$ đến $t$ không quá  $2$.

Chứng minh:

##### $1$. Nếu $s = t$
Đường đi tối ưu có chi phí đúng bằng $|s - t| = 0$. Độ dài đường đi tối ưu bằng $0$.

##### $2$. Nếu $s \not = t$ và $(s, t) \in E$
Từ nhận xét $1$ độ dài đường đi tối ưu có độ dài bằng $1$.


##### $3$. Nếu $s \not = t$ và $(s, t) \not \in E$

Gọi tập giao thức là $\mathcal{P}=\{B,G,R,Y\}$.
Mỗi đỉnh chứa một tập giao thức $|\mathcal{P_i}| = 2$, $\mathcal{P_i} \in P$.
Nếu $(u, v) \in E$ thì $\mathcal{P_u} \cap \mathcal{P_v} \not = \varnothing$. Ngược lại, $\mathcal{P_u} \cap \mathcal{P_v} = \varnothing$


Từ nhận xét $1$, ta có chứng minh đường đi tối ưu luôn có dạng:
$$\{ u_1, u_2, \ldots, u_k \}$$ 
với $k > 2, s = u_1, t = u_k$ và $|\mathcal{P_{i}} \cap \mathcal{P_{i+1}}| = 1$ ($\forall i < k$) luôn thỏa mãn điều kiện:

- Với $\forall i < k, j \in [i + 2, k]$ thì $(u_i, u_j) \not \in E$ hay  $\mathcal{P_i} \cap \mathcal{P_j} = \varnothing$
Ta có thể dễ dàng chứng minh điều này từ nhận xét $1$:
Nếu tồn tại  $i < k, j \in [i + 2, k]$ mà $(u_i, u_j) \not \in E$, thì $cost(\{i, j\}) \le cost(\{i, i+1, \ldots, j\})$
$\Rightarrow$ $cost(\{u_1, u_2, \ldots, u_i, u_j, \ldots u_k\}) \le cost(\{u_1, u_2, \ldots, u_k\})$. 
$\Rightarrow$ $\{u_1, u_2, \ldots, u_k\}$ không tối ưu.

Xét đường đi tối ưu $\{s = u_1, u_2, u_3 = t\}$:
+ Để tồn tại đường đi thỏa mãn, cần tồn tại $u_2$ sao cho:
    + $|\mathcal{P_s} \cap \mathcal{P_{u_2}}| = 1$, $|\mathcal{P_{u_2}} \cap \mathcal{P_{t}} |= 1$ 
$\Rightarrow$ $P_{u_2} = \{a, b\}$ với  $a \in \mathcal{P_s}, b \in \mathcal{P_t}$.

Xét đường đi tối ưu $\{s = u_1, u_2, u_3, u_4 = t\}$:
+ Để tồn tại đường đi thỏa mãn, cần tồn tại $u_2$, $u_3$ sao cho:
    +  $|\mathcal{P_s} \cap \mathcal{P_{u_2}}| = 1$, $|\mathcal{P_{u_2}} \cap \mathcal{P_{u_3}}| = 1$,$|\mathcal{P_{u_3}} \cap \mathcal{P_{t}} |= 1$ 
    + $\mathcal{P_{s}} \cap \mathcal{P_{u_3}} = \varnothing$ ,$\mathcal{P_{s}} \cap \mathcal{P_{t}} = \varnothing$ ,$\mathcal{P_{u_2}} \cap \mathcal{P_{t}} = \varnothing$
 + Xét $\mathcal{P_s} = \{a, b\}$
+ $\mathcal{P_{u_3}} = \{c, d\}$ (Do $\mathcal{P_{s}} \cap \mathcal{P_{u_3}} = \varnothing$).
+ $\mathcal{P_{t}} = \{c, d\}$ (Do $\mathcal{P_{s}} \cap \mathcal{P_{t}} = \varnothing$).
+ $\Rightarrow$ $\mathcal{P_{u_3}} \cup \mathcal{P_{t}} = \{c, d\}$ hay $|\mathcal{P_{u_3}} \cup \mathcal{P_{t}}| = 2$ mâu thuẫn với điều kiện: $|\mathcal{P_{u_3}} \cap \mathcal{P_{t}} |= 1$.
+ 
$\Rightarrow$ Do đó, không tồn tại đường đi thỏa mãn điều kiện.

Chứng minh tương tự với mọi $k \ge 4$.

Do đó nếu tồn tại đường đi từ $s$ đến $t$ thì độ dài đường đi tối ưu có độ đài bằng $k - 1 = 3 - 1 = 2$.


### Cài Đặt Thuật Toán

Ta sẽ biểu diễn $\mathcal{P_u}$ dưới dạng một mask 4 bit $ms_u$ (Nếu bit thứ $b$ bật thì đỉnh chứa giao thức $b+1$).

Nếu $\mathcal{P_{u}} \cap \mathcal{P_{v}} = \varnothing$ thì $ms_u \& ms_v = 0$.
Nếu $\mathcal{P_{u}} \cap \mathcal{P_{v}} \not = \varnothing$ thì $ms_u \& ms_v \not = 0$.

Với mỗi truy vấn $u, v$:
+ Nếu $u = v$ thì đán án bằng $0$.
+ Ngược lại, nếu $ms_u \& ms_v \not = 0$ thì đán án bằng $|u - v|$.
+ Ngược lại, đán án bằng $\min_{k=1}^{n}|k - u| + |k - v|$ với $ms_u \& ms_k \not = 0$, $ms_v \& ms_k \not = 0$ nếu tồn tại $k$ thỏa mãn.
+ Ngược lại, in $-1$.

### Phân Tích Độ Phức Tạp

#### Độ phức tạp thời gian

Ở bước **tiền xử lý**, ta cần xây dựng mảng $ms_u$ với số phép thao tác là $2 \cdot n$. Do đó độ phức tạp là $\Theta (n)$.
Ở mỗi truy vấn, $2$ trường hợp đầu ta chỉ mất một thao tác thực hiện, nhưng với trường hợp thứ ba, ta mất $n$ thao tác để duyệt mọi phần tử trong mảng, do đó mất độ phức tạp $\Theta (n)$.
Tổng độ phức tạp **xử lý các truy vấn** là $\Theta (q * n)$.

**Độ phức tạp thời gian** của bài toán là $<\Theta(n), \Theta(q * n)>$ hay $\Theta(n + q * n)$

#### Độ phức tạp không gian

Ở bước **tiền xử lý, ta cần tạo một mảng $ms_u$ do đó mất độ phức tạp không gian là $\Theta(n)$.
Ở bước xử lý truy vấn, ta không tạo thêm gì nên độ phức tạp không gian là $\Theta (1)$.

**Độ phức tạp không gian** của bài toán là $<\Theta(n), \Theta(1)>$ hay $\Theta(n)$.

## Subtask 2 $(n, q \le 10^5)$

### Mô tả Thuật Toán

Không mất tính tổng quát, ta giả sử $s \le t$.
> **Nhận xét 4**:
> Nếu $(s, t) \not \in E$ và tồn tại đường đi tối ưu thì đường đi tối ưu $\{s, u, t\}$ có $u$ là đỉnh gần $s$ nhất hoặc gần $t$ nhất về bên trái hoặc về bên phải.
> Nói cách khác, Gọi:
> + $L[x]$ là vị trí lớn nhất sao cho $L[x] < s, |\mathcal{P_{L[x]}} \cap \mathcal{P_{s}}| = 1$. 
> + $R[x]$ là vị trí nhỏ nhất sao cho $R[x] \ge s, |\mathcal{P_{R[x]}} \cap \mathcal{P_{s}}| = 1$.
> Đường đi tối ưu $\{s, u, t\}$ có $u \in \{L[s], R[s], L[t], R[t]\}$.

Chứng minh:

Xét $3$ trường hợp của $u$:

+ Nếu $u \le s$ thì:
    $s - L[s] \le s - i$ $\forall i \le s, |\mathcal{P_i} \cap \mathcal{P_s}| = 1$.
    $\Rightarrow$ $u = L[s]$.

+ Nếu $s \le u \le t$ thì:
    Mọi $u$ thỏa mãn đều tạo ra đường đi tối ưu.
    $\Rightarrow$ $u = R[s]$ hoặc $u = L[t]$ đều thỏa mãn.

+ Nếu $t \le u$ thì:
    $R[t] - t \le i - t$ $\forall t \le i, |\mathcal{P_t} \cap \mathcal{P_i}| = 1$.
    $\Rightarrow$ $u = R[t]$.

Do đó, $u \in \{L[s], R[s], L[t], R[t]\}$.
### Cài Đặt Thuật Toán

Để xây dựng $L[x], R[x]$, trong quá trình duyệt các phần tử, ta duy trì mảng $last[4]$ lưu $2$ vị trí cuối cùng có bit thứ $b$ bật, và hai vị trí này có mask khác nhau.

Ban đầu $L[x] = -1, R[x] = n \ \forall x$.

Tại vị trí $i$, nếu bit thứ $b$ bật thì 
+ $p = last[b]$ sao cho $ms_p \not = ms_i$ (Nếu chỉ lưu một vị trí cuối ta có bị dính $ms_{last[b]} = ms_i$, do đó ta phải lưu $2$ vị trí).
+ `L[i] = max(L[i], p), R[p] = min(R[p], i)`
+ Cuối cùng, ta cập nhật lại `last[b]`.

Sau khi đã xác định được $L[x], R[x]$.

Tại mỗi truy vấn, nếu $s = t$ hoặc $(s, t) \in E$ thì ta làm tương tự subtask 1. 
Trường hợp còn lại, ta chỉ cần duyệt $u \in \{L[s], R[s], L[t], R[t]\}$ và tìm $\min |u - s| + |u - t|$ nếu thỏa mãn điều kiện $ms_u \& ms_s \not = 0$ và $ms_u \& ms_t \not = 0$.

### Phân Tích Độ Phức Tạp

#### Độ phức tạp thời gian

Ở bước **tiền xử lý**:
+ Đầu tiên, ta cần xây dựng mảng $ms_u$ với số phép thao tác là $2 \cdot n$. 
+ Tiếp theo, để khởi tạo mảng $L[x]$ và $R[x]$, ta duyệt qua $n$ phần tử, với mỗi phần tử ta kiểm tra tại $2$ bit bật (số phép thao tác là $4$), tại mỗi bit bật ta kiểm tra tối đa $2$ vị trí trong $last[b]$ để tìm $p$ thỏa mãn (số thao tác tại mỗi bit bậc là $2$). Do đó, tổng số phép thao tác để khởi tạo mảng $L[x], R[x]$ là $(4 + 2 \cdot 2) * n = 8 \cdot n$.
$\Rightarrow$ Do đó tổng độ phức tạp thời gian để tiền xử lý là $\Theta(n)$.

Ở bước xử lý truy vấn:
+ Với mỗi truy vấn, $2$ trường hợp đầu ta chỉ mất $1$ thao tác thực hiện. Với trường hợp thứ ba, ta chỉ duyệt $4$ phần tử và kiểm tra điều kiện thỏa mãn. Do đó, số phép thao tác là $4$ cho mỗi truy vấn hay độ phức tạp thời gian để thực hiện mỗi truy vấn là $\Theta(1)$.
$\Rightarrow$ Do đó, độ phức tạp để thực hiện toàn bộ truy vấn là $\Theta(q)$

**Độ phức tạp thời gian** của bài toán là $<\Theta(n), \Theta(q)>$ hay $\Theta(n + q)$.

#### Độ phức tạp không gian

Ở bước **tiền xử lý**:
+ Ta cần tạo mảng $ms_u$, $L[x]$, $R[x]$ nên mất độ phức tạp không gian là $\Theta(n)$. 
+ Mảng $last[4]$ với mỗi phần tử lưu $2$ vị trí nên mất độ phức tạp không gian là $\Theta(1)$.
$\Rightarrow$ Độ phức tạp không gian ở bước tiền xử lý là $\Theta(n)$.

Ở bước xử lý truy vấn, ta không tạo thêm gì nên độ phức tạp không gian là $\Theta(1)$.

**Độ phức tạp không gian** của bài toán là $<\Theta(n), \Theta(1)>$ hay $\Theta(n)$.