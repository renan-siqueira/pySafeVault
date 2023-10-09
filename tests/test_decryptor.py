"""
Tests for the decryptor module.
"""
from src import encryptor, decryptor

def test_decrypt_data():
    """
    Test the decryption process by first encrypting a piece of data 
    and then decrypting it. The decrypted data should match the original.
    """
    password = "testpassword"
    data = b"Hello, World!"
    encrypted_data = encryptor.encrypt_data(data, password)
    decrypted_data = decryptor.decrypt_data(encrypted_data, password)

    assert decrypted_data == data, "Decrypted data should match original data"
