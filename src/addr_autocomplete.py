import requests
from utils.config_manager import get_google_maps_api_key
from settings import AUTOCOMPLETE_URL


def get_address_suggestions(query):
    api_key = get_google_maps_api_key()
    query = query.strip() if query else ""
    if not api_key or len(query) < 4:
        return []

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key,
        "X-Goog-FieldMask": "suggestions.placePrediction.text.text"
    }
    data = {"input": query}

    try:
        response = requests.post(
            AUTOCOMPLETE_URL,
            json=data,
            headers=headers,
            timeout=5
        )
        response.raise_for_status()

        suggestions = response.json().get("suggestions", [])
        return [
            suggestion["placePrediction"]["text"]["text"]
            for suggestion in suggestions
        ]

    except requests.RequestException as exc:
        print(f"Autocomplete request failed: {exc}")
    except (ValueError, KeyError, TypeError) as exc:
        print(f"Invalid autocomplete response: {exc}")

    return []
