import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="thread6",
    version="0.2.0",
    author="Anh Le",
    author_email="hi@imanhle.com",
    description="A plug n play multithreading interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Haizzz/thread6",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
