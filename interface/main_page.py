import streamlit as st
from datetime import datetime, timedelta
from settings import TIMEZONE
from src.ics_generator import create_content
from src.addr_autocomplete import get_address_suggestions


def build_page():
    st.set_page_config(page_title="ICS Calendar Generator", page_icon="📅")
    st.title("ICS Calendar Generator")
    st.write("Create a calendar event and download it as an '.ics' file.")

    title = st.text_input("Event title", value="")

    date_column, time_column, duration_column = st.columns(3)
    with date_column:
        event_date = st.date_input(
            "Date",
            value=None,
            format="YYYY-MM-DD",
        )
    with time_column:
        event_time = st.time_input(
            "Start time",
            value=None,
            step=900,
        )
    with duration_column:
        duration_minutes = st.number_input(
            "Duration (minutes)",
            min_value=1,
            max_value=24 * 60,
            value=60,
            step=15,
        )

    st.session_state.setdefault("location_input", "")
    location = st.text_input("Location", key="location_input")
    suggestions = get_address_suggestions(location)

    if suggestions:
        st.write("Suggestions:")
        suggestion_columns = st.columns(len(suggestions[:3]))
        for index, suggestion in enumerate(suggestions[:3]):
            suggestion_columns[index].button(
                suggestion,
                key=f"suggestion_{index}_{suggestion}",
                on_click=lambda value=suggestion: st.session_state.update(
                    location_input=value
                ),
            )

    url = st.text_input("Event URL", value="")

    description = st.text_area(
        "Description",
        value="",
        height=150,
    )

    file_name = st.text_input("File name", value="")

    submitted = st.button("Create calendar file", type="primary")

    if submitted:
        if not title.strip():
            st.error("Event title is required.")
        elif event_date is None or event_time is None:
            st.error("Date and start time are required.")
        else:
            start = datetime.combine(event_date, event_time, tzinfo=TIMEZONE)
            end = start + timedelta(minutes=duration_minutes)
            ics_content = create_content(
                title=title.strip(),
                start=start,
                end=end,
                description=description,
                location=st.session_state.location_input,
                url=url
            )

            safe_file_name = file_name.strip() or "event.ics"
            if not safe_file_name.lower().endswith(".ics"):
                safe_file_name += ".ics"

            st.success("Your calendar file is ready.")
            st.download_button(
                "Download ICS file",
                data=ics_content.encode("utf-8"),
                file_name=safe_file_name,
                mime="text/calendar; charset=utf-8",
                type="primary"
            )

            with st.expander("Preview ICS content"):
                st.code(ics_content, language=None)
