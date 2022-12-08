import configparser
import tomllib

from setuptools import setup, find_packages

with open("pyproject.toml", "rb") as f:
    data_toml = tomllib.load(f)

config = configparser.ConfigParser()
config.read("setup.cfg")

with open("MANIFEST.in", "r") as r:
    MANIFEST_in = r.read().replace('include', '').replace(' ', '').split('\n')

print(MANIFEST_in)

setup(
    name='raypyc',
    version=config.get('metadata', 'version'),
    python_requires=config.get('options', 'python_requires'),
    description=config.get('metadata', 'description'),
    long_description=config.get('metadata', 'long_description'),
    long_description_content_type=config.get('metadata', 'long_description_content_type'),
    url=config.get('metadata', 'url'),
    author=config.get('metadata', 'author'),
    author_email=config.get('metadata', 'author_email'),
    classifiers=config.get('metadata', 'classifiers'),
    packages=find_packages(),
    install_requires= ["setuptools>=42", "wheel", "inflection"],
    package_data={
        'raylib':  ['raypyc/defines/*', 'raypyc/colors/*', 'raypyc/enums/*', 'raypyc/structures/*', 'raypyc/reasings.py', 'raypyc/__init__.py', 'raypyc/__init__.pyi', 'raypyc/*.json', 'raypyc/*.dll']
    }
)
