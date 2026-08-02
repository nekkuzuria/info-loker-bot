import requests
from config import DISCORD_WEBHOOK_URL_LIST

def send_message(messages):
    chunks = [
        messages[i:i+1999]
        for i in range(0, len(messages), 1999)
    ]

    for chunk in chunks:
        for discord_webhook_url in DISCORD_WEBHOOK_URL_LIST:
            response = requests.post(
                discord_webhook_url,
                json={
                    "content": chunk
                }
            )
            print(response.status_code)
            print(response.text)
