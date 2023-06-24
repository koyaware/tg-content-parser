import os
import shutil
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def move_files_by_format(source_dir, destination_dir, file_format, excluded_items=None):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    files = os.listdir(source_dir)

    for file in files:

        if excluded_items and file in excluded_items:
            continue

        else:
            if file.endswith(tuple(file_format)):
                source_file = os.path.join(source_dir, file)
                destination_file = os.path.join(destination_dir, file)
                shutil.move(source_file, destination_file)


source_directory = BASE_DIR
destination_directory = BASE_DIR / 'source-files'
file_extension = ['.txt', '.MP4', 'mp4', '.OGG', '.jpg', 'img']
excluded_directories = ['requierements.txt']