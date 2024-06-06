from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'My fisrt Python Package'
LONG_DESCRIPTION = 'My first Python Package with a slightly longer description'

setup(
    #
    name='esatpy',
    version=VERSION,
    author='Leoflutter',
    author_email='haibudongshi@gmail.com'
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[]


    keywords=['python', 'first package'],
    classifiers=['Development Status :: 3 - Alpha']
)
