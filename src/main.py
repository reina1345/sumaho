"""Main entry point for the application."""

import sys
from pathlib import Path

from dotenv import load_dotenv

# Set UTF-8 encoding for Windows console
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def setup_environment() -> None:
    """Load environment variables from .env file."""
    # Load .env file from project root
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        load_dotenv(env_path)
        print(f"[OK] Loaded environment from: {env_path}")
    else:
        print("[INFO] No .env file found (optional)")
        print("  Create .env file if you need environment-specific settings")


def main() -> None:
    """Main application entry point."""
    print("=" * 60)
    print("Python mise Template - Application Starting")
    print("=" * 60)

    # Setup environment
    setup_environment()

    print("\n" + "=" * 60)
    print("Ready to develop!")
    print("=" * 60)

    # Add your application logic here
    print("\n[INFO] Add your application code in this file")
    print("[INFO] This is a clean Python project template")


if __name__ == "__main__":
    main()
