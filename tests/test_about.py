#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Rich Lewis
# License: MIT license
"""Tests for metadata loading."""
import importlib
import pathlib
import runpy

import pytest


BASEDIR = pathlib.Path(__file__).parents[1]


@pytest.fixture
def base_pkg():
    """Provide a reloaded base package as a fixture."""
    base_pkg = importlib.import_module("ipython_startup_hook")
    return importlib.reload(base_pkg)


@pytest.mark.parametrize(
    ["field", "value"],
    [
        ("distname", "ipython-startup-hook"),
        ("name", "ipython_startup_hook"),
        ("copyright", "Copyright (c) 2019 Rich Lewis"),
        ("license", "MIT license"),
        ("url", "https://lewisacidic.github.io/ipython-startup-hook"),
    ],
)
def test_metadata(base_pkg, field, value):
    """Test metadata is available on base package."""
    assert getattr(base_pkg, f"__{field}__") is not None


def test_version(base_pkg):
    """Test the version is correctly detected with versioneer."""
    # get version using versioneer.py script
    versioneer_path = str(BASEDIR.joinpath("versioneer.py"))
    versioneer = runpy.run_path(versioneer_path)
    version = versioneer["get_version"]()
    assert base_pkg.__version__ == version


def test_import_fails():
    """Test behaviour if import fails."""
    # if we run __about__ as a script with runpy, imports will fail
    about_path = str(BASEDIR.joinpath("src", "ipython_startup_hook", "__about__.py"))
    about = runpy.run_path(about_path)
    assert about["__version__"] is None
