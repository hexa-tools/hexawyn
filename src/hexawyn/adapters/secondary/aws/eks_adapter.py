import os
import re
from typing import Protocol, TypedDict

from hexawyn.application.ports.driven.k8s_port import (
    ClusterContext,
    ClusterMetrics,
    K8sPort,
    NamespaceInfo,
    PodInfo,
)
from hexawyn.domain.errors import ClusterUnreachableError
from hexawyn.infrastructure.config.region_resolver import resolve_region

_ARN_CLUSTER_NAME_PATTERN = re.compile(r"arn:aws:eks:[a-z0-9-]+:\d+:cluster/(.+)$")
_CREDENTIALS_HINT = "Run 'aws configure' or attach an IAM role, then retry."


class EKSClusterStatus(TypedDict):
    name: str
    status: str
    version: str
    endpoint: str
    region: str


class _EKSClusterField(TypedDict, total=False):
    name: str
    status: str
    version: str
    endpoint: str


class _DescribeClusterResponse(TypedDict):
    cluster: _EKSClusterField


class EKSClient(Protocol):
    """Minimal contract for the boto3 EKS client used by this adapter."""

    def describe_cluster(self, name: str) -> _DescribeClusterResponse:
        """Return metadata for the given EKS cluster."""


class AWSEKSAdapter(K8sPort):
    """K8sPort implementation for AWS EKS.

    Kubernetes read operations are delegated to an injected K8sPort (the
    kubeconfig already carries EKS exec authentication after
    `aws eks update-kubeconfig`). AWS-specific behaviour is limited to region
    detection and CloudWatch/EKS metadata via boto3.
    """

    def __init__(
        self,
        context: ClusterContext,
        k8s_delegate: K8sPort | None = None,
        eks_client: EKSClient | None = None,
        region: str | None = None,
    ) -> None:
        self._context = context
        self._k8s_delegate = k8s_delegate
        self._eks_client = eks_client
        self._region = region

    # ── AWS metadata ──────────────────────────────────────────

    @property
    def region(self) -> str | None:
        if self._region is None:
            self._region = resolve_region(self._context["name"], os.environ)
        return self._region

    def describe_cluster_status(self) -> EKSClusterStatus:
        """Fetch live EKS cluster metadata.

        Raises ClusterUnreachableError when AWS credentials are missing or the
        EKS control plane cannot be reached.
        """
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._eks_client_or_create()
        cluster_name = self._cluster_short_name()
        region = self.region or "unknown"
        try:
            response = client.describe_cluster(name=cluster_name)
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"cluster": cluster_name, "region": region},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise ClusterUnreachableError(
                f"Unable to reach the EKS control plane for '{cluster_name}'.",
                context={"cluster": cluster_name, "region": region, "error": str(exc)},
            ) from exc

        cluster = response["cluster"]
        return {
            "name": cluster.get("name", cluster_name),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    # ── K8sPort ───────────────────────────────────────────────

    def list_pods(self, namespace: str | None = None) -> list[PodInfo]:
        return self._delegate().list_pods(namespace)

    def list_namespaces(self) -> list[NamespaceInfo]:
        return self._delegate().list_namespaces()

    def get_cluster_metrics(self) -> ClusterMetrics:
        return self._delegate().get_cluster_metrics()

    def get_cluster_context(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "aws",
            "namespace": self._context.get("namespace", "default"),
        }

    # ── Helpers ───────────────────────────────────────────────

    def _delegate(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

            self._k8s_delegate = VanillaAdapter(self._context["name"])
        return self._k8s_delegate

    def _eks_client_or_create(self) -> EKSClient:
        if self._eks_client is None:
            import boto3

            self._eks_client = boto3.client("eks", region_name=self.region)
        return self._eks_client

    def _cluster_short_name(self) -> str:
        name = self._context["name"]
        arn_match = _ARN_CLUSTER_NAME_PATTERN.search(name)
        if arn_match:
            return arn_match.group(1)
        return self._context.get("cluster") or name
