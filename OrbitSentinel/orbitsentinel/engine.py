
from __future__ import annotations
import csv, statistics

def load_telemetry(path: str) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def analyze(path: str) -> dict:
    rows = load_telemetry(path)
    temps = [float(r["temperature"]) for r in rows]
    errors = [float(r["attitude_error"]) for r in rows]
    drifts = [float(r["signal_drift"]) for r in rows]
    avg_temp = statistics.mean(temps)
    anomalies = []
    for row in rows:
        score = 0
        if float(row["temperature"]) > avg_temp + 3:
            score += 1
        if float(row["attitude_error"]) > 0.3:
            score += 1
        if float(row["signal_drift"]) > 1.0:
            score += 1
        if score:
            anomalies.append({"timestamp": row["timestamp"], "score": score})
    return {
        "frames": len(rows),
        "avg_temp": round(avg_temp, 2),
        "max_attitude_error": max(errors),
        "max_signal_drift": max(drifts),
        "anomalies": anomalies,
    }
