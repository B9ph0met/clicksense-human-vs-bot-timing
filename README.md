# ClickSense: Human vs Bot Timing Detector

ClickSense is a tiny experimental project that shows how simple timing signals can distinguish humans from automated scripts. It exposes a single web page with a “Continue” button, records how long it takes between page load and click, and then classifies each request as “likely human” or “likely bot” based on reaction time.

The goal is **not** to build a production anti-bot system or target any real website. Instead, this project demonstrates how basic behavioral signals already provide useful signal for abuse detection, in a safe and controlled environment.

---

## Features

- Minimal single-page front-end with a “Continue” button
- Backend that:
  - records page-load and click timestamps
  - computes reaction time in milliseconds
  - applies simple threshold-based classification
- Example “bot client” script (optional in future versions) that sends instant POST requests
- Simple JSON log output so you can inspect human vs bot timings

---

## How it Works

1. A user visits `/` and loads the page.
2. The page immediately records a `pageLoadTime` (using JavaScript).
3. When the user clicks “Continue,” the page sends both:
   - `pageLoadTime`
   - `clickTime`
4. The backend calculates:

   ```text
   reaction_time_ms = clickTime - pageLoadTime
