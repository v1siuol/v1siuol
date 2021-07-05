"""
This module fetches recent posts in v1siuol's blog and then updates README.md.

Example:
    $ pip install -r requirements.txt  # Install dependencies
    $ pylint build_readme.py  # Linter
    $ mypy --ignore-missing-imports build_readme.py
    $ python build_readme.py

Warning:
    This method will overwrite your `README.md`. If you are unfamiliar with this project,
    backup the file first.
"""

from __future__ import annotations  # pylint: disable=no-name-in-module
import pathlib
import re
import os
import feedparser  # pylint: disable=import-error

def default_template() -> str:
    """Return a default template in string."""
    return r"""### Hi there 👋

#### 💛 I'm <a href="https://v1siuol.com/" target="_blank" rel="noopener noreferrer">v1siuol</a>

<!-- self_intro starts -->
- Software Engineer @FactSet
- Recent posts: <!-- recent_posts starts --><!-- recent_posts ends -->
<!-- self_intro ends -->

#### 💚 v1siuol's GitHub Stats

<!-- github_stats starts -->
![v1siuol's github stats](https://github-readme-stats.vercel.app/api?username=v1siuol&count_private=true&show_icons=true&hide_title=true&include_all_commits=true)
<!-- github_stats ends -->

#### 💙 v1sioul's Wakatime Stats

<!-- code_time starts -->
![v1sioul's wakatime stats](https://github-readme-stats.vercel.app/api/wakatime?username=v1siuol&hide_title=true)
<!-- code_time ends -->

#### 💜 The above sections are generated daily by <a href="https://github.com/v1siuol/v1siuol/actions" target="_blank" rel="noopener noreferrer">v1siuol/Actions</a>
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
    template = replace_chunk(template, 'recent_posts', format_posts(), inline=True)
    return template

def fetch_posts() -> list[dict[str, str]]:
    """Fetch posts in rss feed."""
    response = feedparser.parse('https://v1siuol.com/rss2.xml')

    if response.status != 200:
        raise ConnectionError()
    entries = response['entries']
    if len(entries) <= 0:
        raise UserWarning('No fetched posts.')

    return [
        {
            'title': entry['title'],
            'url': entry['link']
        }
        for entry in entries
    ]

def format_posts() -> str:
    """Format posts properly."""
    entries = fetch_posts()[:5]
    posts_md = ' | '.join(
        ['<a href="{url}" target="_blank" rel="noopener noreferrer">{title}</a>'.format(**entry) for entry in entries]  # pylint: disable=line-too-long
    )
    return posts_md

def get_readme_path() -> str:
    """Get the correct readme path."""
    # Get the directory of the script being run
    path = pathlib.Path(__file__).parent.resolve()
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
