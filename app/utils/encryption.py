import hashlib
import os

def generate_encrypted_url(file_id: int):
    salt = os.getenv("SECRET_KEY")
    hash_object = hashlib.sha256(f"{file_id}{salt}".encode())
    return hash_object.hexdigest()