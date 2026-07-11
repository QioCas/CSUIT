Step by step hướng dẫn các bước để tạo website cơ bản.

```cmd
mkdir similar_items
cd simiarl_items
mkdir backend
cd backend
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn

```

Ta sẽ tạo file main.py với nội dung cơ bản sau:

```py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "FastAPI is running"}
```

Ta đã tạo xong local host backend, giờ ta sẽ tạo frontend.


```
npm create vite@latest frontend
```

Chọn option là React and JavaScript.

Chỉnh sửa home page ở `src/App.jsx`.
