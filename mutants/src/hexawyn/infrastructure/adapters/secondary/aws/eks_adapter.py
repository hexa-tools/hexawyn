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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
mutants_xǁAWSEKSAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAWSEKSAdapterǁlist_pods__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAWSEKSAdapterǁ_delegate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAWSEKSAdapterǁ_cluster_short_name__mutmut: MutantDict = {}  # type: ignore


class AWSEKSAdapter(K8sPort):
    """K8sPort implementation for AWS EKS.

    Kubernetes read operations are delegated to an injected K8sPort (the
    kubeconfig already carries EKS exec authentication after
    `aws eks update-kubeconfig`). AWS-specific behaviour is limited to region
    detection and CloudWatch/EKS metadata via boto3.
    """

    @_mutmut_mutated(mutants_xǁAWSEKSAdapterǁ__init____mutmut)
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

    def xǁAWSEKSAdapterǁ__init____mutmut_orig(
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

    def xǁAWSEKSAdapterǁ__init____mutmut_1(
        self,
        context: ClusterContext,
        k8s_delegate: K8sPort | None = None,
        eks_client: EKSClient | None = None,
        region: str | None = None,
    ) -> None:
        self._context = None
        self._k8s_delegate = k8s_delegate
        self._eks_client = eks_client
        self._region = region

    def xǁAWSEKSAdapterǁ__init____mutmut_2(
        self,
        context: ClusterContext,
        k8s_delegate: K8sPort | None = None,
        eks_client: EKSClient | None = None,
        region: str | None = None,
    ) -> None:
        self._context = context
        self._k8s_delegate = None
        self._eks_client = eks_client
        self._region = region

    def xǁAWSEKSAdapterǁ__init____mutmut_3(
        self,
        context: ClusterContext,
        k8s_delegate: K8sPort | None = None,
        eks_client: EKSClient | None = None,
        region: str | None = None,
    ) -> None:
        self._context = context
        self._k8s_delegate = k8s_delegate
        self._eks_client = None
        self._region = region

    def xǁAWSEKSAdapterǁ__init____mutmut_4(
        self,
        context: ClusterContext,
        k8s_delegate: K8sPort | None = None,
        eks_client: EKSClient | None = None,
        region: str | None = None,
    ) -> None:
        self._context = context
        self._k8s_delegate = k8s_delegate
        self._eks_client = eks_client
        self._region = None

    # ── AWS metadata ──────────────────────────────────────────

    @property
    def region(self) -> str | None:
        if self._region is None:
            self._region = resolve_region(self._context["name"], os.environ)
        return self._region

    @_mutmut_mutated(mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut)
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

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_orig(self) -> EKSClusterStatus:
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

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_1(self) -> EKSClusterStatus:
        """Fetch live EKS cluster metadata.

        Raises ClusterUnreachableError when AWS credentials are missing or the
        EKS control plane cannot be reached.
        """
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = None
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

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_2(self) -> EKSClusterStatus:
        """Fetch live EKS cluster metadata.

        Raises ClusterUnreachableError when AWS credentials are missing or the
        EKS control plane cannot be reached.
        """
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._eks_client_or_create()
        cluster_name = None
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

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_3(self) -> EKSClusterStatus:
        """Fetch live EKS cluster metadata.

        Raises ClusterUnreachableError when AWS credentials are missing or the
        EKS control plane cannot be reached.
        """
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._eks_client_or_create()
        cluster_name = self._cluster_short_name()
        region = None
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

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_4(self) -> EKSClusterStatus:
        """Fetch live EKS cluster metadata.

        Raises ClusterUnreachableError when AWS credentials are missing or the
        EKS control plane cannot be reached.
        """
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._eks_client_or_create()
        cluster_name = self._cluster_short_name()
        region = self.region and "unknown"
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

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_5(self) -> EKSClusterStatus:
        """Fetch live EKS cluster metadata.

        Raises ClusterUnreachableError when AWS credentials are missing or the
        EKS control plane cannot be reached.
        """
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._eks_client_or_create()
        cluster_name = self._cluster_short_name()
        region = self.region or "XXunknownXX"
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

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_6(self) -> EKSClusterStatus:
        """Fetch live EKS cluster metadata.

        Raises ClusterUnreachableError when AWS credentials are missing or the
        EKS control plane cannot be reached.
        """
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._eks_client_or_create()
        cluster_name = self._cluster_short_name()
        region = self.region or "UNKNOWN"
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

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_7(self) -> EKSClusterStatus:
        """Fetch live EKS cluster metadata.

        Raises ClusterUnreachableError when AWS credentials are missing or the
        EKS control plane cannot be reached.
        """
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._eks_client_or_create()
        cluster_name = self._cluster_short_name()
        region = self.region or "unknown"
        try:
            response = None
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

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_8(self) -> EKSClusterStatus:
        """Fetch live EKS cluster metadata.

        Raises ClusterUnreachableError when AWS credentials are missing or the
        EKS control plane cannot be reached.
        """
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._eks_client_or_create()
        cluster_name = self._cluster_short_name()
        region = self.region or "unknown"
        try:
            response = client.describe_cluster(name=None)
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

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_9(self) -> EKSClusterStatus:
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
                None,
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

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_10(self) -> EKSClusterStatus:
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
                context=None,
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

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_11(self) -> EKSClusterStatus:
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

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_12(self) -> EKSClusterStatus:
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

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_13(self) -> EKSClusterStatus:
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
                context={"XXclusterXX": cluster_name, "region": region},
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

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_14(self) -> EKSClusterStatus:
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
                context={"CLUSTER": cluster_name, "region": region},
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

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_15(self) -> EKSClusterStatus:
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
                context={"cluster": cluster_name, "XXregionXX": region},
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

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_16(self) -> EKSClusterStatus:
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
                context={"cluster": cluster_name, "REGION": region},
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

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_17(self) -> EKSClusterStatus:
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
                None,
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

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_18(self) -> EKSClusterStatus:
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
                context=None,
            ) from exc

        cluster = response["cluster"]
        return {
            "name": cluster.get("name", cluster_name),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_19(self) -> EKSClusterStatus:
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

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_20(self) -> EKSClusterStatus:
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
                ) from exc

        cluster = response["cluster"]
        return {
            "name": cluster.get("name", cluster_name),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_21(self) -> EKSClusterStatus:
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
                context={"XXclusterXX": cluster_name, "region": region, "error": str(exc)},
            ) from exc

        cluster = response["cluster"]
        return {
            "name": cluster.get("name", cluster_name),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_22(self) -> EKSClusterStatus:
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
                context={"CLUSTER": cluster_name, "region": region, "error": str(exc)},
            ) from exc

        cluster = response["cluster"]
        return {
            "name": cluster.get("name", cluster_name),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_23(self) -> EKSClusterStatus:
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
                context={"cluster": cluster_name, "XXregionXX": region, "error": str(exc)},
            ) from exc

        cluster = response["cluster"]
        return {
            "name": cluster.get("name", cluster_name),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_24(self) -> EKSClusterStatus:
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
                context={"cluster": cluster_name, "REGION": region, "error": str(exc)},
            ) from exc

        cluster = response["cluster"]
        return {
            "name": cluster.get("name", cluster_name),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_25(self) -> EKSClusterStatus:
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
                context={"cluster": cluster_name, "region": region, "XXerrorXX": str(exc)},
            ) from exc

        cluster = response["cluster"]
        return {
            "name": cluster.get("name", cluster_name),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_26(self) -> EKSClusterStatus:
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
                context={"cluster": cluster_name, "region": region, "ERROR": str(exc)},
            ) from exc

        cluster = response["cluster"]
        return {
            "name": cluster.get("name", cluster_name),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_27(self) -> EKSClusterStatus:
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
                context={"cluster": cluster_name, "region": region, "error": str(None)},
            ) from exc

        cluster = response["cluster"]
        return {
            "name": cluster.get("name", cluster_name),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_28(self) -> EKSClusterStatus:
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

        cluster = None
        return {
            "name": cluster.get("name", cluster_name),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_29(self) -> EKSClusterStatus:
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

        cluster = response["XXclusterXX"]
        return {
            "name": cluster.get("name", cluster_name),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_30(self) -> EKSClusterStatus:
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

        cluster = response["CLUSTER"]
        return {
            "name": cluster.get("name", cluster_name),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_31(self) -> EKSClusterStatus:
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
            "XXnameXX": cluster.get("name", cluster_name),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_32(self) -> EKSClusterStatus:
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
            "NAME": cluster.get("name", cluster_name),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_33(self) -> EKSClusterStatus:
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
            "name": cluster.get(None, cluster_name),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_34(self) -> EKSClusterStatus:
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
            "name": cluster.get("name", None),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_35(self) -> EKSClusterStatus:
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
            "name": cluster.get(cluster_name),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_36(self) -> EKSClusterStatus:
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
            "name": cluster.get("name", ),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_37(self) -> EKSClusterStatus:
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
            "name": cluster.get("XXnameXX", cluster_name),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_38(self) -> EKSClusterStatus:
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
            "name": cluster.get("NAME", cluster_name),
            "status": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_39(self) -> EKSClusterStatus:
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
            "XXstatusXX": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_40(self) -> EKSClusterStatus:
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
            "STATUS": cluster.get("status", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_41(self) -> EKSClusterStatus:
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
            "status": cluster.get(None, "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_42(self) -> EKSClusterStatus:
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
            "status": cluster.get("status", None),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_43(self) -> EKSClusterStatus:
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
            "status": cluster.get("UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_44(self) -> EKSClusterStatus:
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
            "status": cluster.get("status", ),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_45(self) -> EKSClusterStatus:
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
            "status": cluster.get("XXstatusXX", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_46(self) -> EKSClusterStatus:
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
            "status": cluster.get("STATUS", "UNKNOWN"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_47(self) -> EKSClusterStatus:
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
            "status": cluster.get("status", "XXUNKNOWNXX"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_48(self) -> EKSClusterStatus:
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
            "status": cluster.get("status", "unknown"),
            "version": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_49(self) -> EKSClusterStatus:
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
            "XXversionXX": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_50(self) -> EKSClusterStatus:
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
            "VERSION": cluster.get("version", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_51(self) -> EKSClusterStatus:
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
            "version": cluster.get(None, ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_52(self) -> EKSClusterStatus:
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
            "version": cluster.get("version", None),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_53(self) -> EKSClusterStatus:
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
            "version": cluster.get(""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_54(self) -> EKSClusterStatus:
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
            "version": cluster.get("version", ),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_55(self) -> EKSClusterStatus:
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
            "version": cluster.get("XXversionXX", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_56(self) -> EKSClusterStatus:
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
            "version": cluster.get("VERSION", ""),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_57(self) -> EKSClusterStatus:
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
            "version": cluster.get("version", "XXXX"),
            "endpoint": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_58(self) -> EKSClusterStatus:
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
            "XXendpointXX": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_59(self) -> EKSClusterStatus:
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
            "ENDPOINT": cluster.get("endpoint", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_60(self) -> EKSClusterStatus:
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
            "endpoint": cluster.get(None, ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_61(self) -> EKSClusterStatus:
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
            "endpoint": cluster.get("endpoint", None),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_62(self) -> EKSClusterStatus:
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
            "endpoint": cluster.get(""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_63(self) -> EKSClusterStatus:
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
            "endpoint": cluster.get("endpoint", ),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_64(self) -> EKSClusterStatus:
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
            "endpoint": cluster.get("XXendpointXX", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_65(self) -> EKSClusterStatus:
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
            "endpoint": cluster.get("ENDPOINT", ""),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_66(self) -> EKSClusterStatus:
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
            "endpoint": cluster.get("endpoint", "XXXX"),
            "region": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_67(self) -> EKSClusterStatus:
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
            "XXregionXX": region,
        }

    def xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_68(self) -> EKSClusterStatus:
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
            "REGION": region,
        }

    # ── K8sPort ───────────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁAWSEKSAdapterǁlist_pods__mutmut)
    def list_pods(self, namespace: str | None = None) -> list[PodInfo]:
        return self._delegate().list_pods(namespace)

    # ── K8sPort ───────────────────────────────────────────────

    def xǁAWSEKSAdapterǁlist_pods__mutmut_orig(self, namespace: str | None = None) -> list[PodInfo]:
        return self._delegate().list_pods(namespace)

    # ── K8sPort ───────────────────────────────────────────────

    def xǁAWSEKSAdapterǁlist_pods__mutmut_1(self, namespace: str | None = None) -> list[PodInfo]:
        return self._delegate().list_pods(None)

    def list_namespaces(self) -> list[NamespaceInfo]:
        return self._delegate().list_namespaces()

    def get_cluster_metrics(self) -> ClusterMetrics:
        return self._delegate().get_cluster_metrics()

    @_mutmut_mutated(mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut)
    def get_cluster_context(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "aws",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_orig(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "aws",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_1(self) -> ClusterContext:
        return {
            "XXnameXX": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "aws",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_2(self) -> ClusterContext:
        return {
            "NAME": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "aws",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_3(self) -> ClusterContext:
        return {
            "name": self._context["XXnameXX"],
            "cluster": self._cluster_short_name(),
            "provider": "aws",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_4(self) -> ClusterContext:
        return {
            "name": self._context["NAME"],
            "cluster": self._cluster_short_name(),
            "provider": "aws",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_5(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "XXclusterXX": self._cluster_short_name(),
            "provider": "aws",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_6(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "CLUSTER": self._cluster_short_name(),
            "provider": "aws",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_7(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "XXproviderXX": "aws",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_8(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "PROVIDER": "aws",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_9(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "XXawsXX",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_10(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "AWS",
            "namespace": self._context.get("namespace", "default"),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_11(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "aws",
            "XXnamespaceXX": self._context.get("namespace", "default"),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_12(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "aws",
            "NAMESPACE": self._context.get("namespace", "default"),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_13(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "aws",
            "namespace": self._context.get(None, "default"),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_14(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "aws",
            "namespace": self._context.get("namespace", None),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_15(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "aws",
            "namespace": self._context.get("default"),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_16(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "aws",
            "namespace": self._context.get("namespace", ),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_17(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "aws",
            "namespace": self._context.get("XXnamespaceXX", "default"),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_18(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "aws",
            "namespace": self._context.get("NAMESPACE", "default"),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_19(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "aws",
            "namespace": self._context.get("namespace", "XXdefaultXX"),
        }

    def xǁAWSEKSAdapterǁget_cluster_context__mutmut_20(self) -> ClusterContext:
        return {
            "name": self._context["name"],
            "cluster": self._cluster_short_name(),
            "provider": "aws",
            "namespace": self._context.get("namespace", "DEFAULT"),
        }

    # ── Helpers ───────────────────────────────────────────────

    @_mutmut_mutated(mutants_xǁAWSEKSAdapterǁ_delegate__mutmut)
    def _delegate(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["name"])
        return self._k8s_delegate

    # ── Helpers ───────────────────────────────────────────────

    def xǁAWSEKSAdapterǁ_delegate__mutmut_orig(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["name"])
        return self._k8s_delegate

    # ── Helpers ───────────────────────────────────────────────

    def xǁAWSEKSAdapterǁ_delegate__mutmut_1(self) -> K8sPort:
        if self._k8s_delegate is not None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["name"])
        return self._k8s_delegate

    # ── Helpers ───────────────────────────────────────────────

    def xǁAWSEKSAdapterǁ_delegate__mutmut_2(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = None
        return self._k8s_delegate

    # ── Helpers ───────────────────────────────────────────────

    def xǁAWSEKSAdapterǁ_delegate__mutmut_3(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(None)
        return self._k8s_delegate

    # ── Helpers ───────────────────────────────────────────────

    def xǁAWSEKSAdapterǁ_delegate__mutmut_4(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["XXnameXX"])
        return self._k8s_delegate

    # ── Helpers ───────────────────────────────────────────────

    def xǁAWSEKSAdapterǁ_delegate__mutmut_5(self) -> K8sPort:
        if self._k8s_delegate is None:
            from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
                VanillaAdapter,
            )

            self._k8s_delegate = VanillaAdapter(self._context["NAME"])
        return self._k8s_delegate

    @_mutmut_mutated(mutants_xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut)
    def _eks_client_or_create(self) -> EKSClient:
        if self._eks_client is None:
            import boto3

            self._eks_client = boto3.client("eks", region_name=self.region)
        return self._eks_client

    def xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_orig(self) -> EKSClient:
        if self._eks_client is None:
            import boto3

            self._eks_client = boto3.client("eks", region_name=self.region)
        return self._eks_client

    def xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_1(self) -> EKSClient:
        if self._eks_client is not None:
            import boto3

            self._eks_client = boto3.client("eks", region_name=self.region)
        return self._eks_client

    def xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_2(self) -> EKSClient:
        if self._eks_client is None:
            import boto3

            self._eks_client = None
        return self._eks_client

    def xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_3(self) -> EKSClient:
        if self._eks_client is None:
            import boto3

            self._eks_client = boto3.client(None, region_name=self.region)
        return self._eks_client

    def xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_4(self) -> EKSClient:
        if self._eks_client is None:
            import boto3

            self._eks_client = boto3.client("eks", region_name=None)
        return self._eks_client

    def xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_5(self) -> EKSClient:
        if self._eks_client is None:
            import boto3

            self._eks_client = boto3.client(region_name=self.region)
        return self._eks_client

    def xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_6(self) -> EKSClient:
        if self._eks_client is None:
            import boto3

            self._eks_client = boto3.client("eks", )
        return self._eks_client

    def xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_7(self) -> EKSClient:
        if self._eks_client is None:
            import boto3

            self._eks_client = boto3.client("XXeksXX", region_name=self.region)
        return self._eks_client

    def xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_8(self) -> EKSClient:
        if self._eks_client is None:
            import boto3

            self._eks_client = boto3.client("EKS", region_name=self.region)
        return self._eks_client

    @_mutmut_mutated(mutants_xǁAWSEKSAdapterǁ_cluster_short_name__mutmut)
    def _cluster_short_name(self) -> str:
        name = self._context["name"]
        arn_match = _ARN_CLUSTER_NAME_PATTERN.search(name)
        if arn_match:
            return arn_match.group(1)
        return self._context.get("cluster") or name

    def xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_orig(self) -> str:
        name = self._context["name"]
        arn_match = _ARN_CLUSTER_NAME_PATTERN.search(name)
        if arn_match:
            return arn_match.group(1)
        return self._context.get("cluster") or name

    def xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_1(self) -> str:
        name = None
        arn_match = _ARN_CLUSTER_NAME_PATTERN.search(name)
        if arn_match:
            return arn_match.group(1)
        return self._context.get("cluster") or name

    def xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_2(self) -> str:
        name = self._context["XXnameXX"]
        arn_match = _ARN_CLUSTER_NAME_PATTERN.search(name)
        if arn_match:
            return arn_match.group(1)
        return self._context.get("cluster") or name

    def xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_3(self) -> str:
        name = self._context["NAME"]
        arn_match = _ARN_CLUSTER_NAME_PATTERN.search(name)
        if arn_match:
            return arn_match.group(1)
        return self._context.get("cluster") or name

    def xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_4(self) -> str:
        name = self._context["name"]
        arn_match = None
        if arn_match:
            return arn_match.group(1)
        return self._context.get("cluster") or name

    def xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_5(self) -> str:
        name = self._context["name"]
        arn_match = _ARN_CLUSTER_NAME_PATTERN.search(None)
        if arn_match:
            return arn_match.group(1)
        return self._context.get("cluster") or name

    def xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_6(self) -> str:
        name = self._context["name"]
        arn_match = _ARN_CLUSTER_NAME_PATTERN.search(name)
        if arn_match:
            return arn_match.group(None)
        return self._context.get("cluster") or name

    def xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_7(self) -> str:
        name = self._context["name"]
        arn_match = _ARN_CLUSTER_NAME_PATTERN.search(name)
        if arn_match:
            return arn_match.group(2)
        return self._context.get("cluster") or name

    def xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_8(self) -> str:
        name = self._context["name"]
        arn_match = _ARN_CLUSTER_NAME_PATTERN.search(name)
        if arn_match:
            return arn_match.group(1)
        return self._context.get("cluster") and name

    def xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_9(self) -> str:
        name = self._context["name"]
        arn_match = _ARN_CLUSTER_NAME_PATTERN.search(name)
        if arn_match:
            return arn_match.group(1)
        return self._context.get(None) or name

    def xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_10(self) -> str:
        name = self._context["name"]
        arn_match = _ARN_CLUSTER_NAME_PATTERN.search(name)
        if arn_match:
            return arn_match.group(1)
        return self._context.get("XXclusterXX") or name

    def xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_11(self) -> str:
        name = self._context["name"]
        arn_match = _ARN_CLUSTER_NAME_PATTERN.search(name)
        if arn_match:
            return arn_match.group(1)
        return self._context.get("CLUSTER") or name

mutants_xǁAWSEKSAdapterǁ__init____mutmut['_mutmut_orig'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ__init____mutmut['xǁAWSEKSAdapterǁ__init____mutmut_1'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ__init____mutmut['xǁAWSEKSAdapterǁ__init____mutmut_2'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ__init____mutmut['xǁAWSEKSAdapterǁ__init____mutmut_3'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ__init____mutmut['xǁAWSEKSAdapterǁ__init____mutmut_4'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ__init____mutmut_4 # type: ignore # mutmut generated

mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['_mutmut_orig'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_1'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_2'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_3'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_4'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_5'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_6'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_7'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_8'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_9'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_10'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_11'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_12'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_13'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_14'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_15'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_16'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_17'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_18'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_19'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_20'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_21'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_22'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_23'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_24'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_25'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_26'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_27'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_28'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_29'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_30'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_31'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_32'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_33'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_34'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_35'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_36'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_37'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_38'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_39'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_40'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_40 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_41'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_41 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_42'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_42 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_43'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_43 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_44'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_44 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_45'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_45 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_46'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_46 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_47'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_47 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_48'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_48 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_49'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_49 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_50'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_50 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_51'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_51 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_52'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_52 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_53'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_53 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_54'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_54 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_55'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_55 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_56'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_56 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_57'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_57 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_58'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_58 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_59'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_59 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_60'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_60 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_61'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_61 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_62'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_62 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_63'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_63 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_64'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_64 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_65'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_65 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_66'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_66 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_67'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_67 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut['xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_68'] = AWSEKSAdapter.xǁAWSEKSAdapterǁdescribe_cluster_status__mutmut_68 # type: ignore # mutmut generated

mutants_xǁAWSEKSAdapterǁlist_pods__mutmut['_mutmut_orig'] = AWSEKSAdapter.xǁAWSEKSAdapterǁlist_pods__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁlist_pods__mutmut['xǁAWSEKSAdapterǁlist_pods__mutmut_1'] = AWSEKSAdapter.xǁAWSEKSAdapterǁlist_pods__mutmut_1 # type: ignore # mutmut generated

mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['_mutmut_orig'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['xǁAWSEKSAdapterǁget_cluster_context__mutmut_1'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['xǁAWSEKSAdapterǁget_cluster_context__mutmut_2'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['xǁAWSEKSAdapterǁget_cluster_context__mutmut_3'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['xǁAWSEKSAdapterǁget_cluster_context__mutmut_4'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['xǁAWSEKSAdapterǁget_cluster_context__mutmut_5'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['xǁAWSEKSAdapterǁget_cluster_context__mutmut_6'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['xǁAWSEKSAdapterǁget_cluster_context__mutmut_7'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['xǁAWSEKSAdapterǁget_cluster_context__mutmut_8'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['xǁAWSEKSAdapterǁget_cluster_context__mutmut_9'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['xǁAWSEKSAdapterǁget_cluster_context__mutmut_10'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['xǁAWSEKSAdapterǁget_cluster_context__mutmut_11'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['xǁAWSEKSAdapterǁget_cluster_context__mutmut_12'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['xǁAWSEKSAdapterǁget_cluster_context__mutmut_13'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['xǁAWSEKSAdapterǁget_cluster_context__mutmut_14'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['xǁAWSEKSAdapterǁget_cluster_context__mutmut_15'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['xǁAWSEKSAdapterǁget_cluster_context__mutmut_16'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['xǁAWSEKSAdapterǁget_cluster_context__mutmut_17'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['xǁAWSEKSAdapterǁget_cluster_context__mutmut_18'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['xǁAWSEKSAdapterǁget_cluster_context__mutmut_19'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁget_cluster_context__mutmut['xǁAWSEKSAdapterǁget_cluster_context__mutmut_20'] = AWSEKSAdapter.xǁAWSEKSAdapterǁget_cluster_context__mutmut_20 # type: ignore # mutmut generated

mutants_xǁAWSEKSAdapterǁ_delegate__mutmut['_mutmut_orig'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_delegate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_delegate__mutmut['xǁAWSEKSAdapterǁ_delegate__mutmut_1'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_delegate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_delegate__mutmut['xǁAWSEKSAdapterǁ_delegate__mutmut_2'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_delegate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_delegate__mutmut['xǁAWSEKSAdapterǁ_delegate__mutmut_3'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_delegate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_delegate__mutmut['xǁAWSEKSAdapterǁ_delegate__mutmut_4'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_delegate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_delegate__mutmut['xǁAWSEKSAdapterǁ_delegate__mutmut_5'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_delegate__mutmut_5 # type: ignore # mutmut generated

mutants_xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut['_mutmut_orig'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut['xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_1'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut['xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_2'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut['xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_3'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut['xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_4'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut['xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_5'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut['xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_6'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut['xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_7'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut['xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_8'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_eks_client_or_create__mutmut_8 # type: ignore # mutmut generated

mutants_xǁAWSEKSAdapterǁ_cluster_short_name__mutmut['_mutmut_orig'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_cluster_short_name__mutmut['xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_1'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_cluster_short_name__mutmut['xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_2'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_cluster_short_name__mutmut['xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_3'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_cluster_short_name__mutmut['xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_4'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_cluster_short_name__mutmut['xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_5'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_cluster_short_name__mutmut['xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_6'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_cluster_short_name__mutmut['xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_7'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_cluster_short_name__mutmut['xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_8'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_cluster_short_name__mutmut['xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_9'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_cluster_short_name__mutmut['xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_10'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAWSEKSAdapterǁ_cluster_short_name__mutmut['xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_11'] = AWSEKSAdapter.xǁAWSEKSAdapterǁ_cluster_short_name__mutmut_11 # type: ignore # mutmut generated
