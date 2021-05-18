import setuptools
import os

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="lima1983analysis",
    version="0.0.0",
    description="Sensitivity, Ti-Pei Li and Yu-Qian-Ma, APJ 272:317-324, 1983",
    long_description=long_description,
    url="https://github.com/cherenkov-plenoscope",
    author="Sebastian Achim Mueller",
    author_email="sebastian-achim.mueller@mpi-hd.mpg.de",
    license="MIT",
    packages=["lima1983analysis",],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Intended Audience :: Science/Research",
    ],
)
