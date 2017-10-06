from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='mygist',
   version='1.0',
   description='Command line tool for gist creation, deletion, fetching, editing and many-more.',
   author='Vishi Choudhary',
   #packages=['mygist'],  
   install_requires=['requests'],
   scripts=['scripts/gists.py',]
)
