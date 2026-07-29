from hexawyn.adapters.secondary.mock.scenarios.gcp_gke import GCP_GKE_SCENARIO

REQUIRED_KEYS = {"context", "health", "pods", "metrics", "findings", "chips", "slack_message"}


class TestGCPGKE:
    def test_has_required_keys(self):
        for key in REQUIRED_KEYS:
            assert key in GCP_GKE_SCENARIO

    def test_health_score(self):
        assert GCP_GKE_SCENARIO["health"]["score"] == 84  # noqa: PLR2004

    def test_slo_breach(self):
        assert GCP_GKE_SCENARIO["metrics"]["p99_latency_ms"] == 820  # noqa: PLR2004
        assert GCP_GKE_SCENARIO["metrics"]["slo_threshold_ms"] == 500  # noqa: PLR2004
