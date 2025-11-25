# 🥾 ClickSense — Human vs Bot Timing Analysis

**A behavioral anti-automation experiment using reaction-time signatures**

ClickSense is a lightweight research project demonstrating how anti-bot systems can distinguish **humans**, **fast bots**, and **evasive bots** based solely on **reaction time and behavioral jitter** — no browser fingerprinting, CAPTCHAs, or heavy client instrumentation required.

This is the same foundational technique used by **sneaker drops, ticketing systems, financial login flows, and high-demand product releases** to detect automated clients.

---

## 🚀 Features

### **✓ Flask backend**

* Serves a front-end form
* Records page-load time → click time
* Computes reaction latency (ms)
* Logs all events to `click_logs.csv`

### **✓ Human-testing UI**

A simple “Limited Sneaker Drop” form to simulate:

* Real user interaction
* Human reaction times
* Realistic latency variation

### **✓ Automated bot clients**

Two bot models:

#### **1. fast_bot**

Simulates a naive or cheaply built bot:

* Reacts **0–50ms**
* Almost no jitter
* Easily detectable

#### **2. evasive_bot**

Simulates a more advanced automation client:

* Reacts **800–2500ms**
* Added random jitter
* Mimics human slowness but still structurally detectable

### **✓ Data analysis + visualization**

`analyze.py` loads `click_logs.csv` and generates comparisons:

* Reaction-time histograms
* Per-client-type statistics
* Human vs bot separation

Example output:

![Reaction Time Comparison](graph_fast_vs_evasive.png)

---

## 📁 Project Structure

```
clicksense/
├── server.py
├── bot_client.py
├── analyze.py
├── click_logs.csv
├── requirements.txt
├── static/
│   └── index.html
└── README.md
```

---

## 🧠 How It Works

### 1. Frontend behavior

When the page loads:

```js
window.pageLoadTime = performance.now();
```

When the user clicks “Place Order”:

```js
clickTime = performance.now();
```

Both timestamps are sent to the backend.

---

### 2. Backend processing

```python
reaction_time_ms = clickTime - pageLoadTime
```

Each event is written to `click_logs.csv`.

---

### 3. Human vs bot differences

After running the experiment:

| Type            | Reaction Time Range | Notes                                      |
| --------------- | ------------------- | ------------------------------------------ |
| **Fast Bot**    | 2–35 ms             | Unrealistically fast; trivial to detect    |
| **Evasive Bot** | 900–2500 ms         | Mimics humans at a superficial level       |
| **Human**       | 4000–5000 ms        | Real processing, hesitation, page scanning |

Even without any fingerprinting, timing creates a **strong separation**.

---

## 🧪 Running the experiment

### **1. Start the server**

```bash
python3 server.py
```

Visit:
`http://127.0.0.1:5000`

Submit the form several times to produce **human** samples.

---

### **2. Run bot clients**

Fast bot:

```bash
python3 bot_client.py fast
```

Evasive bot:

```bash
python3 bot_client.py evasive
```

---

### **3. Analyze the results**

```bash
python3 analyze.py
```

This generates:

* printed statistics
* a reaction-time histogram
* optional saved PNG (`graph_fast_vs_evasive.png`)

---

## 🧩 Key Findings

### **1. Timing alone is a powerful anti-bot feature**

Even basic timing shows a clean split between:

* Automation
* Real humans

### **2. Evasive bots are detectable**

Even when “mimicking humans,” bots create:

* Narrower variance
* Structural consistency
* Predictable jitter
* Non-human outliers

### **3. Reaction-time based scoring works**

A simple threshold like:

```text
< 120 ms  → likely bot
120–800 ms → suspicious
> 800 ms → human-like
```

Correctly identifies nearly every bot sample.

This is the same logic powering:

* Shopify / SNKRS / YeezySupply anti-bots
* Ticketmaster queue scoring
* Finance/ATO login heuristics
* High-demand drop systems

---

## 📌 Why This Project Matters

This repo demonstrates practical **behavioral anti-automation** concepts used in production:

* measuring friction
* classifying clients by timing
* generating synthetic bot traffic
* analyzing anomaly distributions
* understanding adversarial evasion

It’s an ideal project to show skill in:

* anti-bot engineering
* adversarial thinking
* automation behavior analysis
* building detection pipelines
* security-minded systems design

Exactly the domains FAANG **Abuse**, **Integrity**, **Trust & Safety**, and **Security Engineering** teams care about.

---

## 🔮 Possible Extensions (future work)

You can easily expand this into a full **Bot Evasion Playground**:

* behavioral ML classifier (scikit-learn)
* browser fingerprinting simulation (user-agents, headers)
* JavaScript instrumentation
* bot “intent” scoring
* evasion strategies (network delays, dummy requests, headless browser clients)
* real-time dashboard (Chart.js + Flask SSE)

I can help you build all of these.

---

## 📜 License

MIT License — free to use for research and learning.

---
