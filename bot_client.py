import time
import requests
import random
import sys

URL = "http://127.0.0.1:5000/click"


def send_click(client_type: str, offset_ms: int):
    """
    Send a single synthetic click with a given timing offset and client_type.
    """
    page_load = int(time.time() * 1000)
    click_time = page_load + offset_ms

    payload = {
        "pageLoadTime": page_load,
        "clickTime": click_time,
        "clientType": client_type,
        "formData": {
            "name": f"{client_type} client",
            "email": f"{client_type}@example.com",
            "size": "10",
            "quantity": "1",
            "shipping": "Standard (3–5 days)",
        },
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": f"{client_type}/0.1",
    }

    resp = requests.post(URL, json=payload, headers=headers, timeout=5)
    print(resp.json())


def run_fast_bot(n: int = 10):
    """
    Classic fast bot: 0–40ms reaction time.
    """
    print(f"Sending {n} fast_bot clicks...")
    for _ in range(n):
        offset = random.randint(0, 40)
        send_click("fast_bot", offset)
        time.sleep(0.1)


def run_evasive_bot(n: int = 10):
    """
    Evasive bot: tries to look human by waiting 800–2500 ms before 'clicking'.
    """
    print(f"Sending {n} evasive_bot clicks...")
    for _ in range(n):
        # 0.8s to 2.5s delay: more human-like, but still very regular vs real humans
        offset = random.randint(800, 2500)
        send_click("evasive_bot", offset)
        time.sleep(random.uniform(0.2, 0.8))


def main():
    """
    Usage:
        python3 bot_client.py fast
        python3 bot_client.py evasive
    """
    mode = "fast"
    if len(sys.argv) >= 2:
        mode = sys.argv[1].lower()

    if mode in ["fast", "fast_bot"]:
        run_fast_bot()
    elif mode in ["evasive", "evasive_bot"]:
        run_evasive_bot()
    else:
        print(f"Unknown mode '{mode}'. Use 'fast' or 'evasive'.")


if __name__ == "__main__":
    main()
