# adaptgym

[![PyPI](https://img.shields.io/badge/pypi-v0.1-blue)](https://pypi.org/project/adaptgym/#history)


### Environments for assessing adaptation and exploration of reinforcement learning agents.

Many are inspired by animal assays, e.g. a virtual labyrinth (based on [Rosenberg et al.](https://elifesciences.org/articles/66175)), and
a virtual object interaction assay (based on [Ahmadlou et al.](https://pubmed.ncbi.nlm.nih.gov/33986154/)).

<p align="center">
<img width="100%" src="overview.png">
</p>


### Installation
Install from pypi:
`pip install adaptgym`

Install from test pypi:
`pip install -i https://test.pypi.org/simple/ adaptgym`

or to specify a specific version:


`pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple --no-cache-dir adaptgym==0.1.48`

### Playing around with the environments
See `adaptgym/envs/scripts/fiddle_env.py` to visualize and interact with the environments.

To run this demo from the command line:

`python -c 'from adaptgym.fiddle_env import main; main()'`

### Notes:

Local install (from the adaptgym/ directory)
`poetry lock --no-update`
`poetry install`

To update and publish. Change the version number in pyproject.toml, then:
`poetry build`
`poetry publish -r testpypi`
