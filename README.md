# ipython-startup-hook

Provides a hook to run entry points at IPython startup.

## Quickstart/Installation

Install using [`pip`](https://pip.pypa.io/en/stable/):

```shell
pip install ipython_startup_hook
```

Install the hook for your desired [IPython profile](https://ipython.readthedocs.io/en/stable/config/intro.html):

```shell
python -m ipython_startup_hook.install --profile="<your_profile>"
```

Or just add to the default profile:

```shell
python -m ipython_startup_hook.install
```

Install the modules with the entry points you want to run, such as [`richprompt`](https://github.com/lewisacidic/richprompt) or [`ipython-nord-theme`](https://github.com/lewisacidic/ipython-nord-theme).

These will now run on IPython startup!!

## How it Works

On startup, IPython will run every script found in `$IPYTHONDIR/profile_<your_profile>`/startup.
When we ran `python -m ipython_startup_hook.install`, a script was copied into this directory that runs any other installed scripts which declare an [entry point](https://packaging.python.org/specifications/entry-points/) of type `ipython_setup_hook` (for a fun introduction to entry points, see [this post](https://amir.rachum.com/blog/2017/07/28/python-entry-points/)).
If you are interested in adding your own, see one of the examples.

## Development

Create the conda environment:

```shell
conda env create -f envs/dev.yml
conda activate ipython-startup-hook-dev
```

Format code by running the pre-commit tasks:

```shell
pre-commit run --all
```

Run the tests with pytest:

```shell
pytest
```
