import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gembed",
    version="0.0.1",
    author="Eric Kehoe, PhD",
    author_email="ekehoe@colostate.edu",
    description="A library of python classes, function, and scripts for generating gene embeddings.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ekehoe32/GeneEmbedding",
    project_urls={
        "Bug Tracker": "https://github.com/ekehoe32/GeneEmbedding/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
)