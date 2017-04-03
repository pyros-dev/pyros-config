# -*- coding: utf-8 -*-
from __future__ import absolute_import
"""
Small package to provide package bound configuration file
"""
from ._version import __version__

# Configuring logging default handler
import logging
logging.getLogger(__package__).addHandler(logging.NullHandler())

from .packagebound import PackageBound
from .confighandler import ConfigHandler

__all__ = [
    '__version__',
    'PackageBound',
    'ConfigHandler',
]