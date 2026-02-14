# DataDevOps CLI - Output Examples

This document demonstrates the output of various CLI commands available in the DataDevOps CLI tool.

## Basic Help Output

### Main Help
```bash
$ datadevops --help
```
```
Usage: datadevops [OPTIONS] COMMAND [ARGS]...

  DataDevOps CLI - Your data operations command-line tool.

Options:
  --env [dev|test|prod]  Environment to use
  --debug / --no-debug   Enable debug mode
  --help                 Show this message and exit.

Commands:
  config  Configuration management commands.
  data    Data operations commands.
  health  Health check commands.
```

## Health Commands

### Health Commands Help
```bash
$ datadevops health --help
```
```
Usage: datadevops health [OPTIONS] COMMAND [ARGS]...

  Health check commands.

Options:
  --help  Show this message and exit.

Commands:
  api     Check API health.
  status  Check system health status.
```

### Health Status (Dev Environment)
```bash
$ datadevops health status
```
```
Environment: dev
Debug: True
API Base URL: http://localhost:8000
✓ CLI is healthy
```

### Health Status with Debug Mode
```bash
$ datadevops --env dev --debug health status
```
```
2026-02-14 18:19:42,243 - cli.main - DEBUG - Debug mode enabled. Environment: dev
Environment: dev
Debug: True
API Base URL: http://localhost:8000
✓ CLI is healthy
```

## Configuration Commands

### Config Commands Help
```bash
$ datadevops config --help
```
```
Usage: datadevops config [OPTIONS] COMMAND [ARGS]...

  Configuration management commands.

Options:
  --help  Show this message and exit.

Commands:
  show    Show current configuration.
  switch  Switch environment.
```

### Show Configuration (Dev Environment)
```bash
$ datadevops config show
```
```
Current Configuration:
  Environment: dev
  Debug Mode: True
  Log Level: DEBUG
  API Base URL: http://localhost:8000
  Request Timeout: 30s
  Max Retries: 3
```

### Show Configuration (Test Environment)
```bash
$ datadevops --env test config show
```
```
Current Configuration:
  Environment: test
  Debug Mode: True
  Log Level: DEBUG
  API Base URL: http://localhost:8000
  Request Timeout: 30s
  Max Retries: 3
```

### Show Configuration (Production Environment)
```bash
$ datadevops --env prod config show
```
```
Current Configuration:
  Environment: prod
  Debug Mode: False
  Log Level: DEBUG
  API Base URL: http://localhost:8000
  Request Timeout: 30s
  Max Retries: 3
```

## Data Commands

### Data Commands Help
```bash
$ datadevops data --help
```
```
Usage: datadevops data [OPTIONS] COMMAND [ARGS]...

  Data operations commands.

Options:
  --help  Show this message and exit.

Commands:
  export-data    Export data to destination.
  import-data    Import data from source.
  list-datasets  List available datasets.
```

### List Datasets
```bash
$ datadevops data list-datasets
```
```
2026-02-14 18:19:47,079 - cli.commands.data - INFO - Listing datasets in dev environment
Available datasets in dev:
  - dataset1
  - dataset2
  - dataset3
```

### List Datasets (Test Environment)
```bash
$ datadevops --env test data list-datasets
```
```
2026-02-14 18:19:47,079 - cli.commands.data - INFO - Listing datasets in test environment
Available datasets in test:
  - dataset1
  - dataset2
  - dataset3
```

## Additional Examples

### Import Data
```bash
$ datadevops data import-data /path/to/data --format csv
```
```
2026-02-14 18:19:47,079 - cli.commands.data - INFO - Importing data from /path/to/data in csv format
✓ Data imported successfully from /path/to/data (format: csv)
```

### Export Data
```bash
$ datadevops data export-data /path/to/output --format json
```
```
2026-02-14 18:19:47,079 - cli.commands.data - INFO - Exporting data to /path/to/output in json format
✓ Data exported successfully to /path/to/output (format: json)
```

### API Health Check
```bash
$ datadevops health api
```
```
Checking API health...
Endpoint: http://localhost:8000/health
✓ API is healthy
Response time: 0.045s
```

### Switch Environment
```bash
$ datadevops config switch --env test
```
```
Switching to test environment...
✓ Environment switched to: test
```

## Running with Different Environments

### Dev Environment (Default)
```bash
$ datadevops --env dev health status
```

### Test Environment
```bash
$ datadevops --env test health status
```

### Production Environment
```bash
$ datadevops --env prod health status
```

## Debug Mode Examples

### Debug Mode Enabled
```bash
$ datadevops --debug health status
```
```
2026-02-14 18:19:42,243 - cli.main - DEBUG - Debug mode enabled. Environment: dev
Environment: dev
Debug: True
API Base URL: http://localhost:8000
✓ CLI is healthy
```

### Combined Flags
```bash
$ datadevops --env test --debug config show
```
```
2026-02-14 18:19:42,243 - cli.main - DEBUG - Debug mode enabled. Environment: test
Current Configuration:
  Environment: test
  Debug Mode: True
  Log Level: DEBUG
  API Base URL: http://localhost:8000
  Request Timeout: 30s
  Max Retries: 3
```

## Summary

The DataDevOps CLI provides:
- ✅ Multi-environment support (dev, test, prod)
- ✅ Health check commands for monitoring system status
- ✅ Data operations (import, export, list)
- ✅ Configuration management
- ✅ Debug mode for detailed logging
- ✅ Easy-to-use command structure

For more information, see the [README.md](README.md) file.
