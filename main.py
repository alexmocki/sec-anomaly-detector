import pandas as pd
from src.secad.detector import build_alerts

data = [
    {"user": "alice", "status": "OK"},
    {"user": "bob", "status": "Failed"},
    {"user": "charlie", "status": "OK"},
    {"user": "david", "status": "Failed"},
]

df = pd.DataFrame(data)

alerts = build_alerts(df)
print(alerts)