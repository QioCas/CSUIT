conv 

3 hạng tử thì 3 phép cộng.

FxF lẻ -> số phép toán (`+,*`) 
-> flop, -> GFLOPS

stride = (1,1)

padding = 0
        = same

pooling
+ tăng tính bất biến 0 gian
thường stride = (FxF)

Cẩn thận hệ số trượt.

CLayer = COp + activation
CBlock = CLayer + pooling 

3x3x3 = 27 + thêm 1 bias là 28

Flatten 0 phải feature extraction hay classfication 

linear: f(x) = w * x + b
w là vector trọng số.

Số tham số cần học.

mạng học xâu gồm 2 hidden layer 

softmax làm hàm logistic 

tại sao phải xài $e^x$

Đếm số lớp layer có tham số


Xác định số lượng tham số

conv1:
    28x28x1 -> 6(5x5) p=same 
    28x28x6
    -> para = 6( (5x5x1 + 1) = 156
       op : (28x28x6) * (5x5x1)

pool1:
    28x28x6 -> 2x2
    14x14x6 

conv2: 
    14x14x6 -> 16 (5x5) p = 0, s = 1
    10x10x16
    -> para = 16(5x5x6 + 1)
    -> op = (10x10x16) * (5x5x6)
pool2:
    10x10x16 = 5x5x16

flatten:
    5x5x16 -> 400
fc:
    120 * (400 + 1)
    từ fc số phép toán = para 

dropout 50%
