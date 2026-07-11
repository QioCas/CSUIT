### Decomposition

Chia nhỏ bài toán lớn thành các bài toán nhỏ hơn.
Với expect bài toán nhỏ hơn dễ giải quyết.

Dùng cây để biểu diễn kết qủa Decomposition, cây nói về cách phân rả bài toán .
problem. 
component of problem: input, output, requirement (expect output), constraint (expect input).

Mỗi node trên cây là một problem.

Kiểm tra tính logic và khả thi của bài toán.

when stop?
khi problem đó có gỉai pháp.
**có giải pháp, có gỉai pháp thỏa mãn yêu cầu.**
Tìm ra kết qủa thỏa mãn yêu cầu. 
Chính yêu cầu quyết định độ phức tạp của bài toán.

Đố sau của cấi cây thể hiện độ phức tạp của gỉai pháp.

Càng sau thì làm chủ gỉai pháp càng cao.

cây logic chặt chẽ trong luồn input, output. 

input của $P_2$ sẽ là output của $P_1, \ldots, P_n$ hoặc input của $P$. Trường hợp đặc biệt là nguồn từ external sources.

output của $P_2$ sẽ là output của những thằng $P_{2.1}, \ldots, P_{2.k}$.

Yêu cầu của thầy, là thầy nhìn cái cây để thầy đánh giá được tính khả thi của giải pháp.

