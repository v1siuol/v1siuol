"""Template for about_me."""

from __future__ import annotations  # pylint: disable=no-name-in-module
import feedparser  # pylint: disable=import-error


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
