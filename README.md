# Python mise Template

A modern Python project template with [mise](https://mise.jdx.dev) and development best practices.

## Features

- **Modern tooling** - mise for unified version management
- **Code quality** - Black, Ruff, and Mypy preconfigured
- **Testing** - pytest with coverage support
- **Type safe** - Full type hints and strict mypy configuration
- **Developer friendly** - Pre-configured tasks and virtual environment

## Prerequisites

- [mise](https://mise.jdx.dev/getting-started.html) - Install with:
  ```bash
  # macOS/Linux
  curl https://mise.run | sh

  # Windows (PowerShell)
  irm https://mise.run | iex
  ```

## Quick Start

### 1. Clone or Use This Template

```bash
# Clone the repository
git clone https://github.com/yourusername/python-mise-template.git
cd python-mise-template

# Or use as GitHub template
# Click "Use this template" button on GitHub
```

### 2. Install Dependencies

```bash
# mise will automatically:
# - Install Python 3.11
# - Install uv (fast pip replacement)
# - Create virtual environment
# - Activate the environment
mise install

# Install project dependencies
mise run install
```

### 3. Run the Application

```bash
# Run the main application
mise run dev
```

## Project Structure

```
python-mise-template/
├── .mise.toml              # mise configuration (tools, tasks, env)
├── pyproject.toml          # Python project configuration
├── .gitignore              # Git ignore patterns
├── .env.example            # Environment variables template
├── README.md               # This file
├── LICENSE                 # MIT License
├── src/                    # Source code
│   ├── __init__.py
│   └── main.py             # Main entry point
└── tests/                  # Test suite
    ├── __init__.py
    └── test_example.py
```

## Development Commands

All commands are defined in `.mise.toml` and can be run with `mise run <task>`:

```bash
# Code formatting
mise run format         # Format code with Black and Ruff

# Code quality checks
mise run lint           # Check code style without fixing
mise run type-check     # Run mypy type checking

# Testing
mise run test           # Run all tests with pytest
mise run test-cov       # Run tests with coverage report

# Development
mise run dev            # Run the main application
mise run install        # Install/update dependencies
```

### Alternative: Using poethepoet

If you prefer, you can also use `poe` commands directly:

```bash
poe format
poe lint
poe type-check
poe test
```

## Configuration

### Python Version

This template uses Python 3.11. To change the version:

1. Edit `.mise.toml`:
   ```toml
   [tools]
   python = "3.12"  # Change version here
   ```

2. Update `pyproject.toml`:
   ```toml
   requires-python = ">=3.12, <3.13"
   ```

3. Run `mise install` to install the new version

### Code Quality Tools

- **Black** - Line length: 100, Python 3.11 target
- **Ruff** - Fast linter with auto-fix
- **Mypy** - Strict type checking enabled

Configurations are in `pyproject.toml` and can be customized to your needs.

## Testing

Write tests in the `tests/` directory. See `tests/test_example.py` for examples:

```python
def test_example() -> None:
    assert 1 + 1 == 2

@pytest.mark.parametrize("input,expected", [(1, 2), (2, 4)])
def test_parametrized(input: int, expected: int) -> None:
    assert input * 2 == expected
```

Run tests:

```bash
mise run test           # Basic test run
mise run test-cov       # With coverage report
```

## Customization Guide

### Adding New Dependencies

```bash
# Add to pyproject.toml [project.dependencies]
# Then install:
mise exec -- uv pip install -e .

# For development dependencies:
# Add to [project.optional-dependencies.dev]
mise exec -- uv pip install -e .[dev]
```

### Adding New Tasks

Edit `.mise.toml`:

```toml
[tasks.my-task]
description = "Description of my task"
run = "python script.py"
```

Run with: `mise run my-task`

### Environment Variables

Add new variables to `.env.example` and document them in this README.

## Troubleshooting

### mise not found

```bash
# Install mise first
curl https://mise.run | sh

# Then restart your shell
```

### Python not installing

```bash
# Check mise status
mise doctor

# Force reinstall
mise install --force python@3.11
```

### Virtual environment issues

```bash
# Remove and recreate
rm -rf .venv
mise install
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run quality checks: `mise run format && mise run type-check && mise run test`
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

MIT License - see LICENSE file for details

## Resources

- [mise Documentation](https://mise.jdx.dev)
- [pytest Documentation](https://docs.pytest.org/)
- [Black Documentation](https://black.readthedocs.io/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Mypy Documentation](https://mypy.readthedocs.io/)

## Acknowledgments

This template is designed for modern Python development with best practices and developer experience in mind.
