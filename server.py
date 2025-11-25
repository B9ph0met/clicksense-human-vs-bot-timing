from flask import Flask, request, jsonify, send_from_directory
import csv
from datetime import datetime

app = Flask(__name__, static_folder='static')

LOG_FILE = "click_logs.csv"


def log_interaction(reaction_time_ms, label, user_agent, ip):
    """Append a single interaction to a CSV log file."""
    row = [
        datetime.utcnow().isoformat(),
        reaction_time_ms,
        label,
        user_agent,
        ip,
    ]
    header = ["timestamp_utc", "reaction_time_ms", "label", "user_agent", "ip"]

    # Create file with header if it doesn't exist yet
    try:
        with open(LOG_FILE, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(row)
    except FileExistsError:
        with open(LOG_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(row)


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/click", methods=["POST"])
def click():
    data = request.json
    page_load = data["pageLoadTime"]
    click_time = data["clickTime"]

    reaction_time_ms = click_time - page_load

    if reaction_time_ms < 100:
        label = "likely_bot"
    elif reaction_time_ms <= 5000:
        label = "likely_human"
    else:
        label = "uncertain_or_slow"

    # Grab some basic context about the client
    user_agent = request.headers.get("User-Agent", "unknown")
    ip = request.remote_addr or "unknown"

    # Log this interaction
    log_interaction(reaction_time_ms, label, user_agent, ip)

    return jsonify(
        {
            "reaction_time_ms": reaction_time_ms,
            "label": label,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
