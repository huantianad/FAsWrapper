import setuptools

with open('README.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name="FAsWrapper",
    version="0.1.0",
    author="David Li",
    author_email="davidtianli@gmail.com",
    description="A python wrapper for faexport FurAffinity scraper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/huantianad/FAWrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    python_requires='>=2.7'
)