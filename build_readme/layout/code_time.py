"""Template for code_time."""

from config import Config  # pylint: disable=import-error


def enable_code_time() -> bool:
    """Return True if code_time enabled, i.e., output code time block."""
    return Config.ENABLE_WAKATIME_STATS_CARD

def inject_code_time() -> str:
    """Return code_time_md. If disabled, return empty string."""
    if not enable_code_time():
        return ''
    code_time = f"""#### 💙 {Config.NAME}'s WakaTime Stats

![{Config.NAME}'s WakaTime Stats]({Config.WAKATIME_STATS_CARD})"""
    return code_time
