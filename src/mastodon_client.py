import os
import requests
from mastodon import Mastodon

def post_status(base_url: str, token: str, status: str) -> None:
    if not base_url or not token:
        raise ValueError("Missing MASTODON_BASE_URL or MASTODON_ACCESS_TOKEN")

    session = requests.Session()
    session.verify = False

    mastodon = Mastodon(access_token=token, api_base_url=base_url, session=session)
    mastodon.status_post(status)
