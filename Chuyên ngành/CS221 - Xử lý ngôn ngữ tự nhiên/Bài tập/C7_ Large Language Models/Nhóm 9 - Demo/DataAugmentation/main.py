import time
import os
from tqdm import tqdm
from groq import Groq
from dotenv import load_dotenv

# --- CÁC MODULE CỦA BẠN ---
import JSONL
import inference
import RandomFewshotPrompt

# --- 1. LOAD API KEY TỪ .env ---
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ Không tìm thấy GROQ_API_KEY trong file .env")

# Tạo 1 client duy nhất
client = Groq(api_key=GROQ_API_KEY)

# --- 2. CẤU HÌNH ---
data_path = r"train.jsonl"
output_path = r"augmentated_train.jsonl"

MODEL_NAME = "openai/gpt-oss-120b"

start_idx = 1
end_idx = 150

SLEEP_TIME = 5          # thời gian nghỉ giữa mỗi request
RETRY_TIMES = 3         # số lần retry nếu lỗi
AUTOSAVE_EVERY = 50     # autosave mỗi N sample

# --- 3. ĐỌC DỮ LIỆU ---
print(f"📂 Đang đọc dữ liệu từ: {data_path}")
data = JSONL.read(data_path)

processing_data = data[start_idx:end_idx]

augmented_posts = []

print(f"🚀 Bắt đầu xử lý {len(processing_data)} dòng dữ liệu...\n")

# --- 4. HÀM GỌI MODEL CÓ RETRY ---
def call_model_with_retry(messages):
    for attempt in range(RETRY_TIMES):
        try:
            result = inference.infer(
                client=client,
                messages=messages,
                model=MODEL_NAME
            )
            return result
        except Exception as e:
            print(f"[⚠️ Retry {attempt+1}/{RETRY_TIMES}] Lỗi: {e}")
            time.sleep(5)
    return None


# --- 5. XỬ LÝ CHÍNH ---
try:
    for post in tqdm(processing_data, desc="Enriching Context"):

        if post.get('conspiracy') not in ['Yes', 'No']:
            continue

        try:
            time.sleep(SLEEP_TIME)

            # A. Tạo prompt
            messages_payload = RandomFewshotPrompt.build_augmentation_messages_from_jsonl(
                data_path,
                post['conspiracy']
            )

            # B. Gọi model (có retry)
            result = call_model_with_retry(messages_payload)

            # C. Lưu kết quả
            if result and isinstance(result, str):
                new_post = {
                    "_id": "new",
                    "text": result,
                    "conspiracy": post['conspiracy']
                }
                augmented_posts.append(new_post)
            else:
                print(f"[⚠ WARN] Kết quả rỗng cho post ID: {post.get('_id')}")

            # D. Autosave
            if len(augmented_posts) % AUTOSAVE_EVERY == 0 and len(augmented_posts) > 0:
                JSONL.write(output_path, augmented_posts)
                print(f"\n💾 Autosave: {len(augmented_posts)} dòng")

        except Exception as e:
            print(f"[❌ ERROR] Post ID {post.get('_id')}: {e}")
            time.sleep(2)

except KeyboardInterrupt:
    print("\n⛔ Dừng bằng tay! Đang lưu dữ liệu...")
    JSONL.write(output_path, augmented_posts)
    print(f"💾 Đã lưu {len(augmented_posts)} dòng an toàn.")
    exit()

# --- 6. LƯU CUỐI ---
print(f"\n💾 Đang lưu {len(augmented_posts)} kết quả...")
JSONL.write(output_path, augmented_posts)

print("✅ Hoàn tất toàn bộ quá trình.")