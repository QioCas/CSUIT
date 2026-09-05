# ViMedNer: Sequence Labeling for Vietnamese Medical Entities

Dự án này thực hiện nhận diện thực thể y tế trên tiếng Việt (Medical NER) bằng cách so sánh hai mô hình **Hidden Markov Model (HMM)** và **Conditional Random Fields (CRF)**.

---

## 1. Dữ liệu

Dữ liệu được lấy từ bộ **ViMedNer** thông qua GitHub.  
Dữ liệu được gán nhãn theo định dạng **BIO** với các thực thể chính:

- `ten_benh`: Tên bệnh
- `trieu_chung_benh`: Triệu chứng
- `bien_phap_chan_doan`: Biện pháp chẩn đoán
- `bien_phap_dieu_tri`: Biện pháp điều trị
- `nguyen_nhan_benh`: Nguyên nhân gây bệnh

---

## 2. Các mô hình triển khai

### Hidden Markov Model (HMM)

- Sử dụng thuật toán **Viterbi** để tìm chuỗi nhãn tối ưu.
- Được huấn luyện bằng `HiddenMarkovModelTagger` từ thư viện **NLTK**.

### Conditional Random Fields (CRF)

- Sử dụng thuật toán tối ưu hóa **L-BFGS**.
- Các đặc trưng trích xuất bao gồm:
  - Chữ thường
  - Viết hoa
  - Chữ số
  - Hậu tố (2–3 ký tự)
  - Từ vựng xung quanh

---

## 3. Kết quả thực nghiệm

Dưới đây là bảng so sánh chỉ số trung bình (**Weighted Avg**) từ kết quả chạy thực tế:

| Mô hình | Precision | Recall | F1-Score |
|----------|------------|--------|----------|
| HMM | 0.60 | 0.65 | 0.62 |
| CRF | 0.70 | 0.61 | 0.65 |

---

## 4. Nhận xét

- CRF cho kết quả tổng thể (**F1-score**) tốt hơn HMM nhờ khả năng học đặc trưng ngữ cảnh đa dạng.
- Cả hai mô hình đều đạt hiệu quả cao nhất ở thực thể `ten_benh` và thấp nhất ở thực thể `nguyen_nhan_benh`.