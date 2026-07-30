import requests
from utils.config_manager import get_google_maps_api_key
from settings import AUTOCOMPLETE_URL


def get_address_suggestions(query):
    api_key = get_google_maps_api_key()
    if not api_key or not query or len(query) < 4:
        return []

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key
    }
    data = {"input": query}

    try:
        response = requests.post(
            AUTOCOMPLETE_URL,
            json=data,
            headers=headers,
            timeout=5
        )

        if response.status_code == 200:
            suggestions = response.json().get("suggestions", [])
            return [s["placePrediction"]["text"]["text"] for s in suggestions if "placePrediction" in s]
    except Exception:
        pass

    return []
