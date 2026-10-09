# exec_utils

Versatile utility to execute commands. Published on PyPI as
[exec-utils](https://pypi.org/project/exec-utils/).

```
pip install exec-utils
```

## Getting started

```python
from exec_utils import exec_strict

cmd = ["sort", "-n"]
stdout = exec_strict(cmd, stdin_str="2 world\n1 hello\n")
print(stdout)
# "1 hello\n2 world"
```

`exec_strict` blocks until the command finishes and returns its stdout. If the
command fails, an `exec_utils.ExecStrictError` is raised, carrying `stdout`,
`stderr` and `exit_code`. Optional arguments allow logging the output to a
file or the console, passing stdin as `str` or `bytes`, setting `cwd` / `env`,
and returning stderr alongside stdout (`return_stderr=True`).

`exec_strict_direct` runs a command without capturing stdout/stderr, so the
output goes straight to the terminal.

## Development

The project uses [uv](https://docs.astral.sh/uv/).

```
uv sync
uv run pytest
uv run ruff check .
```

## Release

1. Bump `version` in `pyproject.toml` and add an entry to `CHANGELOG.txt`.
2. Commit, tag and push.
3. Build and upload:

```
uv build
uv publish
```
