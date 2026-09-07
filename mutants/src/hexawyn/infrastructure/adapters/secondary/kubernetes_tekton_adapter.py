from __future__ import annotations

from collections.abc import Mapping
from datetime import UTC, datetime

from hexawyn.application.ports.driven.tekton_pipeline_status_port import (
    PipelineRunRecord,
    TektonPipelineStatusPort,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    ComponentNotInstalledError,
    InsufficientPermissionsError,
)

_TEKTON_GROUP = "tekton.dev"
_TEKTON_VERSION = "v1"
_PIPELINERUNS_PLURAL = "pipelineruns"
_K8S_FORBIDDEN = 403
_K8S_NOT_FOUND = 404


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut: MutantDict = {}  # type: ignore


class KubernetesTektonAdapter(TektonPipelineStatusPort):
    """Secondary adapter — reads Tekton PipelineRun CRDs from the K8s API."""

    @_mutmut_mutated(mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut)
    def list_pipeline_runs(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_orig(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_1(self, namespace: str, limit: int = 501) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_2(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = None
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_3(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = None
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_4(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=None,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_5(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=None,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_6(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=None,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_7(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=None,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_8(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=None,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_9(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_10(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_11(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_12(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_13(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_14(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = None
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_15(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(None, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_16(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, None, None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_17(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr("status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_18(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_19(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", )
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_20(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "XXstatusXX", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_21(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "STATUS", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_22(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status != _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_23(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    None,
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_24(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context=None,
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_25(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_26(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_27(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"XXnamespaceXX": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_28(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"NAMESPACE": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_29(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status != _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_30(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    None, "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_31(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", None
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_32(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_33(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_34(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "XXTektonXX", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_35(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_36(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "TEKTON", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_37(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "XXhttps://tekton.dev/docs/installation/XX"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_38(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "HTTPS://TEKTON.DEV/DOCS/INSTALLATION/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_39(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                None
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_40(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = None
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_41(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") and [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_42(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get(None) or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_43(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("XXitemsXX") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_44(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("ITEMS") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]

    def xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_45(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(None) for item in items]

mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['_mutmut_orig'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_1'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_2'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_3'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_4'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_5'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_6'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_7'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_8'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_9'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_10'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_11'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_12'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_13'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_14'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_15'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_16'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_17'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_18'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_19'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_20'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_21'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_22'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_23'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_24'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_25'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_26'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_27'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_28'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_29'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_30'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_31'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_32'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_32 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_33'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_33 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_34'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_34 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_35'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_35 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_36'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_36 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_37'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_37 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_38'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_38 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_39'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_39 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_40'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_40 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_41'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_41 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_42'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_42 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_43'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_43 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_44'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_44 # type: ignore # mutmut generated
mutants_xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut['xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_45'] = KubernetesTektonAdapter.xǁKubernetesTektonAdapterǁlist_pipeline_runs__mutmut_45 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__extract_status__mutmut)
def _extract_status(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_orig(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_1(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is not None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_2(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "XXNotStartedXX", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_3(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "notstarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_4(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NOTSTARTED", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_5(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = None
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_6(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get(None)
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_7(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("XXconditionsXX")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_8(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("CONDITIONS")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_9(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) and not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_10(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_11(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_12(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "XXNotStartedXX", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_13(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "notstarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_14(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NOTSTARTED", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_15(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = None
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_16(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[1]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_17(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_18(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "XXNotStartedXX", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_19(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "notstarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_20(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NOTSTARTED", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_21(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = None
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_22(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = None
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_23(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(None)
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_24(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get(None, "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_25(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", None))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_26(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_27(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", ))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_28(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("XXstatusXX", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_29(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("STATUS", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_30(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "XXUnknownXX"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_31(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_32(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "UNKNOWN"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_33(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = None
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_34(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(None)
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_35(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get(None, ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_36(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", None))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_37(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get(""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_38(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_39(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("XXreasonXX", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_40(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("REASON", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_41(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", "XXXX"))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_42(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded != "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_43(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "XXTrueXX":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_44(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "true":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_45(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "TRUE":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_46(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "XXSucceededXX", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_47(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_48(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "SUCCEEDED", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_49(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded != "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_50(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "XXFalseXX":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_51(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "false":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_52(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "FALSE":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_53(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason not in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_54(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("XXCancelledXX", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_55(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_56(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("CANCELLED", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_57(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "XXPipelineRunCancelledXX"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_58(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "pipelineruncancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_59(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PIPELINERUNCANCELLED"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_60(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "XXCancelledXX", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_61(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_62(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "CANCELLED", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_63(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "XXFailedXX", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_64(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_65(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "FAILED", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_66(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason and None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_67(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" or reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_68(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded != "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_69(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "XXUnknownXX" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_70(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_71(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "UNKNOWN" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_72(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason != "Running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_73(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "XXRunningXX":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_74(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "running":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_75(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "RUNNING":
        return "Running", None
    return "NotStarted", None


def x__extract_status__mutmut_76(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "XXRunningXX", None
    return "NotStarted", None


def x__extract_status__mutmut_77(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "running", None
    return "NotStarted", None


def x__extract_status__mutmut_78(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "RUNNING", None
    return "NotStarted", None


def x__extract_status__mutmut_79(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "XXNotStartedXX", None


def x__extract_status__mutmut_80(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "notstarted", None


def x__extract_status__mutmut_81(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NOTSTARTED", None

mutants_x__extract_status__mutmut['_mutmut_orig'] = x__extract_status__mutmut_orig # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_1'] = x__extract_status__mutmut_1 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_2'] = x__extract_status__mutmut_2 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_3'] = x__extract_status__mutmut_3 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_4'] = x__extract_status__mutmut_4 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_5'] = x__extract_status__mutmut_5 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_6'] = x__extract_status__mutmut_6 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_7'] = x__extract_status__mutmut_7 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_8'] = x__extract_status__mutmut_8 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_9'] = x__extract_status__mutmut_9 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_10'] = x__extract_status__mutmut_10 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_11'] = x__extract_status__mutmut_11 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_12'] = x__extract_status__mutmut_12 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_13'] = x__extract_status__mutmut_13 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_14'] = x__extract_status__mutmut_14 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_15'] = x__extract_status__mutmut_15 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_16'] = x__extract_status__mutmut_16 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_17'] = x__extract_status__mutmut_17 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_18'] = x__extract_status__mutmut_18 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_19'] = x__extract_status__mutmut_19 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_20'] = x__extract_status__mutmut_20 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_21'] = x__extract_status__mutmut_21 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_22'] = x__extract_status__mutmut_22 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_23'] = x__extract_status__mutmut_23 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_24'] = x__extract_status__mutmut_24 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_25'] = x__extract_status__mutmut_25 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_26'] = x__extract_status__mutmut_26 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_27'] = x__extract_status__mutmut_27 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_28'] = x__extract_status__mutmut_28 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_29'] = x__extract_status__mutmut_29 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_30'] = x__extract_status__mutmut_30 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_31'] = x__extract_status__mutmut_31 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_32'] = x__extract_status__mutmut_32 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_33'] = x__extract_status__mutmut_33 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_34'] = x__extract_status__mutmut_34 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_35'] = x__extract_status__mutmut_35 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_36'] = x__extract_status__mutmut_36 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_37'] = x__extract_status__mutmut_37 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_38'] = x__extract_status__mutmut_38 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_39'] = x__extract_status__mutmut_39 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_40'] = x__extract_status__mutmut_40 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_41'] = x__extract_status__mutmut_41 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_42'] = x__extract_status__mutmut_42 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_43'] = x__extract_status__mutmut_43 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_44'] = x__extract_status__mutmut_44 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_45'] = x__extract_status__mutmut_45 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_46'] = x__extract_status__mutmut_46 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_47'] = x__extract_status__mutmut_47 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_48'] = x__extract_status__mutmut_48 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_49'] = x__extract_status__mutmut_49 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_50'] = x__extract_status__mutmut_50 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_51'] = x__extract_status__mutmut_51 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_52'] = x__extract_status__mutmut_52 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_53'] = x__extract_status__mutmut_53 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_54'] = x__extract_status__mutmut_54 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_55'] = x__extract_status__mutmut_55 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_56'] = x__extract_status__mutmut_56 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_57'] = x__extract_status__mutmut_57 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_58'] = x__extract_status__mutmut_58 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_59'] = x__extract_status__mutmut_59 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_60'] = x__extract_status__mutmut_60 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_61'] = x__extract_status__mutmut_61 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_62'] = x__extract_status__mutmut_62 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_63'] = x__extract_status__mutmut_63 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_64'] = x__extract_status__mutmut_64 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_65'] = x__extract_status__mutmut_65 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_66'] = x__extract_status__mutmut_66 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_67'] = x__extract_status__mutmut_67 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_68'] = x__extract_status__mutmut_68 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_69'] = x__extract_status__mutmut_69 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_70'] = x__extract_status__mutmut_70 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_71'] = x__extract_status__mutmut_71 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_72'] = x__extract_status__mutmut_72 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_73'] = x__extract_status__mutmut_73 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_74'] = x__extract_status__mutmut_74 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_75'] = x__extract_status__mutmut_75 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_76'] = x__extract_status__mutmut_76 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_77'] = x__extract_status__mutmut_77 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_78'] = x__extract_status__mutmut_78 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_79'] = x__extract_status__mutmut_79 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_80'] = x__extract_status__mutmut_80 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut['x__extract_status__mutmut_81'] = x__extract_status__mutmut_81 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compute_duration_seconds__mutmut)
def _compute_duration_seconds(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_orig(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_1(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is not None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_2(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = None
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_3(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(None)
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_4(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace(None, "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_5(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", None))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_6(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_7(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", ))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_8(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("XXZXX", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_9(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("z", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_10(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "XX+00:00XX"))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_11(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = None
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_12(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = (
            datetime.fromisoformat(None)
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_13(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace(None, "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_14(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", None))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_15(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_16(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", ))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_17(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("XXZXX", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_18(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_19(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "XX+00:00XX"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_20(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(None)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_21(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(None, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_22(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, None)
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_23(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_24(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, )
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_25(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(1, int((end - start).total_seconds()))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_26(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int(None))
    except ValueError:
        return None


def x__compute_duration_seconds__mutmut_27(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end + start).total_seconds()))
    except ValueError:
        return None

mutants_x__compute_duration_seconds__mutmut['_mutmut_orig'] = x__compute_duration_seconds__mutmut_orig # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_1'] = x__compute_duration_seconds__mutmut_1 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_2'] = x__compute_duration_seconds__mutmut_2 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_3'] = x__compute_duration_seconds__mutmut_3 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_4'] = x__compute_duration_seconds__mutmut_4 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_5'] = x__compute_duration_seconds__mutmut_5 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_6'] = x__compute_duration_seconds__mutmut_6 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_7'] = x__compute_duration_seconds__mutmut_7 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_8'] = x__compute_duration_seconds__mutmut_8 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_9'] = x__compute_duration_seconds__mutmut_9 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_10'] = x__compute_duration_seconds__mutmut_10 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_11'] = x__compute_duration_seconds__mutmut_11 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_12'] = x__compute_duration_seconds__mutmut_12 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_13'] = x__compute_duration_seconds__mutmut_13 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_14'] = x__compute_duration_seconds__mutmut_14 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_15'] = x__compute_duration_seconds__mutmut_15 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_16'] = x__compute_duration_seconds__mutmut_16 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_17'] = x__compute_duration_seconds__mutmut_17 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_18'] = x__compute_duration_seconds__mutmut_18 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_19'] = x__compute_duration_seconds__mutmut_19 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_20'] = x__compute_duration_seconds__mutmut_20 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_21'] = x__compute_duration_seconds__mutmut_21 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_22'] = x__compute_duration_seconds__mutmut_22 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_23'] = x__compute_duration_seconds__mutmut_23 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_24'] = x__compute_duration_seconds__mutmut_24 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_25'] = x__compute_duration_seconds__mutmut_25 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_26'] = x__compute_duration_seconds__mutmut_26 # type: ignore # mutmut generated
mutants_x__compute_duration_seconds__mutmut['x__compute_duration_seconds__mutmut_27'] = x__compute_duration_seconds__mutmut_27 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__extract_pipeline_ref__mutmut)
def _extract_pipeline_ref(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("name")
        if isinstance(name, str) and name:
            return name
    if "pipelineSpec" in spec:
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_orig(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("name")
        if isinstance(name, str) and name:
            return name
    if "pipelineSpec" in spec:
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_1(spec: Mapping[str, object] | None) -> str:
    if spec is not None:
        return "unknown"
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("name")
        if isinstance(name, str) and name:
            return name
    if "pipelineSpec" in spec:
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_2(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "XXunknownXX"
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("name")
        if isinstance(name, str) and name:
            return name
    if "pipelineSpec" in spec:
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_3(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "UNKNOWN"
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("name")
        if isinstance(name, str) and name:
            return name
    if "pipelineSpec" in spec:
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_4(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = None
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("name")
        if isinstance(name, str) and name:
            return name
    if "pipelineSpec" in spec:
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_5(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = spec.get(None)
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("name")
        if isinstance(name, str) and name:
            return name
    if "pipelineSpec" in spec:
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_6(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = spec.get("XXpipelineRefXX")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("name")
        if isinstance(name, str) and name:
            return name
    if "pipelineSpec" in spec:
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_7(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = spec.get("pipelineref")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("name")
        if isinstance(name, str) and name:
            return name
    if "pipelineSpec" in spec:
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_8(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = spec.get("PIPELINEREF")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("name")
        if isinstance(name, str) and name:
            return name
    if "pipelineSpec" in spec:
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_9(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, Mapping):
        name = None
        if isinstance(name, str) and name:
            return name
    if "pipelineSpec" in spec:
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_10(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get(None)
        if isinstance(name, str) and name:
            return name
    if "pipelineSpec" in spec:
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_11(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("XXnameXX")
        if isinstance(name, str) and name:
            return name
    if "pipelineSpec" in spec:
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_12(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("NAME")
        if isinstance(name, str) and name:
            return name
    if "pipelineSpec" in spec:
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_13(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("name")
        if isinstance(name, str) or name:
            return name
    if "pipelineSpec" in spec:
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_14(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("name")
        if isinstance(name, str) and name:
            return name
    if "XXpipelineSpecXX" in spec:
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_15(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("name")
        if isinstance(name, str) and name:
            return name
    if "pipelinespec" in spec:
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_16(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("name")
        if isinstance(name, str) and name:
            return name
    if "PIPELINESPEC" in spec:
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_17(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("name")
        if isinstance(name, str) and name:
            return name
    if "pipelineSpec" not in spec:
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_18(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("name")
        if isinstance(name, str) and name:
            return name
    if "pipelineSpec" in spec:
        return "XXinlineXX"
    return "unknown"


def x__extract_pipeline_ref__mutmut_19(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("name")
        if isinstance(name, str) and name:
            return name
    if "pipelineSpec" in spec:
        return "INLINE"
    return "unknown"


def x__extract_pipeline_ref__mutmut_20(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("name")
        if isinstance(name, str) and name:
            return name
    if "pipelineSpec" in spec:
        return "inline"
    return "XXunknownXX"


def x__extract_pipeline_ref__mutmut_21(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("name")
        if isinstance(name, str) and name:
            return name
    if "pipelineSpec" in spec:
        return "inline"
    return "UNKNOWN"

mutants_x__extract_pipeline_ref__mutmut['_mutmut_orig'] = x__extract_pipeline_ref__mutmut_orig # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_1'] = x__extract_pipeline_ref__mutmut_1 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_2'] = x__extract_pipeline_ref__mutmut_2 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_3'] = x__extract_pipeline_ref__mutmut_3 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_4'] = x__extract_pipeline_ref__mutmut_4 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_5'] = x__extract_pipeline_ref__mutmut_5 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_6'] = x__extract_pipeline_ref__mutmut_6 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_7'] = x__extract_pipeline_ref__mutmut_7 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_8'] = x__extract_pipeline_ref__mutmut_8 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_9'] = x__extract_pipeline_ref__mutmut_9 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_10'] = x__extract_pipeline_ref__mutmut_10 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_11'] = x__extract_pipeline_ref__mutmut_11 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_12'] = x__extract_pipeline_ref__mutmut_12 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_13'] = x__extract_pipeline_ref__mutmut_13 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_14'] = x__extract_pipeline_ref__mutmut_14 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_15'] = x__extract_pipeline_ref__mutmut_15 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_16'] = x__extract_pipeline_ref__mutmut_16 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_17'] = x__extract_pipeline_ref__mutmut_17 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_18'] = x__extract_pipeline_ref__mutmut_18 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_19'] = x__extract_pipeline_ref__mutmut_19 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_20'] = x__extract_pipeline_ref__mutmut_20 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_21'] = x__extract_pipeline_ref__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_record__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_record__mutmut)
def _to_record(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_orig(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_1(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = None
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_2(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get(None)
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_3(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("XXmetadataXX")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_4(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("METADATA")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_5(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = None
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_6(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get(None)
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_7(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("XXspecXX")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_8(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("SPEC")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_9(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = None

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_10(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get(None)

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_11(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("XXstatusXX")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_12(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("STATUS")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_13(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = None
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_14(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_15(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = None

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_16(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = None
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_17(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(None)
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_18(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get(None, "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_19(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", None))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_20(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_21(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", ))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_22(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("XXnameXX", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_23(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("NAME", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_24(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "XXunknownXX"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_25(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "UNKNOWN"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_26(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = None

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_27(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(None)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_28(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = ""
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_29(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = ""
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_30(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_31(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = None
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_32(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get(None)
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_33(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("XXstartTimeXX")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_34(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("starttime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_35(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("STARTTIME")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_36(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = None
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_37(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get(None)
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_38(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("XXcompletionTimeXX")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_39(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completiontime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_40(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("COMPLETIONTIME")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_41(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_42(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(None) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_43(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_44(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_45(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(None) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_46(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_47(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = None

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_48(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(None, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_49(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, None)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_50(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_51(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, )

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_52(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=None,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_53(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=None,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_54(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=None,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_55(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=None,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_56(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=None,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_57(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=None,
    )


def x__to_record__mutmut_58(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_59(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_60(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_61(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_62(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )


def x__to_record__mutmut_63(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        )


def x__to_record__mutmut_64(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(None),
    )

mutants_x__to_record__mutmut['_mutmut_orig'] = x__to_record__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_1'] = x__to_record__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_2'] = x__to_record__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_3'] = x__to_record__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_4'] = x__to_record__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_5'] = x__to_record__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_6'] = x__to_record__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_7'] = x__to_record__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_8'] = x__to_record__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_9'] = x__to_record__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_10'] = x__to_record__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_11'] = x__to_record__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_12'] = x__to_record__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_13'] = x__to_record__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_14'] = x__to_record__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_15'] = x__to_record__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_16'] = x__to_record__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_17'] = x__to_record__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_18'] = x__to_record__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_19'] = x__to_record__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_20'] = x__to_record__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_21'] = x__to_record__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_22'] = x__to_record__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_23'] = x__to_record__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_24'] = x__to_record__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_25'] = x__to_record__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_26'] = x__to_record__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_27'] = x__to_record__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_28'] = x__to_record__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_29'] = x__to_record__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_30'] = x__to_record__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_31'] = x__to_record__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_32'] = x__to_record__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_33'] = x__to_record__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_34'] = x__to_record__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_35'] = x__to_record__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_36'] = x__to_record__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_37'] = x__to_record__mutmut_37 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_38'] = x__to_record__mutmut_38 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_39'] = x__to_record__mutmut_39 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_40'] = x__to_record__mutmut_40 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_41'] = x__to_record__mutmut_41 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_42'] = x__to_record__mutmut_42 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_43'] = x__to_record__mutmut_43 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_44'] = x__to_record__mutmut_44 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_45'] = x__to_record__mutmut_45 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_46'] = x__to_record__mutmut_46 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_47'] = x__to_record__mutmut_47 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_48'] = x__to_record__mutmut_48 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_49'] = x__to_record__mutmut_49 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_50'] = x__to_record__mutmut_50 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_51'] = x__to_record__mutmut_51 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_52'] = x__to_record__mutmut_52 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_53'] = x__to_record__mutmut_53 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_54'] = x__to_record__mutmut_54 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_55'] = x__to_record__mutmut_55 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_56'] = x__to_record__mutmut_56 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_57'] = x__to_record__mutmut_57 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_58'] = x__to_record__mutmut_58 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_59'] = x__to_record__mutmut_59 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_60'] = x__to_record__mutmut_60 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_61'] = x__to_record__mutmut_61 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_62'] = x__to_record__mutmut_62 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_63'] = x__to_record__mutmut_63 # type: ignore # mutmut generated
mutants_x__to_record__mutmut['x__to_record__mutmut_64'] = x__to_record__mutmut_64 # type: ignore # mutmut generated
