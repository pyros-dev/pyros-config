Pyros-config
============

.. image:: https://travis-ci.org/asmodehn/pyros-config.svg?branch=master
    :target: https://travis-ci.org/asmodehn/pyros-config

ROS Release :

.. image:: https://travis-ci.org/asmodehn/pyros-config-rosrelease.svg?branch=master
    :target: https://travis-ci.org/asmodehn/pyros-config-rosrelease

Package to help manage configuration of always running servers
this is heavily inspired from flask configuration

This is a pure python package.
It is also provided as a ROS package for ease of use in pyros

How to use
----------

Install
```
pip install pyros_config
```

Run self tests
```
pyros_config
```

How to develop
--------------

Clone this repository
```
git clone http://github.com/asmodehn/pyros-config
```

Create you virtualenv to workon using virtualenvwrapper
```
mkvirtualenv pyros_config_env
```

Install all dependencies via dev-requirements
```
pip install -r dev-requirements.txt
```

Run self tests
```
pyros_config
```

Run all tests (with all possible configurations) with tox
```
tox
```

Note : Tox envs are recreated every time to ensure consistency.
So it s better to develop while in a non-tox-managed venv.