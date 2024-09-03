"""Module containing Hubstiff client."""
import httpx
import configparser

class HubstaffClient:
    """Hubstaff client class."""

    def __init__(self):
        """Initialize client and get auth token."""
        config = configparser.ConfigParser()
        config.read("config.ini")

        form_data = {
            "email": config["Hubstaff"]["email"],
            "password": config["Hubstaff"]["password"],
        }
        headers = {
            "AppToken": config["Hubstaff"]["AppToken"],
        }
        response = httpx.post(
            config["Hubstaff"]["BASE_URL"],
            headers=headers,
            data=form_data,
        )
        print(form_data)
        print(headers)
        print(response.text)