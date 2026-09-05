import time
from groq import Groq, InternalServerError, RateLimitError, APIConnectionError

# --- Hàm inference cho Groq với cơ chế Retry ---

def infer(client, messages, model="openai/gpt-oss-120b", retries=1, delay=5):
    """
    Gửi request tới Groq với cơ chế tự động thử lại (retry) khi gặp lỗi mạng hoặc quá tải.
    """
    for attempt in range(retries):
        try:
            chat_completion = client.chat.completions.create(
                messages=messages, 
                model=model,
                temperature=0.3,   
            )
            return chat_completion.choices[0].message.content
        
        except (InternalServerError, RateLimitError, APIConnectionError) as e:
            print(f"[WARN] Groq connection issue ({type(e).__name__}), retrying ({attempt+1}/{retries})...")
            print(f"       Details: {e}")
            time.sleep(delay)
            
        except Exception as e:
            raise e

    raise RuntimeError("Groq model unavailable after multiple retries.")
