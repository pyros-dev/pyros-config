^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package pyros_config
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.1.2 (2016-06-03)
------------------
* Merge pull request `#1 <https://github.com/asmodehn/pyros-config/issues/1>`_ from asmodehn/tox_pytest
  Tox pytest
* adding one fake test to succeed tox.
* changing tox command to call py.test directly
* now using pytest form catkin-pip
* now using pytest from __main\_\_
* Merge branch 'master' of https://github.com/asmodehn/pyros-config into tox_pytest
* now using setup.py test command from tox
* first version, adding tox and py.test. removing dependency on importlib, not needed since py2.7 ?
* Contributors: AlexV, alexv

0.1.1 (2016-06-02)
------------------
* fixing repo links in package.xml
* using renamed dependency catkin_pip
* small cleanup.
  removing mention of ros.
  now printing sys.path in case import fails.
  added gitignore.
* Contributors: alexv

0.1.0 (2016-06-01)
------------------
* cleaned up README. added .travis.yml
* copying files from pyros-setup
* Contributors: alexv
