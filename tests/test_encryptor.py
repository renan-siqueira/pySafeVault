from src import encryptor

def test_encrypt_data():
    password = "testpassword"
    data = b"Hello, World!"
    encrypted_data = encryptor.encrypt_data(data, password)

    assert encrypted_data != data, "Encrypted data should not be the same as original data"
    assert len(encrypted_data) > len(data), "Encrypted data should be larger due to salt and IV"
