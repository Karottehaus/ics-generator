from zoneinfo import ZoneInfo
from pathlib import Path

TIMEZONE = ZoneInfo("Europe/Zurich")
CONFIG_FILE = Path(__file__).resolve().parent / "config" / "config.ini"
AUTOCOMPLETE_URL = "https://places.googleapis.com/v1/places:autocomplete"
