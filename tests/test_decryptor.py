from src import encryptor, decryptor

def test_decrypt_data():
    password = "testpassword"
    data = b"Hello, World!"
    encrypted_data = encryptor.encrypt_data(data, password)
    decrypted_data = decryptor.decrypt_data(encrypted_data, password)

    assert decrypted_data == data, "Decrypted data should match original data"
