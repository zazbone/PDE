from setuptools import find_packages, setup


with open("requirements.txt", 'r') as file:
    requirement = file.readlines()
with open("LICENCE.txt", 'r') as file:
    licence = file.read()
with open("README.md", 'r') as file:
    description = file.read()

setup(
    name="PDE",
    version="1.0",
    description=description,
    author="zazbone",
    author_email="coczaz@gmail.com",
    packages=find_packages(),
    install_requires=requirement,
    license=licence,
    include_package_data=True,
    zip_safe=True  # No binary
)
