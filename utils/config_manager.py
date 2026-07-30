import configparser
from settings import CONFIG_FILE


def get_google_maps_api_key():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config.get("google_maps", "api_key", fallback="")
