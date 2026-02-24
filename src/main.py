import os
from src.logger import setup_logger
from src.config import load_config
from src.weather import get_weather
from src.formatter_1 import format_daily_weather
from src.alerts import check_severe_weather
from src.mastodon_client import post_status

def main():
    logger = setup_logger()
    logger.info("Run started")

    try:
        cfg = load_config()
        logger.info("Config loaded")

        data = get_weather(cfg["lat"], cfg["lon"], cfg["timezone"])
        logger.info("Weather fetched successfully")

        alerts = check_severe_weather(data)
        logger.info("Alerts computed: %d", len(alerts))

        status = format_daily_weather(data, alerts)

        mode = os.getenv("MODE", "print")  # print | post
        logger.info("Mode: %s", mode)

        if mode == "post":
            post_status(cfg["mastodon_base_url"], cfg["mastodon_token"], status)
            logger.info("Posted successfully to Mastodon")
            print("Posted successfully.")
        else:
            print(status)
            logger.info("Printed status (no post)")

    except Exception as e:
        logger.exception("Run failed: %s", e)
        raise
    finally:
        logger.info("Run finished")
