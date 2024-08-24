import colorama
from setuptools import setup, find_packages

setup(
    name='popi_lib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        colorama
        # add required packages here
    ],
    author="Popa",
    author_email="prover09_reagent@icloud.com",
    description="A package with various helpful utilities.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
