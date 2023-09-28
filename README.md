# adaptgym

Environments for assessing agent adaptation.

### Installation

Install from online:
`pip install -i https://test.pypi.org/simple/ adaptgym`

or to specify a specific version:

`pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple --no-cache-dir adaptgym==0.1.42`

### Playing around with the environments
See `adaptgym/envs/scripts/fiddle_env.py` to visualize and interact with the environments.


### Notes:

Local install (from the adaptgym/ directory)
`poetry lock --no-update`
`poetry install`

To update and publish. Change the version number in pyproject.toml, then:
`poetry build`
`poetry publish -r testpypi`
