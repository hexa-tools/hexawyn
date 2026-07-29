from __future__ import annotations

import os
from typing import Protocol, TypedDict, cast

from hexawyn.application.ports.driven.k8s_port import (
    ClusterContext,
    ClusterMetrics,
    K8sPort,
    NamespaceInfo,
    PodInfo,
)
from hexawyn.domain.errors import ClusterUnreachableError

_SUBSCRIPTION_ENV = "AZURE_SUBSCRIPTION_ID"
_RESOURCE_GROUP_ENV = "AZURE_RESOURCE_GROUP"
_CREDENTIALS_HINT = "Run 'az login' or attach a managed identity, then retry."
_CONFIG_HINT = f"Set {_SUBSCRIPTION_ENV} and {_RESOURCE_GROUP_ENV} to describe the AKS cluster."


class AKSClusterStatus(TypedDict):
    name: str
    status: str
    version: str
    fqdn: str
    location: str


class _ManagedCluster(Protocol):
    name: str
    provisioning_state: str
    kubernetes_version: str
    fqdn: str
    location: str


class _ManagedClustersOperations(Protocol):
    def get(self, resource_group_name: str, resource_name: str) -> _ManagedCluster: ...


class AKSClient(Protocol):
    """Minimal contract for the azure-mgmt-containerservice client used here."""

    managed_clusters: _ManagedClustersOperations


class AzureAKSAdapter(K8sPort):
    """K8sPort implementation for Azure AKS.

    Kubernetes reads are delegated to an injected K8sPort (the kubeconfig
    already carries AKS auth after `az aks get-credentials`). Azure-specific
    behaviour is limited to cluster metadata via the Container Service API.
    """

    def __init__(  # noqa: PLR0913
        self,
        context: ClusterContext,
        k8s_delegate: K8sPort | None = None,
        aks_client: AKSClient | None = None,
        subscription_id: str | None = None,
        resource_group: str | None = None,
    ) -> None:
        self._context = context
        self._k8s_delegate = k8s_delegate
        self._aks_client = aks_client
        self._subscription_id = subscription_id
        self._resource_group = resource_group

    @property
    def subscription_id(self) -> str | None:
        return self._subscription_id or os.environ.get(_SUBSCRIPTION_ENV) or None

    @property
    def resource_group(self) -> str | None:
        return self._resource_group or os.environ.get(_RESOURCE_GROUP_ENV) or None

    def describe_cluster_status(self) -> AKSClusterStatus:
        """Fetch live AKS cluster metadata.

        Raises ClusterUnreachableError when credentials/config are missing or
        the control plane is unreachable.
        """
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError

        subscription_id = self.subscription_id
        resource_group = self.resource_group
        if not subscription_id or not resource_group:
            raise ClusterUnreachableError(
                f"Missing Azure configuration. {_CONFIG_HINT}",
                context={"cluster": self._cluster_short_name()},
            )

        try:
            cluster = self._client_or_create(subscription_id).managed_clusters.get(
                resource_group_name=resource_group,
                resource_name=self._cluster_short_name(),
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"cluster": self._cluster_short_name()},
            ) from exc
        except HttpResponseError as exc:
            raise ClusterUnreachableError(
                "Unable to reach the AKS control plane.",
                context={"cluster": self._cluster_short_name(), "error": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.provisioning_state),
            "version": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
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
            "provider": "azure",
            "namespace": self._context.get("namespace", "default"),
        }

    # ── Helpers ───────────────────────────────────────────────

    def _delegate(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

            self._k8s_delegate = VanillaAdapter(self._context["name"])
        return self._k8s_delegate

    def _client_or_create(self, subscription_id: str) -> AKSClient:
        client = self._aks_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.mgmt.containerservice import ContainerServiceClient

            client = cast(
                AKSClient, ContainerServiceClient(DefaultAzureCredential(), subscription_id)
            )
            self._aks_client = client
        return client

    def _cluster_short_name(self) -> str:
        return self._context.get("cluster") or self._context["name"]
