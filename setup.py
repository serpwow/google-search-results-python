from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), "r") as fh:
    long_description = fh.read()

setup(name='google-search-results-serpwow',
      version='1.1.4',
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
    packages=['serpwow'],
    long_description=long_description,
    long_description_content_type="text/markdown"
)