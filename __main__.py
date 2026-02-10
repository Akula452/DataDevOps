"""DataDevOps CLI - Configuration and entrypoint runner."""

import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

if __name__ == "__main__":
    from cli.main import cli
    cli(obj={})
