# 🥾 ClickSense — Human vs Bot Timing Classifier

A lightweight experiment demonstrating how simple behavioral signals — specifically **reaction time between page load and form submission** — can reliably distinguish **human users** from **automated bots** during high-demand product releases like sneaker drops.

This project includes:

* A **frontend checkout simulation** (sneaker drop style)
* A **Flask backend** that records:

  * page load timestamps
  * click timestamps
  * user-agent + IP
  * form field values (name, email, size, quantity, shipping)
* A **timing-based classifier** (`< 100ms = likely bot`)
* A **bot client simulator** that mimics automated checkout
* A **CSV logger** capturing all interactions
* A **data analysis + visualization tool** (`analyze.py`)

This repo acts as a miniature anti-bot research sandbox — showing how even a single behavioral signal provides strong separation between humans and automated traffic.

---

## 🚀 Features

### ✔ Realistic Sneaker-Drop UI

A clean frontend with fields for name, email, size, quantity, and shipping.

### ✔ Reaction-Time Classifier

The backend computes:

```
reaction_time_ms = clickTime - pageLoadTime
```

Bots submit instantly → extremely low reaction times.
Humans take seconds → extremely high reaction times.

### ✔ Automated Bot Client

`bot_client.py` sends 10 rapid-fire “checkout” requests with 0–40ms timing jitter.

### ✔ CSV Logging

Each interaction logs:

* timestamp
* reaction time
* label (likely_human / likely_bot)
* user agent
* IP
* form data

Stored in `click_logs.csv`.

### ✔ Data Visualization

`analyze.py` loads the CSV and generates:

* Summary statistics
* A histogram comparing human vs bot distributions

---

## 🧠 How It Works

1. A user loads the page.
2. The frontend immediately records a `pageLoadTime` using JavaScript.
3. When the user clicks **Place Order**, it records a `clickTime`.
4. Both timestamps + form fields are POSTed to the backend.
5. The backend computes a simple timing-based classification:

```python
if reaction_time_ms < 100:
    label = "likely_bot"
else:
    label = "likely_human"
```

6. All data is appended into `click_logs.csv`.
7. `analyze.py` visualizes the difference between human and bot reaction times.

---

## 📊 Results & Observations

During testing, traffic was generated from:

* **Manual human submissions** (by clicking the form normally)
* **Automated bot requests** using `bot_client.py`

The histogram shows a dramatic separation:

* **Bots:** 2–35 ms
* **Humans:** ~4,000–5,000 ms

Even without advanced fingerprinting, timing alone is an extremely strong signal:

* Humans naturally take hundreds to thousands of milliseconds to load → read → decide → click
* Bots submit almost instantly, even when jitter is added

### Key findings:

* **Reaction time is a powerful differentiator**
* A threshold as simple as **< 100 ms → "likely bot"** is highly accurate
* Timing-based scoring can be a useful **first-layer anti-bot defense**
* These measurements match real bot behavior seen in sneaker drops, ticketing systems, and limited-edition releases

---

## 📈 Example Visualization

After collecting data, run:

```bash
python3 analyze.py
```

to produce a histogram like:

```
Human vs Bot Reaction Time Distribution
```

(Humans cluster on the far right; bots cluster near zero.)

To display the chart in your README, add an image like:

```md
![Reaction Time Distribution](reaction_time_histogram.png)
```

---

## 🧪 Running the Project

Clone and install:

```bash
git clone https://github.com/YOUR_USERNAME/clicksense-human-vs-bot-timing.git
cd clicksense-human-vs-bot-timing
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Start the server:

```bash
python3 server.py
```

Visit in your browser:

```
http://127.0.0.1:5000
```

Run the bot simulator in a second terminal:

```bash
source venv/bin/activate
python3 bot_client.py
```

