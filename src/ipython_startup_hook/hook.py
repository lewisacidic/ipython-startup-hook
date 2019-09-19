#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Rich Lewis
# License: MIT License
"""Startup hook generated by {name}@{version}."""

try:
    from ipython_startup_hook import run_hook

    run_hook()
    del run_hook
except ModuleNotFoundError:
    pass
