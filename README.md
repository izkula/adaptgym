# adaptgym

Environments for assessing agent adaptation.

### Installation
From the adaptgym/ directory:

Local install:
`poetry lock --no-update`
`poetry install`

Install from online:
`pip install -i https://test.pypi.org/simple/ adaptgym`

or

`pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple --no-cache-dir adaptgym==0.1.37`


To update and publish. Change the version number in pyproject.toml, then:
`poetry build`
`poetry publish -r testpypi`
