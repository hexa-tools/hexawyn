import pytest
from hexawyn.adapters.secondary.mock.scenarios.aws_eks import AWS_EKS_SCENARIO
from hexawyn.adapters.secondary.mock.scenarios.azure_aks import AZURE_AKS_SCENARIO
from hexawyn.adapters.secondary.mock.scenarios.datadog import DATADOG_SCENARIO
from hexawyn.adapters.secondary.mock.scenarios.gcp_gke import GCP_GKE_SCENARIO
from hexawyn.adapters.secondary.mock.scenarios.openshift import OPENSHIFT_SCENARIO

REQUIRED_KEYS = {"context", "health", "pods", "metrics", "findings", "chips", "slack_message"}


class TestScenarioStructure:
    @pytest.mark.parametrize(
        "scenario",
        [
            AWS_EKS_SCENARIO,
            AZURE_AKS_SCENARIO,
            GCP_GKE_SCENARIO,
            OPENSHIFT_SCENARIO,
            DATADOG_SCENARIO,
        ],
    )
    def test_scenario_has_required_keys(self, scenario: dict):
        for key in REQUIRED_KEYS:
            assert key in scenario, f"Missing key: {key}"

    @pytest.mark.parametrize(
        "scenario",
        [
            AWS_EKS_SCENARIO,
            AZURE_AKS_SCENARIO,
            GCP_GKE_SCENARIO,
            OPENSHIFT_SCENARIO,
            DATADOG_SCENARIO,
        ],
    )
    def test_health_score_between_0_and_100(self, scenario: dict):
        assert 0 <= scenario["health"]["score"] <= 100

    @pytest.mark.parametrize(
        "scenario",
        [
            AWS_EKS_SCENARIO,
            AZURE_AKS_SCENARIO,
            GCP_GKE_SCENARIO,
            OPENSHIFT_SCENARIO,
            DATADOG_SCENARIO,
        ],
    )
    def test_health_status_valid(self, scenario: dict):
        assert scenario["health"]["status"] in {"healthy", "degraded", "critical"}

    @pytest.mark.parametrize(
        "scenario",
        [
            AWS_EKS_SCENARIO,
            AZURE_AKS_SCENARIO,
            GCP_GKE_SCENARIO,
            OPENSHIFT_SCENARIO,
            DATADOG_SCENARIO,
        ],
    )
    def test_chips_max_4(self, scenario: dict):
        assert len(scenario["chips"]) <= 4

    @pytest.mark.parametrize(
        "scenario,expected_score",
        [
            (AWS_EKS_SCENARIO, 76),
            (AZURE_AKS_SCENARIO, 98),
            (GCP_GKE_SCENARIO, 84),
            (OPENSHIFT_SCENARIO, 71),
            (DATADOG_SCENARIO, 79),
        ],
    )
    def test_exact_scores(self, scenario: dict, expected_score: int):
        assert scenario["health"]["score"] == expected_score


class TestAWSEKSScenario:
    def test_has_crashloop_pod(self):
        crashloop = [p for p in AWS_EKS_SCENARIO["pods"] if p["status"] == "CrashLoop"]
        assert len(crashloop) == 1
        assert crashloop[0]["name"] == "payments-api-7d9f8b-m3ql"
        assert crashloop[0]["restarts"] == 8

    def test_has_pending_pod(self):
        pending = [p for p in AWS_EKS_SCENARIO["pods"] if p["status"] == "Pending"]
        assert len(pending) == 1
        assert pending[0]["name"] == "ml-worker-8b3a1e-hn7k"

    def test_has_critical_finding(self):
        critical = [f for f in AWS_EKS_SCENARIO["findings"] if f["severity"] == "critical"]
        assert len(critical) >= 1
        assert "OOM" in critical[0]["message"]


class TestAzureAKSScenario:
    def test_all_pods_running(self):
        non_running = [p for p in AZURE_AKS_SCENARIO["pods"] if p["status"] != "Running"]
        assert len(non_running) == 0

    def test_score_is_healthy(self):
        assert AZURE_AKS_SCENARIO["health"]["status"] == "healthy"
        assert AZURE_AKS_SCENARIO["health"]["score"] >= 95


class TestGCPGKEScenario:
    def test_has_slo_breach(self):
        assert GCP_GKE_SCENARIO["metrics"]["p99_latency_ms"] == 820
        assert GCP_GKE_SCENARIO["metrics"]["slo_threshold_ms"] == 500
        assert (
            GCP_GKE_SCENARIO["metrics"]["p99_latency_ms"]
            > GCP_GKE_SCENARIO["metrics"]["slo_threshold_ms"]
        )

    def test_has_oom_prediction_finding(self):
        oom = [f for f in GCP_GKE_SCENARIO["findings"] if "OOM" in f["message"]]
        assert len(oom) >= 1


class TestOpenShiftScenario:
    def test_has_projects_not_namespaces(self):
        assert "projects" in OPENSHIFT_SCENARIO
        assert len(OPENSHIFT_SCENARIO["projects"]) == 3

    def test_has_routes(self):
        assert "routes" in OPENSHIFT_SCENARIO
        no_tls = [r for r in OPENSHIFT_SCENARIO["routes"] if not r["tls"]]
        assert len(no_tls) == 1
        assert no_tls[0]["name"] == "admin-route"

    def test_has_pipeline_runs(self):
        assert "pipeline_runs" in OPENSHIFT_SCENARIO
        failed = [p for p in OPENSHIFT_SCENARIO["pipeline_runs"] if p["status"] == "Failed"]
        assert len(failed) == 1


class TestDatadogScenario:
    def test_has_triggered_monitors(self):
        assert "triggered_monitors" in DATADOG_SCENARIO
        assert len(DATADOG_SCENARIO["triggered_monitors"]) == 2

    def test_has_alert_monitor(self):
        alert = [m for m in DATADOG_SCENARIO["triggered_monitors"] if m["status"] == "Alert"]
        assert len(alert) == 1
        assert "payments-api" in alert[0]["name"]

    def test_has_apm_services(self):
        assert "apm_services" in DATADOG_SCENARIO
        payments = [s for s in DATADOG_SCENARIO["apm_services"] if s["service"] == "payments-api"]
        assert payments[0]["p99_ms"] == 820
