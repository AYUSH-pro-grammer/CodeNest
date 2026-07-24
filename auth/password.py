import hashlib
import hmac
import os


def hash_password(password):
    salt = os.urandom(16)

    password_bytes = password.encode("utf-8")

    value = hashlib.pbkdf2_hmac(
        "sha256",
        password_bytes,
        salt,
        200000,
    )

    salt_text = salt.hex()
    hash_text = value.hex()

    return f"{salt_text}:{hash_text}"


def check_password(password, stored_value):
    try:
        salt_text, old_hash = stored_value.split(":", 1)
        salt = bytes.fromhex(salt_text)

    except ValueError:
        return False

    password_bytes = password.encode("utf-8")


    value = hashlib.pbkdf2_hmac(
        "sha256",
        password_bytes,
        salt,
        200000,
    )

    new_hash = value.hex()

    return hmac.compare_digest(
        new_hash,
        old_hash,
    )