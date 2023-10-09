import zipfile
import os


def zip_data(folder_path, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                zipf.write(
                    os.path.join(root, file), 
                    os.path.relpath(os.path.join(root, file), folder_path)
                )
    with open(zip_filename, 'rb') as f:
        return f.read()


def unzip_data(data, output_path):
    with open(output_path, 'wb') as f:
        f.write(data)
    with zipfile.ZipFile(output_path, 'r') as zip_ref:
        zip_ref.extractall(os.path.dirname(output_path))
    os.remove(output_path)  # Remove the zip file after extraction
