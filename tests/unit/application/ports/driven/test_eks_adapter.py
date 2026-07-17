from unittest.mock import MagicMock, patch

import pytest

boto3 = pytest.importorskip("boto3")
from botocore.exceptions import (  # noqa: E402
    ClientError,
    EndpointConnectionError,
    NoCredentialsError,
)
from hexawyn.application.ports.driven.k8s_port import (  # noqa: E402
    ClusterContext,
    K8sPort,
)
from hexawyn.domain.errors import ClusterUnreachableError  # noqa: E402

_NO_REGION_ENV = {"AWS_REGION": "", "AWS_DEFAULT_REGION": ""}


def _context(name: str, namespace: str = "default") -> ClusterContext:
    return {
        "name": name,
        "cluster": name,
        "provider": "aws",
        "namespace": namespace,
    }


def _describe_response() -> dict:
    return {
        "cluster": {
            "name": "prod",
            "status": "ACTIVE",
            "version": "1.29",
            "endpoint": "https://ABC.gr7.eu-west-1.eks.amazonaws.com",
        }
    }


class TestRegionDetection:
    def test_region_detected_from_arn(self) -> None:
        import os

        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        ctx = _context("arn:aws:eks:eu-west-1:123456789012:cluster/prod")
        adapter = AWSEKSAdapter(ctx, k8s_delegate=MagicMock(spec=K8sPort))

        with patch.dict(os.environ, _NO_REGION_ENV):
            assert adapter.region == "eu-west-1"

    def test_region_detected_from_name_pattern(self) -> None:
        import os

        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        ctx = _context("prod.us-east-2.eksctl.io")
        adapter = AWSEKSAdapter(ctx, k8s_delegate=MagicMock(spec=K8sPort))

        with patch.dict(os.environ, _NO_REGION_ENV):
            assert adapter.region == "us-east-2"

    def test_region_is_none_when_undetectable(self) -> None:
        import os

        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        ctx = _context("my-eks-cluster")
        adapter = AWSEKSAdapter(ctx, k8s_delegate=MagicMock(spec=K8sPort))

        with patch.dict(os.environ, _NO_REGION_ENV):
            assert adapter.region is None

    def test_aws_region_env_overrides_arn(self) -> None:
        import os

        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        ctx = _context("arn:aws:eks:eu-west-1:123456789012:cluster/prod")
        adapter = AWSEKSAdapter(ctx, k8s_delegate=MagicMock(spec=K8sPort))

        with patch.dict(os.environ, {"AWS_REGION": "ap-south-1"}):
            assert adapter.region == "ap-south-1"

    def test_explicit_region_overrides_detection(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        ctx = _context("arn:aws:eks:eu-west-1:123456789012:cluster/prod")
        adapter = AWSEKSAdapter(ctx, k8s_delegate=MagicMock(spec=K8sPort), region="ap-south-1")

        assert adapter.region == "ap-south-1"


class TestK8sPortDelegation:
    def test_is_a_k8s_port(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        adapter = AWSEKSAdapter(_context("eks-prod"), k8s_delegate=MagicMock(spec=K8sPort))

        assert isinstance(adapter, K8sPort)

    def test_list_pods_delegates(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        delegate = MagicMock(spec=K8sPort)
        delegate.list_pods.return_value = [{"name": "p1", "namespace": "ns"}]
        adapter = AWSEKSAdapter(_context("eks-prod"), k8s_delegate=delegate)

        result = adapter.list_pods("ns")

        delegate.list_pods.assert_called_once_with("ns")
        assert result == [{"name": "p1", "namespace": "ns"}]

    def test_list_namespaces_delegates(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        delegate = MagicMock(spec=K8sPort)
        delegate.list_namespaces.return_value = [{"name": "ns", "status": "Active", "age": "1d"}]
        adapter = AWSEKSAdapter(_context("eks-prod"), k8s_delegate=delegate)

        result = adapter.list_namespaces()

        delegate.list_namespaces.assert_called_once_with()
        assert result[0]["name"] == "ns"

    def test_get_cluster_metrics_delegates(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        delegate = MagicMock(spec=K8sPort)
        delegate.get_cluster_metrics.return_value = {
            "cpu_usage_pct": 10.0,
            "memory_usage_pct": 20.0,
            "node_count": 3,
            "pod_count": 12,
        }
        adapter = AWSEKSAdapter(_context("eks-prod"), k8s_delegate=delegate)

        result = adapter.get_cluster_metrics()

        delegate.get_cluster_metrics.assert_called_once_with()
        assert result["node_count"] == 3

    def test_defaults_to_vanilla_delegate_when_none_injected(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        vanilla_instance = MagicMock(spec=K8sPort)
        vanilla_instance.list_pods.return_value = []
        adapter = AWSEKSAdapter(_context("eks-prod"))

        with patch(
            "hexawyn.adapters.secondary.vanilla.vanilla_adapter.VanillaAdapter",
            return_value=vanilla_instance,
        ) as vanilla_cls:
            result = adapter.list_pods()

        vanilla_cls.assert_called_once_with("eks-prod")
        assert result == []


class TestClusterContext:
    def test_get_cluster_context_reports_aws_provider(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        ctx = _context("arn:aws:eks:eu-west-1:123456789012:cluster/prod", namespace="team-a")
        adapter = AWSEKSAdapter(ctx, k8s_delegate=MagicMock(spec=K8sPort))

        result = adapter.get_cluster_context()

        assert result["provider"] == "aws"
        assert result["cluster"] == "prod"
        assert result["namespace"] == "team-a"
        assert result["name"] == ctx["name"]


class TestDescribeClusterStatus:
    def test_returns_typed_status(self) -> None:
        import os

        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        eks_client = MagicMock()
        eks_client.describe_cluster.return_value = _describe_response()
        ctx = _context("arn:aws:eks:eu-west-1:123456789012:cluster/prod")
        adapter = AWSEKSAdapter(ctx, k8s_delegate=MagicMock(spec=K8sPort), eks_client=eks_client)

        with patch.dict(os.environ, _NO_REGION_ENV):
            status = adapter.describe_cluster_status()

        eks_client.describe_cluster.assert_called_once_with(name="prod")
        assert status["name"] == "prod"
        assert status["status"] == "ACTIVE"
        assert status["version"] == "1.29"
        assert status["endpoint"].startswith("https://")
        assert status["region"] == "eu-west-1"

    def test_missing_credentials_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        eks_client = MagicMock()
        eks_client.describe_cluster.side_effect = NoCredentialsError()
        adapter = AWSEKSAdapter(
            _context("eks-prod"), k8s_delegate=MagicMock(spec=K8sPort), eks_client=eks_client
        )

        with pytest.raises(ClusterUnreachableError) as exc_info:
            adapter.describe_cluster_status()

        assert "aws configure" in str(exc_info.value).lower()

    def test_client_error_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        eks_client = MagicMock()
        eks_client.describe_cluster.side_effect = ClientError(
            {"Error": {"Code": "AccessDeniedException", "Message": "denied"}},
            "DescribeCluster",
        )
        adapter = AWSEKSAdapter(
            _context("eks-prod"), k8s_delegate=MagicMock(spec=K8sPort), eks_client=eks_client
        )

        with pytest.raises(ClusterUnreachableError):
            adapter.describe_cluster_status()

    def test_endpoint_connection_error_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        eks_client = MagicMock()
        eks_client.describe_cluster.side_effect = EndpointConnectionError(
            endpoint_url="https://eks.eu-west-1.amazonaws.com"
        )
        adapter = AWSEKSAdapter(
            _context("eks-prod"), k8s_delegate=MagicMock(spec=K8sPort), eks_client=eks_client
        )

        with pytest.raises(ClusterUnreachableError):
            adapter.describe_cluster_status()

    def test_lazily_creates_boto3_client_when_not_injected(self) -> None:
        import os

        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        created = MagicMock()
        created.describe_cluster.return_value = _describe_response()
        ctx = _context("arn:aws:eks:eu-west-1:123456789012:cluster/prod")
        adapter = AWSEKSAdapter(ctx, k8s_delegate=MagicMock(spec=K8sPort))

        with (
            patch.dict(os.environ, _NO_REGION_ENV),
            patch.object(boto3, "client", return_value=created) as mock_client,
        ):
            adapter.describe_cluster_status()

        mock_client.assert_called_once_with("eks", region_name="eu-west-1")
