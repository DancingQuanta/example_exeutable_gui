import io
import os
import re

from setuptools import find_packages
from setuptools import setup

import versioneer


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding="utf-8") as fd:
        return re.sub(text_type(r":[a-z]+:`~?(.*?)`"), text_type(r"``\1``"), fd.read())

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    name='example_executable_gui',
    url='https://github.com/DancingQuanta/example_executable_gui',
    author="Andrew Tolmie",
    author_email='andytheseeker@gmail.com',
    description="A PyQt5 GUI application that displays a message depending how it is launched",
    long_description=read("README.rst"),
    packages=['toy_gui', 'toy_gui.images', 'toy_gui.tests'],
    package_data={'toy_gui.images': ['*.png']},
    install_requires=[
        r for r in open("requirements.txt").read().splitlines()
        if r and not re.match(r"\s*\#", r)
    ],
    extras_require={
        "dev": [
            r for r in open("requirementsDev.txt").read().splitlines()
            if r and not re.match(r"\s*\#", r)
        ]
    },
    entry_points={
        'console_scripts': [
            'ToyGUI=toy_gui.toy_gui:main'
        ],
        'gui_scripts': [
            'ToyGUI=toy_gui.toy_gui:gui_main'
        ]
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
