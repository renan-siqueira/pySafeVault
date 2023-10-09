"""
Provides functionality to decrypt data.
Uses the AES algorithm for decryption, along with PBKDF2 for key derivation.
"""
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as c_padding


def decrypt_data(encrypted_data, password):
    """
    Decrypt the given encrypted data using the provided password.

    Args:
    - encrypted_data (bytes): The data to decrypt.
    - password (str): The password used for decryption.

    Returns:
    - bytes: The decrypted data.
    """
    salt = encrypted_data[:16]
    iv = encrypted_data[16:32]
    actual_encrypted_data = encrypted_data[32:]

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(actual_encrypted_data) + decryptor.finalize()

    unpadder = c_padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    return decrypted_data
