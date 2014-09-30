from setuptools import setup, find_packages
import os
import re

if os.environ.get('USER', '') == 'vagrant':
    del os.link

setup(
    name='MYPROJECT',
    version=open('VERSION.txt').read().strip(),
    author='Ronan Delacroix',
    author_email='ronan.delacroix@h-t-solutions.com',
    packages=find_packages(where='.', exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={}, #{'mypkg': ['data/*.dat']},
    scripts=[],
    license=open('LICENCE.txt').read().strip(),
    description='MYPROJECT DESCRIPTION',
    long_description=open('README.txt').read().strip(),
    include_package_data=True,
    install_requires=[r.strip() if ('git+' not in r) else re.sub(r".*egg=(.*)", "", r).strip() for r in open('requirements.txt').readlines()],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: Proprietary',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],
)
