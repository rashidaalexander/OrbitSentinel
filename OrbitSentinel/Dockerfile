FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install .
CMD ["python", "-m", "orbitsentinel.cli", "analyze", "data/sample_telemetry.csv"]
