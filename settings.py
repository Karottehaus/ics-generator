from zoneinfo import ZoneInfo
from pathlib import Path

TIMEZONE = ZoneInfo("Europe/Zurich")
CONFIG_FILE = Path(__file__).parent.parent / "config" / "config.ini"
