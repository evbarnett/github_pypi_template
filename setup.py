import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# TODO:
PACKAGE_NAME = ""
VERSION = ""
AUTHOR = ""
AUTHOR_EMAIL = ""
DESC = ""
URL = "" # ex. "https://github.com/<you>/<name>"
LICENSE = "" # ex. "MIT"
INSTALL_REQ = [] # List of str package names

setuptools.setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESC,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    license=LICENSE,
    packages=setuptools.find_packages(),
    install_requires=INSTALL_REQ,
)
