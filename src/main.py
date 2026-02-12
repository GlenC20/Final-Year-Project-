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
