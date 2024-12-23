# setup.py
from setuptools import setup, find_packages

setup(
    name="mypylibrary",
    version="0.1.0",
    author="hamdi",
    author_email="mohammedhamdi500@gmail.com",
    description="A simple library with math and string operations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mohammad-hamdi/hamdi",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
