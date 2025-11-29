# impractical-python
Let's build out Impractical Python - maybe rewrite into other languages.

## Development Setup

### Pre-commit Hooks

This project uses [pre-commit](https://pre-commit.com/) for code quality checks.

**Install dependencies:**
```bash
pip install pre-commit ruff
```

**Install the git hooks:**
```bash
pre-commit install
```

**Run hooks manually:**
```bash
pre-commit run --all-files
```

### Linting & Formatting

We use [Ruff](https://docs.astral.sh/ruff/) for linting and formatting Python code.

**Lint check:**
```bash
ruff check .
```

**Auto-fix lint issues:**
```bash
ruff check --fix .
```

**Format code:**
```bash
ruff format .
```

Ruff configuration is in `pyproject.toml`.
