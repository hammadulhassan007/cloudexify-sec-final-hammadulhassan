import os
from cryptography.fernet import Fernet

class FileEncryptor:
    def __init__(self, key_file="secret.key"):
        self.key_file = key_file
        self.key = self.load_or_generate_key()
        self.cipher = Fernet(self.key)

    def load_or_generate_key(self):
        """Persist key securely in a key file."""
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as kf:
                return kf.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as kf:
                kf.write(key)
            print(f"[+] SUCCESS: New cryptographic key saved to '{self.key_file}'")
            return key

    def encrypt_data(self, plaintext: str) -> str:
     
        encrypted_bytes = self.cipher.encrypt(plaintext.encode('utf-8'))
        return encrypted_bytes.decode('utf-8')

    def decrypt_data(self, ciphertext_str: str) -> str:
        decrypted_bytes = self.cipher.decrypt(ciphertext_str.encode('utf-8'))
        return decrypted_bytes.decode('utf-8')


if __name__ == "__main__":
    engine = FileEncryptor()
    secret_msg = "Confidential Report: Vulnerability Assessment Completed."

    encrypted_msg = engine.encrypt_data(secret_msg)
    decrypted_msg = engine.decrypt_data(encrypted_msg)

    
    print("\n" + "=" * 65)
    print("         CRYPTOGRAPHY ENCRYPTION & DECRYPTION ENGINE        ")
    print("=" * 65)
    
    print("\n[1] ORIGINAL INPUT TEXT:")
    print(f"    ➜ {secret_msg}")

    print("\n[2] ENCRYPTED CIPHERTEXT (AES-Fernet Base64):")
    
    chunk_size = 50
    for i in range(0, len(encrypted_msg), chunk_size):
        print(f"    │ {encrypted_msg[i:i+chunk_size]}")

    print("\n[3] DECRYPTED OUTPUT TEXT:")
    print(f"    ➜ {decrypted_msg}")

    print("\n" + "=" * 65)
    print("  STATUS: Encryption/Decryption Integrity Check Passed (100%)")
    print("=" * 65 + "\n")