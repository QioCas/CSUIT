import pandas as pd

def read(path):
    df = pd.read_json(path, lines=True)
    # Trả về list of dicts để vòng lặp for bên main.py chạy được
    return df.to_dict('records') 

def write(path, data):
    """
    Ghi dữ liệu ra file JSONL.
    Chấp nhận đầu vào là List of Dicts HOẶC Pandas DataFrame.
    """
    # Bước quan trọng: Nếu data là list, chuyển nó thành DataFrame
    if isinstance(data, list):
        df = pd.DataFrame(data)
    else:
        df = data
        
    # force_ascii=False để không bị lỗi font Tiếng Việt
    df.to_json(path, orient='records', lines=True, force_ascii=False)