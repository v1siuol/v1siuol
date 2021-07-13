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
    This module will overwrite your `README.md`. If you are unfamiliar with this project,
    backup the file first.
"""

from __future__ import annotations  # pylint: disable=no-name-in-module
import os
from layout.header import inject_header  # pylint: disable=import-error
from layout.about_me import inject_about_me  # pylint: disable=import-error
from layout.github_stats import inject_github_stats  # pylint: disable=import-error
from layout.code_time import inject_code_time  # pylint: disable=import-error
from layout.footer import inject_footer  # pylint: disable=import-error
import utils  # pylint: disable=import-error


def default_template() -> str:
    """Return a default template in string."""
    # TODO (v1siuol): Consider move it to layout/index
    return r"""<!-- header starts -->

<!-- header ends -->

<!-- about_me_block starts -->

<!-- about_me_block ends -->

<!-- github_stats_block starts -->

<!-- github_stats_block ends -->

<!-- code_time_block starts -->

<!-- code_time_block ends -->

<!-- footer starts -->

<!-- footer ends -->
"""

def overwrite_template(template: str) -> str:
    """Overwrite the template by markers."""
    template = utils.replace_chunk(template, 'header', inject_header(), inline=False)
    template = utils.replace_chunk(template, 'about_me_block', inject_about_me(), inline=False)
    template = utils.replace_chunk(
            template, 'github_stats_block', inject_github_stats(), inline=False)
    template = utils.replace_chunk(template, 'code_time_block', inject_code_time(), inline=False)
    template = utils.replace_chunk(template, 'footer', inject_footer(), inline=False)

    return template

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
    template = default_template()
    template = overwrite_template(template)
    # overwrite_readme(template)
    output_readme(template)

if __name__ == '__main__':
    main()
