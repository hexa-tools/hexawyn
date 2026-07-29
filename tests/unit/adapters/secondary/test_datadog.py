from hexawyn.adapters.secondary.mock.scenarios.datadog import DATADOG_SCENARIO

REQUIRED_KEYS = {"context", "health", "pods", "metrics", "findings", "chips", "slack_message"}


class TestDatadog:
    def test_has_required_keys(self):
        for key in REQUIRED_KEYS:
            assert key in DATADOG_SCENARIO

    def test_health_score(self):
        assert DATADOG_SCENARIO["health"]["score"] == 79  # noqa: PLR2004

    def test_triggered_monitors(self):
        assert "triggered_monitors" in DATADOG_SCENARIO
        assert len(DATADOG_SCENARIO["triggered_monitors"]) == 2  # noqa: PLR2004
