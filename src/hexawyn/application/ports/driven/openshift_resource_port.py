from abc import ABC, abstractmethod
from typing import TypedDict


class ProjectInfo(TypedDict):
    name: str
    status: str
    display_name: str


class RouteInfo(TypedDict):
    name: str
    namespace: str
    host: str
    target_service: str
    tls_enabled: bool


class SecurityContextConstraintInfo(TypedDict):
    name: str
    allow_privileged_container: bool
    run_as_user_type: str


class ImageStreamInfo(TypedDict):
    name: str
    namespace: str
    tag_count: int


class OpenShiftResourcePort(ABC):
    """Driven port — reads OpenShift-native resources via the dynamic API.

    Covers the resources that have no vanilla Kubernetes equivalent:
    Projects (Namespaces), Routes (Ingress), SecurityContextConstraints
    (PodSecurityPolicies) and ImageStreams (container registry).
    """

    @abstractmethod
    def list_projects(self) -> list[ProjectInfo]:
        """List OpenShift Projects (the OpenShift form of Namespaces).

        Raises InsufficientPermissionsError on RBAC 403.
        Raises ClusterUnreachableError on other API failures.
        """

    @abstractmethod
    def list_routes(self, namespace: str) -> list[RouteInfo]:
        """List Routes in *namespace* (the OpenShift form of Ingress).

        Raises InsufficientPermissionsError on RBAC 403.
        Raises ClusterUnreachableError on other API failures.
        """

    @abstractmethod
    def list_security_context_constraints(self) -> list[SecurityContextConstraintInfo]:
        """List cluster-wide SecurityContextConstraints (SCCs).

        Raises InsufficientPermissionsError on RBAC 403.
        Raises ClusterUnreachableError on other API failures.
        """

    @abstractmethod
    def list_image_streams(self, namespace: str) -> list[ImageStreamInfo]:
        """List ImageStreams in *namespace* (OpenShift native registry).

        Raises InsufficientPermissionsError on RBAC 403.
        Raises ClusterUnreachableError on other API failures.
        """
