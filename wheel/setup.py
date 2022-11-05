''' Created on Nov 05, 2022

@author: dgoyal607 '''

from setuptools import setup, find_packages

version = open("version.txt").readline().strip()

requirements = open("requirements.txt").read().splitlines()

# if __name__ == '__main__':
#     setup()

setup( 
      name="Test", 
      version=version,
      author="dgoyal607", 
      author_email="dgoyal607@yahoo.in", 
      description="Test PoC", 
      url="https://github.com/dgoyal607/finalyearproject",
      packages=find_packages("demo"),
      install_requires=requirements, 
      classifiers=[
        "Programming Language :: Python :: 3", 
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent",
    ], python_requires=">=3.6"
)
