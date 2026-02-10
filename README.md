# DataDevOps CLI

A command-line interface for DataDevOps operations with support for multiple environments and automated CI/CD workflows.

## Features

- 🚀 **Multi-environment support**: Dev, Test, and Production environments
- 📦 **Easy installation**: Simple setup with pip or make
- 🧪 **Comprehensive testing**: Unit and integration tests with pytest
- 📝 **Type-safe**: Full type hints with mypy support
- 🔍 **Code quality**: Black formatting, flake8 linting, and isort imports
- 🔄 **CI/CD ready**: GitHub Actions workflows for both develop and main branches
- 📊 **Configuration management**: Environment-specific configurations with .env files
- 🎯 **Logging**: Structured logging with debug support

## Project Structure

```
DataDevOps/
├── src/cli/                          # Main CLI package
│   ├── __init__.py
│   ├── main.py                       # CLI entry point
│   ├── config.py                     # Configuration management
│   ├── logger.py                     # Logging setup
│   └── commands/                     # CLI command groups
│       ├── __init__.py
│       ├── health.py                 # Health check commands
│       ├── data.py                   # Data operation commands
│       └── config.py                 # Configuration commands
├── tests/                            # Test suite
│   ├── __init__.py
│   ├── conftest.py                   # Pytest configuration
│   ├── test_main.py                  # Main CLI tests
│   ├── test_config.py                # Configuration tests
│   └── test_commands.py              # Command tests
├── config/                           # Configuration files
├── .github/workflows/                # CI/CD workflows
│   ├── develop.yml                   # Develop branch workflow
│   └── main.yml                      # Main branch workflow
├── .env.dev                          # Development environment config
├── .env.test                         # Test environment config
├── .env.prod                         # Production environment config
├── .env.example                      # Example environment config
├── setup.py                          # Setup configuration
├── pyproject.toml                    # Modern Python project config
├── requirements.txt                  # Production dependencies
├── requirements-dev.txt              # Development dependencies
├── requirements-test.txt             # Test dependencies
├── pytest.ini                        # Pytest configuration
├── setup.cfg                         # Tool configurations
├── Makefile                          # Development commands
├── __main__.py                       # Module entry point
└── README.md                         # This file
```

## Installation

### Prerequisites

- Python 3.9 or higher
- pip or conda

### Quick Start

#### Option 1: Using Make (Recommended)

```bash
# Install production dependencies
make install

# Install development dependencies
make install-dev

# Install test dependencies
make install-test
```

#### Option 2: Using pip

```bash
# Install in development mode
pip install -e .

# Install with development extras
pip install -e ".[dev]"

# Install with test extras
pip install -e ".[test]"
```

#### Option 3: Manual

```bash
# Install dependencies
pip install -r requirements.txt

# For development
pip install -r requirements-dev.txt

# For testing
pip install -r requirements-test.txt
```

## Usage

### Basic Commands

```bash
# Show help
datadevops --help

# Get status
datadevops health status

# Check API health
datadevops health api

# Show configuration
datadevops config show

# Switch environment
datadevops config switch --env test
```

### With Environment Flag

```bash
# Run in dev environment (default)
datadevops --env dev health status

# Run in test environment
datadevops --env test health status

# Run in production environment
datadevops --env prod health status
```

### With Debug Flag

```bash
# Enable debug mode
datadevops --debug health status

# Combined flags
datadevops --env dev --debug health status
```

### Data Operations

```bash
# Import data
datadevops data import-data /path/to/data --format csv

# Export data
datadevops data export-data /path/to/output --format json

# List datasets
datadevops data list-datasets
```

## Environment Configuration

The CLI supports three environments: **dev**, **test**, and **prod**. Each environment has its own configuration file:

### Development Environment (.env.dev)

```
ENVIRONMENT=dev
LOG_LEVEL=DEBUG
API_BASE_URL=http://localhost:8000
REQUEST_TIMEOUT=30
MAX_RETRIES=3
DEBUG=true
```

### Test Environment (.env.test)

```
ENVIRONMENT=test
LOG_LEVEL=DEBUG
API_BASE_URL=http://localhost:8001
REQUEST_TIMEOUT=10
MAX_RETRIES=1
DEBUG=true
```

### Production Environment (.env.prod)

```
ENVIRONMENT=prod
LOG_LEVEL=INFO
API_BASE_URL=https://api.example.com
REQUEST_TIMEOUT=30
MAX_RETRIES=3
DEBUG=false
```

### Using Custom Configuration

1. Create a `.env.local` file with custom variables
2. Set the `ENVIRONMENT` variable to switch environments
3. Environment-specific `.env.{env}` files are loaded automatically

## Development Workflow

### Running Tests

```bash
# Run all tests
make test

# Run with coverage report
make test-cov

# Run specific test file
pytest tests/test_main.py -v

# Run tests matching pattern
pytest tests/ -v -k "health"
```

### Code Quality

```bash
# Check code style
make lint

# Format code
make format

# Type checking
make type-check

# All code quality checks
make lint && make type-check
```

### Running CLI Locally

```bash
# Run in dev environment
make run-dev

# Run in test environment
make run-test

# Run directly
python -m datadevops --env dev health status
```

### Available Make Commands

Run `make help` to see all available commands:

- `make install` - Install production dependencies
- `make install-dev` - Install development dependencies
- `make install-test` - Install test dependencies
- `make test` - Run pytest suite
- `make test-cov` - Run tests with coverage
- `make lint` - Run flake8 linting
- `make format` - Format code with black/isort
- `make type-check` - Run mypy type checking
- `make run` - Run CLI in dev environment
- `make run-dev` - Run CLI in dev environment
- `make run-test` - Run CLI in test environment
- `make build` - Build distribution packages
- `make clean` - Clean build artifacts

## CI/CD Workflows

### Develop Branch (`develop.yml`)

Triggered on:
- Push to `develop` branch
- Pull requests to `develop` branch

Environment: **test**

Steps:
1. Code quality checks (flake8, black, mypy)
2. Test execution with pytest
3. Coverage reporting to Codecov
4. Package build
5. Deployment to test environment

### Main Branch (`main.yml`)

Triggered on:
- Push to `main` branch
- Pull requests to `main` branch

Environment: **prod**

Steps:
1. Code quality checks (flake8, black, mypy) with stricter requirements
2. Comprehensive test execution
3. Mandatory coverage reporting to Codecov
4. Package build
5. Deployment to production environment
6. Automatic GitHub release creation

## Branch Strategy

```
main (production)
  ↑
  └─ Pull Request ← develop (testing)
                     ↑
                     └─ Feature branches
```

- **main**: Production-ready code
- **develop**: Integration branch for testing
- **feature branches**: Individual feature development

## Adding New Commands

1. Create a new file in `src/cli/commands/`
2. Define command group using Click decorators
3. Register in `src/cli/commands/__init__.py`
4. Add to main CLI in `src/cli/main.py`

Example:

```python
# src/cli/commands/example.py
import click

@click.group()
def example():
    """Example command group."""
    pass

@example.command()
@click.pass_context
def subcommand(ctx):
    """Example subcommand."""
    config = ctx.obj["config"]
    click.echo(f"Running in {config.env} environment")
```

## Testing

The project includes comprehensive tests for:

- CLI main functionality
- Configuration management
- Command execution
- Environment switching
- Debug mode

Run tests with:

```bash
# All tests
pytest tests/

# With coverage
pytest tests/ --cov=src/cli

# Specific test
pytest tests/test_main.py::test_cli_with_dev_env -v
```

## Code Quality Standards

- **Formatting**: Black with 100-character line length
- **Imports**: isort with Black-compatible profile
- **Linting**: flake8 with max line length of 100
- **Type Checking**: mypy with strict mode
- **Testing**: 80%+ code coverage required
- **Documentation**: Docstrings for all public functions

## Dependencies

### Production
- click (8.0+) - CLI framework
- python-dotenv (0.19+) - Environment variable management
- pyyaml (6.0+) - YAML parsing
- requests (2.28+) - HTTP client

### Development
- black - Code formatter
- flake8 - Linter
- isort - Import sorter
- mypy - Type checker
- ipython - Interactive shell
- ipdb - Debugger

### Testing
- pytest - Test framework
- pytest-cov - Coverage plugin
- pytest-mock - Mocking support
- responses - HTTP mocking
- coverage - Coverage measurement

## Troubleshooting

### Command not found

```bash
# Reinstall CLI in development mode
pip install -e .
```

### Import errors

```bash
# Ensure src is in PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
```

### Test failures

```bash
# Run with verbose output
pytest tests/ -v -s

# Run specific test
pytest tests/test_main.py::test_cli_help -v
```

### Environment not switching

```bash
# Check current environment
datadevops config show

# Verify .env files exist
ls -la .env.*

# Set environment explicitly
ENVIRONMENT=test datadevops config show
```

## Contributing

1. Create a feature branch from `develop`
2. Make changes and write tests
3. Run `make lint && make test && make type-check`
4. Create a Pull Request to `develop`
5. After review, merge to `develop`
6. Create PR from `develop` to `main` for release

## License

MIT License - See LICENSE file for details

## Support

For issues, questions, or contributions, please visit:
[GitHub Issues](https://github.com/Akula452/DataDevOps/issues)

## Changelog

### Version 0.1.0 (Initial Release)

- Initial CLI setup with Click framework
- Multi-environment support (dev, test, prod)
- Health check commands
- Data operations commands
- Configuration management
- Comprehensive test suite
- CI/CD workflows for develop and main branches
- Code quality tools integration