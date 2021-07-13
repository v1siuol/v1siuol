"""This module imports user's config."""

class Config:  # pylint: disable=too-few-public-methods
    """Configs are used to generate README template. Feel free to edit the fields."""
    NAME = 'v1siuol'

    ENABLE_HEADER = True

    ENABLE_GITHUB_STATS_CARD = True
    GITHUB_STATS_CARD = 'https://github-readme-stats.vercel.app/api?username=v1siuol&count_private=true&show_icons=true&hide_title=true&include_all_commits=true'  # pylint: disable=line-too-long

    ENABLE_WAKATIME_STATS_CARD = True
    WAKATIME_STATS_CARD = 'https://github-readme-stats.vercel.app/api/wakatime?username=v1siuol&hide_title=true'  # pylint: disable=line-too-long

    ENABLE_FOOTER = True
