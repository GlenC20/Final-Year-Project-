def format_daily_weather(data):
    daily = data["daily"]

    temp_max = daily["temperature_2m_max"][0]
    temp_min = daily["temperature_2m_min"][0]
    rain = daily["precipitation_sum"][0]

    return (
        "🌦 Daily Weather Update\n\n"
        f"🌡 Max: {temp_max}°C\n"
        f"❄ Min: {temp_min}°C\n"
        f"🌧 Rain: {rain} mm\n\n"
        "#weather #bot"
    )
