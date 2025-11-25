import time
import requests
import random

URL = "http://127.0.0.1:5000/click"

def send_bot_click(offset_ms=0):
    # Simulate page load + click very quickly
    page_load = int(time.time() * 1000)
    click_time = page_load + offset_ms  # small offset keeps it bot-fast

    payload = {
        "pageLoadTime": page_load,
        "clickTime": click_time,
    }

    headers = {
        "Content-Type": "application/json",
        # Optional: pretend to be a browser
        "User-Agent": "BotClient/0.1",
    }

    resp = requests.post(URL, json=payload, headers=headers)
    print(resp.json())


def main():
    print("Sending 10 bot clicks...")
    for i in range(10):
        # random jitter between 0 and 40 ms, still extremely fast
        offset = random.randint(0, 40)
        send_bot_click(offset_ms=offset)
        time.sleep(0.1)  # small delay between requests


if __name__ == "__main__":
    main()
