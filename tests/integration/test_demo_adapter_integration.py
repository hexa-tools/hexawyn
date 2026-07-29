import os
from unittest.mock import patch

import pytest
from hexawyn.adapters.secondary.adapter_factory import build_adapters
from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter


class TestAdapterFactoryIntegration:
    @pytest.mark.integration
    @pytest.mark.parametrize(
        "scenario",
        ["aws_eks", "azure_aks", "gcp_gke", "openshift", "datadog"],
    )
    def test_demo_mode_returns_demo_adapter_for_each_scenario(self, scenario):
        with patch.dict(
            os.environ,
            {
                "HEXAWYN_DEMO_MODE": "true",
                "HEXAWYN_DEMO_SCENARIO": scenario,
            },
        ):
            adapter = build_adapters("minikube")
            assert isinstance(adapter, DemoAdapter)
            assert adapter.scenario == scenario

    @pytest.mark.integration
    def test_demo_mode_false_returns_vanilla_adapter(self):
        with patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}, clear=False):
            from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

            adapter = build_adapters("minikube")
            assert isinstance(adapter, VanillaAdapter)

    @pytest.mark.integration
    def test_unknown_scenario_falls_back_to_aws_eks(self):
        with patch.dict(
            os.environ,
            {
                "HEXAWYN_DEMO_MODE": "true",
                "HEXAWYN_DEMO_SCENARIO": "unknown_provider",
            },
        ):
            adapter = build_adapters("minikube")
            assert isinstance(adapter, DemoAdapter)
            assert adapter.scenario == "aws_eks"
            assert adapter.get_health_score() == 76  # noqa: PLR2004


class TestDemoAdapterScenariosIntegration:
    @pytest.mark.integration
    def test_aws_eks_full_scenario_data(self):
        adapter = DemoAdapter(scenario="aws_eks")

        assert adapter.get_health_score() == 76  # noqa: PLR2004
        assert adapter.get_health_status() == "degraded"

        pods = adapter.list_pods()
        assert len(pods) == 6  # noqa: PLR2004

        crashloop = [p for p in pods if p["status"] == "CrashLoop"]
        assert len(crashloop) == 1
        assert crashloop[0]["restarts"] == 8  # noqa: PLR2004

        findings = adapter.get_findings()
        critical = [f for f in findings if f["severity"] == "critical"]
        assert len(critical) >= 1
        assert "OOM" in critical[0]["message"]

        chips = adapter.get_suggestion_chips()
        assert len(chips) <= 4  # noqa: PLR2004
        assert len(chips) >= 1

        slack_msg = adapter.get_slack_message()
        assert "EKS" in slack_msg
        assert "76" in slack_msg

    @pytest.mark.integration
    def test_azure_aks_healthy_scenario(self):
        adapter = DemoAdapter(scenario="azure_aks")
        assert adapter.get_health_score() == 98  # noqa: PLR2004
        assert adapter.get_health_status() == "healthy"

        pods = adapter.list_pods()
        crashloop = [p for p in pods if p["status"] == "CrashLoop"]
        assert len(crashloop) == 0

    @pytest.mark.integration
    def test_gcp_gke_slo_breach(self):
        adapter = DemoAdapter(scenario="gcp_gke")
        metrics = adapter.get_cluster_metrics()
        assert metrics["p99_latency_ms"] > metrics["slo_threshold_ms"]

    @pytest.mark.integration
    def test_openshift_projects_and_routes(self):
        adapter = DemoAdapter(scenario="openshift")

        projects = adapter.list_projects()
        assert len(projects) == 3  # noqa: PLR2004

        routes = adapter.list_routes()
        no_tls = [r for r in routes if not r["tls"]]
        assert len(no_tls) == 1

        pipeline_runs = adapter.list_pipeline_runs()
        failed = [r for r in pipeline_runs if r["status"] == "Failed"]
        assert len(failed) == 1

    @pytest.mark.integration
    def test_datadog_monitors_and_apm(self):
        adapter = DemoAdapter(scenario="datadog")

        monitors = adapter.get_triggered_monitors()
        assert len(monitors) == 2  # noqa: PLR2004
        alert = [m for m in monitors if m["status"] == "Alert"]
        assert len(alert) == 1

        services = adapter.get_apm_services()
        payments = [s for s in services if s["service"] == "payments-api"]
        assert payments[0]["p99_ms"] == 820  # noqa: PLR2004

    @pytest.mark.integration
    def test_namespace_filter_works_across_scenarios(self):
        adapter = DemoAdapter(scenario="aws_eks")

        production_pods = adapter.list_pods(namespace="production")
        ml_pods = adapter.list_pods(namespace="ml")

        assert all(p["namespace"] == "production" for p in production_pods)
        assert all(p["namespace"] == "ml" for p in ml_pods)
        assert len(production_pods) + len(ml_pods) + len(
            adapter.list_pods(namespace="payments")
        ) + len(adapter.list_pods(namespace="auth")) == len(adapter.list_pods())

    @pytest.mark.integration
    def test_slow_traces_above_threshold(self):
        adapter = DemoAdapter(scenario="datadog")
        traces = adapter.get_slow_traces(
            service="payments-api",
            threshold_ms=500,
            time_window_minutes=15,
        )
        assert len(traces) >= 1
        assert all(t["p99_ms"] > 500 for t in traces)  # noqa: PLR2004

    @pytest.mark.integration
    def test_search_logs_returns_mock_results(self):
        adapter = DemoAdapter(scenario="aws_eks")
        logs = adapter.search_logs(
            pattern="OOM",
            time_window_minutes=30,
            namespace="production",
        )
        assert len(logs) >= 1
        assert all("message" in log for log in logs)
        assert all("timestamp" in log for log in logs)
        assert all("severity" in log for log in logs)
