import random

MESSAGES_COLD = [
    "Bundle up out there — it's a chilly one! 🧣",
    "Perfect weather for a hot cup of tea. ☕",
    "Don't forget your coat today! 🧥",
    "Brrr! Keep warm, Dublin. ❄️",
]

MESSAGES_WARM = [
    "Lovely day ahead — make the most of it! ☀️",
    "Rare Dublin sunshine — get outside! 😎",
    "A warm one today, enjoy it while it lasts! 🌞",
    "Summer vibes in Dublin today! 🌻",
]

MESSAGES_RAINY = [
    "Grab your umbrella before heading out! ☂️",
    "Classic Dublin weather — rain's on the way! 🌧️",
    "Don't let the rain dampen your day! 💪",
    "Wellies weather today, folks. 🥾",
]

MESSAGES_NORMAL = [
    "Stay prepared and have a great day! ☘️",
    "Another day in Dublin — make it a good one! 🍀",
    "Typical Irish weather — expect the unexpected! 🌈",
    "Your daily Dublin weather check-in. 🗺️",
    "Stay safe out there, Dublin! 💚",
]

def _pick_message(temp_max, rain):
    if rain > 5:
        return random.choice(MESSAGES_RAINY)
    elif temp_max >= 20:
        return random.choice(MESSAGES_WARM)
    elif temp_max <= 8:
        return random.choice(MESSAGES_COLD)
    else:
        return random.choice(MESSAGES_NORMAL)

def format_daily_weather(data, alerts=None):
    alerts = alerts or []
    daily = data["daily"]

    temp_max = daily["temperature_2m_max"][0]
    temp_min = daily["temperature_2m_min"][0]
    rain = daily["precipitation_sum"][0]

    alert_block = ""
    if alerts:
        alert_block = "\n\n" + "\n".join(alerts)

    message = _pick_message(temp_max, rain)

    return (
        "🌦 Dublin Weather Update\n"
        "📍 Dublin, Ireland\n\n"
        f"🌡 Max: {temp_max}°C\n"
        f"❄ Min: {temp_min}°C\n"
        f"🌧 Rain: {rain} mm"
        f"{alert_block}\n\n"
        f"{message}\n\n"
        "#Dublin #IrishWeather #weather #bot"
    )