from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from dotenv import load_dotenv
import os
import base64

# Load .env variables
load_dotenv()

# Load and decode the base64 AES key
key_b64 = os.getenv("ENCRYPTION_KEY")
if not key_b64:
    raise ValueError("ENCRYPTION_KEY not found in .env file")
key = base64.b64decode(key_b64)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# AES encryption
def encrypt_text(plain_text: str) -> str:
    iv = os.urandom(16)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plain_text.encode()) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return base64.b64encode(iv + encrypted_data).decode()

# AES decryption with friendly error
def decrypt_text(encrypted_text: str) -> str:
    try:
        # Check if the input is valid base64
        try:
            encrypted_data = base64.b64decode(encrypted_text, validate=True)
        except Exception:
            return "[BASE64_ERROR]"
        
        if len(encrypted_data) <= 16:
            return "[DECRYPT_ERROR]"

        iv = encrypted_data[:16]
        ciphertext = encrypted_data[16:]

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        plain_text = unpadder.update(decrypted_data) + unpadder.finalize()

        return plain_text.decode()

    except Exception:
        return "[DECRYPT_ERROR]"


@app.get("/", response_class=HTMLResponse)
async def index():
    with open("index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.post("/encrypt")
async def encrypt(text: str = Form(...)):
    encrypted_text = encrypt_text(text)
    return {"encrypted_text": encrypted_text}

@app.post("/decrypt")
async def decrypt(text: str = Form(...)):
    decrypted_text = decrypt_text(text)
    return {"decrypted_text": decrypted_text}
