from __future__ import annotations

from typing import Protocol, TypedDict, cast

from hexawyn.adapters.secondary.gcp.gke_context_parser import GKEContextInfo, parse_gke_context
from hexawyn.application.ports.driven.k8s_port import (
    ClusterContext,
    ClusterMetrics,
    K8sPort,
    NamespaceInfo,
    PodInfo,
)
from hexawyn.domain.errors import ClusterUnreachableError

_CREDENTIALS_HINT = "Run 'gcloud auth application-default login', then retry."


class GKEClusterStatus(TypedDict):
    name: str
    status: str
    version: str
    endpoint: str
    location: str


class _GKECluster(Protocol):
    name: str
    status: str
    current_master_version: str
    endpoint: str
    location: str


class GKEClient(Protocol):
    """Minimal contract for the google-cloud-container client used here."""

    def get_cluster(self, name: str) -> _GKECluster:
        """Return metadata for the given GKE cluster resource name."""


class GCPGKEAdapter(K8sPort):
    """K8sPort implementation for GCP GKE.

    Kubernetes reads are delegated to an injected K8sPort (the kubeconfig
    already carries GKE auth after `gcloud container clusters get-credentials`).
    GCP-specific behaviour is limited to project/region parsing and cluster
    metadata via the Cloud Container API.
    """

    def __init__(
        self,
        context: ClusterContext,
        k8s_delegate: K8sPort | None = None,
        gke_client: GKEClient | None = None,
        project_id: str | None = None,
    ) -> None:
        self._context = context
        self._k8s_delegate = k8s_delegate
        self._gke_client = gke_client
        self._project_id = project_id
        self._parsed: GKEContextInfo | None = parse_gke_context(context["name"])

    @property
    def project_id(self) -> str | None:
        if self._project_id:
            return self._project_id
        return self._parsed["project_id"] if self._parsed else None

    def describe_cluster_status(self) -> GKEClusterStatus:
        """Fetch live GKE cluster metadata.

        Raises ClusterUnreachableError when credentials are missing, the
        context is not a GKE context, or the control plane is unreachable.
        """
        from google.api_core.exceptions import GoogleAPICallError
        from google.auth.exceptions import DefaultCredentialsError

        if self._parsed is None:
            raise ClusterUnreachableError(
                "Cannot determine GKE cluster from context name.",
                context={"context": self._context["name"]},
            )

        resource_name = (
            f"projects/{self._parsed['project_id']}"
            f"/locations/{self._parsed['region']}"
            f"/clusters/{self._parsed['cluster']}"
        )
        try:
            cluster = self._client_or_create().get_cluster(name=resource_name)
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"cluster": self._parsed["cluster"]},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Unable to reach the GKE control plane.",
                context={"cluster": self._parsed["cluster"], "error": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.status),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
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
            "provider": "gcp",
            "namespace": self._context.get("namespace", "default"),
        }

    # ── Helpers ───────────────────────────────────────────────

    def _delegate(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

            self._k8s_delegate = VanillaAdapter(self._context["name"])
        return self._k8s_delegate

    def _client_or_create(self) -> GKEClient:
        client = self._gke_client
        if client is None:
            from google.cloud import container_v1

            client = cast(GKEClient, container_v1.ClusterManagerClient())
            self._gke_client = client
        return client

    def _cluster_short_name(self) -> str:
        if self._parsed:
            return self._parsed["cluster"]
        return self._context.get("cluster") or self._context["name"]
