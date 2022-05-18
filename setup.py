import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="lima1983analysis_sebastian-achim-mueller",
    version="0.0.2",
    description="Sensitivity, Ti-Pei Li and Yu-Qian-Ma, APJ 272:317-324, 1983",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/cherenkov-plenoscope/lima1983analysis",
    author="Sebastian Achim Mueller",
    author_email="sebastian-achim.mueller@mpi-hd.mpg.de",
    packages=["lima1983analysis",],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Intended Audience :: Science/Research",
    ],
)
