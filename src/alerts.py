def check_severe_weather(data):
    daily = data.get("daily", {})
    alerts = []

    rain = (daily.get("precipitation_sum") or [None])[0]
    tmax = (daily.get("temperature_2m_max") or [None])[0]

    if rain is not None and rain > 10:
        alerts.append(f"⚠ Heavy rain expected ({rain} mm)")

    if tmax is not None and tmax > 30:
        alerts.append(f"⚠ High temperature warning ({tmax}°C)")

    return alerts
