Giải pháp 1: cùng cat.
pro: Tương tự (nhu cầu)
con: Không chắc mua kèm.

Giải pháp 2: mua chung
pro: được kiểm chứng thực tế
con: không chắc là tương tự.

Giải pháp 3: kết hợp lại 1&2
domain knowledge: 
- Sữa: step 1 -> step 2 -> ... -> step 5

- Tả: NB -> S -> M -> L -> XL -> XXL
- piece: nhỏ -> lớn

$$score = co_{buy score} * cat_{score} * size_{score} * piece_{score} * step_{score}$$

o_buy_score là A B xuất hiện chung mấy lần cùng giỏ hàng.

cat_score = 1 / 0.5 / 0.25 / 0.125 

$$size_{score} = \exp(-w_1 * \max(0, X_{size} - A_{size}) - w_2 * \max(0, A_{size} - X_{size}))$$


w_1 = 1.5, w_2 = 0.5

piece_score cũng vậy

step_score y chang
