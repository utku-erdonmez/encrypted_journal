import os
import json
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from argon2.low_level import hash_secret_raw, Type

## argon2
def derive_key(password: str, salt: bytes):
    return hash_secret_raw(
        secret=password.encode(),
        salt=salt,
        time_cost=3,
        memory_cost=65536,
        parallelism=1,
        hash_len=32,
        type=Type.ID
    )


def encrypt(data: dict, password: str):
    salt = os.urandom(16)
    key = derive_key(password, salt)

    aesgcm = AESGCM(key)
    nonce = os.urandom(12)

    ciphertext = aesgcm.encrypt(nonce, json.dumps(data).encode(), None)

    return salt + nonce + ciphertext


def decrypt(blob: bytes, password: str):
    salt = blob[:16]
    nonce = blob[16:28]
    ciphertext = blob[28:]

    key = derive_key(password, salt)
    aesgcm = AESGCM(key)

    return json.loads(aesgcm.decrypt(nonce, ciphertext, None).decode())