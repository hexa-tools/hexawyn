from unittest.mock import MagicMock, patch

import pytest

pytest.importorskip("google.cloud.container")
from google.api_core.exceptions import PermissionDenied  # noqa: E402
from google.auth.exceptions import DefaultCredentialsError  # noqa: E402
from hexawyn.application.ports.driven.k8s_port import ClusterContext, K8sPort  # noqa: E402
from hexawyn.domain.errors import ClusterUnreachableError  # noqa: E402


def _context(name: str, namespace: str = "default") -> ClusterContext:
    return {"name": name, "cluster": name, "provider": "gcp", "namespace": namespace}


_GKE_NAME = "gke_my-project_europe-west1_prod-cluster"


def _cluster_proto() -> MagicMock:
    cluster = MagicMock()
    cluster.name = "prod-cluster"
    cluster.status = "RUNNING"
    cluster.current_master_version = "1.29.1-gke.100"
    cluster.endpoint = "34.10.20.30"
    cluster.location = "europe-west1"
    return cluster


class TestK8sPortDelegation:
    def test_is_a_k8s_port(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        adapter = GCPGKEAdapter(_context(_GKE_NAME), k8s_delegate=MagicMock(spec=K8sPort))

        assert isinstance(adapter, K8sPort)

    def test_list_pods_delegates(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        delegate = MagicMock(spec=K8sPort)
        delegate.list_pods.return_value = [{"name": "p1", "namespace": "ns"}]
        adapter = GCPGKEAdapter(_context(_GKE_NAME), k8s_delegate=delegate)

        result = adapter.list_pods("ns")

        delegate.list_pods.assert_called_once_with("ns")
        assert result[0]["name"] == "p1"

    def test_list_namespaces_delegates(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        delegate = MagicMock(spec=K8sPort)
        delegate.list_namespaces.return_value = [{"name": "ns", "status": "Active", "age": "1d"}]
        adapter = GCPGKEAdapter(_context(_GKE_NAME), k8s_delegate=delegate)

        assert adapter.list_namespaces()[0]["name"] == "ns"

    def test_get_cluster_metrics_delegates(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        delegate = MagicMock(spec=K8sPort)
        delegate.get_cluster_metrics.return_value = {
            "cpu_usage_pct": 1.0,
            "memory_usage_pct": 2.0,
            "node_count": 3,
            "pod_count": 4,
        }
        adapter = GCPGKEAdapter(_context(_GKE_NAME), k8s_delegate=delegate)

        assert adapter.get_cluster_metrics()["node_count"] == 3

    def test_defaults_to_vanilla_delegate(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        vanilla = MagicMock(spec=K8sPort)
        vanilla.list_pods.return_value = []
        adapter = GCPGKEAdapter(_context(_GKE_NAME))

        with patch(
            "hexawyn.adapters.secondary.vanilla.vanilla_adapter.VanillaAdapter",
            return_value=vanilla,
        ) as vanilla_cls:
            result = adapter.list_pods()

        vanilla_cls.assert_called_once_with(_GKE_NAME)
        assert result == []


class TestClusterContext:
    def test_reports_gcp_provider_and_project(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        adapter = GCPGKEAdapter(_context(_GKE_NAME, namespace="team"), k8s_delegate=MagicMock())

        ctx = adapter.get_cluster_context()

        assert ctx["provider"] == "gcp"
        assert ctx["cluster"] == "prod-cluster"
        assert ctx["namespace"] == "team"

    def test_project_id_from_context_name(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        adapter = GCPGKEAdapter(_context(_GKE_NAME), k8s_delegate=MagicMock())

        assert adapter.project_id == "my-project"

    def test_project_id_none_when_unparseable(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        adapter = GCPGKEAdapter(_context("some-cluster"), k8s_delegate=MagicMock())

        assert adapter.project_id is None

    def test_explicit_project_id_wins(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        adapter = GCPGKEAdapter(
            _context("some-cluster"), k8s_delegate=MagicMock(), project_id="explicit-proj"
        )

        assert adapter.project_id == "explicit-proj"

    def test_cluster_context_falls_back_when_unparseable(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        adapter = GCPGKEAdapter(_context("plain-cluster"), k8s_delegate=MagicMock())

        ctx = adapter.get_cluster_context()

        assert ctx["provider"] == "gcp"
        assert ctx["cluster"] == "plain-cluster"


class TestDescribeClusterStatus:
    def test_returns_typed_status(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        client = MagicMock()
        client.get_cluster.return_value = _cluster_proto()
        adapter = GCPGKEAdapter(_context(_GKE_NAME), k8s_delegate=MagicMock(), gke_client=client)

        status = adapter.describe_cluster_status()

        expected_name = "projects/my-project/locations/europe-west1/clusters/prod-cluster"
        client.get_cluster.assert_called_once_with(name=expected_name)
        assert status["status"] == "RUNNING"
        assert status["version"] == "1.29.1-gke.100"
        assert status["location"] == "europe-west1"

    def test_unparseable_context_raises(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        adapter = GCPGKEAdapter(
            _context("some-cluster"), k8s_delegate=MagicMock(), gke_client=MagicMock()
        )

        with pytest.raises(ClusterUnreachableError):
            adapter.describe_cluster_status()

    def test_missing_credentials_raises_with_hint(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        client = MagicMock()
        client.get_cluster.side_effect = DefaultCredentialsError("no creds")
        adapter = GCPGKEAdapter(_context(_GKE_NAME), k8s_delegate=MagicMock(), gke_client=client)

        with pytest.raises(ClusterUnreachableError) as exc_info:
            adapter.describe_cluster_status()

        assert "gcloud auth" in str(exc_info.value).lower()

    def test_api_error_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        client = MagicMock()
        client.get_cluster.side_effect = PermissionDenied("denied")
        adapter = GCPGKEAdapter(_context(_GKE_NAME), k8s_delegate=MagicMock(), gke_client=client)

        with pytest.raises(ClusterUnreachableError):
            adapter.describe_cluster_status()

    def test_lazily_creates_client_when_not_injected(self) -> None:
        from hexawyn.adapters.secondary.gcp import gke_adapter as module
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        created = MagicMock()
        created.get_cluster.return_value = _cluster_proto()
        adapter = GCPGKEAdapter(_context(_GKE_NAME), k8s_delegate=MagicMock())

        with patch(
            "google.cloud.container_v1.ClusterManagerClient", return_value=created
        ) as client_cls:
            adapter.describe_cluster_status()

        client_cls.assert_called_once_with()
        assert module is not None
