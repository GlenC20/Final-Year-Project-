from src.config import load_config
from src.weather import get_weather
from src.formatter_1 import format_daily_weather


def main():
    cfg = load_config()
    data = get_weather(cfg["lat"], cfg["lon"], cfg["timezone"])
    post = format_daily_weather(data)
    print(post)

if __name__ == "__main__":
    main()
import os
from src.config import load_config
from src.weather import get_weather
from src.formatter_1 import format_daily_weather
from src.mastodon_client import post_status

def main():
    cfg = load_config()
    data = get_weather(cfg["lat"], cfg["lon"], cfg["timezone"])
    status = format_daily_weather(data)

    mode = os.getenv("MODE", "print")  # print | post
    if mode == "post":
        post_status(cfg["mastodon_base_url"], cfg["mastodon_token"], status)
        print("Posted successfully.")
    else:
        print(status)

if __name__ == "__main__":
    main()
