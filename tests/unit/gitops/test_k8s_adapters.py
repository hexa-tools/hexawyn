from __future__ import annotations

from unittest.mock import MagicMock, patch

_CFG = "kubernetes.config.load_kube_config"
_API = "kubernetes.client.CoreV1Api"


class TestKubernetesResourceYAMLAdapter:
    def test_fetch_resource_returns_dict(self) -> None:
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0, stdout="kind: Pod\n  name: test\n")
            from hexawyn.adapters.secondary.gitops.kubernetes_resource_yaml_adapter import (
                KubernetesResourceYAMLAdapter,
            )
            from hexawyn.domain.models.resource_yaml import ResourceYAMLRequest

            adapter = KubernetesResourceYAMLAdapter()
            result = adapter.fetch_resource(
                ResourceYAMLRequest(resource_name="test", namespace="default", kind="Pod")
            )
            assert isinstance(result, dict)
            assert result.get("yaml", "").startswith("kind: Pod")

    def test_fetch_resource_empty_on_error(self) -> None:
        with patch("subprocess.run", side_effect=Exception("kubectl not found")):
            from hexawyn.adapters.secondary.gitops.kubernetes_resource_yaml_adapter import (
                KubernetesResourceYAMLAdapter,
            )
            from hexawyn.domain.models.resource_yaml import ResourceYAMLRequest

            adapter = KubernetesResourceYAMLAdapter()
            result = adapter.fetch_resource(
                ResourceYAMLRequest(resource_name="nonexistent", namespace="default", kind="Pod")
            )
            assert result == {}

    def test_fetch_resource_empty_on_non_zero(self) -> None:
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=1, stdout="")
            from hexawyn.adapters.secondary.gitops.kubernetes_resource_yaml_adapter import (
                KubernetesResourceYAMLAdapter,
            )
            from hexawyn.domain.models.resource_yaml import ResourceYAMLRequest

            adapter = KubernetesResourceYAMLAdapter()
            result = adapter.fetch_resource(
                ResourceYAMLRequest(resource_name="nonexistent", namespace="default", kind="Pod")
            )
            assert result == {}

    def test_resource_exists_true(self) -> None:
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0)
            from hexawyn.adapters.secondary.gitops.kubernetes_resource_yaml_adapter import (
                KubernetesResourceYAMLAdapter,
            )
            from hexawyn.domain.models.resource_yaml import ResourceYAMLRequest

            adapter = KubernetesResourceYAMLAdapter()
            result = adapter.resource_exists(
                ResourceYAMLRequest(resource_name="test", namespace="default", kind="Pod")
            )
            assert result is True

    def test_resource_exists_false_on_error(self) -> None:
        with patch("subprocess.run", side_effect=Exception("kubectl not found")):
            from hexawyn.adapters.secondary.gitops.kubernetes_resource_yaml_adapter import (
                KubernetesResourceYAMLAdapter,
            )
            from hexawyn.domain.models.resource_yaml import ResourceYAMLRequest

            adapter = KubernetesResourceYAMLAdapter()
            result = adapter.resource_exists(
                ResourceYAMLRequest(resource_name="test", namespace="default", kind="Pod")
            )
            assert result is False


class TestKubernetesETCDLogsAdapter:
    def test_fetch_logs_with_etcd_pods(self) -> None:
        with patch(_CFG), patch(_API) as mock_api:
            mock_v1 = MagicMock()
            pod = MagicMock()
            pod.metadata = MagicMock()
            pod.metadata.name = "etcd-node1"
            pod.metadata.namespace = "kube-system"
            mock_v1.list_pod_for_all_namespaces.return_value = MagicMock(items=[pod])
            mock_v1.read_namespaced_pod_log.return_value = (
                "2026-01-01 INFO etcd started\n2026-01-01 INFO etcd ready\n"  # noqa: E501
            )
            mock_api.return_value = mock_v1

            from hexawyn.adapters.secondary.gitops.kubernetes_etcd_logs_adapter import (
                KubernetesETCDLogsAdapter,
            )
            from hexawyn.domain.models.etcd_logs import ETCDLogsRequest

            adapter = KubernetesETCDLogsAdapter()
            result = adapter.fetch_logs(ETCDLogsRequest(time_window_minutes=30))

            assert len(result) >= 1
            assert "etcd started" in result[0].message

    def test_fetch_logs_empty_on_error(self) -> None:
        with patch(_CFG), patch(_API, side_effect=Exception("no cluster")):
            from hexawyn.adapters.secondary.gitops.kubernetes_etcd_logs_adapter import (
                KubernetesETCDLogsAdapter,
            )
            from hexawyn.domain.models.etcd_logs import ETCDLogsRequest

            adapter = KubernetesETCDLogsAdapter()
            result = adapter.fetch_logs(ETCDLogsRequest(time_window_minutes=30))
            assert result == []

    def test_fetch_logs_no_etcd_pods(self) -> None:
        with patch(_CFG), patch(_API) as mock_api:
            mock_v1 = MagicMock()
            mock_v1.list_pod_for_all_namespaces.return_value = MagicMock(items=[])
            mock_api.return_value = mock_v1

            from hexawyn.adapters.secondary.gitops.kubernetes_etcd_logs_adapter import (
                KubernetesETCDLogsAdapter,
            )
            from hexawyn.domain.models.etcd_logs import ETCDLogsRequest

            adapter = KubernetesETCDLogsAdapter()
            result = adapter.fetch_logs(ETCDLogsRequest(time_window_minutes=30))
            assert result == []


class TestKubernetesEventAdapter:
    def test_fetch_k8s_events_with_warning(self) -> None:
        with patch(_CFG), patch(_API) as mock_api:
            mock_v1 = MagicMock()
            event = MagicMock()
            event.message = "Failed to pull image"
            event.reason = "Failed"
            event.type = "Warning"
            event.involved_object = MagicMock()
            event.involved_object.kind = "Pod"
            event.involved_object.name = "crash-pod"
            event.involved_object.namespace = "default"
            event.last_timestamp = None
            mock_v1.list_event_for_all_namespaces.return_value = MagicMock(items=[event])
            mock_api.return_value = mock_v1

            from hexawyn.adapters.secondary.gitops.kubernetes_event_adapter import (
                KubernetesEventAdapter,
            )
            from hexawyn.domain.models.trace_k8s_events import TraceEventCorrelationRequest

            adapter = KubernetesEventAdapter()
            result = adapter.fetch_k8s_events(TraceEventCorrelationRequest(trace_id="abc"))

            assert len(result) == 1
            assert result[0].reason == "Failed"

    def test_fetch_k8s_events_empty_on_error(self) -> None:
        with patch(_CFG), patch(_API, side_effect=Exception("no cluster")):
            from hexawyn.adapters.secondary.gitops.kubernetes_event_adapter import (
                KubernetesEventAdapter,
            )
            from hexawyn.domain.models.trace_k8s_events import TraceEventCorrelationRequest

            adapter = KubernetesEventAdapter()
            result = adapter.fetch_k8s_events(TraceEventCorrelationRequest(trace_id="abc"))
            assert result == []

    def test_fetch_slowest_span_warning_found(self) -> None:
        with patch(_CFG), patch(_API) as mock_api:
            mock_v1 = MagicMock()
            event = MagicMock()
            event.type = "Warning"
            event.reason = "OOMKilled"
            event.involved_object = MagicMock()
            event.involved_object.kind = "Pod"
            event.involved_object.name = "oom-pod"
            mock_v1.list_event_for_all_namespaces.return_value = MagicMock(items=[event])
            mock_api.return_value = mock_v1

            from hexawyn.adapters.secondary.gitops.kubernetes_event_adapter import (
                KubernetesEventAdapter,
            )
            from hexawyn.domain.models.trace_k8s_events import TraceEventCorrelationRequest

            adapter = KubernetesEventAdapter()
            result = adapter.fetch_slowest_span(TraceEventCorrelationRequest(trace_id="abc"))

            assert isinstance(result, str)
            assert "OOMKilled" in result

    def test_fetch_slowest_span_no_warnings(self) -> None:
        with patch(_CFG), patch(_API) as mock_api:
            mock_v1 = MagicMock()
            event = MagicMock()
            event.type = "Normal"
            event.reason = "Started"
            event.involved_object = None
            mock_v1.list_event_for_all_namespaces.return_value = MagicMock(items=[event])
            mock_api.return_value = mock_v1

            from hexawyn.adapters.secondary.gitops.kubernetes_event_adapter import (
                KubernetesEventAdapter,
            )
            from hexawyn.domain.models.trace_k8s_events import TraceEventCorrelationRequest

            adapter = KubernetesEventAdapter()
            result = adapter.fetch_slowest_span(TraceEventCorrelationRequest(trace_id="abc"))
            assert result is None

    def test_fetch_k8s_events_no_involved_object(self) -> None:
        with patch(_CFG), patch(_API) as mock_api:
            mock_v1 = MagicMock()
            event = MagicMock()
            event.type = "Normal"
            event.reason = "Scheduled"
            event.involved_object = None
            event.last_timestamp = None
            mock_v1.list_event_for_all_namespaces.return_value = MagicMock(items=[event])
            mock_api.return_value = mock_v1

            from hexawyn.adapters.secondary.gitops.kubernetes_event_adapter import (
                KubernetesEventAdapter,
            )
            from hexawyn.domain.models.trace_k8s_events import TraceEventCorrelationRequest

            adapter = KubernetesEventAdapter()
            result = adapter.fetch_k8s_events(TraceEventCorrelationRequest(trace_id="abc"))
            assert isinstance(result, list)


class TestKubernetesPipelineForServiceAdapter:
    def test_find_pipelines_with_tekton(self) -> None:
        with patch(_CFG), patch("kubernetes.client.CustomObjectsApi") as mock_api:
            mock_crd = MagicMock()
            mock_crd.list_namespaced_custom_object.return_value = {
                "items": [
                    {
                        "metadata": {
                            "name": "build-run-1",
                            "labels": {"app.kubernetes.io/name": "myapp"},
                        },  # noqa: E501
                        "spec": {"pipelineRef": {"name": "build-pipeline"}},
                        "status": {
                            "startTime": "2026-07-01",
                            "conditions": [{"type": "Succeeded", "status": "True"}],
                        },  # noqa: E501
                    }
                ]
            }
            mock_api.return_value = mock_crd

            from hexawyn.adapters.secondary.gitops.kubernetes_pipeline_for_service_adapter import (
                KubernetesPipelineForServiceAdapter,
            )
            from hexawyn.domain.models.pipeline_for_service import PipelineForServiceRequest

            adapter = KubernetesPipelineForServiceAdapter()
            result = adapter.find_pipelines(PipelineForServiceRequest(service_name="myapp"))

            assert len(result) >= 1
            assert result[0].namespace == "default"

    def test_find_pipelines_empty_on_error(self) -> None:
        with (
            patch(_CFG),
            patch("kubernetes.client.CustomObjectsApi", side_effect=Exception("no cluster")),
        ):  # noqa: E501
            from hexawyn.adapters.secondary.gitops.kubernetes_pipeline_for_service_adapter import (
                KubernetesPipelineForServiceAdapter,
            )
            from hexawyn.domain.models.pipeline_for_service import PipelineForServiceRequest

            adapter = KubernetesPipelineForServiceAdapter()
            result = adapter.find_pipelines(PipelineForServiceRequest(service_name="test"))
            assert result == []

    def test_find_pipelines_no_tekton_installed(self) -> None:
        with patch(_CFG), patch("kubernetes.client.CustomObjectsApi") as mock_api:
            mock_crd = MagicMock()
            mock_crd.list_namespaced_custom_object.side_effect = Exception("CRD not found")
            mock_api.return_value = mock_crd

            from hexawyn.adapters.secondary.gitops.kubernetes_pipeline_for_service_adapter import (
                KubernetesPipelineForServiceAdapter,
            )
            from hexawyn.domain.models.pipeline_for_service import PipelineForServiceRequest

            adapter = KubernetesPipelineForServiceAdapter()
            result = adapter.find_pipelines(PipelineForServiceRequest(service_name="test"))
            assert result == []


class TestKubernetesPipelineRunLogsAdapter:
    def test_fetch_step_logs_with_data(self) -> None:
        with patch(_CFG), patch(_API) as mock_api:
            mock_v1 = MagicMock()
            pod = MagicMock()
            pod.metadata = MagicMock()
            pod.metadata.name = "test-run-fetch-pod"
            container = MagicMock()
            container.name = "fetch-source"
            pod.spec = MagicMock()
            pod.spec.containers = [container]
            mock_v1.list_namespaced_pod.return_value = MagicMock(items=[pod])
            mock_v1.read_namespaced_pod_log.return_value = "Cloning repo...\nBuilding...\n"
            mock_api.return_value = mock_v1

            from hexawyn.adapters.secondary.gitops.kubernetes_pipeline_run_logs_adapter import (
                KubernetesPipelineRunLogsAdapter,
            )
            from hexawyn.domain.models.pipeline_run_logs import PipelineRunLogsRequest

            adapter = KubernetesPipelineRunLogsAdapter()
            result = adapter.fetch_step_logs(
                PipelineRunLogsRequest(pipeline_run_name="test-run", namespace="default")
            )

            assert len(result) >= 1
            assert result[0].step_name == "fetch-source"
            assert "Cloning repo" in result[0].log_lines[0]

    def test_fetch_step_logs_empty_on_error(self) -> None:
        with patch(_CFG), patch(_API, side_effect=Exception("no cluster")):
            from hexawyn.adapters.secondary.gitops.kubernetes_pipeline_run_logs_adapter import (
                KubernetesPipelineRunLogsAdapter,
            )
            from hexawyn.domain.models.pipeline_run_logs import PipelineRunLogsRequest

            adapter = KubernetesPipelineRunLogsAdapter()
            result = adapter.fetch_step_logs(
                PipelineRunLogsRequest(pipeline_run_name="test-run", namespace="default")
            )
            assert result == []

    def test_fetch_step_logs_no_pods(self) -> None:
        with patch(_CFG), patch(_API) as mock_api:
            mock_v1 = MagicMock()
            mock_v1.list_namespaced_pod.return_value = MagicMock(items=[])
            mock_api.return_value = mock_v1

            from hexawyn.adapters.secondary.gitops.kubernetes_pipeline_run_logs_adapter import (
                KubernetesPipelineRunLogsAdapter,
            )
            from hexawyn.domain.models.pipeline_run_logs import PipelineRunLogsRequest

            adapter = KubernetesPipelineRunLogsAdapter()
            result = adapter.fetch_step_logs(
                PipelineRunLogsRequest(pipeline_run_name="test-run", namespace="default")
            )
            assert result == []


class TestRecurringIncidentAdapter:
    def test_fetch_incidents_with_warnings(self) -> None:
        with patch(_CFG), patch(_API) as mock_api:
            mock_v1 = MagicMock()
            event1 = MagicMock()
            event1.type = "Warning"
            event1.reason = "OOMKilled"
            event1.metadata = MagicMock()
            event1.metadata.uid = "evt-001"
            event1.last_timestamp = None
            event1.involved_object = MagicMock()
            event1.involved_object.kind = "Pod"
            event1.involved_object.name = "oom-pod"
            event2 = MagicMock()
            event2.type = "Warning"
            event2.reason = "OOMKilled"
            event2.metadata = MagicMock()
            event2.metadata.uid = "evt-002"
            event2.last_timestamp = None
            event2.involved_object = MagicMock()
            event2.involved_object.kind = "Pod"
            event2.involved_object.name = "oom-pod"
            mock_v1.list_event_for_all_namespaces.return_value = MagicMock(items=[event1, event2])
            mock_api.return_value = mock_v1

            from hexawyn.adapters.secondary.gitops.recurring_incident_adapter import (
                RecurringIncidentAdapter,
            )

            adapter = RecurringIncidentAdapter()
            result = adapter.fetch_incidents(30)

            assert len(result) == 2  # noqa: PLR2004
            assert result[0]["root_cause"] == "OOMKilled"

    def test_fetch_incidents_empty_on_error(self) -> None:
        with patch(_CFG), patch(_API, side_effect=Exception("no cluster")):
            from hexawyn.adapters.secondary.gitops.recurring_incident_adapter import (
                RecurringIncidentAdapter,
            )

            adapter = RecurringIncidentAdapter()
            result = adapter.fetch_incidents(30)
            assert result == []

    def test_fetch_incidents_empty_no_warnings(self) -> None:
        with patch(_CFG), patch(_API) as mock_api:
            mock_v1 = MagicMock()
            mock_v1.list_event_for_all_namespaces.return_value = MagicMock(items=[])
            mock_api.return_value = mock_v1

            from hexawyn.adapters.secondary.gitops.recurring_incident_adapter import (
                RecurringIncidentAdapter,
            )

            adapter = RecurringIncidentAdapter()
            result = adapter.fetch_incidents(30)
            assert result == []


class TestMonthlyIncidentAdapter:
    def test_fetch_incidents_with_data(self) -> None:
        with patch(_CFG), patch(_API) as mock_api:
            mock_v1 = MagicMock()
            event = MagicMock()
            event.type = "Warning"
            event.reason = "CrashLoopBackOff"
            event.count = 5
            event.metadata = MagicMock()
            event.metadata.uid = "evt-001"
            event.first_timestamp = None
            event.last_timestamp = None
            event.involved_object = MagicMock()
            event.involved_object.kind = "Pod"
            event.involved_object.name = "crash-pod"
            mock_v1.list_event_for_all_namespaces.return_value = MagicMock(items=[event])
            mock_api.return_value = mock_v1

            from hexawyn.adapters.secondary.gitops.monthly_incident_adapter import (
                MonthlyIncidentAdapter,
            )

            adapter = MonthlyIncidentAdapter()
            result = adapter.fetch_incidents("2026-07")

            assert len(result) == 1
            assert result[0]["severity"] == "warning"

    def test_fetch_incidents_empty_on_error(self) -> None:
        with patch(_CFG), patch(_API, side_effect=Exception("no cluster")):
            from hexawyn.adapters.secondary.gitops.monthly_incident_adapter import (
                MonthlyIncidentAdapter,
            )

            adapter = MonthlyIncidentAdapter()
            result = adapter.fetch_incidents("2026-07")
            assert result == []

    def test_fetch_incidents_empty_no_warnings(self) -> None:
        with patch(_CFG), patch(_API) as mock_api:
            mock_v1 = MagicMock()
            mock_v1.list_event_for_all_namespaces.return_value = MagicMock(items=[])
            mock_api.return_value = mock_v1

            from hexawyn.adapters.secondary.gitops.monthly_incident_adapter import (
                MonthlyIncidentAdapter,
            )

            adapter = MonthlyIncidentAdapter()
            result = adapter.fetch_incidents("2026-07")
            assert result == []


class TestMTTRTrendAdapter:
    def test_fetch_incidents_with_data(self) -> None:
        with patch(_CFG), patch(_API) as mock_api:
            mock_v1 = MagicMock()
            event = MagicMock()
            event.type = "Warning"
            event.reason = "Failed"
            event.metadata = MagicMock()
            event.metadata.uid = "abc-123"
            event.first_timestamp = None
            event.last_timestamp = None
            event.involved_object = MagicMock()
            event.involved_object.kind = "Pod"
            event.involved_object.name = "failed-pod"
            mock_v1.list_event_for_all_namespaces.return_value = MagicMock(items=[event])
            mock_api.return_value = mock_v1

            from hexawyn.adapters.secondary.gitops.mttr_trend_adapter import MTTRTrendAdapter

            adapter = MTTRTrendAdapter()
            result = adapter.fetch_incidents_by_month("2026-07")

            assert len(result) == 1
            assert result[0]["root_cause"] == "Failed"

    def test_fetch_incidents_empty_on_error(self) -> None:
        with patch(_CFG), patch(_API, side_effect=Exception("no cluster")):
            from hexawyn.adapters.secondary.gitops.mttr_trend_adapter import MTTRTrendAdapter

            adapter = MTTRTrendAdapter()
            result = adapter.fetch_incidents_by_month("2026-07")
            assert result == []

    def test_fetch_incidents_empty_no_warnings(self) -> None:
        with patch(_CFG), patch(_API) as mock_api:
            mock_v1 = MagicMock()
            mock_v1.list_event_for_all_namespaces.return_value = MagicMock(items=[])
            mock_api.return_value = mock_v1

            from hexawyn.adapters.secondary.gitops.mttr_trend_adapter import MTTRTrendAdapter

            adapter = MTTRTrendAdapter()
            result = adapter.fetch_incidents_by_month("2026-07")
            assert result == []
