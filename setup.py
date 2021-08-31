from setuptools import setup

requirements = [
    # TODO: put your package requirements here
]

setup(
    name='example_executable_gui',
    version='0.0.1',
    description="A PyQt5 GUI application that displays a message depending how it is launched",
    author="Andrew Tolmie",
    author_email='andytheseeker@gmail.com',
    url='https://github.com/DancingQuanta/example_executable_gui',
    packages=['toy_gui', 'toy_gui.images',
              'toy_gui.tests'],
    package_data={'toy_gui.images': ['*.png']},
    entry_points={
        'console_scripts': [
            'Toy GUI=toy_gui.toy_gui:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='example_executable_gui',
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
