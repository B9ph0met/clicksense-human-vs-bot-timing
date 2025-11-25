from flask import Flask, request, jsonify
from flask import send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/click', methods=['POST'])
def click():
    data = request.json
    page_load = data['pageLoadTime']
    click = data['clickTime']

    reaction_time_ms = click - page_load

    if reaction_time_ms < 100:
        label = "likely_bot"
    elif reaction_time_ms <= 5000:
        label = "likely_human"
    else:
        label = "uncertain_or_slow"

    return jsonify({
        "reaction_time_ms": reaction_time_ms,
        "label": label
    })

if __name__ == "__main__":
    app.run(debug=True)
