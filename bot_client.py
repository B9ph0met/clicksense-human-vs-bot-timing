import time
import requests
import random

URL = "http://127.0.0.1:5000/click"


def send_bot_click(offset_ms=0):
    """
    Simulate a 'bot' that loads the page and clicks almost instantly.
    """
    page_load = int(time.time() * 1000)
    click_time = page_load + offset_ms  # tiny delay, still way faster than humans

    payload = {
        "pageLoadTime": page_load,
        "clickTime": click_time,
        "formData": {
            "name": "Bot Client",
            "email": "bot@example.com",
            "size": "10",
            "quantity": "1",
            "shipping": "Standard (3–5 days)",
        },
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "BotClient/0.1",
    }

    resp = requests.post(URL, json=payload, headers=headers, timeout=5)
    print(resp.json())


def main():
    print("Sending 10 bot clicks...")
    for i in range(10):
        # small random jitter between 0 and 40ms
        offset = random.randint(0, 40)
        send_bot_click(offset_ms=offset)
        time.sleep(0.1)  # short pause between clicks


if __name__ == "__main__":
    main()
