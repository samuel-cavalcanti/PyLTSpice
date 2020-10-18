import sys

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

if 'linux' in sys.platform:
    init_script = 'PyLTSpice/__init__.py'
else:
    init_script = 'PyLTSpice\\__init__.py'

setuptools.setup(
    name='PyLTSpice',
    version='1.1',
    scripts=[init_script
             # 'PyLTSpice\\Histogram.py',
             # 'PyLTSpice\\LTSpice_RawRead.py',
             # 'PyLTSpice\\LTSpiceBatch.py',
             # 'PyLTSpice\\LTSteps.py',
             # 'PyLTSpice\\sketch.py'
             ],
    # install_requires = [],
    author="Nuno Brum",
    author_email="me@nunobrum.com",
    description="An set of tools to Automate LTSpice simulations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nunobrum/PyLTSpice",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
)
