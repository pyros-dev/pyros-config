Pyros-config
===========

.. image:: https://travis-ci.org/asmodehn/pyros-config.svg?branch=master
    :target: https://travis-ci.org/asmodehn/pyros-config

Package to help manage configuration of always running servers
this is heavily inspired from flask configuration

This is a pure python package.
It is also provided as a ROS package for ease of use in pyros

HowTo install
^^^^^^^^^^^^^

To install it::

  pip install pyros_config

To run the self tests, using entry_points defined in setup.py::

  pyros_setup

OR using the python package directly::

  python -m pyros_setup

OR using nosetests specifically::

  nosetests pyros_setup

It can also be used from source inside a catkin workspace in the same way.
The workspace act as a virtual environment (using https://github.com/asmodehn/catkin_pure_python).
This is useful for development along with ROS packages::

  $ catkin_make
  $ source devel/setup.bash
  $ python -m pyros_setup
  $ pyros_setup
  $ nosetests pyros_setup


HowTo code
^^^^^^^^^^

Basically it allows you to do this::

  import pyros_setup
  try:
      import rospy
      import roslaunch
      import rosgraph
      import rosnode
  except ImportError:  # if ROS environment is not setup, we emulate it.
      pyros_setup.configurable_import().configure('mysetup.cfg').activate()  # this will use mysetup.cfg from pyros-setup instance folder
      import rospy
      import roslaunch
      import rosgraph
      import rosnode

With mysetup.cfg in pyros-setup instance folder containing::

  import os
  WORKSPACES=[os.path.join('home', 'user', 'ROS', 'workspace', 'devel')]
  DISTRO='indigo'


Note: If you know any easier / less tricky / more pythonic way of handling configurable dynamic imports, let me know!

HowTo deploy
^^^^^^^^^^^^

If you want to use pyros-setup, you should use the pip package, since the whole point is to provide access to ROS from pure python environment.
This is now possible thanks to [catkin_pure_python](https://github.com/asmodehn/catkin_pure_python)

For simpler pyros-setup development, and for use from an installed ROS package, a pyros-setup ROS package is currently provided.
But this is only temporary, until a pure python ubuntu deb package can be provided.

Remarks
^^^^^^^

Although it would technically be possible to build a ROS package from this source, this will NOT be done.
The catkin build system is only here to help having pyros-setup in a source workspace while developing on it.
When using ROS directly this package is not needed, and having it installed among ROS packages would cause much confusion when importing packages.

Roadmap
^^^^^^^

- [ ] A launchpad project to generate a ubuntu deb package, to be able to have pyros-setup as a deb dependency from other ROS/python packages (pyros, etc.).