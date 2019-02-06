from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

import pypandoc
long_description = pypandoc.convert(path.join(here, 'README.md'), 'rst')


setup(name='google-search-results-serpwow',
      version='1.0.6',
      description='PIP package to scrape and parse Google Search Results using SerpWow. Visit https://serpwow.com to get a free API key.',
      url='https://github.com/serpwow/google-search-results-python',
      author='SerpWow',
      author_email='hello@serpwow.com',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        ],
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*',
    install_requires = ["requests"],
    packages=find_packages(),
    long_description=long_description,
)