import splitfolders
import os
import shutil

from utils.config import (
    dataset_folder,
    image_bank_folder,
    seed,
    train_ratio,
    validation_ratio,
    test_ratio,
)


def clean_dataset():
    """
    Clean the dataset
    """
    if os.path.exists(dataset_folder):
        shutil.rmtree(dataset_folder)
        print("Dataset has been cleaned.")
    else:
        print("Dataset does not exist.")


def split_image_bank():
    """
    Split the image bank into train, validation, and test sets
    """
    if not os.path.exists(image_bank_folder):
        print("Image bank does not exist.")
        return
    clean_dataset()

    splitfolders.ratio(
        image_bank_folder,
        output=dataset_folder,
        seed=seed,
        ratio=(train_ratio, validation_ratio, test_ratio),
    )

    print(
        "Image bank has been successfully split into train, validation, and test sets."
    )
