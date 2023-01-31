import configparser
import tomllib

from setuptools import setup, find_packages

with open("README.md", "r") as long_description_reader:
    _long_description = long_description_reader.read()


setup(
    name='raypyc',
    version='0.1.8',
    description='A python wrapper for raylib using ctypes',
    long_description=_long_description,
    long_description_content_type='text/markdown',
    author='Dor Shapira',
    license='MIT License',
    author_email='sdor2803@gmail.com',
    packages=['raypyc'],
    url='https://github.com/sDos280/raylib-python-ctypes',
    classifiers=['Programming Language :: Python :: 3', 'License :: OSI Approved :: MIT License'],
    install_requires=['setuptools>=42', 'wheel'],
    package_data={
        'raypyc': ['defines/*', 'colors/*', 'enums/*', 'structures/*', 'reasings.py', '__init__.pyi', '*.json', 'libs/*']
    },
    include_package_data=True
)
