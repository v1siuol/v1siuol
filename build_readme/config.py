"""This module imports user's config."""

class Config:  # pylint: disable=too-few-public-methods
    """Configs are used to generate README template. Feel free to edit the fields."""
    NAME = 'v1siuol'
    SITE_URL = 'https://v1siuol.com/'

    ENABLE_HEADER = True

    SELF_INTRO = 'Grad Student at CMU | Software Engineer Intern at eBay | ex Software Engineer at FactSet | Schreyer Honors Scholar at Penn State'  # pylint: disable=line-too-long
    ENABLE_RECENT_POSTS = True
    BLOG_FEED_URL = 'https://v1siuol.com/rss2.xml'
    POSTS_DISPLAYED_NUM = 5

    ENABLE_GITHUB_STATS_CARD = False
    GITHUB_STATS_CARD = 'https://github-readme-stats.vercel.app/api?username=v1siuol&count_private=true&show_icons=true&hide_title=true&include_all_commits=true&theme=transparent'  # pylint: disable=line-too-long

    ENABLE_WAKATIME_STATS_CARD = True
    WAKATIME_STATS_CARD = 'https://github-readme-stats.vercel.app/api/wakatime?username=v1siuol&hide_title=true&langs_count=10&layout=compact'  # pylint: disable=line-too-long

    ENABLE_FOOTER = True
