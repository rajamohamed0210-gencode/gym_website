#!/usr/bin/env python
"""Root-level Django manage.py shim.

Allows running `python manage.py ...` from the workspace root.
"""

import os
import sys


def main() -> None:
    project_root = os.path.dirname(os.path.abspath(__file__))
    django_project_dir = os.path.join(project_root, "realtimegym")

    # Ensure the nested Django project is importable from root commands.
    if django_project_dir not in sys.path:
        sys.path.insert(0, django_project_dir)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "realtimegym.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Use the virtual environment Python:\n"
            r"..\venv\Scripts\python.exe manage.py <command>"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
