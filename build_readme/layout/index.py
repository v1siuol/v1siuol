"""Template for the README.md layout."""

import utils  # pylint: disable=import-error
from .header import inject_header
from .about_me import inject_about_me
from .github_stats import inject_github_stats
from .code_time import inject_code_time
from .footer import inject_footer

def default_template() -> str:
    """Return a default template in string."""
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

def generate_readme() -> str:
    """Return README.md as str."""
    template = default_template()
    template = overwrite_template(template)
    return template
