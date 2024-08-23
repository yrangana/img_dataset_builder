from setuptools import setup, find_packages

setup(
    name="img_dataset_builder",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'split-folders',
        'PyYAML',
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'img-dataset-builder=img_dataset_builder.cli:cli',
        ],
    },
    author="Yasiru Rangana",
    author_email="yrkau86@example.com",
    description="A simple package to create image datasets for computer vision models.",
    url="https://github.com/yrangana/img_dataset_builder",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
