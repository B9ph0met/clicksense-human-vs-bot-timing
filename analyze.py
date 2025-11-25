import pandas as pd
import matplotlib.pyplot as plt
import os

LOG_FILE = "click_logs.csv"


def main():
    if not os.path.isfile(LOG_FILE):
        print(f"[!] {LOG_FILE} not found. Generate some data first.")
        return

    df = pd.read_csv(LOG_FILE)

    if "reaction_time_ms" not in df.columns or "label" not in df.columns:
        print("[!] CSV does not have the expected columns.")
        print("    Columns found:", list(df.columns))
        return

    print("=== Overall reaction time stats (ms) ===")
    print(df["reaction_time_ms"].describe())
    print()

    # Basic splits
    humans = df[df["client_type"] == "human"]["reaction_time_ms"]
    fast_bots = df[df["client_type"] == "fast_bot"]["reaction_time_ms"]
    evasive_bots = df[df["client_type"] == "evasive_bot"]["reaction_time_ms"]

    print("=== Counts by client_type ===")
    print(df["client_type"].value_counts())
    print()

    print("=== Counts by label ===")
    print(df["label"].value_counts())
    print()

    # Confusion-style view: how often did each client_type get each label?
    if "client_type" in df.columns:
        print("=== client_type vs label ===")
        print(pd.crosstab(df["client_type"], df["label"]))
        print()

    # Only plot if we have some data
    plt.figure()
    if len(humans) > 0:
        plt.hist(humans, bins=15, alpha=0.7, label="human")
    if len(fast_bots) > 0:
        plt.hist(fast_bots, bins=15, alpha=0.7, label="fast_bot")
    if len(evasive_bots) > 0:
        plt.hist(evasive_bots, bins=15, alpha=0.7, label="evasive_bot")

    plt.xlabel("Reaction time (ms)")
    plt.ylabel("Count")
    plt.title("Reaction Time by Client Type")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
