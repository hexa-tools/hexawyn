import os
from unittest.mock import MagicMock, patch

import pytest

pytest.importorskip("azure.identity")
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError  # noqa: E402
from hexawyn.application.ports.driven.k8s_port import ClusterContext, K8sPort  # noqa: E402
from hexawyn.domain.errors import ClusterUnreachableError  # noqa: E402

_SUB = "sub-123"
_RG = "my-rg"


def _context(name: str = "aks-prod", namespace: str = "default") -> ClusterContext:
    return {"name": name, "cluster": name, "provider": "azure", "namespace": namespace}


def _managed_cluster() -> MagicMock:
    cluster = MagicMock()
    cluster.name = "aks-prod"
    cluster.provisioning_state = "Succeeded"
    cluster.kubernetes_version = "1.29.2"
    cluster.fqdn = "aks-prod-abc.hcp.westeurope.azmk8s.io"
    cluster.location = "westeurope"
    return cluster


def _adapter(**kwargs) -> object:
    from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter

    defaults = {
        "context": _context(),
        "k8s_delegate": MagicMock(spec=K8sPort),
        "subscription_id": _SUB,
        "resource_group": _RG,
    }
    defaults.update(kwargs)
    return AzureAKSAdapter(**defaults)


class TestK8sPortDelegation:
    def test_is_a_k8s_port(self) -> None:
        assert isinstance(_adapter(), K8sPort)

    def test_list_pods_delegates(self) -> None:
        delegate = MagicMock(spec=K8sPort)
        delegate.list_pods.return_value = [{"name": "p1", "namespace": "ns"}]
        adapter = _adapter(k8s_delegate=delegate)

        result = adapter.list_pods("ns")  # type: ignore[attr-defined]

        delegate.list_pods.assert_called_once_with("ns")
        assert result[0]["name"] == "p1"

    def test_list_namespaces_delegates(self) -> None:
        delegate = MagicMock(spec=K8sPort)
        delegate.list_namespaces.return_value = [{"name": "ns", "status": "Active", "age": "1d"}]
        adapter = _adapter(k8s_delegate=delegate)

        assert adapter.list_namespaces()[0]["name"] == "ns"  # type: ignore[attr-defined]

    def test_get_cluster_metrics_delegates(self) -> None:
        delegate = MagicMock(spec=K8sPort)
        delegate.get_cluster_metrics.return_value = {
            "cpu_usage_pct": 1.0,
            "memory_usage_pct": 2.0,
            "node_count": 3,
            "pod_count": 4,
        }
        adapter = _adapter(k8s_delegate=delegate)

        assert adapter.get_cluster_metrics()["node_count"] == 3  # type: ignore[attr-defined]

    def test_defaults_to_vanilla_delegate(self) -> None:
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter

        vanilla = MagicMock(spec=K8sPort)
        vanilla.list_pods.return_value = []
        adapter = AzureAKSAdapter(_context("aks-prod"), subscription_id=_SUB, resource_group=_RG)

        with patch(
            "hexawyn.adapters.secondary.vanilla.vanilla_adapter.VanillaAdapter",
            return_value=vanilla,
        ) as vanilla_cls:
            result = adapter.list_pods()

        vanilla_cls.assert_called_once_with("aks-prod")
        assert result == []


class TestClusterContext:
    def test_reports_azure_provider(self) -> None:
        adapter = _adapter(context=_context("aks-prod", namespace="team"))

        ctx = adapter.get_cluster_context()  # type: ignore[attr-defined]

        assert ctx["provider"] == "azure"
        assert ctx["cluster"] == "aks-prod"
        assert ctx["namespace"] == "team"


class TestSubscriptionResolution:
    def test_subscription_from_env(self) -> None:
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter

        adapter = AzureAKSAdapter(_context(), k8s_delegate=MagicMock(spec=K8sPort))

        with patch.dict(os.environ, {"AZURE_SUBSCRIPTION_ID": "env-sub"}):
            assert adapter.subscription_id == "env-sub"

    def test_explicit_subscription_wins(self) -> None:
        adapter = _adapter(subscription_id="explicit")

        assert adapter.subscription_id == "explicit"  # type: ignore[attr-defined]


class TestDescribeClusterStatus:
    def test_returns_typed_status(self) -> None:
        client = MagicMock()
        client.managed_clusters.get.return_value = _managed_cluster()
        adapter = _adapter(aks_client=client)

        status = adapter.describe_cluster_status()  # type: ignore[attr-defined]

        client.managed_clusters.get.assert_called_once_with(
            resource_group_name=_RG, resource_name="aks-prod"
        )
        assert status["status"] == "Succeeded"
        assert status["version"] == "1.29.2"
        assert status["location"] == "westeurope"

    def test_missing_config_raises(self) -> None:
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter

        adapter = AzureAKSAdapter(
            _context(), k8s_delegate=MagicMock(spec=K8sPort), aks_client=MagicMock()
        )

        with patch.dict(os.environ, {"AZURE_SUBSCRIPTION_ID": "", "AZURE_RESOURCE_GROUP": ""}):
            with pytest.raises(ClusterUnreachableError):
                adapter.describe_cluster_status()

    def test_auth_error_raises_with_hint(self) -> None:
        client = MagicMock()
        client.managed_clusters.get.side_effect = ClientAuthenticationError("no creds")
        adapter = _adapter(aks_client=client)

        with pytest.raises(ClusterUnreachableError) as exc_info:
            adapter.describe_cluster_status()  # type: ignore[attr-defined]

        assert "az login" in str(exc_info.value).lower()

    def test_http_error_raises_cluster_unreachable(self) -> None:
        client = MagicMock()
        client.managed_clusters.get.side_effect = HttpResponseError("boom")
        adapter = _adapter(aks_client=client)

        with pytest.raises(ClusterUnreachableError):
            adapter.describe_cluster_status()  # type: ignore[attr-defined]

    def test_lazily_creates_client(self) -> None:
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter

        created = MagicMock()
        created.managed_clusters.get.return_value = _managed_cluster()
        adapter = AzureAKSAdapter(
            _context(),
            k8s_delegate=MagicMock(spec=K8sPort),
            subscription_id=_SUB,
            resource_group=_RG,
        )

        with (
            patch("azure.identity.DefaultAzureCredential", return_value=MagicMock()),
            patch(
                "azure.mgmt.containerservice.ContainerServiceClient", return_value=created
            ) as client_cls,
        ):
            adapter.describe_cluster_status()

        client_cls.assert_called_once()
