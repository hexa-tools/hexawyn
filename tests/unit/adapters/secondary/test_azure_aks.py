from hexawyn.adapters.secondary.mock.scenarios.azure_aks import AZURE_AKS_SCENARIO

REQUIRED_KEYS = {"context", "health", "pods", "metrics", "findings", "chips", "slack_message"}


class TestAzureAKS:
    def test_has_required_keys(self):
        for key in REQUIRED_KEYS:
            assert key in AZURE_AKS_SCENARIO

    def test_health_score(self):
        assert AZURE_AKS_SCENARIO["health"]["score"] == 98  # noqa: PLR2004

    def test_all_pods_running(self):
        non_running = [p for p in AZURE_AKS_SCENARIO["pods"] if p["status"] != "Running"]
        assert len(non_running) == 0
