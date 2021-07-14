"""
This module fetches recent posts in v1siuol's blog and then updates README.md.

Example:
    $ pip install -r requirements.txt  # Install dependencies
    $ pylint *.py **/*.py  # Linter
    $ mypy --ignore-missing-imports .
    $ python build_readme/build_readme.py > README-dev.md  # For development
    $ python build_readme/build_readme.py > README.md  # For release
    $ python build_readme.py  # For development
    $ ENV=release python build_readme.py  # For release

Warning:
    This module might overwrite your `README.md`. If you are unfamiliar with this project,
    backup the file first.
"""

import os
from layout.index import generate_readme  # pylint: disable=import-error


def get_readme_path() -> str:
    """Get the current readme path."""
    # Get the directory of the script being run
    path = os.path.dirname(os.path.abspath(__file__))
    environment = os.environ.get('ENV') or 'development'
    file_name = 'README-dev.md'
    if environment == 'release':
        file_name = 'README.md'
    readme_path = os.path.join(path, file_name)
    return readme_path

def overwrite_readme(template: str) -> None:
    """[deprecated] Overwrite readme."""
    readme_path = get_readme_path()
    with open(readme_path, 'w+') as readme:
        readme.write(template)

def output_readme(template: str) -> None:
    """stdout template to terminal and write to README.md via `>`"""
    print(template, end='')

def main() -> None:
    """Main entry point."""
    template = generate_readme()
    # overwrite_readme(template)
    output_readme(template)

if __name__ == '__main__':
    main()
