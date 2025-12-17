# SecAD - Security Anomaly Detector

SecAD is a lightweight command-line tool for detecting security anomalies in authentication logs.

The project demonstrates a practical security analytics pipeline:
logs -> detection logic -> alerts (table / JSON).

---

## Features

- Parse authentication logs from CSV or JSON files
- Detect failed authentication events
- Output alerts as a table in terminal
- Export alerts to JSON for further analysis
- Simple and extensible CLI interface

---

## Project Structure

sec-anomaly-detector/
 |----src/secad/
| |----init.py
| |----detector.py  #Detection logic
| |----cli.py     #Command-line interface
 |----data/
| |----sample_logins.csv
 |----alerts.json.  #Generated alerts
(example output)
|----README.md
|----requirements.txt

---

## Usage

python -m src.secad.cli analyze data/sample_logins.csv --out alerts.json