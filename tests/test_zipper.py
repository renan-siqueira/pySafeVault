import os
from src import zipper
import shutil


def create_sample_files(base_path):
    """Creates some sample folders and files for testing."""

    # Ensure the parent directory 'test_files' exists
    parent_dir = os.path.dirname(base_path)
    if not os.path.exists(parent_dir):
        os.mkdir(parent_dir)

    os.mkdir(base_path)

    subfolders = ["subfolder1", "subfolder2"]
    for sub in subfolders:
        os.mkdir(os.path.join(base_path, sub))
        for i in range(3):  # Create 3 files in each subfolder
            with open(os.path.join(base_path, sub, f"file{i}.txt"), "w") as f:
                f.write(f"This is content for {sub}/file{i}.txt")


def test_zip_and_unzip():
    # Pre-test setup: Create test files and folders
    test_folder_name = "sample_test_folder"
    test_path = os.path.join("test_files", test_folder_name)
    create_sample_files(test_path)

    zip_filename = os.path.join("test_files", "temp_test.zip")

    # Test zipping
    zipped_data = zipper.zip_data(test_path, zip_filename)
    assert len(zipped_data) > 0, "Zipped data should not be empty"

    # Test unzipping
    unzip_folder = os.path.join("test_files", "unzipped_folder")
    if not os.path.exists(unzip_folder):
        os.mkdir(unzip_folder)
    output_path = os.path.join(unzip_folder, f"{test_folder_name}.zip")

    zipper.unzip_data(zipped_data, output_path)

    # Ensure unzipped files exist and match the original
    original_files = os.listdir(test_path)
    unzipped_files = os.listdir(os.path.join(unzip_folder, test_folder_name))
    assert set(original_files) == set(unzipped_files), "Original and unzipped files do not match"

    # Cleanup
    os.remove(zip_filename)
    shutil.rmtree('test_files')
