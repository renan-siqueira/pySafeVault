"""
Provides utility functions for zipping and unzipping data.
"""
import zipfile
import os


def zip_data(path, zip_filename):
    """
    Compress a given file or directory into a zip format.
    
    Args:
    - path (str): The path to the file or directory to zip.
    - zip_filename (str): The name of the resulting zip file.
    
    Returns:
    - bytes: The compressed data in zip format.
    """
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        if os.path.isdir(path):
            _, dir_to_zip = os.path.split(path)
            for dirpath, _, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(dirpath, file)
                    arcname = os.path.join(dir_to_zip, os.path.relpath(file_path, path))
                    zipf.write(file_path, arcname=arcname)
        else:
            zipf.write(path, os.path.basename(path))
    with open(zip_filename, 'rb') as f:
        return f.read()


def unzip_data(data, output_path):
    """
    Extract the zipped data to a specified location.
    
    Args:
    - data (bytes): The compressed data in zip format.
    - output_path (str): The path where the data should be extracted.
    
    Raises:
    - zipfile.BadZipFile: If the data cannot be opened as a zip file.
    """
    with open(output_path, 'wb') as f:
        f.write(data)

    try:
        with zipfile.ZipFile(output_path, 'r') as zip_ref:
            zip_ref.extractall(os.path.dirname(output_path))
    except zipfile.BadZipFile:
        print(f"Failed to open {output_path} as a zip file.")
        raise
    os.remove(output_path)
