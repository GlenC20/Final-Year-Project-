import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()

    return {
        "mastodon_base_url": os.getenv("MASTODON_BASE_URL"),
        "mastodon_token": os.getenv("MASTODON_ACCESS_TOKEN"),
        "lat": os.getenv("LAT", "53.3498"),
        "lon": os.getenv("LON", "-6.2603"),
        "timezone": os.getenv("TIMEZONE", "Europe/Dublin"),
        "max_posts_per_day": int(os.getenv("MAX_POSTS_PER_DAY", 2)),
    }