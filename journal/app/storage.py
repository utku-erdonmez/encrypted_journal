import os
import shutil
from app.crypto import encrypt, decrypt

FILE = "journal.enc"

def load_data(password):
    if not os.path.exists(FILE):
        return {"entries": []}

    with open(FILE, "rb") as f:
        blob = f.read()

    return decrypt(blob, password)

def save_data(data, password):
    blob = encrypt(data, password)
    
    temp_file = FILE + ".tmp"
    backup_file = FILE + ".bak"

    # 1. ESKİ DOSYAYI YEDEKLE
    # Eğer asıl dosya varsa, kaydetmeden önce güvenli bir kopyasını alıyoruz.
    if os.path.exists(FILE):
        shutil.copy2(FILE, backup_file)

    # 2. yaz
    with open(temp_file, "wb") as f:
        f.write(blob)

    # 3. YER DEĞİŞTİRME
    # Geçici dosyanın adını asıl dosyanın adı ile değiştiriyoruz. 
    os.replace(temp_file, FILE)