"""TektonPipelineTracerAdapter — fetches PipelineRun + child TaskRuns from K8s CRDs."""

from __future__ import annotations

from typing import cast

from hexawyn.application.ports.driven.pipeline_tracer_port import (
    PipelineRunRecord,
    PipelineTracerPort,
    TaskRunRecord,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    ComponentNotInstalledError,
    InsufficientPermissionsError,
    PipelineNotFoundError,
)

_TEKTON_GROUP = "tekton.dev"
_TEKTON_VERSION = "v1"
_PIPELINERUN_PLURAL = "pipelineruns"
_TASKRUN_PLURAL = "taskruns"
_LABEL_PIPELINERUN = "tekton.dev/pipelineRun"
_K8S_FORBIDDEN = 403
_K8S_NOT_FOUND = 404


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut: MutantDict = {}  # type: ignore


class TektonPipelineTracerAdapter(PipelineTracerPort):
    @_mutmut_mutated(mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut)
    def get_pipeline_run(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_orig(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_1(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = None
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_2(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = None
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_3(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=None,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_4(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=None,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_5(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=None,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_6(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=None,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_7(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=None,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_8(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_9(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_10(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_11(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_12(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_13(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = None
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_14(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(None, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_15(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, None, None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_16(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr("status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_17(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_18(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", )
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_19(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "XXstatusXX", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_20(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "STATUS", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_21(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status != _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_22(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(None) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_23(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status != _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_24(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    None,
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_25(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context=None,
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_26(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_27(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_28(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"XXnameXX": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_29(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"NAME": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_30(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "XXnamespaceXX": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_31(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "NAMESPACE": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_32(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(None) from exc

        return _to_pipeline_run_record(raw)
    def xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_33(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(None)

    @_mutmut_mutated(mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut)
    def list_task_runs_for_pipeline(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_orig(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_1(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = None
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_2(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = None
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_3(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=None,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_4(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=None,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_5(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=None,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_6(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=None,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_7(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=None,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_8(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_9(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_10(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_11(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_12(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_13(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = None
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_14(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(None, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_15(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, None, None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_16(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr("status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_17(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_18(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", )
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_19(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "XXstatusXX", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_20(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "STATUS", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_21(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status != _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_22(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    None, "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_23(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", None
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_24(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_25(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_26(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "XXTektonXX", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_27(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_28(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "TEKTON", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_29(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "XXhttps://tekton.dev/docs/installation/XX"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_30(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "HTTPS://TEKTON.DEV/DOCS/INSTALLATION/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_31(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status != _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_32(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    None,
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_33(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context=None,
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_34(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_35(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_36(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"XXnamespaceXX": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_37(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"NAMESPACE": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_38(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                None
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_39(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = None
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_40(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") and [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_41(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get(None) or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_42(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("XXitemsXX") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_43(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("ITEMS") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_44(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(None, pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_45(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, None) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_46(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(pipeline_run_name) for item in items]

    def xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_47(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, ) for item in items]

mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['_mutmut_orig'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_1'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_2'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_3'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_4'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_5'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_6'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_7'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_8'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_9'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_10'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_11'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_12'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_13'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_14'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_15'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_16'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_17'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_18'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_19'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_20'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_21'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_22'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_22 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_23'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_23 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_24'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_24 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_25'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_25 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_26'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_26 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_27'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_27 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_28'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_28 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_29'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_29 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_30'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_30 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_31'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_31 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_32'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_32 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut['xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_33'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁget_pipeline_run__mutmut_33 # type: ignore # mutmut generated

mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['_mutmut_orig'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_1'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_2'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_3'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_4'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_5'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_6'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_7'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_8'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_9'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_10'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_11'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_12'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_13'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_14'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_15'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_16'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_17'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_18'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_19'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_20'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_21'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_22'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_22 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_23'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_23 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_24'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_24 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_25'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_25 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_26'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_26 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_27'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_27 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_28'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_28 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_29'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_29 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_30'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_30 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_31'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_31 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_32'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_32 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_33'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_33 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_34'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_34 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_35'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_35 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_36'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_36 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_37'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_37 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_38'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_38 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_39'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_39 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_40'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_40 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_41'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_41 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_42'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_42 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_43'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_43 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_44'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_44 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_45'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_45 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_46'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_46 # type: ignore # mutmut generated
mutants_xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut['xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_47'] = TektonPipelineTracerAdapter.xǁTektonPipelineTracerAdapterǁlist_task_runs_for_pipeline__mutmut_47 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_pipeline_run_record__mutmut)
def _to_pipeline_run_record(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_orig(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_1(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = None
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_2(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(None, raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_3(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], None)
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_4(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_5(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], )
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_6(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") and {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_7(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get(None) or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_8(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("XXmetadataXX") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_9(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("METADATA") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_10(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = None
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_11(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(None, raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_12(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], None)
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_13(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_14(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], )
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_15(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") and {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_16(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get(None) or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_17(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("XXstatusXX") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_18(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("STATUS") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_19(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = None
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_20(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(None, raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_21(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], None)
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_22(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_23(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], )
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_24(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") and {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_25(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get(None) or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_26(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("XXspecXX") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_27(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("SPEC") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_28(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=None,
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_29(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=None,
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_30(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=None,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_31(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=None,
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_32(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=None,
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_33(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=None,
    )


def x__to_pipeline_run_record__mutmut_34(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_35(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_36(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_37(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_38(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_39(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        )


def x__to_pipeline_run_record__mutmut_40(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(None),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_41(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(None, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_42(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, None)),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_43(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_44(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, )),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_45(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") and "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_46(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get(None) or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_47(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("XXnameXX") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_48(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("NAME") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_49(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "XXXX")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_50(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(None),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_51(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(None, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_52(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, None)),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_53(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_54(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, )),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_55(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") and "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_56(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get(None) or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_57(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("XXnamespaceXX") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_58(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("NAMESPACE") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_59(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "XXXX")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_60(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(None),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_61(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get(None)),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_62(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("XXconditionsXX")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_63(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("CONDITIONS")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_64(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(None),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_65(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get(None)),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_66(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("XXstartTimeXX")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_67(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("starttime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_68(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("STARTTIME")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_69(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(None),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_70(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get(None)),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_71(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("XXcompletionTimeXX")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_72(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completiontime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_73(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("COMPLETIONTIME")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def x__to_pipeline_run_record__mutmut_74(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(None),
    )

mutants_x__to_pipeline_run_record__mutmut['_mutmut_orig'] = x__to_pipeline_run_record__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_1'] = x__to_pipeline_run_record__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_2'] = x__to_pipeline_run_record__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_3'] = x__to_pipeline_run_record__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_4'] = x__to_pipeline_run_record__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_5'] = x__to_pipeline_run_record__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_6'] = x__to_pipeline_run_record__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_7'] = x__to_pipeline_run_record__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_8'] = x__to_pipeline_run_record__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_9'] = x__to_pipeline_run_record__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_10'] = x__to_pipeline_run_record__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_11'] = x__to_pipeline_run_record__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_12'] = x__to_pipeline_run_record__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_13'] = x__to_pipeline_run_record__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_14'] = x__to_pipeline_run_record__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_15'] = x__to_pipeline_run_record__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_16'] = x__to_pipeline_run_record__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_17'] = x__to_pipeline_run_record__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_18'] = x__to_pipeline_run_record__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_19'] = x__to_pipeline_run_record__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_20'] = x__to_pipeline_run_record__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_21'] = x__to_pipeline_run_record__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_22'] = x__to_pipeline_run_record__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_23'] = x__to_pipeline_run_record__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_24'] = x__to_pipeline_run_record__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_25'] = x__to_pipeline_run_record__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_26'] = x__to_pipeline_run_record__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_27'] = x__to_pipeline_run_record__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_28'] = x__to_pipeline_run_record__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_29'] = x__to_pipeline_run_record__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_30'] = x__to_pipeline_run_record__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_31'] = x__to_pipeline_run_record__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_32'] = x__to_pipeline_run_record__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_33'] = x__to_pipeline_run_record__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_34'] = x__to_pipeline_run_record__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_35'] = x__to_pipeline_run_record__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_36'] = x__to_pipeline_run_record__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_37'] = x__to_pipeline_run_record__mutmut_37 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_38'] = x__to_pipeline_run_record__mutmut_38 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_39'] = x__to_pipeline_run_record__mutmut_39 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_40'] = x__to_pipeline_run_record__mutmut_40 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_41'] = x__to_pipeline_run_record__mutmut_41 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_42'] = x__to_pipeline_run_record__mutmut_42 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_43'] = x__to_pipeline_run_record__mutmut_43 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_44'] = x__to_pipeline_run_record__mutmut_44 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_45'] = x__to_pipeline_run_record__mutmut_45 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_46'] = x__to_pipeline_run_record__mutmut_46 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_47'] = x__to_pipeline_run_record__mutmut_47 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_48'] = x__to_pipeline_run_record__mutmut_48 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_49'] = x__to_pipeline_run_record__mutmut_49 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_50'] = x__to_pipeline_run_record__mutmut_50 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_51'] = x__to_pipeline_run_record__mutmut_51 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_52'] = x__to_pipeline_run_record__mutmut_52 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_53'] = x__to_pipeline_run_record__mutmut_53 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_54'] = x__to_pipeline_run_record__mutmut_54 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_55'] = x__to_pipeline_run_record__mutmut_55 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_56'] = x__to_pipeline_run_record__mutmut_56 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_57'] = x__to_pipeline_run_record__mutmut_57 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_58'] = x__to_pipeline_run_record__mutmut_58 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_59'] = x__to_pipeline_run_record__mutmut_59 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_60'] = x__to_pipeline_run_record__mutmut_60 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_61'] = x__to_pipeline_run_record__mutmut_61 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_62'] = x__to_pipeline_run_record__mutmut_62 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_63'] = x__to_pipeline_run_record__mutmut_63 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_64'] = x__to_pipeline_run_record__mutmut_64 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_65'] = x__to_pipeline_run_record__mutmut_65 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_66'] = x__to_pipeline_run_record__mutmut_66 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_67'] = x__to_pipeline_run_record__mutmut_67 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_68'] = x__to_pipeline_run_record__mutmut_68 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_69'] = x__to_pipeline_run_record__mutmut_69 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_70'] = x__to_pipeline_run_record__mutmut_70 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_71'] = x__to_pipeline_run_record__mutmut_71 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_72'] = x__to_pipeline_run_record__mutmut_72 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_73'] = x__to_pipeline_run_record__mutmut_73 # type: ignore # mutmut generated
mutants_x__to_pipeline_run_record__mutmut['x__to_pipeline_run_record__mutmut_74'] = x__to_pipeline_run_record__mutmut_74 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_task_run_record__mutmut)
def _to_task_run_record(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_orig(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_1(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = None
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_2(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(None, raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_3(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], None)
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_4(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_5(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], )
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_6(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") and {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_7(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get(None) or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_8(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("XXmetadataXX") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_9(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("METADATA") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_10(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = None
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_11(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(None, raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_12(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], None)
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_13(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_14(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], )
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_15(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") and {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_16(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get(None) or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_17(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("XXstatusXX") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_18(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("STATUS") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_19(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = None
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_20(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(None, raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_21(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], None)
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_22(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_23(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], )
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_24(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") and {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_25(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get(None) or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_26(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("XXspecXX") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_27(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("SPEC") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_28(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=None,
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_29(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=None,
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_30(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=None,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_31(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=None,
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_32(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=None,
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_33(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=None,
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_34(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=None,
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_35(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=None,
    )


def x__to_task_run_record__mutmut_36(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_37(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_38(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_39(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_40(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_41(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_42(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_43(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        )


def x__to_task_run_record__mutmut_44(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(None),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_45(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(None, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_46(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, None)),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_47(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_48(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, )),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_49(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") and "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_50(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get(None) or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_51(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("XXnameXX") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_52(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("NAME") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_53(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "XXXX")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_54(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(None),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_55(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(None, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_56(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, None)),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_57(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_58(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, )),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_59(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") and "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_60(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get(None) or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_61(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("XXnamespaceXX") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_62(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("NAMESPACE") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_63(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "XXXX")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_64(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(None),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_65(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get(None)),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_66(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("XXstartTimeXX")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_67(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("starttime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_68(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("STARTTIME")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_69(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(None),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_70(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get(None)),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_71(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("XXcompletionTimeXX")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_72(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completiontime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_73(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("COMPLETIONTIME")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_74(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(None),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_75(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get(None)),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_76(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("XXconditionsXX")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_77(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("CONDITIONS")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_78(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(None),
        failure_reason=_extract_failure_reason(status_block),
    )


def x__to_task_run_record__mutmut_79(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(None),
    )

mutants_x__to_task_run_record__mutmut['_mutmut_orig'] = x__to_task_run_record__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_1'] = x__to_task_run_record__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_2'] = x__to_task_run_record__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_3'] = x__to_task_run_record__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_4'] = x__to_task_run_record__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_5'] = x__to_task_run_record__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_6'] = x__to_task_run_record__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_7'] = x__to_task_run_record__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_8'] = x__to_task_run_record__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_9'] = x__to_task_run_record__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_10'] = x__to_task_run_record__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_11'] = x__to_task_run_record__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_12'] = x__to_task_run_record__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_13'] = x__to_task_run_record__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_14'] = x__to_task_run_record__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_15'] = x__to_task_run_record__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_16'] = x__to_task_run_record__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_17'] = x__to_task_run_record__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_18'] = x__to_task_run_record__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_19'] = x__to_task_run_record__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_20'] = x__to_task_run_record__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_21'] = x__to_task_run_record__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_22'] = x__to_task_run_record__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_23'] = x__to_task_run_record__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_24'] = x__to_task_run_record__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_25'] = x__to_task_run_record__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_26'] = x__to_task_run_record__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_27'] = x__to_task_run_record__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_28'] = x__to_task_run_record__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_29'] = x__to_task_run_record__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_30'] = x__to_task_run_record__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_31'] = x__to_task_run_record__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_32'] = x__to_task_run_record__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_33'] = x__to_task_run_record__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_34'] = x__to_task_run_record__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_35'] = x__to_task_run_record__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_36'] = x__to_task_run_record__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_37'] = x__to_task_run_record__mutmut_37 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_38'] = x__to_task_run_record__mutmut_38 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_39'] = x__to_task_run_record__mutmut_39 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_40'] = x__to_task_run_record__mutmut_40 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_41'] = x__to_task_run_record__mutmut_41 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_42'] = x__to_task_run_record__mutmut_42 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_43'] = x__to_task_run_record__mutmut_43 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_44'] = x__to_task_run_record__mutmut_44 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_45'] = x__to_task_run_record__mutmut_45 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_46'] = x__to_task_run_record__mutmut_46 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_47'] = x__to_task_run_record__mutmut_47 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_48'] = x__to_task_run_record__mutmut_48 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_49'] = x__to_task_run_record__mutmut_49 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_50'] = x__to_task_run_record__mutmut_50 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_51'] = x__to_task_run_record__mutmut_51 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_52'] = x__to_task_run_record__mutmut_52 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_53'] = x__to_task_run_record__mutmut_53 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_54'] = x__to_task_run_record__mutmut_54 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_55'] = x__to_task_run_record__mutmut_55 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_56'] = x__to_task_run_record__mutmut_56 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_57'] = x__to_task_run_record__mutmut_57 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_58'] = x__to_task_run_record__mutmut_58 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_59'] = x__to_task_run_record__mutmut_59 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_60'] = x__to_task_run_record__mutmut_60 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_61'] = x__to_task_run_record__mutmut_61 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_62'] = x__to_task_run_record__mutmut_62 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_63'] = x__to_task_run_record__mutmut_63 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_64'] = x__to_task_run_record__mutmut_64 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_65'] = x__to_task_run_record__mutmut_65 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_66'] = x__to_task_run_record__mutmut_66 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_67'] = x__to_task_run_record__mutmut_67 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_68'] = x__to_task_run_record__mutmut_68 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_69'] = x__to_task_run_record__mutmut_69 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_70'] = x__to_task_run_record__mutmut_70 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_71'] = x__to_task_run_record__mutmut_71 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_72'] = x__to_task_run_record__mutmut_72 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_73'] = x__to_task_run_record__mutmut_73 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_74'] = x__to_task_run_record__mutmut_74 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_75'] = x__to_task_run_record__mutmut_75 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_76'] = x__to_task_run_record__mutmut_76 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_77'] = x__to_task_run_record__mutmut_77 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_78'] = x__to_task_run_record__mutmut_78 # type: ignore # mutmut generated
mutants_x__to_task_run_record__mutmut['x__to_task_run_record__mutmut_79'] = x__to_task_run_record__mutmut_79 # type: ignore # mutmut generated
mutants_x__extract_status__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__extract_status__mutmut)
def _extract_status(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_orig(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_1(conditions: object) -> str:
    if isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_2(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "XXUnknownXX"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_3(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_4(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "UNKNOWN"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_5(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_6(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            break
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_7(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get(None) == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_8(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("XXtypeXX") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_9(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("TYPE") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_10(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") != "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_11(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "XXSucceededXX":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_12(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_13(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "SUCCEEDED":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_14(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = None
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_15(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get(None, "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_16(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", None)
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_17(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_18(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", )
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_19(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("XXstatusXX", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_20(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("STATUS", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_21(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "XXUnknownXX")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_22(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_23(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "UNKNOWN")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_24(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val != "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_25(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "XXTrueXX":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_26(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "true":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_27(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "TRUE":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_28(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "XXSucceededXX"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_29(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_30(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "SUCCEEDED"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_31(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val != "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_32(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "XXFalseXX":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_33(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "false":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_34(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "FALSE":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_35(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = None
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_36(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get(None, "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_37(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", None)
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_38(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_39(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", )
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_40(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("XXreasonXX", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_41(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("REASON", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_42(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "XXXX")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_43(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason not in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_44(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("XXPipelineRunCancelledXX", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_45(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("pipelineruncancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_46(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PIPELINERUNCANCELLED", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_47(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "XXTaskRunCancelledXX"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_48(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "taskruncancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_49(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TASKRUNCANCELLED"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_50(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "XXCancelledXX"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_51(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_52(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "CANCELLED"
                return "Failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_53(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "XXFailedXX"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_54(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "failed"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_55(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "FAILED"
            return "Running"
    return "NotStarted"


def x__extract_status__mutmut_56(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "XXRunningXX"
    return "NotStarted"


def x__extract_status__mutmut_57(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "running"
    return "NotStarted"


def x__extract_status__mutmut_58(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "RUNNING"
    return "NotStarted"


def x__extract_status__mutmut_59(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "XXNotStartedXX"


def x__extract_status__mutmut_60(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "notstarted"


def x__extract_status__mutmut_61(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NOTSTARTED"

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
mutants_x__extract_failure_reason__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__extract_failure_reason__mutmut)
def _extract_failure_reason(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_orig(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_1(status_block: dict[str, object]) -> str:
    conditions = None
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_2(status_block: dict[str, object]) -> str:
    conditions = status_block.get(None)
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_3(status_block: dict[str, object]) -> str:
    conditions = status_block.get("XXconditionsXX")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_4(status_block: dict[str, object]) -> str:
    conditions = status_block.get("CONDITIONS")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_5(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_6(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return "XXXX"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_7(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_8(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            break
        if c.get("type") == "Succeeded" and c.get("status") == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_9(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" or c.get("status") == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_10(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get(None) == "Succeeded" and c.get("status") == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_11(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("XXtypeXX") == "Succeeded" and c.get("status") == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_12(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("TYPE") == "Succeeded" and c.get("status") == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_13(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") != "Succeeded" and c.get("status") == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_14(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "XXSucceededXX" and c.get("status") == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_15(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "succeeded" and c.get("status") == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_16(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "SUCCEEDED" and c.get("status") == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_17(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get(None) == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_18(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("XXstatusXX") == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_19(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("STATUS") == "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_20(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") != "False":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_21(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "XXFalseXX":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_22(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "false":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_23(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "FALSE":
            return str(c.get("message", ""))
    return ""


def x__extract_failure_reason__mutmut_24(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "False":
            return str(None)
    return ""


def x__extract_failure_reason__mutmut_25(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "False":
            return str(c.get(None, ""))
    return ""


def x__extract_failure_reason__mutmut_26(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "False":
            return str(c.get("message", None))
    return ""


def x__extract_failure_reason__mutmut_27(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "False":
            return str(c.get(""))
    return ""


def x__extract_failure_reason__mutmut_28(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "False":
            return str(c.get("message", ))
    return ""


def x__extract_failure_reason__mutmut_29(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "False":
            return str(c.get("XXmessageXX", ""))
    return ""


def x__extract_failure_reason__mutmut_30(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "False":
            return str(c.get("MESSAGE", ""))
    return ""


def x__extract_failure_reason__mutmut_31(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "False":
            return str(c.get("message", "XXXX"))
    return ""


def x__extract_failure_reason__mutmut_32(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "False":
            return str(c.get("message", ""))
    return "XXXX"

mutants_x__extract_failure_reason__mutmut['_mutmut_orig'] = x__extract_failure_reason__mutmut_orig # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_1'] = x__extract_failure_reason__mutmut_1 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_2'] = x__extract_failure_reason__mutmut_2 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_3'] = x__extract_failure_reason__mutmut_3 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_4'] = x__extract_failure_reason__mutmut_4 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_5'] = x__extract_failure_reason__mutmut_5 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_6'] = x__extract_failure_reason__mutmut_6 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_7'] = x__extract_failure_reason__mutmut_7 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_8'] = x__extract_failure_reason__mutmut_8 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_9'] = x__extract_failure_reason__mutmut_9 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_10'] = x__extract_failure_reason__mutmut_10 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_11'] = x__extract_failure_reason__mutmut_11 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_12'] = x__extract_failure_reason__mutmut_12 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_13'] = x__extract_failure_reason__mutmut_13 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_14'] = x__extract_failure_reason__mutmut_14 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_15'] = x__extract_failure_reason__mutmut_15 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_16'] = x__extract_failure_reason__mutmut_16 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_17'] = x__extract_failure_reason__mutmut_17 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_18'] = x__extract_failure_reason__mutmut_18 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_19'] = x__extract_failure_reason__mutmut_19 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_20'] = x__extract_failure_reason__mutmut_20 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_21'] = x__extract_failure_reason__mutmut_21 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_22'] = x__extract_failure_reason__mutmut_22 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_23'] = x__extract_failure_reason__mutmut_23 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_24'] = x__extract_failure_reason__mutmut_24 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_25'] = x__extract_failure_reason__mutmut_25 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_26'] = x__extract_failure_reason__mutmut_26 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_27'] = x__extract_failure_reason__mutmut_27 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_28'] = x__extract_failure_reason__mutmut_28 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_29'] = x__extract_failure_reason__mutmut_29 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_30'] = x__extract_failure_reason__mutmut_30 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_31'] = x__extract_failure_reason__mutmut_31 # type: ignore # mutmut generated
mutants_x__extract_failure_reason__mutmut['x__extract_failure_reason__mutmut_32'] = x__extract_failure_reason__mutmut_32 # type: ignore # mutmut generated
mutants_x__extract_run_after__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__extract_run_after__mutmut)
def _extract_run_after(spec: dict[str, object]) -> list[str]:
    raw = spec.get("runAfter")
    if isinstance(raw, list):
        return [str(r) for r in raw]
    return []


def x__extract_run_after__mutmut_orig(spec: dict[str, object]) -> list[str]:
    raw = spec.get("runAfter")
    if isinstance(raw, list):
        return [str(r) for r in raw]
    return []


def x__extract_run_after__mutmut_1(spec: dict[str, object]) -> list[str]:
    raw = None
    if isinstance(raw, list):
        return [str(r) for r in raw]
    return []


def x__extract_run_after__mutmut_2(spec: dict[str, object]) -> list[str]:
    raw = spec.get(None)
    if isinstance(raw, list):
        return [str(r) for r in raw]
    return []


def x__extract_run_after__mutmut_3(spec: dict[str, object]) -> list[str]:
    raw = spec.get("XXrunAfterXX")
    if isinstance(raw, list):
        return [str(r) for r in raw]
    return []


def x__extract_run_after__mutmut_4(spec: dict[str, object]) -> list[str]:
    raw = spec.get("runafter")
    if isinstance(raw, list):
        return [str(r) for r in raw]
    return []


def x__extract_run_after__mutmut_5(spec: dict[str, object]) -> list[str]:
    raw = spec.get("RUNAFTER")
    if isinstance(raw, list):
        return [str(r) for r in raw]
    return []


def x__extract_run_after__mutmut_6(spec: dict[str, object]) -> list[str]:
    raw = spec.get("runAfter")
    if isinstance(raw, list):
        return [str(None) for r in raw]
    return []

mutants_x__extract_run_after__mutmut['_mutmut_orig'] = x__extract_run_after__mutmut_orig # type: ignore # mutmut generated
mutants_x__extract_run_after__mutmut['x__extract_run_after__mutmut_1'] = x__extract_run_after__mutmut_1 # type: ignore # mutmut generated
mutants_x__extract_run_after__mutmut['x__extract_run_after__mutmut_2'] = x__extract_run_after__mutmut_2 # type: ignore # mutmut generated
mutants_x__extract_run_after__mutmut['x__extract_run_after__mutmut_3'] = x__extract_run_after__mutmut_3 # type: ignore # mutmut generated
mutants_x__extract_run_after__mutmut['x__extract_run_after__mutmut_4'] = x__extract_run_after__mutmut_4 # type: ignore # mutmut generated
mutants_x__extract_run_after__mutmut['x__extract_run_after__mutmut_5'] = x__extract_run_after__mutmut_5 # type: ignore # mutmut generated
mutants_x__extract_run_after__mutmut['x__extract_run_after__mutmut_6'] = x__extract_run_after__mutmut_6 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__extract_pipeline_ref__mutmut)
def _extract_pipeline_ref(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", "unknown"))
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_orig(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", "unknown"))
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_1(spec: dict[str, object]) -> str:
    pipeline_ref = None
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", "unknown"))
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_2(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get(None)
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", "unknown"))
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_3(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("XXpipelineRefXX")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", "unknown"))
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_4(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineref")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", "unknown"))
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_5(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("PIPELINEREF")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", "unknown"))
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_6(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(None)
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_7(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get(None, "unknown"))
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_8(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", None))
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_9(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("unknown"))
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_10(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", ))
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_11(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("XXnameXX", "unknown"))
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_12(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("NAME", "unknown"))
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_13(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", "XXunknownXX"))
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_14(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", "UNKNOWN"))
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_15(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", "unknown"))
    pipeline_spec = None
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_16(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", "unknown"))
    pipeline_spec = spec.get(None)
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_17(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", "unknown"))
    pipeline_spec = spec.get("XXpipelineSpecXX")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_18(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", "unknown"))
    pipeline_spec = spec.get("pipelinespec")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_19(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", "unknown"))
    pipeline_spec = spec.get("PIPELINESPEC")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def x__extract_pipeline_ref__mutmut_20(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", "unknown"))
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
        return "XXinlineXX"
    return "unknown"


def x__extract_pipeline_ref__mutmut_21(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", "unknown"))
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
        return "INLINE"
    return "unknown"


def x__extract_pipeline_ref__mutmut_22(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", "unknown"))
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "XXunknownXX"


def x__extract_pipeline_ref__mutmut_23(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", "unknown"))
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
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
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_22'] = x__extract_pipeline_ref__mutmut_22 # type: ignore # mutmut generated
mutants_x__extract_pipeline_ref__mutmut['x__extract_pipeline_ref__mutmut_23'] = x__extract_pipeline_ref__mutmut_23 # type: ignore # mutmut generated


def _to_iso(value: object) -> str | None:
    if isinstance(value, str):
        return value
    return None
