#!/usr/bin/env python
import os
import sys
import environ  # <-- add this
import warnings
warnings.filterwarnings("ignore")

# Initialize environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(os.path.dirname(__file__), '.env'))  # <-- this line loads .env file

# Ensure the project root directory is in the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set the default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fraud_detection_api.settings")

def main():
    """Run administrative tasks."""
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
