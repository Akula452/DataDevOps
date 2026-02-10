# Quick Start Guide

## 1. Installation (5 minutes)

```bash
cd /workspaces/DataDevOps

# Install dependencies
pip install -r requirements.txt

# Or install in development mode
pip install -e .
```

## 2. First Run (2 minutes)

```bash
# Check help
python -m cli.main --help

# Run health check in dev environment
python -m cli.main --env dev health status

# Run health check in test environment
python -m cli.main --env test health status
```

## 3. Run Tests (3 minutes)

```bash
# Install test dependencies
pip install -r requirements-test.txt

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=src/cli
```

## 4. Code Quality Checks (2 minutes)

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run all checks
make lint
make type-check
make format
```

## 5. Using Make Commands

```bash
# See all available commands
make help

# Install in development mode
make install-dev

# Run tests
make test

# Format and lint
make format
make lint

# Run CLI
make run-dev
make run-test
```

## Available Environments

### Development (dev)
- **When**: Local development
- **API**: http://localhost:8000
- **Log Level**: DEBUG
- **Debug Mode**: Enabled
- **Command**: `datadevops --env dev ...`

### Testing (test)
- **When**: CI/CD on develop branch
- **API**: http://localhost:8001
- **Log Level**: DEBUG
- **Debug Mode**: Enabled
- **Command**: `datadevops --env test ...`

### Production (prod)
- **When**: CI/CD on main branch
- **API**: https://api.example.com
- **Log Level**: INFO
- **Debug Mode**: Disabled
- **Command**: `datadevops --env prod ...`

## Git Workflow

### Create a feature branch
```bash
git checkout -b feature/my-feature develop
```

### Make changes and test
```bash
make test
make lint
```

### Create Pull Request
- Base: `develop`
- Head: `feature/my-feature`

### After approval
```bash
git checkout develop
git pull
```

### Release to production
- Create PR from `develop` to `main`
- Automatically triggers production deployment
- Creates GitHub release

## Common Commands

```bash
# Show current configuration
datadevops config show

# Switch environments
datadevops --env test config show

# Health checks
datadevops health status
datadevops health api

# Data operations
datadevops data list-datasets
datadevops data import-data /path/to/data --format csv
datadevops data export-data /path/to/output --format json
```

## Environment Variables

Create `.env.local` to override settings:

```bash
ENVIRONMENT=dev
LOG_LEVEL=DEBUG
API_BASE_URL=http://localhost:8000
REQUEST_TIMEOUT=30
MAX_RETRIES=3
```

## Troubleshooting

### Command not found
```bash
pip install -e .
```

### Tests failing
```bash
pip install -r requirements-test.txt
pytest tests/ -v -s
```

### Import errors
```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
```

## Next Steps

1. **Add Commands**: Create new command files in `src/cli/commands/`
2. **Add Tests**: Write tests in `tests/` directory
3. **Configure API**: Update `.env.{env}` files with real API endpoints
4. **Push to Repository**: Create develop branch and start development
5. **Set up CI/CD**: GitHub Actions workflows are ready to use

## Support

- Documentation: See [README.md](README.md)
- Issues: https://github.com/Akula452/DataDevOps/issues
- PR Template: Create comprehensive PR descriptions with changes
