Changelog
=========

0.1.5 (2016-08-31)
------------------

- Fixed regression about accepting dict and object when configuring.
  [alexv]

- Improved logging. cosmetics. [alexv]

0.1.4 (2016-08-30)
------------------

- V0.1.4. [alexv]

- Generated changelog. [alexv]

- Improved setup.py publish and tag commands. [alexv]

- Fix creating directory for generated default config file if it doesnt
  exists yet. [alexv]

- Adding IOError handling by creating default configuration file from
  provided string. [alexv]

- Changed version number to patch .99 to denote devel version. [alexv]

- Removing useless cmakelists. [alexv]

- Fixed configimport for python3. [alexv]

- Added setup.cfg. added badge for ros release builds. [alexv]

0.1.3 (2016-08-10)
------------------

- More cleanup of ros stuff. preparing 0.1.3. [alexv]

- Improved setup to do releases. removed ros files from master branch.
  [alexv]

- Improve self test. [AlexV]

- Reviewing tox and tests. [AlexV]

- Refining tox test command, importing more from __future__. [AlexV]

- Making check for string work with python3. [AlexV]

- Adding .idea folder to gitignore. [AlexV]

- Removing ROS and not using site-package, this is a pure python
  package. [alexv]

- Revert "improving travis files to test catkin_pip build with
  rosdistros." [alexv]

  This reverts commit 3c3bdd1d65f28f24bf3891ff1567e084b0dfb6bf.

- Improving travis files to test catkin_pip build with rosdistros.
  [alexv]

0.1.2 (2016-06-03)
------------------

- Preparing version 0.1.2. [alexv]

- Merge pull request #1 from asmodehn/tox_pytest. [AlexV]

  Tox pytest

- Adding one fake test to succeed tox. [alexv]

- Changing tox command to call py.test directly. [alexv]

- Now using pytest form catkin-pip. [alexv]

- Now using pytest from __main__ [alexv]

- Merge branch 'master' of https://github.com/asmodehn/pyros-config into
  tox_pytest. [alexv]

- Now using setup.py test command from tox. [alexv]

- First version, adding tox and py.test. removing dependency on
  importlib, not needed since py2.7 ? [alexv]

0.1.1 (2016-06-02)
------------------

- Preparing v0.1.1. [alexv]

- Fixing repo links in package.xml. [alexv]

- Using renamed dependency catkin_pip. [alexv]

- Small cleanup. removing mention of ros. now printing sys.path in case
  import fails. added gitignore. [alexv]

0.1.0 (2016-06-01)
------------------

- Generated changelog. [alexv]

- Cleaned up README. added .travis.yml. [alexv]

- Copying files from pyros-setup. [alexv]


