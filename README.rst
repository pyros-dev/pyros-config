Pyros-config
============

.. image:: https://travis-ci.org/pyros-dev/pyros-config.svg?branch=master
    :target: https://travis-ci.org/pyros-dev/pyros-config

Package to help manage configuration of always running servers/nodes
This is heavily inspired from flask configuration

This is a pure python package.

How to use
----------
Using the virtual environment of your choice, you can :: 
  
- Install
```
pip install pyros_config
```

- Run self tests
```
pyros_config
```

How to develop
--------------

Clone this repository
```
git clone http://github.com/pyro-dev/pyros-config
```

- The easy way : use pipenv. For most users.

Enter the virtual env to have access to pyros_config and dependencies
```
Pipenv shell
```
You can also use direnv for implicit virtualenv activation. 

- The hard way : use the python of your choice and pip to setup your environment. Use only if you want a total control of your environments. For python experts.

Create you virtualenv to workon (example using virtualenvwrapper)
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

