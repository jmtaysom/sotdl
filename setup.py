from distutils.core import setup
from setuptools import find_packages

setup(name='sotdl',
      version='0.1',
      description='Shadow of the Demon Lord Character Creator',
      author='James Taysom',
      author_email='james.taysom@gmail.com',
      py_modules=['ancestry',],
      packages=find_packages(where='src'),
      package_dir={'': 'src'},
      )