from setuptools import setup, find_packages
 
setup(name='port-scanner',
      version='0.1.4',
      url='http://github.com/cjanis/python-port-scanner',
      license='Unlicense',
      author='Craig Janis',
      author_email='cjanis@gmail.com',
      description='A simple Python port scanner',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      long_description=open('README.md').read(),
      zip_safe=False)