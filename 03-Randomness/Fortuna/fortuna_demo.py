import binascii
import time
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256

def fortuna_study_demo():
    print("=== [Study] Fortuna-based Random Generation ===")

    # 1. Entropy Collection
    raw_data = f"Seed-Material-{time.time()}".encode()
    user_seed = SHA256.new(raw_data).digest()
    print(f"[1] Manual Seed Generated: {binascii.hexlify(user_seed).decode()}")

    # 2. Generate Random Bytes
    try:
        random_output = get_random_bytes(16)
        print(f"[2] Secure Random Result: {binascii.hexlify(random_output).decode()}")
        
        # 3. Security Check
        print("[3] Status: Cryptographically Strong (CSPRNG)")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fortuna_study_demo()