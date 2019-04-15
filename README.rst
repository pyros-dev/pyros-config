Pyros-config
============

.. image:: https://travis-ci.org/pyros-dev/pyros-config.svg?branch=master
    :target: https://travis-ci.org/pyros-dev/pyros-config

Package to help manage configuration of always running servers/nodes
This is heavily inspired from flask configuration

This is a pure python package.


How to use
----------

Using the virtual environment of your choice, you can

- Install this package :

``pip install pyros_config``

- Run self tests :

``pyros_config``

- Run all tests (with all possible configurations) with tox

``tox``

Note : Tox envs are recreated every time to ensure consistency.


How to develop
--------------

1. Clone this repository

``git clone http://github.com/pyro-dev/pyros-config``

2. The easy way : use pipenv. For most users.

- Enter the virtual env to have access to pyros_config and dependencies (You can also use direnv for implicit virtualenv activation).

``pipenv install``

- Run self tests

``pyros_config``


2. The hard way : use the python of your choice and pip to setup your environment. Use only if you want a total control of your environments. For python experts.

- Create you virtualenv to workon (example using virtualenvwrapper)

``mkvirtualenv pyros_config_env``

- Install this package as editable

``pip install -e .``

- Run self tests

``pyros_config``




