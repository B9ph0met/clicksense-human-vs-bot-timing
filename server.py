from flask import Flask, request, jsonify, send_from_directory
import csv
from datetime import datetime
import os

app = Flask(__name__, static_folder='static')

LOG_FILE = "click_logs.csv"


def log_interaction(reaction_time_ms, label, user_agent, ip, name, email, size, quantity, shipping):
    """Append a single interaction to a CSV log file."""
    row = [
        datetime.utcnow().isoformat(),
        reaction_time_ms,
        label,
        user_agent,
        ip,
        name,
        email,
        size,
        quantity,
        shipping
    ]

    header = [
        "timestamp_utc",
        "reaction_time_ms",
        "label",
        "user_agent",
        "ip",
        "name",
        "email",
        "size",
        "quantity",
        "shipping"
    ]

    # If file doesn't exist, create it with the header
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(row)


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/click", methods=["POST"])
def click():
    data = request.json

    page_load = data["pageLoadTime"]
    click_time = data["clickTime"]

    # compute timing
    reaction_time_ms = click_time - page_load

    # classify
    if reaction_time_ms < 100:
        label = "likely_bot"
    elif reaction_time_ms <= 5000:
        label = "likely_human"
    else:
        label = "uncertain_or_slow"

    # extract form fields (optional)
    form_data = data.get("formData", {})
    name = form_data.get("name", "")
    email = form_data.get("email", "")
    size = form_data.get("size", "")
    quantity = form_data.get("quantity", "")
    shipping = form_data.get("shipping", "")

    # client context
    user_agent = request.headers.get("User-Agent", "unknown")
    ip = request.remote_addr or "unknown"

    # write to CSV
    log_interaction(
        reaction_time_ms,
        label,
        user_agent,
        ip,
        name,
        email,
        size,
        quantity,
        shipping
    )

    return jsonify({
        "reaction_time_ms": reaction_time_ms,
        "label": label
    })


if __name__ == "__main__":
    app.run(debug=True)
