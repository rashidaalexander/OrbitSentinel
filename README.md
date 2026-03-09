# OrbitSentinel
<img width="1600" height="420" alt="banner" src="https://github.com/user-attachments/assets/b8f84e7e-fea8-42e6-9363-74a2767724e6" />

![starfield](https://github.com/user-attachments/assets/6eabb67a-5752-460b-a0b9-3317771117ab)


<p align="center">
  <img src="assets/starfield.gif" alt="OrbitSentinel starfield" width="100%" />
</p>

```text
ORBITSENTINEL
```

**AI telemetry anomaly watchtower for orbital systems**

![License](https://img.shields.io/badge/license-MIT-ff4d4f) ![Python](https://img.shields.io/badge/python-3.11+-ff4d4f) ![Docker](https://img.shields.io/badge/docker-ready-ff4d4f) ![Tests](https://img.shields.io/badge/tests-passing-ff4d4f)

**Related:** [SignalNebula](../SignalNebula) • [OrbitalGraph](../OrbitalGraph)

## Overview

Analyzes satellite telemetry samples, scores anomalies, and generates operator-ready incident summaries.

## Why this repo exists

OrbitSentinel is part of a space-AI-security ecosystem designed to look and behave like a small open research lab. It ships with runnable code, sample data, a CLI, tests, Docker support, architecture notes, and ADR-style design records so the repository feels serious the second someone lands on it.

## Architecture

<img width="762" height="220" alt="Screenshot 2026-03-09 at 1 09 11 AM" src="https://github.com/user-attachments/assets/51b50e5a-d761-4990-97c5-57f9445f9c51" />

**Pipeline**

Telemetry ingest → anomaly scoring → threshold reasoning → operator report

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m orbitsentinel.cli analyze data/sample_telemetry.csv
python -m orbitsentinel.cli report data/sample_telemetry.csv --format markdown
```

## Docker

```bash
docker build -t orbitsentinel .
docker run --rm orbitsentinel
```

## Repository layout

```text
orbitsentinel/
├── orbitsentinel/
│   ├── cli.py
│   ├── engine.py
│   ├── models.py
│   └── utils.py
├── data/
├── docs/
│   ├── architecture.md
│   └── adr/
├── tests/
├── assets/
├── README.md
├── requirements.txt
├── Dockerfile
└── LICENSE
```

## Documentation

- `docs/architecture.md` for end-to-end system design
- `docs/adr/ADR-001.md` for processing choices
- `docs/adr/ADR-002.md` for report strategy
- `docs/adr/ADR-003.md` for ecosystem links

## Tests

```bash
pytest
```

## Notes

This project is a **research-style prototype** with sample datasets and operator-friendly outputs. It is intentionally presentation-heavy, but it still runs and produces real output from bundled data.

## License

MIT
