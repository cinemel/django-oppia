#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    is_test = 'test' in sys.argv or 'test _coverage' in sys.argv  # Covers regular testing and django-coverage
    settings = 'oppiamobile.settings_test' if is_test else 'oppiamobile.settings'
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?")
    execute_from_command_line(sys.argv)
