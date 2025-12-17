import argparse
import json
from pathlib import Path

import pandas as pd

from src.secad.detector import build_alerts


def read_events(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    suffix = path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(path)
    if suffix == ".json":
        return pd.read_json(path)

    raise ValueError("Unsupported input format. Use .csv or .json")


def write_alerts(df: pd.DataFrame, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    records = df.to_dict(orient="records")
    out_path.write_text(json.dumps(records, indent=2), encoding="utf-8")


def cmd_analyze(args: argparse.Namespace) -> int:
    inp = Path(args.input)
    out = Path(args.out) if args.out else Path("alerts.json")

    df = read_events(inp)
    alerts = build_alerts(df)

    if args.out:
        write_alerts(alerts, out)

    if len(alerts) == 0:
        print("No alerts.")
    else:
        print(alerts)

    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="sercad", description="Security anomaly detector (starter).")
    sub = p.add_subparsers(dest="command", required=True)

    a = sub.add_parser("analyze", help="Analyze events and output alerts")
    a.add_argument("input", help="Path to input file (.csv or .json)")
    a.add_argument("--out", help="Write alerts to JSON file (default: no file unless provided)")
    a.set_defaults(func=cmd_analyze)

    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())