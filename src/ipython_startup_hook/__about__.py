#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Rich Lewis
# License: MIT license
"""Metadata for ipython-startup-hook."""
# guard import as this is exec'd with runpy in setup.py so import will fail
try:
    from ._version import get_versions

    __version__ = get_versions()["version"]
    del get_versions
except ImportError:
    __version__ = None

__distname__ = "ipython-startup-hook"
__name__ = "ipython_startup_hook"
__description__ = "Project to run hooks at IPython startup."
__license__ = "MIT license"
__copyright__ = "Copyright (c) 2019 Rich Lewis"

__author__ = "Rich Lewis"
__author_email__ = "opensource@richlew.is"

__url__ = "https://lewisacidic.github.io/ipython-startup-hook"
__docs_url__ = "https://lewisacidic.github.io/ipython-startup-hook/docs"
__source_url__ = "https://github.com/lewisacidic/ipython-startup-hook"
__bugtracker_url__ = "https://github.com/lewisacidic/ipython-startup-hook/issues"
__download_url__ = "https://github.com/lewisacidic/ipython-startup-hook/releases"

__classifiers__ = [
    "Development Status :: 2 - Pre-Alpha",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.7",
    "Natural Language :: English",
]

__keywords__ = ["ipython", "hooks", "entrypoints", "startup"]

__all__ = [
    "__author__",
    "__author_email__",
    "__bugtracker_url__",
    "__classifiers__",
    "__copyright__",
    "__description__",
    "__distname__",
    "__docs_url__",
    "__download_url__",
    "__keywords__",
    "__license__",
    "__name__",
    "__source_url__",
    "__url__",
    "__version__",
]
