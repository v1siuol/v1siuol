"""This module imports user's config."""

class Config:  # pylint: disable=too-few-public-methods
    """Configs are used to generate README template. Feel free to edit the fields."""
    NAME = 'v1siuol'
    SITE_URL = 'https://v1siuol.com/'

    ENABLE_HEADER = True

    SELF_INTRO = 'Software Engineer @FactSet'
    ENABLE_RECENT_POSTS = True
    BLOG_FEED_URL = 'https://v1siuol.com/rss2.xml'
    POSTS_DISPLAYED_NUM = 5

    ENABLE_GITHUB_STATS_CARD = True
    GITHUB_STATS_CARD = 'https://github-readme-stats.vercel.app/api?username=v1siuol&count_private=true&show_icons=true&hide_title=true&include_all_commits=true'  # pylint: disable=line-too-long

    ENABLE_WAKATIME_STATS_CARD = True
    WAKATIME_STATS_CARD = 'https://github-readme-stats.vercel.app/api/wakatime?username=v1siuol&hide_title=true'  # pylint: disable=line-too-long

    ENABLE_FOOTER = True
