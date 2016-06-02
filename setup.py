# PYTHON PACKAGING
# using setuptools : http://pythonhosted.org/setuptools/
from setuptools import setup

with open('pyros_config/_version.py') as vf:
    exec(vf.read())

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
            'pyros_config = pyros_config.__main__:nosemain'
        ]
    },
    include_package_data=True,  # use MANIFEST.in during install.
    install_requires=[
        'six',
        'importlib'
    ],
    # TODO: pytest and tox
    test_suite="nose.collector",
    tests_require=[
        'nose>=1.3.7'
    ],
    zip_safe=False,  # TODO testing...
)

