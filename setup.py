import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open('requirements.txt') as f:
    install_reqs = f.readlines()
    reqs = [str(ir) for ir in install_reqs]

with open(os.path.join(here, 'README.md')) as fp:
    long_description = fp.read()

setup(
    name='cert-core',
    version='3.0.0',
    description='Blockcerts core models for python',
    author='info@blockcerts.org',
    tests_require=['tox'],
    url='https://github.com/blockchain-certificates/cert-core',
    license='MIT',
    author_email='info@blockcerts.org',
    long_description=long_description,
    packages=find_packages(),
    install_requires=reqs
)
