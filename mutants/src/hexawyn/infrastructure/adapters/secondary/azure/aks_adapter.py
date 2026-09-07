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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
mutants_xǁAzureAKSAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureAKSAdapterǁlist_pods__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureAKSAdapterǁ_delegate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureAKSAdapterǁ_client_or_create__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureAKSAdapterǁ_cluster_short_name__mutmut: MutantDict = {}  # type: ignore


class AzureAKSAdapter(K8sPort):
    """K8sPort implementation for Azure AKS.

    Kubernetes reads are delegated to an injected K8sPort (the kubeconfig
    already carries AKS auth after `az aks get-credentials`). Azure-specific
    behaviour is limited to cluster metadata via the Container Service API.
    """

    @_mutmut_mutated(mutants_xǁAzureAKSAdapterǁ__init____mutmut)
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

    def xǁAzureAKSAdapterǁ__init____mutmut_orig(  # noqa: PLR0913
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

    def xǁAzureAKSAdapterǁ__init____mutmut_1(  # noqa: PLR0913
        self,
        context: ClusterContext,
        k8s_delegate: K8sPort | None = None,
        aks_client: AKSClient | None = None,
        subscription_id: str | None = None,
        resource_group: str | None = None,
    ) -> None:
        self._context = None
        self._k8s_delegate = k8s_delegate
        self._aks_client = aks_client
        self._subscription_id = subscription_id
        self._resource_group = resource_group

    def xǁAzureAKSAdapterǁ__init____mutmut_2(  # noqa: PLR0913
        self,
        context: ClusterContext,
        k8s_delegate: K8sPort | None = None,
        aks_client: AKSClient | None = None,
        subscription_id: str | None = None,
        resource_group: str | None = None,
    ) -> None:
        self._context = context
        self._k8s_delegate = None
        self._aks_client = aks_client
        self._subscription_id = subscription_id
        self._resource_group = resource_group

    def xǁAzureAKSAdapterǁ__init____mutmut_3(  # noqa: PLR0913
        self,
        context: ClusterContext,
        k8s_delegate: K8sPort | None = None,
        aks_client: AKSClient | None = None,
        subscription_id: str | None = None,
        resource_group: str | None = None,
    ) -> None:
        self._context = context
        self._k8s_delegate = k8s_delegate
        self._aks_client = None
        self._subscription_id = subscription_id
        self._resource_group = resource_group

    def xǁAzureAKSAdapterǁ__init____mutmut_4(  # noqa: PLR0913
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
        self._subscription_id = None
        self._resource_group = resource_group

    def xǁAzureAKSAdapterǁ__init____mutmut_5(  # noqa: PLR0913
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
        self._resource_group = None

    @property
    def subscription_id(self) -> str | None:
        return self._subscription_id or os.environ.get(_SUBSCRIPTION_ENV) or None

    @property
    def resource_group(self) -> str | None:
        return self._resource_group or os.environ.get(_RESOURCE_GROUP_ENV) or None

    @_mutmut_mutated(mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut)
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_orig(self) -> AKSClusterStatus:
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_1(self) -> AKSClusterStatus:
        """Fetch live AKS cluster metadata.

        Raises ClusterUnreachableError when credentials/config are missing or
        the control plane is unreachable.
        """
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError

        subscription_id = None
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_2(self) -> AKSClusterStatus:
        """Fetch live AKS cluster metadata.

        Raises ClusterUnreachableError when credentials/config are missing or
        the control plane is unreachable.
        """
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError

        subscription_id = self.subscription_id
        resource_group = None
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_3(self) -> AKSClusterStatus:
        """Fetch live AKS cluster metadata.

        Raises ClusterUnreachableError when credentials/config are missing or
        the control plane is unreachable.
        """
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError

        subscription_id = self.subscription_id
        resource_group = self.resource_group
        if not subscription_id and not resource_group:
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_4(self) -> AKSClusterStatus:
        """Fetch live AKS cluster metadata.

        Raises ClusterUnreachableError when credentials/config are missing or
        the control plane is unreachable.
        """
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError

        subscription_id = self.subscription_id
        resource_group = self.resource_group
        if subscription_id or not resource_group:
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_5(self) -> AKSClusterStatus:
        """Fetch live AKS cluster metadata.

        Raises ClusterUnreachableError when credentials/config are missing or
        the control plane is unreachable.
        """
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError

        subscription_id = self.subscription_id
        resource_group = self.resource_group
        if not subscription_id or resource_group:
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_6(self) -> AKSClusterStatus:
        """Fetch live AKS cluster metadata.

        Raises ClusterUnreachableError when credentials/config are missing or
        the control plane is unreachable.
        """
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError

        subscription_id = self.subscription_id
        resource_group = self.resource_group
        if not subscription_id or not resource_group:
            raise ClusterUnreachableError(
                None,
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_7(self) -> AKSClusterStatus:
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
                context=None,
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_8(self) -> AKSClusterStatus:
        """Fetch live AKS cluster metadata.

        Raises ClusterUnreachableError when credentials/config are missing or
        the control plane is unreachable.
        """
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError

        subscription_id = self.subscription_id
        resource_group = self.resource_group
        if not subscription_id or not resource_group:
            raise ClusterUnreachableError(
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_9(self) -> AKSClusterStatus:
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_10(self) -> AKSClusterStatus:
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
                context={"XXclusterXX": self._cluster_short_name()},
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_11(self) -> AKSClusterStatus:
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
                context={"CLUSTER": self._cluster_short_name()},
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_12(self) -> AKSClusterStatus:
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
            cluster = None
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_13(self) -> AKSClusterStatus:
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
                resource_group_name=None,
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_14(self) -> AKSClusterStatus:
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
                resource_name=None,
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_15(self) -> AKSClusterStatus:
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_16(self) -> AKSClusterStatus:
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_17(self) -> AKSClusterStatus:
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
            cluster = self._client_or_create(None).managed_clusters.get(
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_18(self) -> AKSClusterStatus:
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
                None,
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_19(self) -> AKSClusterStatus:
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
                context=None,
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_20(self) -> AKSClusterStatus:
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_21(self) -> AKSClusterStatus:
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_22(self) -> AKSClusterStatus:
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
                context={"XXclusterXX": self._cluster_short_name()},
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_23(self) -> AKSClusterStatus:
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
                context={"CLUSTER": self._cluster_short_name()},
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

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_24(self) -> AKSClusterStatus:
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
                None,
                context={"cluster": self._cluster_short_name(), "error": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.provisioning_state),
            "version": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_25(self) -> AKSClusterStatus:
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
                context=None,
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.provisioning_state),
            "version": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_26(self) -> AKSClusterStatus:
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
                context={"cluster": self._cluster_short_name(), "error": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.provisioning_state),
            "version": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_27(self) -> AKSClusterStatus:
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
                ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.provisioning_state),
            "version": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_28(self) -> AKSClusterStatus:
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
                "XXUnable to reach the AKS control plane.XX",
                context={"cluster": self._cluster_short_name(), "error": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.provisioning_state),
            "version": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_29(self) -> AKSClusterStatus:
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
                "unable to reach the aks control plane.",
                context={"cluster": self._cluster_short_name(), "error": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.provisioning_state),
            "version": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_30(self) -> AKSClusterStatus:
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
                "UNABLE TO REACH THE AKS CONTROL PLANE.",
                context={"cluster": self._cluster_short_name(), "error": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.provisioning_state),
            "version": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_31(self) -> AKSClusterStatus:
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
                context={"XXclusterXX": self._cluster_short_name(), "error": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.provisioning_state),
            "version": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_32(self) -> AKSClusterStatus:
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
                context={"CLUSTER": self._cluster_short_name(), "error": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.provisioning_state),
            "version": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_33(self) -> AKSClusterStatus:
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
                context={"cluster": self._cluster_short_name(), "XXerrorXX": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.provisioning_state),
            "version": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_34(self) -> AKSClusterStatus:
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
                context={"cluster": self._cluster_short_name(), "ERROR": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.provisioning_state),
            "version": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_35(self) -> AKSClusterStatus:
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
                context={"cluster": self._cluster_short_name(), "error": str(None)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.provisioning_state),
            "version": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_36(self) -> AKSClusterStatus:
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
            "XXnameXX": str(cluster.name),
            "status": str(cluster.provisioning_state),
            "version": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_37(self) -> AKSClusterStatus:
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
            "NAME": str(cluster.name),
            "status": str(cluster.provisioning_state),
            "version": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_38(self) -> AKSClusterStatus:
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
            "name": str(None),
            "status": str(cluster.provisioning_state),
            "version": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_39(self) -> AKSClusterStatus:
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
            "XXstatusXX": str(cluster.provisioning_state),
            "version": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_40(self) -> AKSClusterStatus:
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
            "STATUS": str(cluster.provisioning_state),
            "version": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_41(self) -> AKSClusterStatus:
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
            "status": str(None),
            "version": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_42(self) -> AKSClusterStatus:
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
            "XXversionXX": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_43(self) -> AKSClusterStatus:
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
            "VERSION": str(cluster.kubernetes_version),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_44(self) -> AKSClusterStatus:
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
            "version": str(None),
            "fqdn": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_45(self) -> AKSClusterStatus:
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
            "XXfqdnXX": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_46(self) -> AKSClusterStatus:
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
            "FQDN": str(cluster.fqdn),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_47(self) -> AKSClusterStatus:
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
            "fqdn": str(None),
            "location": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_48(self) -> AKSClusterStatus:
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
            "XXlocationXX": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_49(self) -> AKSClusterStatus:
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
            "LOCATION": str(cluster.location),
        }

    def xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_50(self) -> AKSClusterStatus:
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
            "location": str(None),
        }

    # ── K8sPort ───────────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁAzureAKSAdapterǁlist_pods__mutmut)
    def list_pods(self, namespace: str | None = None) -> list[PodInfo]:
        return self._delegate().list_pods(namespace)

    # ── K8sPort ───────────────────────────────────────────────

    def xǁAzureAKSAdapterǁlist_pods__mutmut_orig(self, namespace: str | None = None) -> list[PodInfo]:
        return self._delegate().list_pods(namespace)

    # ── K8sPort ───────────────────────────────────────────────

    def xǁAzureAKSAdapterǁlist_pods__mutmut_1(self, namespace: str | None = None) -> list[PodInfo]:
        return self._delegate().list_pods(None)

    def list_namespaces(self) -> list[NamespaceInfo]:
        return self._delegate().list_namespaces()

    def get_cluster_metrics(self) -> ClusterMetrics:
        return self._delegate().get_cluster_metrics()

    @_mutmut_mutated(mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut)
    def get_cluster_context(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "azure",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_orig(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "azure",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_1(self) -> ClusterContext:
        return {
            "XXnameXX": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "azure",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_2(self) -> ClusterContext:
        return {
            "NAME": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "azure",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_3(self) -> ClusterContext:
        return {
            "name": self._context["XXnameXX"],
            "cluster": self._cluster_short_name(),
            "provider": "azure",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_4(self) -> ClusterContext:
        return {
            "name": self._context["NAME"],
            "cluster": self._cluster_short_name(),
            "provider": "azure",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_5(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "XXclusterXX": self._cluster_short_name(),
            "provider": "azure",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_6(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "CLUSTER": self._cluster_short_name(),
            "provider": "azure",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_7(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "XXproviderXX": "azure",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_8(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "PROVIDER": "azure",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_9(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "XXazureXX",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_10(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "AZURE",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_11(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "azure",
            "XXnamespaceXX": self._context.get("namespace", "default"),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_12(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "azure",
            "NAMESPACE": self._context.get("namespace", "default"),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_13(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "azure",
            "namespace": self._context.get(None, "default"),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_14(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "azure",
            "namespace": self._context.get("namespace", None),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_15(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "azure",
            "namespace": self._context.get("default"),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_16(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "azure",
            "namespace": self._context.get("namespace", ),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_17(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "azure",
            "namespace": self._context.get("XXnamespaceXX", "default"),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_18(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "azure",
            "namespace": self._context.get("NAMESPACE", "default"),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_19(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "azure",
            "namespace": self._context.get("namespace", "XXdefaultXX"),
        }

    def xǁAzureAKSAdapterǁget_cluster_context__mutmut_20(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "azure",
            "namespace": self._context.get("namespace", "DEFAULT"),
        }

    # ── Helpers ───────────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁAzureAKSAdapterǁ_delegate__mutmut)
    def _delegate(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["name"])
        return self._k8s_delegate

    # ── Helpers ───────────────────────────────────────────────

    def xǁAzureAKSAdapterǁ_delegate__mutmut_orig(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["name"])
        return self._k8s_delegate

    # ── Helpers ───────────────────────────────────────────────

    def xǁAzureAKSAdapterǁ_delegate__mutmut_1(self) -> K8sPort:
        if self._k8s_delegate is not None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["name"])
        return self._k8s_delegate

    # ── Helpers ───────────────────────────────────────────────

    def xǁAzureAKSAdapterǁ_delegate__mutmut_2(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = None
        return self._k8s_delegate

    # ── Helpers ───────────────────────────────────────────────

    def xǁAzureAKSAdapterǁ_delegate__mutmut_3(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(None)
        return self._k8s_delegate

    # ── Helpers ───────────────────────────────────────────────

    def xǁAzureAKSAdapterǁ_delegate__mutmut_4(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["XXnameXX"])
        return self._k8s_delegate

    # ── Helpers ───────────────────────────────────────────────

    def xǁAzureAKSAdapterǁ_delegate__mutmut_5(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["NAME"])
        return self._k8s_delegate

    @_mutmut_mutated(mutants_xǁAzureAKSAdapterǁ_client_or_create__mutmut)
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

    def xǁAzureAKSAdapterǁ_client_or_create__mutmut_orig(self, subscription_id: str) -> AKSClient:
        client = self._aks_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.mgmt.containerservice import ContainerServiceClient

            client = cast(
                AKSClient, ContainerServiceClient(DefaultAzureCredential(), subscription_id)
            )
            self._aks_client = client
        return client

    def xǁAzureAKSAdapterǁ_client_or_create__mutmut_1(self, subscription_id: str) -> AKSClient:
        client = None
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.mgmt.containerservice import ContainerServiceClient

            client = cast(
                AKSClient, ContainerServiceClient(DefaultAzureCredential(), subscription_id)
            )
            self._aks_client = client
        return client

    def xǁAzureAKSAdapterǁ_client_or_create__mutmut_2(self, subscription_id: str) -> AKSClient:
        client = self._aks_client
        if client is not None:
            from azure.identity import DefaultAzureCredential
            from azure.mgmt.containerservice import ContainerServiceClient

            client = cast(
                AKSClient, ContainerServiceClient(DefaultAzureCredential(), subscription_id)
            )
            self._aks_client = client
        return client

    def xǁAzureAKSAdapterǁ_client_or_create__mutmut_3(self, subscription_id: str) -> AKSClient:
        client = self._aks_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.mgmt.containerservice import ContainerServiceClient

            client = None
            self._aks_client = client
        return client

    def xǁAzureAKSAdapterǁ_client_or_create__mutmut_4(self, subscription_id: str) -> AKSClient:
        client = self._aks_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.mgmt.containerservice import ContainerServiceClient

            client = cast(
                None, ContainerServiceClient(DefaultAzureCredential(), subscription_id)
            )
            self._aks_client = client
        return client

    def xǁAzureAKSAdapterǁ_client_or_create__mutmut_5(self, subscription_id: str) -> AKSClient:
        client = self._aks_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.mgmt.containerservice import ContainerServiceClient

            client = cast(
                AKSClient, None
            )
            self._aks_client = client
        return client

    def xǁAzureAKSAdapterǁ_client_or_create__mutmut_6(self, subscription_id: str) -> AKSClient:
        client = self._aks_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.mgmt.containerservice import ContainerServiceClient

            client = cast(
                ContainerServiceClient(DefaultAzureCredential(), subscription_id)
            )
            self._aks_client = client
        return client

    def xǁAzureAKSAdapterǁ_client_or_create__mutmut_7(self, subscription_id: str) -> AKSClient:
        client = self._aks_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.mgmt.containerservice import ContainerServiceClient

            client = cast(
                AKSClient, )
            self._aks_client = client
        return client

    def xǁAzureAKSAdapterǁ_client_or_create__mutmut_8(self, subscription_id: str) -> AKSClient:
        client = self._aks_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.mgmt.containerservice import ContainerServiceClient

            client = cast(
                AKSClient, ContainerServiceClient(None, subscription_id)
            )
            self._aks_client = client
        return client

    def xǁAzureAKSAdapterǁ_client_or_create__mutmut_9(self, subscription_id: str) -> AKSClient:
        client = self._aks_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.mgmt.containerservice import ContainerServiceClient

            client = cast(
                AKSClient, ContainerServiceClient(DefaultAzureCredential(), None)
            )
            self._aks_client = client
        return client

    def xǁAzureAKSAdapterǁ_client_or_create__mutmut_10(self, subscription_id: str) -> AKSClient:
        client = self._aks_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.mgmt.containerservice import ContainerServiceClient

            client = cast(
                AKSClient, ContainerServiceClient(subscription_id)
            )
            self._aks_client = client
        return client

    def xǁAzureAKSAdapterǁ_client_or_create__mutmut_11(self, subscription_id: str) -> AKSClient:
        client = self._aks_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.mgmt.containerservice import ContainerServiceClient

            client = cast(
                AKSClient, ContainerServiceClient(DefaultAzureCredential(), )
            )
            self._aks_client = client
        return client

    def xǁAzureAKSAdapterǁ_client_or_create__mutmut_12(self, subscription_id: str) -> AKSClient:
        client = self._aks_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.mgmt.containerservice import ContainerServiceClient

            client = cast(
                AKSClient, ContainerServiceClient(DefaultAzureCredential(), subscription_id)
            )
            self._aks_client = None
        return client

    @_mutmut_mutated(mutants_xǁAzureAKSAdapterǁ_cluster_short_name__mutmut)
    def _cluster_short_name(self) -> str:
        return self._context.get("cluster") or self._context["name"]

    def xǁAzureAKSAdapterǁ_cluster_short_name__mutmut_orig(self) -> str:
        return self._context.get("cluster") or self._context["name"]

    def xǁAzureAKSAdapterǁ_cluster_short_name__mutmut_1(self) -> str:
        return self._context.get("cluster") and self._context["name"]

    def xǁAzureAKSAdapterǁ_cluster_short_name__mutmut_2(self) -> str:
        return self._context.get(None) or self._context["name"]

    def xǁAzureAKSAdapterǁ_cluster_short_name__mutmut_3(self) -> str:
        return self._context.get("XXclusterXX") or self._context["name"]

    def xǁAzureAKSAdapterǁ_cluster_short_name__mutmut_4(self) -> str:
        return self._context.get("CLUSTER") or self._context["name"]

    def xǁAzureAKSAdapterǁ_cluster_short_name__mutmut_5(self) -> str:
        return self._context.get("cluster") or self._context["XXnameXX"]

    def xǁAzureAKSAdapterǁ_cluster_short_name__mutmut_6(self) -> str:
        return self._context.get("cluster") or self._context["NAME"]

mutants_xǁAzureAKSAdapterǁ__init____mutmut['_mutmut_orig'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ__init____mutmut['xǁAzureAKSAdapterǁ__init____mutmut_1'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ__init____mutmut['xǁAzureAKSAdapterǁ__init____mutmut_2'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ__init____mutmut['xǁAzureAKSAdapterǁ__init____mutmut_3'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ__init____mutmut['xǁAzureAKSAdapterǁ__init____mutmut_4'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ__init____mutmut['xǁAzureAKSAdapterǁ__init____mutmut_5'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ__init____mutmut_5 # type: ignore # mutmut generated

mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['_mutmut_orig'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_1'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_2'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_3'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_4'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_5'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_6'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_7'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_8'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_9'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_10'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_11'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_12'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_13'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_14'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_15'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_16'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_17'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_18'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_19'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_20'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_21'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_22'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_23'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_24'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_25'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_26'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_27'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_28'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_29'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_30'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_31'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_32'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_33'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_34'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_35'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_36'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_37'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_38'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_39'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_40'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_40 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_41'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_41 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_42'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_42 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_43'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_43 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_44'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_44 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_45'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_45 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_46'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_46 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_47'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_47 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_48'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_48 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_49'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_49 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut['xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_50'] = AzureAKSAdapter.xǁAzureAKSAdapterǁdescribe_cluster_status__mutmut_50 # type: ignore # mutmut generated

mutants_xǁAzureAKSAdapterǁlist_pods__mutmut['_mutmut_orig'] = AzureAKSAdapter.xǁAzureAKSAdapterǁlist_pods__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁlist_pods__mutmut['xǁAzureAKSAdapterǁlist_pods__mutmut_1'] = AzureAKSAdapter.xǁAzureAKSAdapterǁlist_pods__mutmut_1 # type: ignore # mutmut generated

mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['_mutmut_orig'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['xǁAzureAKSAdapterǁget_cluster_context__mutmut_1'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['xǁAzureAKSAdapterǁget_cluster_context__mutmut_2'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['xǁAzureAKSAdapterǁget_cluster_context__mutmut_3'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['xǁAzureAKSAdapterǁget_cluster_context__mutmut_4'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['xǁAzureAKSAdapterǁget_cluster_context__mutmut_5'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['xǁAzureAKSAdapterǁget_cluster_context__mutmut_6'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['xǁAzureAKSAdapterǁget_cluster_context__mutmut_7'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['xǁAzureAKSAdapterǁget_cluster_context__mutmut_8'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['xǁAzureAKSAdapterǁget_cluster_context__mutmut_9'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['xǁAzureAKSAdapterǁget_cluster_context__mutmut_10'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['xǁAzureAKSAdapterǁget_cluster_context__mutmut_11'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['xǁAzureAKSAdapterǁget_cluster_context__mutmut_12'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['xǁAzureAKSAdapterǁget_cluster_context__mutmut_13'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['xǁAzureAKSAdapterǁget_cluster_context__mutmut_14'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['xǁAzureAKSAdapterǁget_cluster_context__mutmut_15'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['xǁAzureAKSAdapterǁget_cluster_context__mutmut_16'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['xǁAzureAKSAdapterǁget_cluster_context__mutmut_17'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['xǁAzureAKSAdapterǁget_cluster_context__mutmut_18'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['xǁAzureAKSAdapterǁget_cluster_context__mutmut_19'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁget_cluster_context__mutmut['xǁAzureAKSAdapterǁget_cluster_context__mutmut_20'] = AzureAKSAdapter.xǁAzureAKSAdapterǁget_cluster_context__mutmut_20 # type: ignore # mutmut generated

mutants_xǁAzureAKSAdapterǁ_delegate__mutmut['_mutmut_orig'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_delegate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_delegate__mutmut['xǁAzureAKSAdapterǁ_delegate__mutmut_1'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_delegate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_delegate__mutmut['xǁAzureAKSAdapterǁ_delegate__mutmut_2'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_delegate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_delegate__mutmut['xǁAzureAKSAdapterǁ_delegate__mutmut_3'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_delegate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_delegate__mutmut['xǁAzureAKSAdapterǁ_delegate__mutmut_4'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_delegate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_delegate__mutmut['xǁAzureAKSAdapterǁ_delegate__mutmut_5'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_delegate__mutmut_5 # type: ignore # mutmut generated

mutants_xǁAzureAKSAdapterǁ_client_or_create__mutmut['_mutmut_orig'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_client_or_create__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_client_or_create__mutmut['xǁAzureAKSAdapterǁ_client_or_create__mutmut_1'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_client_or_create__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_client_or_create__mutmut['xǁAzureAKSAdapterǁ_client_or_create__mutmut_2'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_client_or_create__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_client_or_create__mutmut['xǁAzureAKSAdapterǁ_client_or_create__mutmut_3'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_client_or_create__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_client_or_create__mutmut['xǁAzureAKSAdapterǁ_client_or_create__mutmut_4'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_client_or_create__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_client_or_create__mutmut['xǁAzureAKSAdapterǁ_client_or_create__mutmut_5'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_client_or_create__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_client_or_create__mutmut['xǁAzureAKSAdapterǁ_client_or_create__mutmut_6'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_client_or_create__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_client_or_create__mutmut['xǁAzureAKSAdapterǁ_client_or_create__mutmut_7'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_client_or_create__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_client_or_create__mutmut['xǁAzureAKSAdapterǁ_client_or_create__mutmut_8'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_client_or_create__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_client_or_create__mutmut['xǁAzureAKSAdapterǁ_client_or_create__mutmut_9'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_client_or_create__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_client_or_create__mutmut['xǁAzureAKSAdapterǁ_client_or_create__mutmut_10'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_client_or_create__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_client_or_create__mutmut['xǁAzureAKSAdapterǁ_client_or_create__mutmut_11'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_client_or_create__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_client_or_create__mutmut['xǁAzureAKSAdapterǁ_client_or_create__mutmut_12'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_client_or_create__mutmut_12 # type: ignore # mutmut generated

mutants_xǁAzureAKSAdapterǁ_cluster_short_name__mutmut['_mutmut_orig'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_cluster_short_name__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_cluster_short_name__mutmut['xǁAzureAKSAdapterǁ_cluster_short_name__mutmut_1'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_cluster_short_name__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_cluster_short_name__mutmut['xǁAzureAKSAdapterǁ_cluster_short_name__mutmut_2'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_cluster_short_name__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_cluster_short_name__mutmut['xǁAzureAKSAdapterǁ_cluster_short_name__mutmut_3'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_cluster_short_name__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_cluster_short_name__mutmut['xǁAzureAKSAdapterǁ_cluster_short_name__mutmut_4'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_cluster_short_name__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_cluster_short_name__mutmut['xǁAzureAKSAdapterǁ_cluster_short_name__mutmut_5'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_cluster_short_name__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAzureAKSAdapterǁ_cluster_short_name__mutmut['xǁAzureAKSAdapterǁ_cluster_short_name__mutmut_6'] = AzureAKSAdapter.xǁAzureAKSAdapterǁ_cluster_short_name__mutmut_6 # type: ignore # mutmut generated
