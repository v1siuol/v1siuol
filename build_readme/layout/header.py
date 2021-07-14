"""Template for header."""

  # pylint: disable=no-name-in-module
from config import Config  # pylint: disable=import-error


def enable_header() -> bool:
    """Return True if header enabled, i.e., output header."""
    return Config.ENABLE_HEADER

def inject_header() -> str:
    """Return header_md. If disabled, return empty string."""
    if not enable_header():
        return ''

    header = """### Hi there 👋"""
    return header
