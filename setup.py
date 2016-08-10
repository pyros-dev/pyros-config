# PYTHON PACKAGING
# using setuptools : http://pythonhosted.org/setuptools/
import os

import sys
from setuptools import setup

with open('pyros_config/_version.py') as vf:
    exec(vf.read())

if sys.argv[-1] == 'publish':

    os.system("python setup.py sdist")
    os.system("python setup.py bdist_wheel")
    # OLD way:
    #os.system("python setup.py sdist bdist_wheel upload")
    # NEW way:
    # Ref: https://packaging.python.org/distributing/
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  python setup.py tag")
    sys.exit()

if sys.argv[-1] == 'tag':
    os.system("git tag -a {0} -m 'version {0}'".format(__version__))
    os.system("git push --tags")
    sys.exit()

setup(name='pyros_config',
    version=__version__,
    description='Classes to manage a server configuration. Heavily inspired by flask',
    url='http://github.com/asmodehn/pyros-config',
    author='AlexV',
    author_email='asmodehn@gmail.com',
    license='BSD',
    packages=[
        'pyros_config',
        'pyros_config.tests',
    ],
    entry_points={
        'console_scripts': [
            'pyros_config = pyros_config.__main__:main'
        ]
    },
    include_package_data=True,  # use MANIFEST.in during install.
    install_requires=[
        'six',
        'pytest'  # since tests are embedded in the package
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    zip_safe=False,  # TODO testing...
)

