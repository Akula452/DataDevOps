#!/usr/bin/env python3
"""Setup configuration for DataDevOps CLI."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="datadevops",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI tool for DataDevOps operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Akula452/DataDevOps",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "datadevops=cli.main:cli",
        ],
    },
    install_requires=[
        "click>=8.0.0",
        "python-dotenv>=0.19.0",
        "pyyaml>=6.0",
        "requests>=2.28.0",
    ],
)
