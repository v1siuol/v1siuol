"""Template for footer."""

import sys
sys.path.append('..')
from config import Config  # pylint: disable=wrong-import-position


def enable_footer() -> bool:
    """Return True if footer enabled, i.e., output footer."""
    return Config.ENABLE_FOOTER

def inject_footer() -> str:
    """Return footer_md. If disabled, return empty string."""
    if not enable_footer():
        return ''

    footer = f"""#### 💜 The sections above are generated daily by <a href="https://github.com/{Config.NAME}/{Config.NAME}/actions" target="_blank" rel="noopener noreferrer">{Config.NAME}/Actions</a>"""  # pylint: disable=line-too-long
    return footer
