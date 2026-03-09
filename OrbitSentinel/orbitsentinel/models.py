
from dataclasses import dataclass

@dataclass
class Summary:
    project: str
    status: str
    notes: str = "AI telemetry anomaly watchtower for orbital systems"
