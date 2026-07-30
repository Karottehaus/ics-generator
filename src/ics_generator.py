from datetime import datetime
from pathlib import Path
from ics import Calendar, Event


def create_content(title: str, start: datetime, end: datetime, description: str, location: str, url: str) -> str:
    cal = Calendar()
    evt = Event(
        name=title,
        begin=start,
        end=end,
        description=description,
        location=location,
        url=url
    )
    cal.events.add(evt)
    return cal.serialize()


def save_file(content: str, output_path: Path) -> None:
    output_path.write_text(content, encoding="utf-8")
