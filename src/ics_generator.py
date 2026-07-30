from datetime import datetime
from pathlib import Path
from textwrap import dedent
from uuid import uuid4
from settings import TIMEZONE


def format_datetime(dt: datetime) -> str:
    return dt.strftime("%Y%m%dT%H%M%S")


def escape_text(value: str) -> str:
    return (
        value.replace("\\", "\\\\")
        .replace("\r\n", "\n")
        .replace("\r", "\n")
        .replace("\n", "\\n")
        .replace(";", "\\;")
        .replace(",", "\\,")
    )


def create_content(title: str, start: datetime, end: datetime, description: str, location: str, url: str) -> str:
    return dedent(f"""\
    BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:-//Hanyu//ICS Generator//EN
    CALSCALE:GREGORIAN
    BEGIN:VEVENT
    UID:{uuid4()}
    DTSTAMP:{format_datetime(datetime.now(TIMEZONE))}
    DTSTART;TZID=Europe/Zurich:{format_datetime(start)}
    DTEND;TZID=Europe/Zurich:{format_datetime(end)}
    SUMMARY:{escape_text(title)}
    DESCRIPTION:{escape_text(description)}
    LOCATION:{escape_text(location)}
    URL:{url}
    END:VEVENT
    END:VCALENDAR
    """)


def save_file(content: str, output_path: Path) -> None:
    output_path.write_text(content, encoding="utf-8")
