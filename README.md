# Demo of a python project packaged with uv

Showcases how uv is used for:
 -  configuring a dedicated python version per project
 -  isolating 3rd party packages per project 
 -  cross platform deterministic locking
 -  package upgrades within semver policy
 -  dependabot automatic dependency upgrades

NOTE: Dependabot currently does neither support uv.lock nor uv pip compile (See [dependabot-core#10478](https://github.com/dependabot/dependabot-core/issues/10478)).
A workaround is implemented for simulating pip-compile workflow (See [check-uv.sh](./bin/check-uv.sh) and [workflows/push.yml](.github/workflows/push.yml])).

Run with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv run pytest test
```

To upgrade dependencies but stay within defined semver policy in pyproject.toml:

```
uv lock -U 
```
