#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Rich Lewis
# License: MIT License
"""Install the hook in an IPython profile."""
import logging
import os

from IPython.paths import get_ipython_dir

from .__about__ import __distname__ as distname
from .__about__ import __version__ as version


logger = logging.getLogger(__name__)


def install_hook(profile="default"):
    """Install the hook in a given IPython profile.

    Args:
        profile: the IPython profile for which to install the hook.

    """
    hook_source_path = os.path.join(os.path.dirname(__file__), "hook.py")
    ipython_dir = get_ipython_dir()
    startup_dir = os.path.join(ipython_dir, "profile_" + profile, "startup")
    hook_target_path = os.path.join(startup_dir, "000-ipython-startup-hook.py")
    logger.info("Installing hook for IPython profile %s", profile)
    logger.debug("Writing hook at %s to %s", hook_source_path, hook_target_path)
    with open(hook_source_path) as source, open(hook_target_path, "w") as target:
        target.write(source.read().format(name=distname, version=version))


def main():
    """Run a simple CLI to install the hook manually."""
    import argparse

    parser = argparse.ArgumentParser(description="Install hook.")
    parser.add_argument(
        "--profile",
        type=str,
        default="default",
        help="the IPython profile on which to install the hook.",
    )
    parser.add_argument(
        "--log-level", default="INFO", help="the level of log messages."
    )
    args = parser.parse_args()
    logging.basicConfig(level=args.log_level)
    install_hook(args.profile)


if __name__ == "__main__":
    main()
