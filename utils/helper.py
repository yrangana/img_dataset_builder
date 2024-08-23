# Description: Helper functions for the scripts
import os
from .config import raw_data_folder, image_folder


def get_dirs_inside_data_folder():
    """
    Get directories inside the given directory
    :return: list of directories inside the data folder
    """
    dirs = []
    for directory in os.listdir(raw_data_folder):
        dirs.append(directory)
    return dirs


def find_duplicate_file_names():
    """
    Find duplicate file names in the images folder
    :return: list of duplicate file names in the images folder
    """
    file_names = []
    duplicate_file_names = []
    sources = get_dirs_inside_data_folder()
    for directory in sources:
        directory = raw_data_folder + "/" + os.path.join(directory) + "/" + image_folder
        for _, _, files in os.walk(dir):
            for file in files:
                if file in file_names:
                    duplicate_file_names.append(
                        raw_data_folder
                        + "/"
                        + os.path.join(directory)
                        + "/"
                        + image_folder
                        + "/"
                        + file
                    )
                else:
                    file_names.append(file)
    return duplicate_file_names


def check_duplicate_file_names():
    """
    Check if there are any duplicate file names in the images folder
    :return: True if there are duplicate file names, False otherwise
    """
    duplicate_file_names = find_duplicate_file_names()
    if len(duplicate_file_names) > 0:
        return True
    else:
        return False
