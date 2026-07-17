import os
from unittest.mock import patch

import pytest

SCENARIOS = ["aws_eks", "azure_aks", "gcp_gke", "openshift", "datadog"]
EXPECTED_SCORES = {
    "aws_eks": 76,
    "azure_aks": 98,
    "gcp_gke": 84,
    "openshift": 71,
    "datadog": 79,
}


class TestDemoIntegration:
    @pytest.mark.parametrize("scenario", SCENARIOS)
    def test_adapter_factory_returns_demo_adapter_for_each_scenario(self, scenario: str):
        with patch.dict(
            os.environ,
            {
                "HEXAWYN_DEMO_MODE": "true",
                "HEXAWYN_DEMO_SCENARIO": scenario,
            },
        ):
            from hexawyn.adapters.secondary.adapter_factory import build_adapters
            from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

            adapter = build_adapters("test-cluster")
            assert isinstance(adapter, DemoAdapter)
            assert adapter.scenario == scenario

    @pytest.mark.parametrize("scenario,expected_score", EXPECTED_SCORES.items())
    def test_each_scenario_health_score(self, scenario: str, expected_score: int):
        from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

        adapter = DemoAdapter(scenario=scenario)
        assert adapter.get_health_score() == expected_score

    @pytest.mark.parametrize("scenario", SCENARIOS)
    def test_each_scenario_has_findings(self, scenario: str):
        from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

        adapter = DemoAdapter(scenario=scenario)
        findings = adapter.get_findings()
        assert len(findings) >= 1
        assert all("severity" in f for f in findings)
        assert all("message" in f for f in findings)
        assert all("remediation" in f for f in findings)

    @pytest.mark.parametrize("scenario", SCENARIOS)
    def test_each_scenario_has_chips(self, scenario: str):
        from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

        adapter = DemoAdapter(scenario=scenario)
        chips = adapter.get_suggestion_chips()
        assert 1 <= len(chips) <= 4

    @pytest.mark.parametrize("scenario", SCENARIOS)
    def test_each_scenario_slack_message_not_empty(self, scenario: str):
        from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

        adapter = DemoAdapter(scenario=scenario)
        msg = adapter.get_slack_message()
        assert len(msg) > 0

    def test_demo_mode_false_does_not_use_demo_adapter(self):
        with patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}, clear=False):
            from hexawyn.adapters.secondary.adapter_factory import build_adapters
            from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

            adapter = build_adapters("vanilla-cluster")
            assert not isinstance(adapter, DemoAdapter)
