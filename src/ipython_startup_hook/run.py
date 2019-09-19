#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Rich Lewis
# License: MIT License
"""Run startup hook."""
import logging

import pkg_resources

logger = logging.getLogger(__name__)


def run_hook():
    """Import the startup hooks defined as entry points."""
    for entry_point in pkg_resources.iter_entry_points("ipython_startup_hook"):
        try:
            startup_func = entry_point.load()
        except Exception:
            logger.warn('Startup hook "%s" failed to load.', entry_point.name)
            continue
        try:
            startup_func()
        except Exception:
            logger.warn('Startup hook "%s" failed to run.', entry_point.name)
