**NLP Chapter 5: Word Embeddings Demo**

Dữ liệu thực tế được sử dụng để huấn luyện mô hình là tập IMDB Dataset of 50K Movie Reviews từ Kaggle.



**Nội dung Demo**

Notebook Chapter5\_Embeddings\_Demo.ipynb minh họa 5 nội dung chính:

Count-based Embeddings \& Cosine Similarity: Xây dựng ma trận từ vựng đếm đồng xuất hiện cơ bản và tính độ tương đồng Cosine.

Dense Embeddings với Word2Vec: Huấn luyện mô hình nhúng từ (Skip-gram) bằng thư viện gensim.

Thuộc tính Ngữ nghĩa (Semantic Properties): Tìm từ đồng nghĩa và thực hiện các phép loại suy (Analogy), ví dụ: king - man + woman = queen.

Trực quan hóa (Visualization): Dùng thuật toán t-SNE để giảm chiều và vẽ đồ thị phân bố các vector từ trên không gian 2D.

Thiên vị trong AI (Bias in Embeddings): Khám phá định kiến giới tính/nghề nghiệp ẩn trong các pre-trained embeddings (ví dụ GloVe).



**Cài đặt (Installation)**

Đảm bảo đã cài đặt Python (>= 3.7). Cài đặt các thư viện cần thiết thông qua pip:

code

Bash

pip install pandas numpy nltk gensim scikit-learn matplotlib

Tải dữ liệu:

Truy cập Kaggle IMDB Dataset.

Tải về và giải nén file IMDB Dataset.csv.

Đặt file CSV này vào cùng thư mục với file notebook.



**Hướng dẫn chạy code**

Có thể chạy dự án này trên môi trường Local, Google Colab hoặc Kaggle Notebook:

Cách 1: Chạy Local (Jupyter Notebook)

Mở terminal/command prompt tại thư mục chứa code.

Khởi chạy Jupyter: jupyter notebook

Mở file Chapter5\_Embeddings\_Demo.ipynb và chạy lần lượt từng cell (Shift + Enter).

Cách 2: Chạy trực tiếp trên nền tảng Kaggle

Tạo một Notebook mới trên Kaggle.

Ở menu bên phải, chọn Add Data, tìm kiếm IMDB Dataset of 50K Movie Reviews và thêm vào.

Upload file .ipynb này lên Kaggle (hoặc copy nội dung) và ấn Run All.

