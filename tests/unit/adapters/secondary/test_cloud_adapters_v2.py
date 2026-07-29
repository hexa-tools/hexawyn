"""Comprehensive tests for cloud adapters — target 95%+ coverage each."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest


def _ctx(name: str = "test-cluster") -> dict[str, str]:
    return {"name": name, "cluster": name, "provider": "vanilla", "namespace": "default"}


class TestEKSAdapter:
    """Cover all remaining AWSEKSAdapter branches."""

    def test_region_lazy_resolution(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        adapter = AWSEKSAdapter(context=_ctx("arn:aws:eks:eu-west-1:123:cluster/prod"))
        with patch(
            "hexawyn.adapters.secondary.aws.eks_adapter.resolve_region",
            return_value="eu-west-1",
        ):
            assert adapter.region == "eu-west-1"

    def test_describe_cluster_status(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

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
            region="eu-west-1",
        )
        result = adapter.describe_cluster_status()
        assert result["name"] == "prod-eu"
        assert result["status"] == "ACTIVE"
        assert result["region"] == "eu-west-1"

    def test_describe_cluster_status_no_credentials(self) -> None:
        from botocore.exceptions import NoCredentialsError
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.domain.errors import ClusterUnreachableError

        mock_client = MagicMock()
        mock_client.describe_cluster.side_effect = NoCredentialsError()

        adapter = AWSEKSAdapter(context=_ctx("prod-eu"), eks_client=mock_client, region="us-east-1")
        with pytest.raises(ClusterUnreachableError, match="credentials"):
            adapter.describe_cluster_status()

    def test_describe_cluster_status_client_error(self) -> None:
        from botocore.exceptions import ClientError
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.domain.errors import ClusterUnreachableError

        mock_client = MagicMock()
        mock_client.describe_cluster.side_effect = ClientError(
            {"Error": {"Code": "ResourceNotFoundException"}}, "describe_cluster"
        )

        adapter = AWSEKSAdapter(context=_ctx("prod-eu"), eks_client=mock_client, region="us-east-1")
        with pytest.raises(ClusterUnreachableError):
            adapter.describe_cluster_status()

    def test_delegate_lazy_creation(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        adapter = AWSEKSAdapter(context=_ctx("prod-eu"))
        assert adapter._k8s_delegate is None
        with patch("hexawyn.adapters.secondary.vanilla.vanilla_adapter.VanillaAdapter") as mock_va:
            mock_va.return_value = MagicMock()
            adapter._delegate()
            mock_va.assert_called_once_with("prod-eu")

    def test_eks_client_or_create_lazy(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        adapter = AWSEKSAdapter(context=_ctx("prod-eu"), region="us-east-1")
        assert adapter._eks_client is None
        with patch("boto3.client") as mock_boto3:
            adapter._eks_client_or_create()
            mock_boto3.assert_called_once_with("eks", region_name="us-east-1")

    def test_cluster_short_name_without_arn(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        adapter = AWSEKSAdapter(context=_ctx("simple-name"))
        assert adapter._cluster_short_name() == "simple-name"

    def test_get_cluster_context(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        mock_k8s = MagicMock()
        adapter = AWSEKSAdapter(
            context=_ctx("arn:aws:eks:eu-west-1:123:cluster/prod-eu"),
            k8s_delegate=mock_k8s,
            eks_client=MagicMock(),
        )
        ctx = adapter.get_cluster_context()
        assert ctx["provider"] == "aws"
        assert ctx["cluster"] == "prod-eu"


class TestGKEAdapter:
    """Cover all remaining GCPGKEAdapter branches."""

    def test_project_id_from_parsed(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        adapter = GCPGKEAdapter(context=_ctx("gke_myproj_us-central1-a_mycluster"))
        assert adapter.project_id == "myproj"

    def test_project_id_manual_override(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        adapter = GCPGKEAdapter(context=_ctx("gke_x_y_z"), project_id="override-id")
        assert adapter.project_id == "override-id"

    def test_describe_cluster_status(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        mock_client = MagicMock()
        mock_cluster = MagicMock()
        mock_cluster.name = "mycluster"
        mock_cluster.status = "RUNNING"
        mock_cluster.current_master_version = "1.29"
        mock_cluster.endpoint = "https://gke.example.com"
        mock_cluster.location = "us-central1-a"
        mock_client.get_cluster.return_value = mock_cluster

        adapter = GCPGKEAdapter(
            context=_ctx("gke_myproj_us-central1-a_mycluster"),
            gke_client=mock_client,
        )
        result = adapter.describe_cluster_status()
        assert result["name"] == "mycluster"
        assert result["status"] == "RUNNING"
        assert result["location"] == "us-central1-a"

    def test_describe_cluster_status_no_parsed_context(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.domain.errors import ClusterUnreachableError

        adapter = GCPGKEAdapter(context=_ctx("not-a-gke-context"))
        with pytest.raises(ClusterUnreachableError, match="Cannot determine GKE cluster"):
            adapter.describe_cluster_status()

    def test_describe_cluster_status_credentials_error(self) -> None:
        from google.auth.exceptions import DefaultCredentialsError
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.domain.errors import ClusterUnreachableError

        mock_client = MagicMock()
        mock_client.get_cluster.side_effect = DefaultCredentialsError()

        adapter = GCPGKEAdapter(
            context=_ctx("gke_myproj_us-central1-a_mycluster"),
            gke_client=mock_client,
        )
        with pytest.raises(ClusterUnreachableError, match="credentials"):
            adapter.describe_cluster_status()

    def test_describe_cluster_status_api_error(self) -> None:
        from google.api_core.exceptions import GoogleAPICallError
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.domain.errors import ClusterUnreachableError

        mock_client = MagicMock()
        mock_client.get_cluster.side_effect = GoogleAPICallError("api error")

        adapter = GCPGKEAdapter(
            context=_ctx("gke_myproj_us-central1-a_mycluster"),
            gke_client=mock_client,
        )
        with pytest.raises(ClusterUnreachableError):
            adapter.describe_cluster_status()

    def test_list_namespaces_delegates(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        mock_k8s = MagicMock()
        mock_k8s.list_namespaces.return_value = [MagicMock()]
        adapter = GCPGKEAdapter(context=_ctx("gke_p_z_c"), k8s_delegate=mock_k8s)
        result = adapter.list_namespaces()
        assert len(result) == 1

    def test_gke_delegate_lazy_creation(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        adapter = GCPGKEAdapter(context=_ctx("gke_p_z_c"))
        assert adapter._k8s_delegate is None
        with patch("hexawyn.adapters.secondary.vanilla.vanilla_adapter.VanillaAdapter") as mock_va:
            mock_va.return_value = MagicMock()
            adapter._delegate()
            mock_va.assert_called_once_with("gke_p_z_c")

    def test_client_or_create_lazy(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        adapter = GCPGKEAdapter(context=_ctx("gke_p_z_c"))
        assert adapter._gke_client is None
        with patch("google.cloud.container_v1.ClusterManagerClient") as mock_cm:
            adapter._client_or_create()
            mock_cm.assert_called_once()

    def test_cluster_short_name_with_parsed(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        adapter = GCPGKEAdapter(context=_ctx("gke_myproj_us-central1-a_mycluster"))
        assert adapter._cluster_short_name() == "mycluster"

    def test_cluster_short_name_without_parsed(self) -> None:
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        adapter = GCPGKEAdapter(context=_ctx("simple-name"))
        assert adapter._cluster_short_name() == "simple-name"


class TestAKSAdapter:
    """Cover all remaining AzureAKSAdapter branches."""

    def test_subscription_id_from_env(self) -> None:
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter

        with patch.dict("os.environ", {"AZURE_SUBSCRIPTION_ID": "env-sub-id"}, clear=True):
            adapter = AzureAKSAdapter(context=_ctx("aks-prod"))
            assert adapter.subscription_id == "env-sub-id"

    def test_resource_group_from_env(self) -> None:
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter

        with patch.dict("os.environ", {"AZURE_RESOURCE_GROUP": "env-rg"}, clear=True):
            adapter = AzureAKSAdapter(context=_ctx("aks-prod"))
            assert adapter.resource_group == "env-rg"

    def test_describe_cluster_status_missing_config(self) -> None:
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter
        from hexawyn.domain.errors import ClusterUnreachableError

        with patch.dict("os.environ", {}, clear=True):
            adapter = AzureAKSAdapter(context=_ctx("aks-prod"))
            with pytest.raises(ClusterUnreachableError, match="Missing Azure"):
                adapter.describe_cluster_status()

    def test_describe_cluster_status(self) -> None:
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter

        mock_cluster = MagicMock()
        mock_cluster.name = "aks-prod"
        mock_cluster.provisioning_state = "Succeeded"
        mock_cluster.kubernetes_version = "1.29"
        mock_cluster.fqdn = "aks-prod.hcp.westeurope.azmk8s.io"
        mock_cluster.location = "westeurope"

        mock_client = MagicMock()
        mock_client.managed_clusters.get.return_value = mock_cluster

        adapter = AzureAKSAdapter(
            context=_ctx("aks-prod"),
            aks_client=mock_client,
            subscription_id="sub-123",
            resource_group="rg-1",
        )
        result = adapter.describe_cluster_status()
        assert result["name"] == "aks-prod"
        assert result["status"] == "Succeeded"
        assert result["location"] == "westeurope"

    def test_describe_cluster_status_auth_error(self) -> None:
        from azure.core.exceptions import ClientAuthenticationError
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter
        from hexawyn.domain.errors import ClusterUnreachableError

        mock_client = MagicMock()
        mock_client.managed_clusters.get.side_effect = ClientAuthenticationError()

        adapter = AzureAKSAdapter(
            context=_ctx("aks-prod"),
            aks_client=mock_client,
            subscription_id="sub-123",
            resource_group="rg-1",
        )
        with pytest.raises(ClusterUnreachableError, match="credentials"):
            adapter.describe_cluster_status()

    def test_describe_cluster_status_http_error(self) -> None:
        from azure.core.exceptions import HttpResponseError
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter
        from hexawyn.domain.errors import ClusterUnreachableError

        mock_client = MagicMock()
        mock_client.managed_clusters.get.side_effect = HttpResponseError(
            message="not found", response=MagicMock()
        )

        adapter = AzureAKSAdapter(
            context=_ctx("aks-prod"),
            aks_client=mock_client,
            subscription_id="sub-123",
            resource_group="rg-1",
        )
        with pytest.raises(ClusterUnreachableError):
            adapter.describe_cluster_status()

    def test_delegate_lazy_creation(self) -> None:
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter

        adapter = AzureAKSAdapter(context=_ctx("aks-prod"))
        assert adapter._k8s_delegate is None
        with patch("hexawyn.adapters.secondary.vanilla.vanilla_adapter.VanillaAdapter") as mock_va:
            mock_va.return_value = MagicMock()
            adapter._delegate()
            mock_va.assert_called_once_with("aks-prod")

    def test_client_or_create_lazy(self) -> None:
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter

        adapter = AzureAKSAdapter(context=_ctx("aks-prod"))
        assert adapter._aks_client is None
        with patch(
            "azure.identity.DefaultAzureCredential",
            return_value=MagicMock(),
        ):
            with patch(
                "azure.mgmt.containerservice.ContainerServiceClient",
                return_value=MagicMock(),
            ):
                client = adapter._client_or_create("sub-id")
                assert client is not None

    def test_cluster_short_name(self) -> None:
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter

        adapter = AzureAKSAdapter(context=_ctx("aks-prod"))
        assert adapter._cluster_short_name() == "aks-prod"

    def test_get_cluster_context(self) -> None:
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter

        mock_k8s = MagicMock()
        adapter = AzureAKSAdapter(
            context=_ctx("aks-prod"),
            k8s_delegate=mock_k8s,
        )
        ctx = adapter.get_cluster_context()
        assert ctx["provider"] == "azure"
