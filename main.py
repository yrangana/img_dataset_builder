import sys
from src.merger import copy_all, clean_image_bank
from src.splitter import clean_dataset, split_image_bank

msg = "Invalid argument. Please use 'rebuild_image_bank' or 'clean_image_bank' or 'split_image_bank' or 'clean_dataset' as argument."

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(msg)
        exit()
    if sys.argv[1] == "rebuild_image_bank":
        copy_all()
    elif sys.argv[1] == "clean_image_bank":
        clean_image_bank()
    elif sys.argv[1] == "split_image_bank":
        split_image_bank()
    elif sys.argv[1] == "clean_dataset":
        clean_dataset()
    else:
        print(msg)
