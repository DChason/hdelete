from setuptools import find_packages, setup

VERSION = "0.1.0"
DESCRIPTION = "Simple tool for finding and deleting hidden operating system files."

setup(
    name="hdelete",
    version=VERSION,
    description=DESCRIPTION,
    author="Damien Chason",
    packages=find_packages(),
)
