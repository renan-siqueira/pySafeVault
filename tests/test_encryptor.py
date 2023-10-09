"""
Tests for the encryptor module.
"""
from src import encryptor

def test_encrypt_data():
    """
    Test the encryption process to ensure that the encrypted data 
    is not the same as the original and that it has increased in size
    due to the addition of salt and IV.
    """
    password = "testpassword"
    data = b"Hello, World!"
    encrypted_data = encryptor.encrypt_data(data, password)

    assert encrypted_data != data, "Encrypted data should not be the same as original data"
    assert len(encrypted_data) > len(data), "Encrypted data should be larger due to salt and IV"
