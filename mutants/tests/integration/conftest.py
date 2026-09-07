def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "integration: requires real DuckDB or real components — no mocks",
    )
