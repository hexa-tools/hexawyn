from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter
from hexawyn.application.ports.driven.datadog_port import DatadogMonitoringPort
from hexawyn.application.ports.driven.k8s_port import ClusterHealthPort, K8sPort
from hexawyn.application.ports.driven.logs_port import LogsPort
from hexawyn.application.ports.driven.metrics_port import MetricsPort
from hexawyn.application.ports.driven.openshift_port import OpenshiftPort
from hexawyn.application.ports.driven.traces_port import TracesPort


class TestDemoAdapterInit:
    def test_default_scenario_is_aws_eks(self):
        adapter = DemoAdapter()
        assert adapter.scenario == "aws_eks"

    def test_unknown_scenario_falls_back_to_aws_eks(self):
        adapter = DemoAdapter(scenario="unknown_provider")
        assert adapter.scenario == "aws_eks"
        assert adapter.get_health_score() == 76

    def test_implements_all_ports(self):
        adapter = DemoAdapter()
        assert isinstance(adapter, K8sPort)
        assert isinstance(adapter, ClusterHealthPort)
        assert isinstance(adapter, MetricsPort)
        assert isinstance(adapter, TracesPort)
        assert isinstance(adapter, LogsPort)
        assert isinstance(adapter, OpenshiftPort)
        assert isinstance(adapter, DatadogMonitoringPort)


class TestDemoAdapterAWSEKS:
    def setup_method(self):
        self.adapter = DemoAdapter(scenario="aws_eks")

    def test_health_score(self):
        assert self.adapter.get_health_score() == 76

    def test_health_status(self):
        assert self.adapter.get_health_status() == "degraded"

    def test_list_pods_returns_all(self):
        pods = self.adapter.list_pods()
        assert len(pods) == 6

    def test_list_pods_filtered_by_namespace(self):
        pods = self.adapter.list_pods(namespace="production")
        assert all(p["namespace"] == "production" for p in pods)

    def test_list_pods_has_crashloop(self):
        pods = self.adapter.list_pods()
        crashloop = [p for p in pods if p["status"] == "CrashLoop"]
        assert len(crashloop) == 1
        assert crashloop[0]["restarts"] == 8

    def test_list_pods_has_pending(self):
        pods = self.adapter.list_pods()
        pending = [p for p in pods if p["status"] == "Pending"]
        assert len(pending) == 1

    def test_get_findings_has_critical(self):
        findings = self.adapter.get_findings()
        critical = [f for f in findings if f["severity"] == "critical"]
        assert len(critical) >= 1

    def test_get_suggestion_chips_max_4(self):
        chips = self.adapter.get_suggestion_chips()
        assert len(chips) <= 4

    def test_get_cluster_metrics(self):
        metrics = self.adapter.get_cluster_metrics()
        assert "cpu_utilization" in metrics
        assert "memory_utilization" in metrics
        assert metrics["pods_crashloop"] == 1


class TestDemoAdapterAzureAKS:
    def setup_method(self):
        self.adapter = DemoAdapter(scenario="azure_aks")

    def test_health_score_is_98(self):
        assert self.adapter.get_health_score() == 98

    def test_health_status_is_healthy(self):
        assert self.adapter.get_health_status() == "healthy"

    def test_no_crashloop_pods(self):
        pods = self.adapter.list_pods()
        crashloop = [p for p in pods if p["status"] == "CrashLoop"]
        assert len(crashloop) == 0


class TestDemoAdapterGCPGKE:
    def setup_method(self):
        self.adapter = DemoAdapter(scenario="gcp_gke")

    def test_health_score_is_84(self):
        assert self.adapter.get_health_score() == 84

    def test_slo_breach_in_metrics(self):
        metrics = self.adapter.get_cluster_metrics()
        assert metrics["p99_latency_ms"] > metrics["slo_threshold_ms"]


class TestDemoAdapterOpenShift:
    def setup_method(self):
        self.adapter = DemoAdapter(scenario="openshift")

    def test_health_score_is_71(self):
        assert self.adapter.get_health_score() == 71

    def test_list_projects(self):
        projects = self.adapter.list_projects()
        assert len(projects) == 3
        assert projects[0]["name"] == "production"

    def test_list_routes_has_no_tls_route(self):
        routes = self.adapter.list_routes()
        no_tls = [r for r in routes if not r["tls"]]
        assert len(no_tls) == 1
        assert no_tls[0]["name"] == "admin-route"

    def test_list_pipeline_runs_has_failed(self):
        runs = self.adapter.list_pipeline_runs()
        failed = [r for r in runs if r["status"] == "Failed"]
        assert len(failed) == 1


class TestDemoAdapterDatadog:
    def setup_method(self):
        self.adapter = DemoAdapter(scenario="datadog")

    def test_health_score_is_79(self):
        assert self.adapter.get_health_score() == 79

    def test_triggered_monitors_count(self):
        monitors = self.adapter.get_triggered_monitors()
        assert len(monitors) == 2

    def test_has_alert_monitor(self):
        monitors = self.adapter.get_triggered_monitors()
        alert = [m for m in monitors if m["status"] == "Alert"]
        assert len(alert) == 1

    def test_apm_payments_api_p99(self):
        services = self.adapter.get_apm_services()
        payments = [s for s in services if s["service"] == "payments-api"]
        assert payments[0]["p99_ms"] == 820

    def test_get_slow_traces_above_threshold(self):
        traces = self.adapter.get_slow_traces(
            service="payments-api",
            threshold_ms=500,
            time_window_minutes=15,
        )
        assert len(traces) >= 1
        assert all(t["p99_ms"] > 500 for t in traces)


class TestDemoAdapterClusterContext:
    def test_get_cluster_context_aws(self):
        adapter = DemoAdapter(scenario="aws_eks")
        ctx = adapter.get_cluster_context()
        assert ctx["name"] == "prod-eks-us-east-1"
        assert ctx["cluster"] == "eks-prod"
        assert ctx["provider"] == "aws"

    def test_get_cluster_context_azure(self):
        adapter = DemoAdapter(scenario="azure_aks")
        ctx = adapter.get_cluster_context()
        assert ctx["provider"] == "azure"

    def test_get_cluster_context_gcp(self):
        adapter = DemoAdapter(scenario="gcp_gke")
        ctx = adapter.get_cluster_context()
        assert ctx["provider"] == "gcp"

    def test_get_cluster_context_openshift(self):
        adapter = DemoAdapter(scenario="openshift")
        ctx = adapter.get_cluster_context()
        assert ctx["provider"] == "openshift"

    def test_get_cluster_context_datadog(self):
        adapter = DemoAdapter(scenario="datadog")
        ctx = adapter.get_cluster_context()
        assert ctx["name"] == "prod-eks-datadog"


class TestDemoAdapterSlackMessage:
    def test_get_slack_message_aws(self):
        adapter = DemoAdapter(scenario="aws_eks")
        msg = adapter.get_slack_message()
        assert "EKS" in msg
        assert "OOM" in msg

    def test_get_slack_message_azure(self):
        adapter = DemoAdapter(scenario="azure_aks")
        msg = adapter.get_slack_message()
        assert "AKS" in msg
        assert "healthy" in msg.lower()

    def test_get_slack_message_gcp(self):
        adapter = DemoAdapter(scenario="gcp_gke")
        msg = adapter.get_slack_message()
        assert "GKE" in msg

    def test_get_slack_message_openshift(self):
        adapter = DemoAdapter(scenario="openshift")
        msg = adapter.get_slack_message()
        assert "OpenShift" in msg
        assert "TLS" in msg

    def test_get_slack_message_datadog(self):
        adapter = DemoAdapter(scenario="datadog")
        msg = adapter.get_slack_message()
        assert "Datadog" in msg
        assert "820ms" in msg


class TestDemoAdapterSlowTracesEdgeCases:
    def test_get_slow_traces_fallback_when_service_not_found(self):
        adapter = DemoAdapter(scenario="datadog")
        traces = adapter.get_slow_traces(
            service="nonexistent-service",
            threshold_ms=100,
            time_window_minutes=10,
        )
        assert len(traces) >= 1
        assert all(t.get("trace_id", "").startswith("trace-nonexistent") for t in traces)

    def test_get_slow_traces_no_match_but_service_empty_returns_empty(self):
        adapter = DemoAdapter(scenario="datadog")
        traces = adapter.get_slow_traces(
            service="",
            threshold_ms=10,
            time_window_minutes=5,
        )
        assert len(traces) == 0


class TestDemoAdapterLogs:
    def test_search_logs_returns_mock_result(self):
        adapter = DemoAdapter(scenario="aws_eks")
        logs = adapter.search_logs(
            pattern="OOM",
            time_window_minutes=30,
            namespace="production",
        )
        assert len(logs) >= 1
        assert "message" in logs[0]
        assert "timestamp" in logs[0]

    def test_search_logs_without_namespace(self):
        adapter = DemoAdapter(scenario="aws_eks")
        logs = adapter.search_logs(
            pattern="error",
            time_window_minutes=15,
        )
        assert len(logs) == 2
        assert all("timestamp" in entry for entry in logs)
        assert "namespace all" in logs[0]["message"]


class TestDemoAdapterNamespaceFilterEdgeCases:
    def test_list_pods_namespace_no_match_returns_empty(self):
        adapter = DemoAdapter(scenario="aws_eks")
        pods = adapter.list_pods(namespace="nonexistent")
        assert len(pods) == 0

    def test_list_pods_namespace_filter_ml(self):
        adapter = DemoAdapter(scenario="aws_eks")
        pods = adapter.list_pods(namespace="ml")
        assert len(pods) == 1
        assert pods[0]["name"] == "ml-worker-8b3a1e-hn7k"


class TestDemoAdapterNonScenarioSpecific:
    def test_list_projects_on_aws_returns_empty(self):
        adapter = DemoAdapter(scenario="aws_eks")
        projects = adapter.list_projects()
        assert projects == []

    def test_list_routes_on_azure_returns_empty(self):
        adapter = DemoAdapter(scenario="azure_aks")
        routes = adapter.list_routes()
        assert routes == []

    def test_list_pipeline_runs_on_gcp_returns_empty(self):
        adapter = DemoAdapter(scenario="gcp_gke")
        runs = adapter.list_pipeline_runs()
        assert runs == []

    def test_get_triggered_monitors_on_vanilla_returns_empty(self):
        adapter = DemoAdapter(scenario="aws_eks")
        monitors = adapter.get_triggered_monitors()
        assert monitors == []

    def test_get_apm_services_on_gcp_returns_empty(self):
        adapter = DemoAdapter(scenario="gcp_gke")
        services = adapter.get_apm_services()
        assert services == []
