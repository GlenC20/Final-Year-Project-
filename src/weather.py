import requests

def get_weather(lat, lon, timezone):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
        "timezone": timezone,
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()
