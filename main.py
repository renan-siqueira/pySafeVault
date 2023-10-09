import os
from getpass import getpass
from src import encryptor, decryptor, zipper


def main():
    choice = input("Would you like to (e)ncrypt or (d)ecrypt? ")

    if choice.lower() == 'e':
        folder_path = input("Enter the path of the folder or file you want to encrypt: ")
        output_filename = input("Enter the name of the encrypted output file (e.g., output.enc): ")
        password = getpass("Enter the password for encryption (password will not be displayed): ")

        zip_data = zipper.zip_data(folder_path, folder_path + ".zip")
        print(f"Size of zip data: {len(zip_data)} bytes")

        encrypted_data = encryptor.encrypt_data(zip_data, password)

        with open(output_filename, 'wb') as f:
            f.write(encrypted_data)

        os.remove(folder_path + ".zip")
        print("Data successfully encrypted!")

    elif choice.lower() == 'd':
        encrypted_file_path = input("Enter the path of the encrypted file you want to decrypt: ")
        output_folder_path = input("Enter the path where the decrypted folder or file should be placed: ")
        password = getpass("Enter the decryption password (password will not be displayed): ")

        with open(encrypted_file_path, 'rb') as f:
            encrypted_data = f.read()

        decrypted_data = decryptor.decrypt_data(encrypted_data, password)
        output_zip_path = os.path.join(output_folder_path, "decrypted_output.zip")
        zipper.unzip_data(decrypted_data, output_zip_path)

        print("Data successfully decrypted and extracted to:", output_folder_path)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
