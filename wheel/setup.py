''' Created on Nov 05, 2022

@author: dgoyal607 '''

from setuptools import setup, find_packages

setup( 
      name="demo", 
      version="0.0.1",
      author="dgoyal607", 
      author_email="dgoyal607@yahoo.in", 
      description="Test PoC", 
      packages=find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3", 
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent"], 
      python_requires=">=3.6"
)
