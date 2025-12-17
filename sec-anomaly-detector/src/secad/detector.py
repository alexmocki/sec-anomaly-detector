import pandas as pd

def build_alerts(df: pd.DataFrame) -> pd.DataFrame:
    if 'status' not in df.columns:
        raise ValueError("Expected column 'status' in input data")

    status = df["status"].astype(str).str.strip().str.lower()
    alerts = df[status == "failed"].copy()
    alerts["alert"] = "FAILED_EVENT"
    return alerts
