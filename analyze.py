import pandas as pd
import matplotlib.pyplot as plt
import os


LOG_FILE = "click_logs.csv"


def main():
    if not os.path.isfile(LOG_FILE):
        print(f"[!] {LOG_FILE} not found. Generate some data first by using the site and/or bot_client.py.")
        return

    # Load data
    df = pd.read_csv(LOG_FILE)

    # Basic sanity check
    if "reaction_time_ms" not in df.columns or "label" not in df.columns:
        print("[!] CSV does not have the expected columns.")
        print("    Columns found:", list(df.columns))
        return

    # Overall stats
    print("=== Overall reaction time stats (ms) ===")
    print(df["reaction_time_ms"].describe())
    print()

    # Human vs bot splits
    humans = df[df["label"] == "likely_human"]["reaction_time_ms"]
    bots = df[df["label"] == "likely_bot"]["reaction_time_ms"]

    print("=== Human samples ===")
    print(f"Count: {len(humans)}")
    if len(humans) > 0:
        print(humans.describe())
    print()

    print("=== Bot samples ===")
    print(f"Count: {len(bots)}")
    if len(bots) > 0:
        print(bots.describe())
    print()

    if len(humans) == 0 or len(bots) == 0:
        print("[!] Need both human and bot samples to make a meaningful comparison.")
        return

    # Histogram: humans vs bots
    plt.figure()
    plt.hist(humans, bins=15, alpha=0.7, label="likely_human")
    plt.hist(bots, bins=15, alpha=0.7, label="likely_bot")
    plt.xlabel("Reaction time (ms)")
    plt.ylabel("Count")
    plt.title("Human vs Bot Reaction Time Distribution")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
