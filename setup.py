import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yahoostock",
    version="1.0.0",
    author="rohan0x",
    license="MIT",
    description="A package designed to scrape data from Yahoo Finance.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rohan0x/stockscrape",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)