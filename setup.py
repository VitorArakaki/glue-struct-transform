# Always prefer setuptools over distutils
from setuptools import setup

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="glue-struct-transform",
    version="0.3.6",
    description="This libs works to convert a json schema or json to a glue schema struct.",
    long_description_content_type='text/markdown',
    long_description = long_description,
    url="https://github.com/VitorArakaki/glue-struct-transform",
    author="Vitor Guirardeli Arakaki",
    author_email="vi.arakaki@hotmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["glue_struct_transform"],
    include_package_data=True
)