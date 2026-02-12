def format_daily_weather(data, alerts=None):
    alerts = alerts or []
    daily = data["daily"]

    temp_max = daily["temperature_2m_max"][0]
    temp_min = daily["temperature_2m_min"][0]
    rain = daily["precipitation_sum"][0]

    alert_block = ""
    if alerts:
        alert_block = "\n\n" + "\n".join(alerts)

    return (
        "🌦 Daily Weather Update\n\n"
        f"🌡 Max: {temp_max}°C\n"
        f"❄ Min: {temp_min}°C\n"
        f"🌧 Rain: {rain} mm"
        f"{alert_block}\n\n"
        "#weather #bot"
    )