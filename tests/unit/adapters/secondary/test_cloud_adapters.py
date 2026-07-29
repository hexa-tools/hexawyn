"""Tests for AWS EKS, GCP GKE, and Azure AKS adapters."""

from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driven.k8s_port import K8sPort


def _ctx(name: str = "test-cluster") -> dict[str, str]:
    return {
        "name": name,
        "cluster": name,
        "provider": "vanilla",
        "namespace": "default",
    }


class TestAWSEKSAdapter:
    """Cover AWSEKSAdapter."""

    def test_instantiation_and_ports(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        mock_k8s = MagicMock(spec=K8sPort)
        mock_client = MagicMock()
        mock_client.describe_cluster.return_value = {
            "cluster": {
                "name": "prod-eu",
                "status": "ACTIVE",
                "version": "1.29",
                "endpoint": "https://eks.example.com",
            }
        }

        adapter = AWSEKSAdapter(
            context=_ctx("arn:aws:eks:eu-west-1:123:cluster/prod-eu"),
            eks_client=mock_client,
            k8s_delegate=mock_k8s,
        )
        assert isinstance(adapter, K8sPort)

    def test_get_cluster_context(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        mock_k8s = MagicMock(spec=K8sPort)
        mock_k8s.get_cluster_context.return_value = {
            "name": "eks",
            "cluster": "eks",
            "provider": "aws",
            "namespace": "default",
        }
        mock_client = MagicMock()
        mock_client.describe_cluster.return_value = {
            "cluster": {
                "name": "prod-eu",
                "status": "ACTIVE",
                "version": "1.29",
                "endpoint": "https://eks.example.com",
            }
        }

        adapter = AWSEKSAdapter(
            context=_ctx("prod-eu"),
            eks_client=mock_client,
            k8s_delegate=mock_k8s,
        )
        result = adapter.get_cluster_context()
        assert result["provider"] == "aws"

    def test_get_cluster_context_fallback_on_error(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        mock_k8s = MagicMock(spec=K8sPort)
        mock_k8s.get_cluster_context.return_value = {
            "name": "eks",
            "cluster": "eks",
            "provider": "vanilla",
            "namespace": "ns",
        }
        mock_client = MagicMock()
        mock_client.describe_cluster.side_effect = Exception("no access")

        adapter = AWSEKSAdapter(
            context=_ctx("prod-eu"),
            eks_client=mock_client,
            k8s_delegate=mock_k8s,
        )
        result = adapter.get_cluster_context()
        assert result["provider"] == "aws"

    def test_list_pods_delegates(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        mock_k8s = MagicMock(spec=K8sPort)
        mock_k8s.list_pods.return_value = [MagicMock()]
        adapter = AWSEKSAdapter(context=_ctx(), k8s_delegate=mock_k8s, eks_client=MagicMock())
        result = adapter.list_pods()
        assert len(result) == 1  # noqa: PLR2004

    def test_list_namespaces_delegates(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        mock_k8s = MagicMock(spec=K8sPort)
        mock_k8s.list_namespaces.return_value = [MagicMock()]
        adapter = AWSEKSAdapter(context=_ctx(), k8s_delegate=mock_k8s, eks_client=MagicMock())
        result = adapter.list_namespaces()
        assert len(result) > 0

    def test_get_cluster_metrics_delegates(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        mock_k8s = MagicMock(spec=K8sPort)
        mock_k8s.get_cluster_metrics.return_value = {"cpu_usage_percent": 45.0}
        adapter = AWSEKSAdapter(context=_ctx(), k8s_delegate=mock_k8s, eks_client=MagicMock())
        result = adapter.get_cluster_metrics()
        assert result["cpu_usage_percent"] == 45.0  # noqa: PLR2004

    def test_region_property(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        mock_k8s = MagicMock(spec=K8sPort)
        adapter = AWSEKSAdapter(
            context=_ctx("arn:aws:eks:eu-west-1:123:cluster/prod"),
            region="us-east-1",
            k8s_delegate=mock_k8s,
            eks_client=MagicMock(),
        )
        assert adapter.region == "us-east-1"


class TestGCPGKEAdapter:
    """Cover GCPGKEAdapter."""

    def test_instantiation(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        mock_k8s = MagicMock(spec=K8sPort)
        adapter = GCPGKEAdapter(
            context=_ctx("gke_my-project_us-central1-a_cluster1"),
            k8s_delegate=mock_k8s,
        )
        assert isinstance(adapter, K8sPort)

    def test_project_id_parsed_from_context(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        mock_k8s = MagicMock(spec=K8sPort)
        adapter = GCPGKEAdapter(
            context=_ctx("gke_my-project_us-central1-a_cluster1"),
            k8s_delegate=mock_k8s,
        )
        pid = adapter.project_id
        assert isinstance(pid, str)

    def test_get_cluster_context(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        mock_k8s = MagicMock(spec=K8sPort)
        mock_k8s.get_cluster_context.return_value = {
            "name": "gke",
            "cluster": "gke",
            "provider": "gcp",
            "namespace": "ns",
        }

        adapter = GCPGKEAdapter(context=_ctx("gke_proj_zone_cluster"), k8s_delegate=mock_k8s)
        result = adapter.get_cluster_context()
        assert result["provider"] == "gcp"

    def test_list_pods_delegates(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        mock_k8s = MagicMock(spec=K8sPort)
        mock_k8s.list_pods.return_value = [MagicMock()]
        adapter = GCPGKEAdapter(context=_ctx("gke_p_z_c"), k8s_delegate=mock_k8s)
        result = adapter.list_pods()
        assert len(result) == 1  # noqa: PLR2004

    def test_get_cluster_metrics_delegates(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        mock_k8s = MagicMock(spec=K8sPort)
        mock_k8s.get_cluster_metrics.return_value = {"cpu_usage_percent": 70.0}
        adapter = GCPGKEAdapter(context=_ctx("gke_p_z_c"), k8s_delegate=mock_k8s)
        result = adapter.get_cluster_metrics()
        assert result["cpu_usage_percent"] == 70.0  # noqa: PLR2004


class TestAzureAKSAdapter:
    """Cover AzureAKSAdapter."""

    def test_instantiation(self) -> None:
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter

        mock_k8s = MagicMock(spec=K8sPort)
        adapter = AzureAKSAdapter(context=_ctx("aks-prod"), k8s_delegate=mock_k8s)
        assert isinstance(adapter, K8sPort)

    def test_get_cluster_context(self) -> None:
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter

        mock_k8s = MagicMock(spec=K8sPort)
        mock_k8s.get_cluster_context.return_value = {
            "name": "aks",
            "cluster": "aks",
            "provider": "azure",
            "namespace": "ns",
        }
        adapter = AzureAKSAdapter(context=_ctx("aks-prod"), k8s_delegate=mock_k8s)
        result = adapter.get_cluster_context()
        assert result["provider"] == "azure"

    def test_list_pods_delegates(self) -> None:
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter

        mock_k8s = MagicMock(spec=K8sPort)
        mock_k8s.list_pods.return_value = [MagicMock()]
        adapter = AzureAKSAdapter(context=_ctx("aks"), k8s_delegate=mock_k8s)
        result = adapter.list_pods()
        assert len(result) == 1  # noqa: PLR2004

    def test_list_namespaces_delegates(self) -> None:
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter

        mock_k8s = MagicMock(spec=K8sPort)
        mock_k8s.list_namespaces.return_value = [MagicMock()]
        adapter = AzureAKSAdapter(context=_ctx("aks"), k8s_delegate=mock_k8s)
        result = adapter.list_namespaces()
        assert len(result) > 0

    def test_get_cluster_metrics_delegates(self) -> None:
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter

        mock_k8s = MagicMock(spec=K8sPort)
        mock_k8s.get_cluster_metrics.return_value = {"cpu_usage_percent": 30.0}
        adapter = AzureAKSAdapter(context=_ctx("aks"), k8s_delegate=mock_k8s)
        result = adapter.get_cluster_metrics()
        assert result["cpu_usage_percent"] == 30.0  # noqa: PLR2004

    def test_subscription_id_from_env(self) -> None:
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter

        mock_k8s = MagicMock(spec=K8sPort)
        adapter = AzureAKSAdapter(
            context=_ctx("aks"), k8s_delegate=mock_k8s, subscription_id="sub-123"
        )
        assert adapter.subscription_id == "sub-123"
