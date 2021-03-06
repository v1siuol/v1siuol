"""Template for github_stats."""

  # pylint: disable=no-name-in-module
from config import Config  # pylint: disable=import-error


def enable_github_stats() -> bool:
    """Return True if github_stats enabled, i.e., output github stats block."""
    return Config.ENABLE_GITHUB_STATS_CARD

def inject_github_stats() -> str:
    """Return github_stats_md. If disabled, return empty string."""
    if not enable_github_stats():
        return ''
    github_stats = f"""#### 💚 {Config.NAME}'s GitHub Stats

![{Config.NAME}'s GitHub Stats]({Config.GITHUB_STATS_CARD})"""
    return github_stats
