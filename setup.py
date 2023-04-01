#!/usr/bin/env python

from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name="pycroupier",
      version="1.0.0",
      description="Rand select utils",
      long_description=long_description,
      long_description_content_type='text/markdown',
      author="marsliu",
      author_email="mars.liu@outlook.com",
      url="https://github.com/MarchLiu/pycroupier",
      license="MIT",
      packages=["pycroupier"],
      package_dir={
          "pycroupier": "src/pycroupier"
      },
      classifiers=[
          "Topic :: Utilities",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3 :: Only",
          "License :: OSI Approved :: MIT License"
      ]
      )
