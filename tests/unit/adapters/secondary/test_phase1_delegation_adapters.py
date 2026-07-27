"""Tests for remaining delegation adapters."""

from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.night_intervention_adapter import NightInterventionAdapter
from hexawyn.adapters.secondary.gitops.optimization_roi_adapter import OptimizationRoiAdapter
from hexawyn.adapters.secondary.gitops.platform_reliability_adapter import (
    PlatformReliabilityAdapter,
)
from hexawyn.adapters.secondary.gitops.sla_report_adapter import SlaReportAdapter
from hexawyn.adapters.secondary.gitops.team_cost_kubernetes_adapter import TeamCostKubernetesAdapter


class TestNightInterventionAdapter:
    def test_delegates(self) -> None:
        source = Mock()
        source.fetch_night_intervention_data.return_value = []
        adapter = NightInterventionAdapter(source=source)
        assert adapter.get_night_intervention_data(6) == []
        source.fetch_night_intervention_data.assert_called_once_with(6)


class TestOptimizationRoiAdapter:
    def test_delegates(self) -> None:
        source = Mock()
        source.fetch_sprint_roi_data.return_value = {
            "has_baseline": False,
            "baseline_monthly_eur": 0.0,
        }
        adapter = OptimizationRoiAdapter(source=source)
        result = adapter.get_sprint_roi_data("sprint-1")
        assert result["has_baseline"] is False
        source.fetch_sprint_roi_data.assert_called_once_with("sprint-1")


class TestPlatformReliabilityAdapter:
    def test_delegates(self) -> None:
        source = Mock()
        source.fetch_reliability_data.return_value = {}
        adapter = PlatformReliabilityAdapter(source=source)
        result = adapter.get_reliability_data("2026-Q3")
        assert result == {}
        source.fetch_reliability_data.assert_called_once_with("2026-Q3")


class TestSlaReportAdapter:
    def test_get_quarter_sla_data_delegates(self) -> None:
        source = Mock()
        source.fetch_quarter_sla_data.return_value = {
            "has_data": False,
            "services": [],
            "breaches": [],
        }
        adapter = SlaReportAdapter(source=source)
        result = adapter.get_quarter_sla_data("2026-Q2")
        assert result["has_data"] is False

    def test_get_previous_quarter_avg_uptime_delegates(self) -> None:
        source = Mock()
        source.fetch_previous_quarter_avg_uptime.return_value = 99.9
        adapter = SlaReportAdapter(source=source)
        result = adapter.get_previous_quarter_avg_uptime("2026-Q2")
        assert result == 99.9  # noqa: PLR2004


from hexawyn.adapters.secondary.gitops.kubernetes_certificate_adapter import (  # noqa: E402
    KubernetesCertificateAdapter,
)
from hexawyn.adapters.secondary.gitops.kubernetes_event_adapter import (  # noqa: E402
    KubernetesEventAdapter,  # noqa: E402
)
from hexawyn.adapters.secondary.gitops.recurring_incident_adapter import (  # noqa: E402
    RecurringIncidentAdapter,  # noqa: E402
)
from hexawyn.domain.models.tls_certificate_diagnosis import (  # noqa: E402
    TLSCertificateDiagnosticRequest,  # noqa: E402
)


class TestKubernetesCertificateAdapter:
    def test_fetch_certificate_pem_returns_none(self) -> None:
        adapter = KubernetesCertificateAdapter()
        req = TLSCertificateDiagnosticRequest(ingress_name="test", namespace="ns")
        assert adapter.fetch_certificate_pem(req) is None

    def test_fetch_ingress_hostname_returns_ingress_name(self) -> None:
        adapter = KubernetesCertificateAdapter()
        req = TLSCertificateDiagnosticRequest(ingress_name="my-ingress", namespace="ns")
        assert adapter.fetch_ingress_hostname(req) == "my-ingress"


class TestKubernetesEventAdapter:
    def test_fetch_k8s_events_returns_empty(self) -> None:
        adapter = KubernetesEventAdapter()
        req = Mock()
        assert adapter.fetch_k8s_events(req) == []

    def test_fetch_slowest_span_returns_none(self) -> None:
        adapter = KubernetesEventAdapter()
        assert adapter.fetch_slowest_span(Mock()) is None


from hexawyn.adapters.secondary.gitops.kubernetes_etcd_logs_adapter import (  # noqa: E402
    KubernetesETCDLogsAdapter,  # noqa: E402
)
from hexawyn.adapters.secondary.gitops.kubernetes_pipeline_for_service_adapter import (  # noqa: E402
    KubernetesPipelineForServiceAdapter,
)
from hexawyn.adapters.secondary.gitops.kubernetes_pipeline_run_logs_adapter import (  # noqa: E402
    KubernetesPipelineRunLogsAdapter,
)
from hexawyn.adapters.secondary.gitops.kubernetes_resource_yaml_adapter import (  # noqa: E402
    KubernetesResourceYAMLAdapter,
)
from hexawyn.domain.models.resource_yaml import ResourceYAMLRequest  # noqa: E402


class TestKubernetesResourceYAMLAdapter:
    def test_fetch_resource_returns_empty(self) -> None:
        adapter = KubernetesResourceYAMLAdapter()
        assert (
            adapter.fetch_resource(
                ResourceYAMLRequest(kind="Pod", resource_name="x", namespace="ns")
            )
            == {}
        )

    def test_resource_exists_returns_false(self) -> None:
        adapter = KubernetesResourceYAMLAdapter()
        assert (
            adapter.resource_exists(
                ResourceYAMLRequest(kind="Pod", resource_name="x", namespace="ns")
            )
            is False
        )


class TestKubernetesETCDLogsAdapter:
    def test_fetch_logs_returns_empty(self) -> None:
        adapter = KubernetesETCDLogsAdapter()
        assert adapter.fetch_logs(Mock()) == []


class TestKubernetesPipelineForServiceAdapter:
    def test_find_pipelines_returns_empty(self) -> None:
        adapter = KubernetesPipelineForServiceAdapter()
        assert adapter.find_pipelines(Mock()) == []


class TestKubernetesPipelineRunLogsAdapter:
    def test_fetch_step_logs_returns_empty(self) -> None:
        adapter = KubernetesPipelineRunLogsAdapter()
        assert adapter.fetch_step_logs(Mock()) == []


class TestRecurringIncidentAdapter:
    def test_fetch_incidents_returns_empty(self) -> None:
        adapter = RecurringIncidentAdapter()
        assert adapter.fetch_incidents(30) == []


class TestTeamCostKubernetesAdapter:
    def test_returns_empty(self) -> None:
        adapter = TeamCostKubernetesAdapter()
        assert adapter.fetch_namespace_resources("2026-07") == []
