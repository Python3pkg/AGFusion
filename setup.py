import os
import re
import shutil
import site

from setuptools import setup, find_packages

VERSIONFILE = "agfusion/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

README = open('README.md').read()

setup(
    version=verstr,
    name='agfusion',
    packages=find_packages(),
    description="Python package to annotate and visualize gene fusions.",
    author='Charles Murphy',
    author_email='murphy.charlesj@gmail.com',
    license='MIT',
    url='https://github.com/murphycj/AGFusion',
    long_description=README,
    include_package_data=True,
    scripts=['bin/agfusion'],
    install_requires=[
        'pyensembl>=0.9.5',
        'matplotlib>=1.5.0',
        'biomart>=0.9.0',
        'pandas>=0.18.1',
        'biopython>=1.67',
        'jsonpickle>=0.9.3',
        'tqdm>=4.8.4'
    ]
)
