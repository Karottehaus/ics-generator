import streamlit as st


def show_error(message: str):
    """
    Displays an error message using Streamlit.
    """
    st.error(message)


def validate_input(title, event_date, event_time):
    """
    Validates the input fields and displays errors if necessary.
    """
    if not title.strip():
        show_error("Event title is required.")
        return False
    if event_date is None or event_time is None:
        show_error("Date and start time are required.")
        return False
    return True
