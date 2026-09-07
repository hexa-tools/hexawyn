from __future__ import annotations

from typing import Protocol, TypedDict, cast

from hexawyn.application.ports.driven.k8s_port import (
    ClusterContext,
    ClusterMetrics,
    K8sPort,
    NamespaceInfo,
    PodInfo,
)
from hexawyn.domain.errors import ClusterUnreachableError
from hexawyn.infrastructure.adapters.secondary.gcp.gke_context_parser import (
    GKEContextInfo,
    parse_gke_context,
)

_CREDENTIALS_HINT = "Run 'gcloud auth application-default login', then retry."


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
mutants_xǁGCPGKEAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPGKEAdapterǁlist_pods__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPGKEAdapterǁ_delegate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPGKEAdapterǁ_client_or_create__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPGKEAdapterǁ_cluster_short_name__mutmut: MutantDict = {}  # type: ignore


class GCPGKEAdapter(K8sPort):
    """K8sPort implementation for GCP GKE.

    Kubernetes reads are delegated to an injected K8sPort (the kubeconfig
    already carries GKE auth after `gcloud container clusters get-credentials`).
    GCP-specific behaviour is limited to project/region parsing and cluster
    metadata via the Cloud Container API.
    """

    @_mutmut_mutated(mutants_xǁGCPGKEAdapterǁ__init____mutmut)
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

    def xǁGCPGKEAdapterǁ__init____mutmut_orig(
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

    def xǁGCPGKEAdapterǁ__init____mutmut_1(
        self,
        context: ClusterContext,
        k8s_delegate: K8sPort | None = None,
        gke_client: GKEClient | None = None,
        project_id: str | None = None,
    ) -> None:
        self._context = None
        self._k8s_delegate = k8s_delegate
        self._gke_client = gke_client
        self._project_id = project_id
        self._parsed: GKEContextInfo | None = parse_gke_context(context["name"])

    def xǁGCPGKEAdapterǁ__init____mutmut_2(
        self,
        context: ClusterContext,
        k8s_delegate: K8sPort | None = None,
        gke_client: GKEClient | None = None,
        project_id: str | None = None,
    ) -> None:
        self._context = context
        self._k8s_delegate = None
        self._gke_client = gke_client
        self._project_id = project_id
        self._parsed: GKEContextInfo | None = parse_gke_context(context["name"])

    def xǁGCPGKEAdapterǁ__init____mutmut_3(
        self,
        context: ClusterContext,
        k8s_delegate: K8sPort | None = None,
        gke_client: GKEClient | None = None,
        project_id: str | None = None,
    ) -> None:
        self._context = context
        self._k8s_delegate = k8s_delegate
        self._gke_client = None
        self._project_id = project_id
        self._parsed: GKEContextInfo | None = parse_gke_context(context["name"])

    def xǁGCPGKEAdapterǁ__init____mutmut_4(
        self,
        context: ClusterContext,
        k8s_delegate: K8sPort | None = None,
        gke_client: GKEClient | None = None,
        project_id: str | None = None,
    ) -> None:
        self._context = context
        self._k8s_delegate = k8s_delegate
        self._gke_client = gke_client
        self._project_id = None
        self._parsed: GKEContextInfo | None = parse_gke_context(context["name"])

    def xǁGCPGKEAdapterǁ__init____mutmut_5(
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
        self._parsed: GKEContextInfo | None = None

    def xǁGCPGKEAdapterǁ__init____mutmut_6(
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
        self._parsed: GKEContextInfo | None = parse_gke_context(None)

    def xǁGCPGKEAdapterǁ__init____mutmut_7(
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
        self._parsed: GKEContextInfo | None = parse_gke_context(context["XXnameXX"])

    def xǁGCPGKEAdapterǁ__init____mutmut_8(
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
        self._parsed: GKEContextInfo | None = parse_gke_context(context["NAME"])

    @property
    def project_id(self) -> str | None:
        if self._project_id:
            return self._project_id
        return self._parsed["project_id"] if self._parsed else None

    @_mutmut_mutated(mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut)
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_orig(self) -> GKEClusterStatus:
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_1(self) -> GKEClusterStatus:
        """Fetch live GKE cluster metadata.

        Raises ClusterUnreachableError when credentials are missing, the
        context is not a GKE context, or the control plane is unreachable.
        """
        from google.api_core.exceptions import GoogleAPICallError
        from google.auth.exceptions import DefaultCredentialsError

        if self._parsed is not None:
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_2(self) -> GKEClusterStatus:
        """Fetch live GKE cluster metadata.

        Raises ClusterUnreachableError when credentials are missing, the
        context is not a GKE context, or the control plane is unreachable.
        """
        from google.api_core.exceptions import GoogleAPICallError
        from google.auth.exceptions import DefaultCredentialsError

        if self._parsed is None:
            raise ClusterUnreachableError(
                None,
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_3(self) -> GKEClusterStatus:
        """Fetch live GKE cluster metadata.

        Raises ClusterUnreachableError when credentials are missing, the
        context is not a GKE context, or the control plane is unreachable.
        """
        from google.api_core.exceptions import GoogleAPICallError
        from google.auth.exceptions import DefaultCredentialsError

        if self._parsed is None:
            raise ClusterUnreachableError(
                "Cannot determine GKE cluster from context name.",
                context=None,
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_4(self) -> GKEClusterStatus:
        """Fetch live GKE cluster metadata.

        Raises ClusterUnreachableError when credentials are missing, the
        context is not a GKE context, or the control plane is unreachable.
        """
        from google.api_core.exceptions import GoogleAPICallError
        from google.auth.exceptions import DefaultCredentialsError

        if self._parsed is None:
            raise ClusterUnreachableError(
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_5(self) -> GKEClusterStatus:
        """Fetch live GKE cluster metadata.

        Raises ClusterUnreachableError when credentials are missing, the
        context is not a GKE context, or the control plane is unreachable.
        """
        from google.api_core.exceptions import GoogleAPICallError
        from google.auth.exceptions import DefaultCredentialsError

        if self._parsed is None:
            raise ClusterUnreachableError(
                "Cannot determine GKE cluster from context name.",
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_6(self) -> GKEClusterStatus:
        """Fetch live GKE cluster metadata.

        Raises ClusterUnreachableError when credentials are missing, the
        context is not a GKE context, or the control plane is unreachable.
        """
        from google.api_core.exceptions import GoogleAPICallError
        from google.auth.exceptions import DefaultCredentialsError

        if self._parsed is None:
            raise ClusterUnreachableError(
                "XXCannot determine GKE cluster from context name.XX",
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_7(self) -> GKEClusterStatus:
        """Fetch live GKE cluster metadata.

        Raises ClusterUnreachableError when credentials are missing, the
        context is not a GKE context, or the control plane is unreachable.
        """
        from google.api_core.exceptions import GoogleAPICallError
        from google.auth.exceptions import DefaultCredentialsError

        if self._parsed is None:
            raise ClusterUnreachableError(
                "cannot determine gke cluster from context name.",
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_8(self) -> GKEClusterStatus:
        """Fetch live GKE cluster metadata.

        Raises ClusterUnreachableError when credentials are missing, the
        context is not a GKE context, or the control plane is unreachable.
        """
        from google.api_core.exceptions import GoogleAPICallError
        from google.auth.exceptions import DefaultCredentialsError

        if self._parsed is None:
            raise ClusterUnreachableError(
                "CANNOT DETERMINE GKE CLUSTER FROM CONTEXT NAME.",
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_9(self) -> GKEClusterStatus:
        """Fetch live GKE cluster metadata.

        Raises ClusterUnreachableError when credentials are missing, the
        context is not a GKE context, or the control plane is unreachable.
        """
        from google.api_core.exceptions import GoogleAPICallError
        from google.auth.exceptions import DefaultCredentialsError

        if self._parsed is None:
            raise ClusterUnreachableError(
                "Cannot determine GKE cluster from context name.",
                context={"XXcontextXX": self._context["name"]},
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_10(self) -> GKEClusterStatus:
        """Fetch live GKE cluster metadata.

        Raises ClusterUnreachableError when credentials are missing, the
        context is not a GKE context, or the control plane is unreachable.
        """
        from google.api_core.exceptions import GoogleAPICallError
        from google.auth.exceptions import DefaultCredentialsError

        if self._parsed is None:
            raise ClusterUnreachableError(
                "Cannot determine GKE cluster from context name.",
                context={"CONTEXT": self._context["name"]},
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_11(self) -> GKEClusterStatus:
        """Fetch live GKE cluster metadata.

        Raises ClusterUnreachableError when credentials are missing, the
        context is not a GKE context, or the control plane is unreachable.
        """
        from google.api_core.exceptions import GoogleAPICallError
        from google.auth.exceptions import DefaultCredentialsError

        if self._parsed is None:
            raise ClusterUnreachableError(
                "Cannot determine GKE cluster from context name.",
                context={"context": self._context["XXnameXX"]},
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_12(self) -> GKEClusterStatus:
        """Fetch live GKE cluster metadata.

        Raises ClusterUnreachableError when credentials are missing, the
        context is not a GKE context, or the control plane is unreachable.
        """
        from google.api_core.exceptions import GoogleAPICallError
        from google.auth.exceptions import DefaultCredentialsError

        if self._parsed is None:
            raise ClusterUnreachableError(
                "Cannot determine GKE cluster from context name.",
                context={"context": self._context["NAME"]},
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_13(self) -> GKEClusterStatus:
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

        resource_name = None
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_14(self) -> GKEClusterStatus:
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
            f"projects/{self._parsed['XXproject_idXX']}"
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_15(self) -> GKEClusterStatus:
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
            f"projects/{self._parsed['PROJECT_ID']}"
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_16(self) -> GKEClusterStatus:
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
            f"/locations/{self._parsed['XXregionXX']}"
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_17(self) -> GKEClusterStatus:
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
            f"/locations/{self._parsed['REGION']}"
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_18(self) -> GKEClusterStatus:
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
            f"/clusters/{self._parsed['XXclusterXX']}"
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_19(self) -> GKEClusterStatus:
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
            f"/clusters/{self._parsed['CLUSTER']}"
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_20(self) -> GKEClusterStatus:
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
            cluster = None
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_21(self) -> GKEClusterStatus:
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
            cluster = self._client_or_create().get_cluster(name=None)
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_22(self) -> GKEClusterStatus:
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
                None,
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_23(self) -> GKEClusterStatus:
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
                context=None,
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_24(self) -> GKEClusterStatus:
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_25(self) -> GKEClusterStatus:
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_26(self) -> GKEClusterStatus:
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
                context={"XXclusterXX": self._parsed["cluster"]},
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_27(self) -> GKEClusterStatus:
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
                context={"CLUSTER": self._parsed["cluster"]},
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_28(self) -> GKEClusterStatus:
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
                context={"cluster": self._parsed["XXclusterXX"]},
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_29(self) -> GKEClusterStatus:
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
                context={"cluster": self._parsed["CLUSTER"]},
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

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_30(self) -> GKEClusterStatus:
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
                None,
                context={"cluster": self._parsed["cluster"], "error": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.status),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_31(self) -> GKEClusterStatus:
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
                context=None,
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.status),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_32(self) -> GKEClusterStatus:
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
                context={"cluster": self._parsed["cluster"], "error": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.status),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_33(self) -> GKEClusterStatus:
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
                ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.status),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_34(self) -> GKEClusterStatus:
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
                "XXUnable to reach the GKE control plane.XX",
                context={"cluster": self._parsed["cluster"], "error": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.status),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_35(self) -> GKEClusterStatus:
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
                "unable to reach the gke control plane.",
                context={"cluster": self._parsed["cluster"], "error": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.status),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_36(self) -> GKEClusterStatus:
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
                "UNABLE TO REACH THE GKE CONTROL PLANE.",
                context={"cluster": self._parsed["cluster"], "error": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.status),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_37(self) -> GKEClusterStatus:
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
                context={"XXclusterXX": self._parsed["cluster"], "error": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.status),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_38(self) -> GKEClusterStatus:
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
                context={"CLUSTER": self._parsed["cluster"], "error": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.status),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_39(self) -> GKEClusterStatus:
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
                context={"cluster": self._parsed["XXclusterXX"], "error": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.status),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_40(self) -> GKEClusterStatus:
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
                context={"cluster": self._parsed["CLUSTER"], "error": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.status),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_41(self) -> GKEClusterStatus:
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
                context={"cluster": self._parsed["cluster"], "XXerrorXX": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.status),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_42(self) -> GKEClusterStatus:
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
                context={"cluster": self._parsed["cluster"], "ERROR": str(exc)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.status),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_43(self) -> GKEClusterStatus:
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
                context={"cluster": self._parsed["cluster"], "error": str(None)},
            ) from exc

        return {
            "name": str(cluster.name),
            "status": str(cluster.status),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_44(self) -> GKEClusterStatus:
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
            "XXnameXX": str(cluster.name),
            "status": str(cluster.status),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_45(self) -> GKEClusterStatus:
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
            "NAME": str(cluster.name),
            "status": str(cluster.status),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_46(self) -> GKEClusterStatus:
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
            "name": str(None),
            "status": str(cluster.status),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_47(self) -> GKEClusterStatus:
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
            "XXstatusXX": str(cluster.status),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_48(self) -> GKEClusterStatus:
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
            "STATUS": str(cluster.status),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_49(self) -> GKEClusterStatus:
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
            "status": str(None),
            "version": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_50(self) -> GKEClusterStatus:
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
            "XXversionXX": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_51(self) -> GKEClusterStatus:
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
            "VERSION": str(cluster.current_master_version),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_52(self) -> GKEClusterStatus:
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
            "version": str(None),
            "endpoint": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_53(self) -> GKEClusterStatus:
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
            "XXendpointXX": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_54(self) -> GKEClusterStatus:
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
            "ENDPOINT": str(cluster.endpoint),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_55(self) -> GKEClusterStatus:
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
            "endpoint": str(None),
            "location": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_56(self) -> GKEClusterStatus:
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
            "XXlocationXX": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_57(self) -> GKEClusterStatus:
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
            "LOCATION": str(cluster.location),
        }

    def xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_58(self) -> GKEClusterStatus:
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
            "location": str(None),
        }

    # ── K8sPort ───────────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁGCPGKEAdapterǁlist_pods__mutmut)
    def list_pods(self, namespace: str | None = None) -> list[PodInfo]:
        return self._delegate().list_pods(namespace)

    # ── K8sPort ───────────────────────────────────────────────

    def xǁGCPGKEAdapterǁlist_pods__mutmut_orig(self, namespace: str | None = None) -> list[PodInfo]:
        return self._delegate().list_pods(namespace)

    # ── K8sPort ───────────────────────────────────────────────

    def xǁGCPGKEAdapterǁlist_pods__mutmut_1(self, namespace: str | None = None) -> list[PodInfo]:
        return self._delegate().list_pods(None)

    def list_namespaces(self) -> list[NamespaceInfo]:
        return self._delegate().list_namespaces()

    def get_cluster_metrics(self) -> ClusterMetrics:
        return self._delegate().get_cluster_metrics()

    @_mutmut_mutated(mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut)
    def get_cluster_context(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "gcp",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_orig(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "gcp",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_1(self) -> ClusterContext:
        return {
            "XXnameXX": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "gcp",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_2(self) -> ClusterContext:
        return {
            "NAME": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "gcp",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_3(self) -> ClusterContext:
        return {
            "name": self._context["XXnameXX"],
            "cluster": self._cluster_short_name(),
            "provider": "gcp",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_4(self) -> ClusterContext:
        return {
            "name": self._context["NAME"],
            "cluster": self._cluster_short_name(),
            "provider": "gcp",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_5(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "XXclusterXX": self._cluster_short_name(),
            "provider": "gcp",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_6(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "CLUSTER": self._cluster_short_name(),
            "provider": "gcp",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_7(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "XXproviderXX": "gcp",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_8(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "PROVIDER": "gcp",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_9(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "XXgcpXX",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_10(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "GCP",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_11(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "gcp",
            "XXnamespaceXX": self._context.get("namespace", "default"),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_12(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "gcp",
            "NAMESPACE": self._context.get("namespace", "default"),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_13(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "gcp",
            "namespace": self._context.get(None, "default"),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_14(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "gcp",
            "namespace": self._context.get("namespace", None),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_15(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "gcp",
            "namespace": self._context.get("default"),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_16(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "gcp",
            "namespace": self._context.get("namespace", ),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_17(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "gcp",
            "namespace": self._context.get("XXnamespaceXX", "default"),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_18(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "gcp",
            "namespace": self._context.get("NAMESPACE", "default"),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_19(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "gcp",
            "namespace": self._context.get("namespace", "XXdefaultXX"),
        }

    def xǁGCPGKEAdapterǁget_cluster_context__mutmut_20(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "gcp",
            "namespace": self._context.get("namespace", "DEFAULT"),
        }

    # ── Helpers ───────────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁGCPGKEAdapterǁ_delegate__mutmut)
    def _delegate(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["name"])
        return self._k8s_delegate

    # ── Helpers ───────────────────────────────────────────────

    def xǁGCPGKEAdapterǁ_delegate__mutmut_orig(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["name"])
        return self._k8s_delegate

    # ── Helpers ───────────────────────────────────────────────

    def xǁGCPGKEAdapterǁ_delegate__mutmut_1(self) -> K8sPort:
        if self._k8s_delegate is not None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["name"])
        return self._k8s_delegate

    # ── Helpers ───────────────────────────────────────────────

    def xǁGCPGKEAdapterǁ_delegate__mutmut_2(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = None
        return self._k8s_delegate

    # ── Helpers ───────────────────────────────────────────────

    def xǁGCPGKEAdapterǁ_delegate__mutmut_3(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(None)
        return self._k8s_delegate

    # ── Helpers ───────────────────────────────────────────────

    def xǁGCPGKEAdapterǁ_delegate__mutmut_4(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["XXnameXX"])
        return self._k8s_delegate

    # ── Helpers ───────────────────────────────────────────────

    def xǁGCPGKEAdapterǁ_delegate__mutmut_5(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["NAME"])
        return self._k8s_delegate

    @_mutmut_mutated(mutants_xǁGCPGKEAdapterǁ_client_or_create__mutmut)
    def _client_or_create(self) -> GKEClient:
        client = self._gke_client
        if client is None:
            from google.cloud import container_v1

            client = cast(GKEClient, container_v1.ClusterManagerClient())
            self._gke_client = client
        return client

    def xǁGCPGKEAdapterǁ_client_or_create__mutmut_orig(self) -> GKEClient:
        client = self._gke_client
        if client is None:
            from google.cloud import container_v1

            client = cast(GKEClient, container_v1.ClusterManagerClient())
            self._gke_client = client
        return client

    def xǁGCPGKEAdapterǁ_client_or_create__mutmut_1(self) -> GKEClient:
        client = None
        if client is None:
            from google.cloud import container_v1

            client = cast(GKEClient, container_v1.ClusterManagerClient())
            self._gke_client = client
        return client

    def xǁGCPGKEAdapterǁ_client_or_create__mutmut_2(self) -> GKEClient:
        client = self._gke_client
        if client is not None:
            from google.cloud import container_v1

            client = cast(GKEClient, container_v1.ClusterManagerClient())
            self._gke_client = client
        return client

    def xǁGCPGKEAdapterǁ_client_or_create__mutmut_3(self) -> GKEClient:
        client = self._gke_client
        if client is None:
            from google.cloud import container_v1

            client = None
            self._gke_client = client
        return client

    def xǁGCPGKEAdapterǁ_client_or_create__mutmut_4(self) -> GKEClient:
        client = self._gke_client
        if client is None:
            from google.cloud import container_v1

            client = cast(None, container_v1.ClusterManagerClient())
            self._gke_client = client
        return client

    def xǁGCPGKEAdapterǁ_client_or_create__mutmut_5(self) -> GKEClient:
        client = self._gke_client
        if client is None:
            from google.cloud import container_v1

            client = cast(GKEClient, None)
            self._gke_client = client
        return client

    def xǁGCPGKEAdapterǁ_client_or_create__mutmut_6(self) -> GKEClient:
        client = self._gke_client
        if client is None:
            from google.cloud import container_v1

            client = cast(container_v1.ClusterManagerClient())
            self._gke_client = client
        return client

    def xǁGCPGKEAdapterǁ_client_or_create__mutmut_7(self) -> GKEClient:
        client = self._gke_client
        if client is None:
            from google.cloud import container_v1

            client = cast(GKEClient, )
            self._gke_client = client
        return client

    def xǁGCPGKEAdapterǁ_client_or_create__mutmut_8(self) -> GKEClient:
        client = self._gke_client
        if client is None:
            from google.cloud import container_v1

            client = cast(GKEClient, container_v1.ClusterManagerClient())
            self._gke_client = None
        return client

    @_mutmut_mutated(mutants_xǁGCPGKEAdapterǁ_cluster_short_name__mutmut)
    def _cluster_short_name(self) -> str:
        if self._parsed:
            return self._parsed["cluster"]
        return self._context.get("cluster") or self._context["name"]

    def xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_orig(self) -> str:
        if self._parsed:
            return self._parsed["cluster"]
        return self._context.get("cluster") or self._context["name"]

    def xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_1(self) -> str:
        if self._parsed:
            return self._parsed["XXclusterXX"]
        return self._context.get("cluster") or self._context["name"]

    def xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_2(self) -> str:
        if self._parsed:
            return self._parsed["CLUSTER"]
        return self._context.get("cluster") or self._context["name"]

    def xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_3(self) -> str:
        if self._parsed:
            return self._parsed["cluster"]
        return self._context.get("cluster") and self._context["name"]

    def xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_4(self) -> str:
        if self._parsed:
            return self._parsed["cluster"]
        return self._context.get(None) or self._context["name"]

    def xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_5(self) -> str:
        if self._parsed:
            return self._parsed["cluster"]
        return self._context.get("XXclusterXX") or self._context["name"]

    def xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_6(self) -> str:
        if self._parsed:
            return self._parsed["cluster"]
        return self._context.get("CLUSTER") or self._context["name"]

    def xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_7(self) -> str:
        if self._parsed:
            return self._parsed["cluster"]
        return self._context.get("cluster") or self._context["XXnameXX"]

    def xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_8(self) -> str:
        if self._parsed:
            return self._parsed["cluster"]
        return self._context.get("cluster") or self._context["NAME"]

mutants_xǁGCPGKEAdapterǁ__init____mutmut['_mutmut_orig'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ__init____mutmut['xǁGCPGKEAdapterǁ__init____mutmut_1'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ__init____mutmut['xǁGCPGKEAdapterǁ__init____mutmut_2'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ__init____mutmut['xǁGCPGKEAdapterǁ__init____mutmut_3'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ__init____mutmut['xǁGCPGKEAdapterǁ__init____mutmut_4'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ__init____mutmut['xǁGCPGKEAdapterǁ__init____mutmut_5'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ__init____mutmut['xǁGCPGKEAdapterǁ__init____mutmut_6'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ__init____mutmut['xǁGCPGKEAdapterǁ__init____mutmut_7'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ__init____mutmut['xǁGCPGKEAdapterǁ__init____mutmut_8'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ__init____mutmut_8 # type: ignore # mutmut generated

mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['_mutmut_orig'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_1'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_2'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_3'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_4'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_5'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_6'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_7'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_8'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_9'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_10'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_11'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_12'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_13'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_14'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_15'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_16'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_17'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_18'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_19'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_20'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_21'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_22'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_23'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_24'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_25'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_26'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_27'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_28'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_29'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_30'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_31'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_32'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_33'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_34'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_35'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_36'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_37'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_38'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_38 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_39'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_39 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_40'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_40 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_41'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_41 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_42'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_42 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_43'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_43 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_44'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_44 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_45'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_45 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_46'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_46 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_47'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_47 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_48'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_48 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_49'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_49 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_50'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_50 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_51'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_51 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_52'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_52 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_53'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_53 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_54'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_54 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_55'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_55 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_56'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_56 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_57'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_57 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut['xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_58'] = GCPGKEAdapter.xǁGCPGKEAdapterǁdescribe_cluster_status__mutmut_58 # type: ignore # mutmut generated

mutants_xǁGCPGKEAdapterǁlist_pods__mutmut['_mutmut_orig'] = GCPGKEAdapter.xǁGCPGKEAdapterǁlist_pods__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁlist_pods__mutmut['xǁGCPGKEAdapterǁlist_pods__mutmut_1'] = GCPGKEAdapter.xǁGCPGKEAdapterǁlist_pods__mutmut_1 # type: ignore # mutmut generated

mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['_mutmut_orig'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['xǁGCPGKEAdapterǁget_cluster_context__mutmut_1'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['xǁGCPGKEAdapterǁget_cluster_context__mutmut_2'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['xǁGCPGKEAdapterǁget_cluster_context__mutmut_3'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['xǁGCPGKEAdapterǁget_cluster_context__mutmut_4'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['xǁGCPGKEAdapterǁget_cluster_context__mutmut_5'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['xǁGCPGKEAdapterǁget_cluster_context__mutmut_6'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['xǁGCPGKEAdapterǁget_cluster_context__mutmut_7'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['xǁGCPGKEAdapterǁget_cluster_context__mutmut_8'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['xǁGCPGKEAdapterǁget_cluster_context__mutmut_9'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['xǁGCPGKEAdapterǁget_cluster_context__mutmut_10'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['xǁGCPGKEAdapterǁget_cluster_context__mutmut_11'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['xǁGCPGKEAdapterǁget_cluster_context__mutmut_12'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['xǁGCPGKEAdapterǁget_cluster_context__mutmut_13'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['xǁGCPGKEAdapterǁget_cluster_context__mutmut_14'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['xǁGCPGKEAdapterǁget_cluster_context__mutmut_15'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['xǁGCPGKEAdapterǁget_cluster_context__mutmut_16'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['xǁGCPGKEAdapterǁget_cluster_context__mutmut_17'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['xǁGCPGKEAdapterǁget_cluster_context__mutmut_18'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['xǁGCPGKEAdapterǁget_cluster_context__mutmut_19'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁget_cluster_context__mutmut['xǁGCPGKEAdapterǁget_cluster_context__mutmut_20'] = GCPGKEAdapter.xǁGCPGKEAdapterǁget_cluster_context__mutmut_20 # type: ignore # mutmut generated

mutants_xǁGCPGKEAdapterǁ_delegate__mutmut['_mutmut_orig'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_delegate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_delegate__mutmut['xǁGCPGKEAdapterǁ_delegate__mutmut_1'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_delegate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_delegate__mutmut['xǁGCPGKEAdapterǁ_delegate__mutmut_2'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_delegate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_delegate__mutmut['xǁGCPGKEAdapterǁ_delegate__mutmut_3'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_delegate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_delegate__mutmut['xǁGCPGKEAdapterǁ_delegate__mutmut_4'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_delegate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_delegate__mutmut['xǁGCPGKEAdapterǁ_delegate__mutmut_5'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_delegate__mutmut_5 # type: ignore # mutmut generated

mutants_xǁGCPGKEAdapterǁ_client_or_create__mutmut['_mutmut_orig'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_client_or_create__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_client_or_create__mutmut['xǁGCPGKEAdapterǁ_client_or_create__mutmut_1'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_client_or_create__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_client_or_create__mutmut['xǁGCPGKEAdapterǁ_client_or_create__mutmut_2'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_client_or_create__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_client_or_create__mutmut['xǁGCPGKEAdapterǁ_client_or_create__mutmut_3'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_client_or_create__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_client_or_create__mutmut['xǁGCPGKEAdapterǁ_client_or_create__mutmut_4'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_client_or_create__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_client_or_create__mutmut['xǁGCPGKEAdapterǁ_client_or_create__mutmut_5'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_client_or_create__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_client_or_create__mutmut['xǁGCPGKEAdapterǁ_client_or_create__mutmut_6'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_client_or_create__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_client_or_create__mutmut['xǁGCPGKEAdapterǁ_client_or_create__mutmut_7'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_client_or_create__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_client_or_create__mutmut['xǁGCPGKEAdapterǁ_client_or_create__mutmut_8'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_client_or_create__mutmut_8 # type: ignore # mutmut generated

mutants_xǁGCPGKEAdapterǁ_cluster_short_name__mutmut['_mutmut_orig'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_cluster_short_name__mutmut['xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_1'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_cluster_short_name__mutmut['xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_2'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_cluster_short_name__mutmut['xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_3'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_cluster_short_name__mutmut['xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_4'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_cluster_short_name__mutmut['xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_5'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_cluster_short_name__mutmut['xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_6'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_cluster_short_name__mutmut['xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_7'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGCPGKEAdapterǁ_cluster_short_name__mutmut['xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_8'] = GCPGKEAdapter.xǁGCPGKEAdapterǁ_cluster_short_name__mutmut_8 # type: ignore # mutmut generated
