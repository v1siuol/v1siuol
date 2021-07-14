"""Template for about_me."""

import feedparser  # pylint: disable=import-error
from config import Config  # pylint: disable=import-error
import utils  # pylint: disable=import-error

def inject_about_me() -> str:
    """Return about_me_block_md."""
    template = default_template()
    template = overwrite_template(template)
    return template

def default_template() -> str:
    """Return a default template in string."""
    # pylint: disable=line-too-long
    return f"""#### 💛 I'm <a href="{Config.SITE_URL}" target="_blank" rel="noopener noreferrer">{Config.NAME}</a>

<!-- self_intro starts -->

<!-- self_intro ends -->
<!-- recent_posts starts -->

<!-- recent_posts ends -->"""
    # pylint: enable=line-too-long

def overwrite_template(template: str) -> str:
    """Overwrite the template by markers."""
    template = utils.replace_chunk(template, 'self_intro', inject_self_intro(), inline=False)
    template = utils.replace_chunk(template, 'recent_posts', inject_posts(), inline=False)
    return template

def inject_self_intro() -> str:
    """Return self_intro_md. For example, you can put your title here."""
    self_intro_md = f'- {Config.SELF_INTRO}'
    return self_intro_md

def enable_recent_posts() -> bool:
    """Return True if recent_posts enabled, i.e., output recent posts block."""
    return Config.ENABLE_RECENT_POSTS

def fetch_posts() -> list[dict[str, str]]:  # pylint: disable=unsubscriptable-object
    """Fetch posts in rss feed."""
    response = feedparser.parse(Config.BLOG_FEED_URL)

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
    entries = fetch_posts()[:Config.POSTS_DISPLAYED_NUM]
    posts_md = ' | '.join(
        ['<a href="{url}" target="_blank" rel="noopener noreferrer">{title}</a>'.format(**entry) for entry in entries]  # pylint: disable=line-too-long
    )
    return posts_md

def inject_posts() -> str:
    """Return recent_posts_md."""
    if not enable_recent_posts():
        return ''

    front_md = '- Recent posts: '
    posts_md = format_posts()
    return front_md + posts_md
