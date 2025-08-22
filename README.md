# Text Encryption & Decryption Using Cryptographic Algorithms (AES)

This project provides a web-based application for **text encryption** and **decryption** using **AES (Advanced Encryption Standard)** with **CBC (Cipher Block Chaining)** mode. The application allows users to securely encrypt and decrypt text via a simple user interface.

## Features

* **AES Encryption (CBC mode)**: Encrypts plain text into secure ciphertext.
* **Decryption**: Decrypts AES-encrypted text (base64 encoded).
* **Base64 Encoding**: Encrypted text is base64 encoded for easy storage and transmission.
* **Error Handling**: Proper error messages for invalid base64 or corrupted ciphertext.

## Technologies Used

* **FastAPI**: Backend web framework for building APIs.
* **Cryptography Library**: For AES encryption and decryption.
* **HTML/CSS/JavaScript**: Frontend user interface.
* **dotenv**: For securely storing environment variables (like the encryption key).

## Setup Instructions

Follow these steps to run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/JV-Vigneesh/Text-Encryption-Using-Cryptographic-Algorithms.git
cd your-repository-name
```

### 2. Create a Virtual Environment

It's best to run the project inside a virtual environment to manage dependencies.

```bash
python -m venv venv
```

### 3. Install Dependencies

Activate your virtual environment and install the required dependencies.

#### For Windows:

```bash
venv\Scripts\activate
```

#### For macOS/Linux:

```bash
source venv/bin/activate
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File

In the root directory of the project, create a `.env` file to store your AES encryption key.

```plaintext
ENCRYPTION_KEY=your_base64_encoded_key_here
```

You can generate a base64-encoded AES key using Python:

```python
import os
import base64

key = os.urandom(32)  # 32 bytes = 256 bits for AES-256
print(base64.b64encode(key).decode('utf-8'))
```

Paste the base64-encoded key into the `.env` file.

### 5. Run the Application

Start the FastAPI server by running:

```bash
uvicorn main:app --reload
```

The server will be available at `http://127.0.0.1:8000`.

### 6. Access the Web Application

Open your browser and navigate to `http://127.0.0.1:8000`. You should see the **Text Encryption & Decryption** page.

## How to Use

### Encrypt Text

1. Enter the text you want to encrypt in the "Enter text to encrypt..." input box.
2. Click the "Encrypt" button.
3. The encrypted text will appear in the "Encrypted Text" field in base64 format.
4. You can copy the encrypted text by clicking the "Copy Encrypted" button.

### Decrypt Text

1. Copy the base64-encoded encrypted text and paste it into the "Enter text to decrypt..." input box.
2. Click the "Decrypt" button.
3. The decrypted text will appear in the "Decrypted Text" field.

### Error Handling

* **Invalid Base64**: If you input a corrupted or invalid base64 string, you'll see an error message: "⚠️ Invalid base64 input."
* **Decryption Errors**: If the ciphertext cannot be decrypted (e.g., due to tampering), you'll see: "⚠️ The encrypted input seems corrupted or tampered with."

## Security Considerations

* **AES Key**: The AES encryption key is loaded from the `.env` file. In a production environment, consider using a key management service or storing the key more securely.
* **IV (Initialization Vector)**: A random 16-byte IV is generated for each encryption operation to ensure that the same plaintext produces different ciphertexts.

## Project Structure

```plaintext
.
├── .env                # Environment variables (for storing the AES key)
├── index.html          # Frontend HTML for user interaction
├── main.py             # FastAPI application and encryption logic
├── requirements.txt    # Python dependencies
├── static/
│   └── styles.css      # Custom CSS styles for the frontend
└── README.md           # Project documentation
```

## License

This project is licensed under the MIT License.
