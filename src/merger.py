import os
import shutil
from utils.helper import (
    get_dirs_inside_data_folder,
    check_duplicate_file_names,
    find_duplicate_file_names,
)
from utils.config import raw_data_folder, image_bank_folder, image_folder, label_folder

sources = get_dirs_inside_data_folder()


def clean_image_bank():
    """
    Clean the image bank
    """
    if os.path.exists(image_bank_folder):
        shutil.rmtree(image_bank_folder)
        print("Image bank has been cleaned.")
    else:
        print("Image bank does not exist.")


def create_image_bank_folders():
    """
    Create image bank folders if they do not exist
    """
    if not os.path.exists(image_bank_folder):
        os.makedirs(image_bank_folder)
    if not os.path.exists(image_bank_folder + "/" + image_folder):
        os.makedirs(image_bank_folder + "/" + image_folder)
    if not os.path.exists(image_bank_folder + "/" + label_folder):
        os.makedirs(image_bank_folder + "/" + label_folder)


def copy_all_images():
    """
    Copy all images from raw_data to image_bank if no duplicate file names exist
    """
    if check_duplicate_file_names():
        print("Duplicate file names exist. Cannot merge images.")
        print("Duplicate file names:")
        for file in find_duplicate_file_names():
            print(file)
    else:
        for directory in sources:
            source_dir = (
                raw_data_folder + "/" + os.path.join(directory) + "/" + image_folder
            )
            destination_dir = image_bank_folder + "/" + image_folder
            for _, _, files in os.walk(source_dir):
                for file in files:
                    shutil.copy(source_dir + "/" + file, destination_dir)
        print("All images have been successfully copied to the image bank.")


def copy_all_labels():
    """
    Copy all labels from raw_data to image_bank
    """
    for directory in sources:
        source_dir = (
            raw_data_folder + "/" + os.path.join(directory) + "/" + label_folder
        )
        destination_dir = image_bank_folder + "/" + label_folder
        for _, _, files in os.walk(source_dir):
            for file in files:
                shutil.copy(source_dir + "/" + file, destination_dir)
    print("All labels have been successfully copied to the image bank.")


def copy_all():
    """
    Copy all images and labels from raw_data to image_bank
    """
    clean_image_bank()
    create_image_bank_folders()
    copy_all_images()
    copy_all_labels()
