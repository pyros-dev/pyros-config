# -*- coding: utf-8 -*-
"""
    pyros_config.confighandler
    ~~~~~~~~~~~~~

    Implements a class to access configuration files
    Inspired from Flask
"""

from __future__ import absolute_import
from __future__ import print_function

import os
import logging

import errno
import six

# create logger
_logger = logging.getLogger(__name__)
# and let it propagate to parent logger, or other handler
# the user of pyros-config should configure handlers

from .config import Config
from .packagebound import PackageBound
from .helpers import locked_cached_property


class ConfigHandler(PackageBound):
    config_class = Config

    def __init__(self, import_name, instance_path=None, instance_relative_config=True, root_path=None, default_config=None):

        #: default config passed to the constructor. should not be changed
        self.default_config = default_config or {}

        super(ConfigHandler, self).__init__(import_name,
                                            instance_path=instance_path,
                                            instance_relative_config=instance_relative_config,
                                            root_path=root_path)

        #: The configuration dictionary as :class:`Config`.  This behaves
        #: exactly like a regular dictionary but supports additional methods
        #: to load a config from files.
        self.config = self.make_config(instance_relative_config)

    @locked_cached_property
    def instance_relative_config(self):
        return self.config.root_path == self.instance_path

    # This function attempts to find out what was the configuration passed
    # And retrieve values accordingly...

    def configure_file(self, config, create_if_missing=None):
        """
        :param config: a filepath to the configuration.
        :param create_if_missing: If file is not found, it will be created with this.
        :return: self
        """
        # We default to using a config file named after the import_name:
        config = config or self.name + '.cfg'
        cfg_filename = None
        if isinstance(config, six.string_types):
            # we assume the intent is filename. predicting fullpath...
            cfg_filename = os.path.join(self.config.root_path, config)
            _logger.info("Loading configuration from {0}".format(cfg_filename))

        try:
            self.configure(config)
        except IOError as e:  # should happen only in filename case
            if e.errno not in (errno.EISDIR,) and create_if_missing and cfg_filename:
                if not os.path.exists(os.path.dirname(cfg_filename)):
                    try:
                        os.makedirs(os.path.dirname(cfg_filename))
                    except OSError as exc:  # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise

                with open(cfg_filename, 'w+') as cfg_file:
                    cfg_file.write(create_if_missing)
                    _logger.warning("Default configuration has been generated in {cfg_filename}".format(**locals()))

    def configure(self, config):
        if isinstance(config, six.string_types):
            self.config.from_pyfile(config)
        elif isinstance(config, dict):
            self.config.from_mapping(**config)
        else:
            self.config.from_object(config)
        return self

    def make_config(self, instance_relative=False):
        """Used to create the config attribute by the Flask constructor.
        The `instance_relative` parameter is passed in from the constructor
        of Flask (there named `instance_relative_config`) and indicates if
        the config should be relative to the instance path or the root path
        of the application.
        """
        root_path = self.root_path
        if instance_relative:
            root_path = self.instance_path
        return self.config_class(root_path, self.default_config)

