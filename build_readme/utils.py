"""This module provides utility functions that are used within build_readme."""

import re
import sys


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

def eprint(*args, **kwargs):
    """Print to stderr for debugging."""
    print(*args, file=sys.stderr, **kwargs)
