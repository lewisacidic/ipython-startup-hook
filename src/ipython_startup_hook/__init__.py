#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Rich Lewis
# License: MIT license
"""Project to run hooks at IPython startup.

See `ipython_startup_hook.__about__` for more info.
"""
from .__about__ import __copyright__
from .__about__ import __distname__
from .__about__ import __license__
from .__about__ import __url__
from .__about__ import __version__
from .run import run_hook


__all__ = [
    "__copyright__",
    "__distname__",
    "__license__",
    "__url__",
    "__version__",
    "run_hook",
]
