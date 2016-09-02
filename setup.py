# PYTHON PACKAGING
# using setuptools : http://pythonhosted.org/setuptools/
import os

import sys
import setuptools

with open('pyros_config/_version.py') as vf:
    exec(vf.read())

# Best Flow :
# $ gitchangelog >CHANGELOG.rst
# $ git commit CHANGELOG.rst -m "updating changelog"
# change version in code and changelog
# $ git commit CHANGELOG.rst pyros_config/_version.py -m "v<M.m.p>"
# $ git push
# WAIT FOR TRAVIS CHECKS
# $ python setup.py publish
# $ python setup.py tag
# => TODO : try to do a simpler "release" command


# Clean way to add a custom "python setup.py <command>"
# Ref setup.py command extension : https://blog.niteoweb.com/setuptools-run-custom-code-in-setup-py/
class PublishCommand(setuptools.Command):
    """Command to release this package to Pypi"""
    description = "releases pyros_setup to Pypi"
    user_options = []

    def initialize_options(self):
        """init options"""
        pass

    def finalize_options(self):
        """finalize options"""
        pass

    def run(self):
        """runner"""

        os.system("python setup.py sdist")
        os.system("python setup.py bdist_wheel")
        # OLD way:
        # os.system("python setup.py sdist bdist_wheel upload")
        # NEW way:
        # Ref: https://packaging.python.org/distributing/
        os.system("twine upload dist/*")
        print("You probably want to also tag the version now:")
        print("  python setup.py tag")
        sys.exit()


# Clean way to add a custom "python setup.py <command>"
# Ref setup.py command extension : https://blog.niteoweb.com/setuptools-run-custom-code-in-setup-py/
class TagCommand(setuptools.Command):
    """Command to release this package to Pypi"""
    description = "tag a release of pyros_setup"
    user_options = []

    def initialize_options(self):
        """init options"""
        pass

    def finalize_options(self):
        """finalize options"""
        pass

    def run(self):
        """runner"""

        os.system("git tag -a {0} -m 'version {0}'".format(__version__))
        os.system("git push --tags")
        sys.exit()


setuptools.setup(name='pyros_config',
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
    cmdclass={
        'tag': TagCommand,
        'publish': PublishCommand,
    },
    zip_safe=False,  # TODO testing...
)

