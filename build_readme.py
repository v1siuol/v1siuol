"""
This module fetches recent posts in v1siuol's blog and then updates README.md.

Example:
    $ pip install -r requirements.txt  # Install dependencies
    $ pylint *.py **/*.py  # Linter
    $ mypy --ignore-missing-imports .
    $ python build_readme.py  # For development
    $ ENV=release python build_readme.py  # For release

Warning:
    This module will overwrite your `README.md`. If you are unfamiliar with this project,
    backup the file first.
"""

from __future__ import annotations  # pylint: disable=no-name-in-module
import pathlib
import re
import os
from layout.header import inject_header  # pylint: disable=import-error
from layout.about_me import format_posts  # pylint: disable=import-error
from layout.github_stats import inject_github_stats  # pylint: disable=import-error
from layout.code_time import inject_code_time  # pylint: disable=import-error
from layout.footer import inject_footer  # pylint: disable=import-error


def default_template() -> str:
    """Return a default template in string."""
    # TODO (v1siuol): Consider move it to layout/index
    return r"""<!-- header starts -->

<!-- header ends -->

<!-- about_me_block starts -->
#### 💛 I'm <a href="https://v1siuol.com/" target="_blank" rel="noopener noreferrer">v1siuol</a>

<!-- my_title starts -->
- Software Engineer @FactSet
<!-- my_title ends -->
- Recent posts: <!-- recent_posts starts --><!-- recent_posts ends -->
<!-- about_me_block starts -->

<!-- github_stats_block starts -->

<!-- github_stats_block ends -->

<!-- code_time_block starts -->

<!-- code_time_block ends -->

<!-- footer starts -->

<!-- footer ends -->
"""

def replace_chunk(content: str, marker: str, chunk: str, inline : bool = False) -> str:
    """Find the place where marker indicates in content, replace it by chunk.
    Line break is controlled by inline."""
    pattern = re.compile(
        r'<!\-\- {section} starts \-\->.*<!\-\- {section} ends \-\->'.format(section=marker),
        re.DOTALL,
    )
    if not inline:
        chunk = '\n{}\n'.format(chunk)
    chunk = '<!-- {section} starts -->{section_info}<!-- {section} ends -->'.format(
        section=marker, section_info=chunk)
    return pattern.sub(chunk, content)

def overwrite_template(template: str) -> str:
    """Overwrite the template by markers."""
    template = replace_chunk(template, 'header', inject_header(), inline=False)
    # TODO (v1siuol): Enhance about_me_block layout
    template = replace_chunk(template, 'recent_posts', format_posts(), inline=True)
    template = replace_chunk(template, 'github_stats_block', inject_github_stats(), inline=False)
    template = replace_chunk(template, 'code_time_block', inject_code_time(), inline=False)
    template = replace_chunk(template, 'footer', inject_footer(), inline=False)

    return template

def get_readme_path() -> str:
    """Get the current readme path."""
    # Get the directory of the script being run
    path = pathlib.Path(__file__).parent.resolve()
    environment = os.environ.get('ENV') or 'development'
    file_name = 'README-dev.md'
    if environment == 'release':
        file_name = 'README.md'
    readme_path = os.path.join(path, file_name)
    return readme_path

def overwrite_readme(template: str) -> None:
    """Overwrite readme."""
    readme_path = get_readme_path()
    with open(readme_path, 'w+') as readme:
        readme.write(template)

def main() -> None:
    """Main entry point."""
    template = default_template()
    template = overwrite_template(template)
    overwrite_readme(template)

if __name__ == '__main__':
    main()
