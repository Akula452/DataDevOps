.PHONY: help install install-dev install-test test lint format type-check clean build run run-dev

help:
	@echo "DataDevOps CLI - Available commands:"
	@echo ""
	@echo "Setup:"
	@echo "  make install          - Install production dependencies"
	@echo "  make install-dev      - Install development dependencies"
	@echo "  make install-test     - Install test dependencies"
	@echo ""
	@echo "Development:"
	@echo "  make run              - Run CLI (default: dev environment)"
	@echo "  make run-dev          - Run CLI in dev environment"
	@echo "  make run-test         - Run CLI in test environment"
	@echo ""
	@echo "Code Quality:"
	@echo "  make lint             - Run flake8 linting"
	@echo "  make format           - Format code with black and isort"
	@echo "  make type-check       - Run mypy type checking"
	@echo "  make test             - Run pytest suite"
	@echo "  make test-cov         - Run tests with coverage report"
	@echo ""
	@echo "Maintenance:"
	@echo "  make clean            - Remove build artifacts and cache files"
	@echo "  make build            - Build distribution packages"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

install-test:
	pip install -r requirements-test.txt

test:
	pytest tests/ -v

test-cov:
	pytest tests/ -v --cov=src/cli --cov-report=html --cov-report=term-missing

lint:
	flake8 src/cli tests

format:
	black src/cli tests
	isort src/cli tests

type-check:
	mypy src/cli

run: run-dev

run-dev:
	ENVIRONMENT=dev python -m cli.main --env dev

run-test:
	ENVIRONMENT=test python -m cli.main --env test

build: clean
	pip install build
	python -m build

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	find . -type d -name '*.egg-info' -exec rm -rf {} +
	rm -rf build/
	rm -rf dist/
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .coverage
