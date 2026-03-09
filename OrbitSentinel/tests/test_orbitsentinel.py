from orbitsentinel.engine import analyze

def test_analyze():
    result = analyze('data/sample_telemetry.csv')
    assert 'anomalies' in result