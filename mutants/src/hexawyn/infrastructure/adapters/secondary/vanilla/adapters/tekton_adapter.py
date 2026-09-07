from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime
from typing import cast

from kubernetes import client
from kubernetes.client.exceptions import ApiException

from hexawyn.application.ports.driven.tekton_port import (
    NamespacedPipelineRunInfo,
    PipelineRunInfo,
    TaskRunInfo,
    TektonPort,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    ComponentNotInstalledError,
    InsufficientPermissionsError,
    PipelineNotFoundError,
    ServiceNotFoundError,
)
from hexawyn.infrastructure.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesCRDApi,
)

_TEKTON_GROUP = "tekton.dev"
_TEKTON_VERSION = "v1"
_TEKTON_TASKRUNS_PLURAL = "taskruns"
_TEKTON_PIPELINERUNS_PLURAL = "pipelineruns"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁVanillaTektonAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁlist_task_runs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_task_run_duration__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_crd_items__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_crd_mapping__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_crd_str__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_crd_optional_str__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaTektonAdapterǁ_crd_api_client__mutmut: MutantDict = {}  # type: ignore


class VanillaTektonAdapter(TektonPort):
    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ__init____mutmut)
    def __init__(self, crd_api: KubernetesCRDApi | None = None) -> None:
        self._crd_api = crd_api
    def xǁVanillaTektonAdapterǁ__init____mutmut_orig(self, crd_api: KubernetesCRDApi | None = None) -> None:
        self._crd_api = crd_api
    def xǁVanillaTektonAdapterǁ__init____mutmut_1(self, crd_api: KubernetesCRDApi | None = None) -> None:
        self._crd_api = None

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁlist_task_runs__mutmut)
    def list_task_runs(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        raw = self._fetch_task_runs(pipeline_name, namespace)
        items = self._crd_items(raw)
        if not items:
            raise PipelineNotFoundError(pipeline_name=pipeline_name)
        return [self._to_task_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_task_runs__mutmut_orig(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        raw = self._fetch_task_runs(pipeline_name, namespace)
        items = self._crd_items(raw)
        if not items:
            raise PipelineNotFoundError(pipeline_name=pipeline_name)
        return [self._to_task_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_task_runs__mutmut_1(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        raw = None
        items = self._crd_items(raw)
        if not items:
            raise PipelineNotFoundError(pipeline_name=pipeline_name)
        return [self._to_task_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_task_runs__mutmut_2(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        raw = self._fetch_task_runs(None, namespace)
        items = self._crd_items(raw)
        if not items:
            raise PipelineNotFoundError(pipeline_name=pipeline_name)
        return [self._to_task_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_task_runs__mutmut_3(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        raw = self._fetch_task_runs(pipeline_name, None)
        items = self._crd_items(raw)
        if not items:
            raise PipelineNotFoundError(pipeline_name=pipeline_name)
        return [self._to_task_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_task_runs__mutmut_4(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        raw = self._fetch_task_runs(namespace)
        items = self._crd_items(raw)
        if not items:
            raise PipelineNotFoundError(pipeline_name=pipeline_name)
        return [self._to_task_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_task_runs__mutmut_5(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        raw = self._fetch_task_runs(pipeline_name, )
        items = self._crd_items(raw)
        if not items:
            raise PipelineNotFoundError(pipeline_name=pipeline_name)
        return [self._to_task_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_task_runs__mutmut_6(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        raw = self._fetch_task_runs(pipeline_name, namespace)
        items = None
        if not items:
            raise PipelineNotFoundError(pipeline_name=pipeline_name)
        return [self._to_task_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_task_runs__mutmut_7(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        raw = self._fetch_task_runs(pipeline_name, namespace)
        items = self._crd_items(None)
        if not items:
            raise PipelineNotFoundError(pipeline_name=pipeline_name)
        return [self._to_task_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_task_runs__mutmut_8(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        raw = self._fetch_task_runs(pipeline_name, namespace)
        items = self._crd_items(raw)
        if items:
            raise PipelineNotFoundError(pipeline_name=pipeline_name)
        return [self._to_task_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_task_runs__mutmut_9(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        raw = self._fetch_task_runs(pipeline_name, namespace)
        items = self._crd_items(raw)
        if not items:
            raise PipelineNotFoundError(pipeline_name=None)
        return [self._to_task_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_task_runs__mutmut_10(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        raw = self._fetch_task_runs(pipeline_name, namespace)
        items = self._crd_items(raw)
        if not items:
            raise PipelineNotFoundError(pipeline_name=pipeline_name)
        return [self._to_task_run_info(None) for item in items]

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut)
    def list_pipeline_runs(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        raw = self._fetch_pipeline_runs(service_name, namespace)
        items = self._crd_items(raw)
        if not items:
            raise ServiceNotFoundError(service_name=service_name)
        return [self._to_pipeline_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_orig(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        raw = self._fetch_pipeline_runs(service_name, namespace)
        items = self._crd_items(raw)
        if not items:
            raise ServiceNotFoundError(service_name=service_name)
        return [self._to_pipeline_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_1(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        raw = None
        items = self._crd_items(raw)
        if not items:
            raise ServiceNotFoundError(service_name=service_name)
        return [self._to_pipeline_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_2(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        raw = self._fetch_pipeline_runs(None, namespace)
        items = self._crd_items(raw)
        if not items:
            raise ServiceNotFoundError(service_name=service_name)
        return [self._to_pipeline_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_3(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        raw = self._fetch_pipeline_runs(service_name, None)
        items = self._crd_items(raw)
        if not items:
            raise ServiceNotFoundError(service_name=service_name)
        return [self._to_pipeline_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_4(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        raw = self._fetch_pipeline_runs(namespace)
        items = self._crd_items(raw)
        if not items:
            raise ServiceNotFoundError(service_name=service_name)
        return [self._to_pipeline_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_5(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        raw = self._fetch_pipeline_runs(service_name, )
        items = self._crd_items(raw)
        if not items:
            raise ServiceNotFoundError(service_name=service_name)
        return [self._to_pipeline_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_6(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        raw = self._fetch_pipeline_runs(service_name, namespace)
        items = None
        if not items:
            raise ServiceNotFoundError(service_name=service_name)
        return [self._to_pipeline_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_7(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        raw = self._fetch_pipeline_runs(service_name, namespace)
        items = self._crd_items(None)
        if not items:
            raise ServiceNotFoundError(service_name=service_name)
        return [self._to_pipeline_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_8(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        raw = self._fetch_pipeline_runs(service_name, namespace)
        items = self._crd_items(raw)
        if items:
            raise ServiceNotFoundError(service_name=service_name)
        return [self._to_pipeline_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_9(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        raw = self._fetch_pipeline_runs(service_name, namespace)
        items = self._crd_items(raw)
        if not items:
            raise ServiceNotFoundError(service_name=None)
        return [self._to_pipeline_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_10(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        raw = self._fetch_pipeline_runs(service_name, namespace)
        items = self._crd_items(raw)
        if not items:
            raise ServiceNotFoundError(service_name=service_name)
        return [self._to_pipeline_run_info(None) for item in items]

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut)
    def list_pipeline_runs_in_namespace(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        raw = self._fetch_pipeline_runs_in_namespace(namespace)
        items = self._crd_items(raw)
        return [self._to_namespaced_pipeline_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut_orig(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        raw = self._fetch_pipeline_runs_in_namespace(namespace)
        items = self._crd_items(raw)
        return [self._to_namespaced_pipeline_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut_1(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        raw = None
        items = self._crd_items(raw)
        return [self._to_namespaced_pipeline_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut_2(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        raw = self._fetch_pipeline_runs_in_namespace(None)
        items = self._crd_items(raw)
        return [self._to_namespaced_pipeline_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut_3(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        raw = self._fetch_pipeline_runs_in_namespace(namespace)
        items = None
        return [self._to_namespaced_pipeline_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut_4(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        raw = self._fetch_pipeline_runs_in_namespace(namespace)
        items = self._crd_items(None)
        return [self._to_namespaced_pipeline_run_info(item) for item in items]

    def xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut_5(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        raw = self._fetch_pipeline_runs_in_namespace(namespace)
        items = self._crd_items(raw)
        return [self._to_namespaced_pipeline_run_info(None) for item in items]

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut)
    def _fetch_pipeline_runs_in_namespace(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_orig(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_1(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=None,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_2(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=None,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_3(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=None,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_4(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=None,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_5(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_6(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_7(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_8(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_9(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status != 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_10(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 404:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_11(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    None
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_12(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status != 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_13(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 405:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_14(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    None, "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_15(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", None
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_16(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_17(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_18(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "XXTektonXX", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_19(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_20(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "TEKTON", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_21(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", "XXhttps://tekton.dev/docs/installation/XX"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_22(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", "HTTPS://TEKTON.DEV/DOCS/INSTALLATION/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_23(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(None) from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_24(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(None) from exc

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut)
    def _to_namespaced_pipeline_run_info(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_orig(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_1(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = None
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_2(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(None)
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_3(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get(None))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_4(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("XXmetadataXX"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_5(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("METADATA"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_6(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = None
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_7(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(None)
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_8(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get(None))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_9(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("XXspecXX"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_10(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("SPEC"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_11(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = None
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_12(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(None)
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_13(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get(None))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_14(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("XXstatusXX"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_15(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("STATUS"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_16(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = None
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_17(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(None)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_18(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = None
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_19(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(None, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_20(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, None)
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_21(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str("startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_22(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, )
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_23(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "XXstartTimeXX")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_24(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "starttime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_25(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "STARTTIME")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_26(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = None
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_27(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(None, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_28(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, None)
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_29(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str("completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_30(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, )
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_31(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "XXcompletionTimeXX")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_32(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completiontime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_33(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "COMPLETIONTIME")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_34(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = None
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_35(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(None, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_36(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, None)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_37(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_38(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, )
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_39(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "XXnameXX": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_40(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "NAME": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_41(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(None, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_42(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, None, "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_43(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", None),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_44(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str("name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_45(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_46(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", ),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_47(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "XXnameXX", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_48(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "NAME", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_49(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "XXunknownXX"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_50(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "UNKNOWN"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_51(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "XXstatusXX": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_52(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "STATUS": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_53(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "XXstart_timeXX": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_54(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "START_TIME": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_55(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "XXdurationXX": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_56(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "DURATION": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_57(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(None),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_58(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "XXduration_secondsXX": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_59(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "DURATION_SECONDS": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_60(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "XXpipeline_refXX": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_61(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "PIPELINE_REF": self._extract_pipeline_ref(spec),
        }

    def xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_62(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(None),
        }

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut)
    def _extract_pipeline_ref(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_orig(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_1(self, spec: Mapping[str, object] | None) -> str:
        if spec is not None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_2(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "XXinlineXX"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_3(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "INLINE"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_4(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = None
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_5(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(None)
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_6(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get(None))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_7(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("XXpipelineRefXX"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_8(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineref"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_9(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("PIPELINEREF"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_10(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_11(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(None, "name", "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_12(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, None, "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_13(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", None)
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_14(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str("name", "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_15(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_16(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", )
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_17(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "XXnameXX", "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_18(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "NAME", "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_19(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "XXinlineXX")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_20(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "INLINE")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_21(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "XXpipelineSpecXX" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_22(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "pipelinespec" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_23(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "PIPELINESPEC" in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_24(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "pipelineSpec" not in spec:
            return "inline"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_25(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "pipelineSpec" in spec:
            return "XXinlineXX"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_26(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "pipelineSpec" in spec:
            return "INLINE"
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_27(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "XXunknownXX"

    def xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_28(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "UNKNOWN"

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut)
    def _fetch_pipeline_runs(self, service_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={service_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_orig(self, service_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={service_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_1(self, service_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=None,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={service_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_2(self, service_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=None,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={service_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_3(self, service_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=None,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={service_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_4(self, service_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=None,
                label_selector=f"tekton.dev/pipeline={service_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_5(self, service_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
                label_selector=None,
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_6(self, service_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={service_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_7(self, service_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={service_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_8(self, service_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={service_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_9(self, service_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                label_selector=f"tekton.dev/pipeline={service_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_10(self, service_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
                )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_11(self, service_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={service_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(None) from exc

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut)
    def _to_pipeline_run_info(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_orig(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_1(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = None
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_2(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(None)
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_3(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get(None))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_4(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("XXmetadataXX"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_5(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("METADATA"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_6(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = None
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_7(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(None)
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_8(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get(None))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_9(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("XXstatusXX"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_10(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("STATUS"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_11(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = None
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_12(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(None)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_13(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = None
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_14(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(None, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_15(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, None)
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_16(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str("startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_17(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, )
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_18(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "XXstartTimeXX")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_19(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "starttime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_20(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "STARTTIME")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_21(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = None
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_22(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(None, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_23(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, None)
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_24(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str("completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_25(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, )
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_26(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "XXcompletionTimeXX")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_27(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completiontime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_28(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "COMPLETIONTIME")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_29(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = None
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_30(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(None, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_31(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, None)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_32(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_33(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, )
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_34(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "XXnameXX": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_35(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "NAME": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_36(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(None, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_37(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, None, "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_38(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", None),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_39(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str("name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_40(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_41(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", ),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_42(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "XXnameXX", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_43(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "NAME", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_44(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "XXunknownXX"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_45(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "UNKNOWN"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_46(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "XXstatusXX": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_47(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "STATUS": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_48(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "XXstart_timeXX": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_49(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "START_TIME": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_50(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "XXdurationXX": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_51(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "DURATION": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_52(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(None),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_53(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "XXduration_secondsXX": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_54(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "DURATION_SECONDS": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_55(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "XXtriggered_byXX": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_56(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "TRIGGERED_BY": self._extract_triggered_by(metadata),
        }

    def xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_57(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(None),
        }

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut)
    def _pipeline_run_status(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_orig(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_1(self, status: Mapping[str, object] | None) -> str:
        if status is not None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_2(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "XXNotStartedXX"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_3(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "notstarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_4(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NOTSTARTED"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_5(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = None
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_6(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get(None)
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_7(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("XXconditionsXX")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_8(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("CONDITIONS")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_9(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) and not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_10(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_11(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_12(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "XXNotStartedXX"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_13(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "notstarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_14(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NOTSTARTED"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_15(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = None
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_16(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[1]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_17(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_18(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "XXNotStartedXX"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_19(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "notstarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_20(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NOTSTARTED"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_21(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = None
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_22(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = None
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_23(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(None, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_24(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, None, "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_25(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", None)
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_26(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str("status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_27(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_28(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", )
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_29(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "XXstatusXX", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_30(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "STATUS", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_31(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "XXUnknownXX")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_32(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_33(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "UNKNOWN")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_34(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = None
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_35(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(None, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_36(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, None, "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_37(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", None)
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_38(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str("reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_39(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_40(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", )
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_41(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "XXreasonXX", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_42(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "REASON", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_43(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "XXXX")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_44(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded != "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_45(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "XXTrueXX":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_46(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "true":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_47(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "TRUE":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_48(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "XXSucceededXX"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_49(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_50(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "SUCCEEDED"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_51(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded != "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_52(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "XXFalseXX":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_53(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "false":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_54(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "FALSE":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_55(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason not in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_56(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("XXCancelledXX", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_57(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_58(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("CANCELLED", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_59(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "XXPipelineRunCancelledXX"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_60(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "pipelineruncancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_61(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PIPELINERUNCANCELLED"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_62(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "XXCancelledXX"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_63(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_64(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "CANCELLED"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_65(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "XXFailedXX"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_66(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_67(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "FAILED"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_68(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" or reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_69(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded != "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_70(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "XXUnknownXX" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_71(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_72(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "UNKNOWN" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_73(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason != "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_74(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "XXRunningXX":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_75(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_76(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "RUNNING":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_77(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "XXRunningXX"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_78(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_79(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "RUNNING"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_80(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "XXNotStartedXX"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_81(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "notstarted"

    def xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_82(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NOTSTARTED"

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut)
    def _pipeline_run_duration_seconds(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(start_time, fmt)
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_orig(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(start_time, fmt)
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_1(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None and completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(start_time, fmt)
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_2(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is not None or completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(start_time, fmt)
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_3(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is not None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(start_time, fmt)
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_4(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = None
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(start_time, fmt)
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_5(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "XX%Y-%m-%dT%H:%M:%SZXX"
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(start_time, fmt)
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_6(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%y-%m-%dt%h:%m:%sz"
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(start_time, fmt)
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_7(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%Y-%M-%DT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(start_time, fmt)
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_8(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = None
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_9(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, fmt) + datetime.strptime(start_time, fmt)
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_10(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(None, fmt) - datetime.strptime(start_time, fmt)
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_11(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, None) - datetime.strptime(start_time, fmt)
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_12(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(fmt) - datetime.strptime(start_time, fmt)
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_13(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, ) - datetime.strptime(start_time, fmt)
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_14(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(None, fmt)
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_15(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(start_time, None)
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_16(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(fmt)
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_17(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(start_time, )
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_18(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(start_time, fmt)
            return max(None, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_19(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(start_time, fmt)
            return max(0, None)
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_20(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(start_time, fmt)
            return max(int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_21(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(start_time, fmt)
            return max(0, )
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_22(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(start_time, fmt)
            return max(1, int(delta.total_seconds()))
        except ValueError:
            return None

    def xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_23(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(start_time, fmt)
            return max(0, int(None))
        except ValueError:
            return None

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut)
    def _seconds_to_human(self, seconds: int | None) -> str | None:
        if seconds is None:
            return None
        if seconds >= 60:  # noqa: PLR2004
            minutes, remaining = divmod(seconds, 60)
            return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
        return f"{seconds}s"

    def xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_orig(self, seconds: int | None) -> str | None:
        if seconds is None:
            return None
        if seconds >= 60:  # noqa: PLR2004
            minutes, remaining = divmod(seconds, 60)
            return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
        return f"{seconds}s"

    def xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_1(self, seconds: int | None) -> str | None:
        if seconds is not None:
            return None
        if seconds >= 60:  # noqa: PLR2004
            minutes, remaining = divmod(seconds, 60)
            return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
        return f"{seconds}s"

    def xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_2(self, seconds: int | None) -> str | None:
        if seconds is None:
            return None
        if seconds > 60:  # noqa: PLR2004
            minutes, remaining = divmod(seconds, 60)
            return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
        return f"{seconds}s"

    def xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_3(self, seconds: int | None) -> str | None:
        if seconds is None:
            return None
        if seconds >= 61:  # noqa: PLR2004
            minutes, remaining = divmod(seconds, 60)
            return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
        return f"{seconds}s"

    def xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_4(self, seconds: int | None) -> str | None:
        if seconds is None:
            return None
        if seconds >= 60:  # noqa: PLR2004
            minutes, remaining = None
            return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
        return f"{seconds}s"

    def xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_5(self, seconds: int | None) -> str | None:
        if seconds is None:
            return None
        if seconds >= 60:  # noqa: PLR2004
            minutes, remaining = divmod(None, 60)
            return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
        return f"{seconds}s"

    def xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_6(self, seconds: int | None) -> str | None:
        if seconds is None:
            return None
        if seconds >= 60:  # noqa: PLR2004
            minutes, remaining = divmod(seconds, None)
            return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
        return f"{seconds}s"

    def xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_7(self, seconds: int | None) -> str | None:
        if seconds is None:
            return None
        if seconds >= 60:  # noqa: PLR2004
            minutes, remaining = divmod(60)
            return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
        return f"{seconds}s"

    def xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_8(self, seconds: int | None) -> str | None:
        if seconds is None:
            return None
        if seconds >= 60:  # noqa: PLR2004
            minutes, remaining = divmod(seconds, )
            return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
        return f"{seconds}s"

    def xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_9(self, seconds: int | None) -> str | None:
        if seconds is None:
            return None
        if seconds >= 60:  # noqa: PLR2004
            minutes, remaining = divmod(seconds, 61)
            return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
        return f"{seconds}s"

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut)
    def _extract_triggered_by(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_orig(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_1(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is not None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_2(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = None
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_3(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(None)
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_4(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get(None))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_5(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("XXannotationsXX"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_6(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("ANNOTATIONS"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_7(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_8(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = None
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_9(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(None, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_10(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, None)
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_11(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str("pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_12(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, )
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_13(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "XXpipelinesascode.tekton.dev/senderXX")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_14(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "PIPELINESASCODE.TEKTON.DEV/SENDER")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_15(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = None
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_16(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(None)
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_17(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get(None))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_18(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("XXlabelsXX"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_19(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("LABELS"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_20(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_21(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = None
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_22(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(None, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_23(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, None)
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_24(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str("triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_25(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, )
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_26(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "XXtriggers.tekton.dev/eventlistenerXX")
            if listener:
                return listener
        return None

    def xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_27(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "TRIGGERS.TEKTON.DEV/EVENTLISTENER")
            if listener:
                return listener
        return None

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut)
    def _fetch_task_runs(self, pipeline_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_TASKRUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={pipeline_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_orig(self, pipeline_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_TASKRUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={pipeline_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_1(self, pipeline_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=None,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_TASKRUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={pipeline_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_2(self, pipeline_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=None,
                namespace=namespace,
                plural=_TEKTON_TASKRUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={pipeline_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_3(self, pipeline_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=None,
                plural=_TEKTON_TASKRUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={pipeline_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_4(self, pipeline_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=None,
                label_selector=f"tekton.dev/pipeline={pipeline_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_5(self, pipeline_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_TASKRUNS_PLURAL,
                label_selector=None,
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_6(self, pipeline_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_TASKRUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={pipeline_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_7(self, pipeline_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                namespace=namespace,
                plural=_TEKTON_TASKRUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={pipeline_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_8(self, pipeline_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                plural=_TEKTON_TASKRUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={pipeline_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_9(self, pipeline_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                label_selector=f"tekton.dev/pipeline={pipeline_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_10(self, pipeline_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_TASKRUNS_PLURAL,
                )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_11(self, pipeline_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_TASKRUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={pipeline_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(None) from exc

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut)
    def _to_task_run_info(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_orig(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_1(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = None
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_2(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(None)
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_3(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get(None))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_4(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("XXmetadataXX"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_5(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("METADATA"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_6(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = None
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_7(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(None)
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_8(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get(None))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_9(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("XXspecXX"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_10(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("SPEC"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_11(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = None
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_12(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(None)
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_13(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get(None))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_14(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("XXstatusXX"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_15(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("STATUS"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_16(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = None
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_17(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(None)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_18(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = None
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_19(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(None, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_20(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, None)
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_21(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str("startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_22(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, )
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_23(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "XXstartTimeXX")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_24(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "starttime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_25(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "STARTTIME")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_26(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = None
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_27(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(None, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_28(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, None)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_29(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_30(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, )
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_31(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "XXnameXX": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_32(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "NAME": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_33(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(None, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_34(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, None, "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_35(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", None),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_36(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str("name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_37(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_38(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", ),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_39(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "XXnameXX", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_40(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "NAME", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_41(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "XXunknownXX"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_42(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "UNKNOWN"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_43(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "XXtask_refXX": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_44(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "TASK_REF": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_45(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(None),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_46(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "XXstatusXX": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_47(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "STATUS": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_48(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "XXstart_timeXX": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_49(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "START_TIME": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_50(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "XXdurationXX": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_51(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "DURATION": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_52(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(None, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_53(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, None, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_54(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, None),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_55(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_56(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_57(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, ),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_58(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "XXfailing_stepXX": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_59(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "FAILING_STEP": failing_step,
            "failing_step_error": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_60(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "XXfailing_step_errorXX": failing_step_error,
        }

    def xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_61(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "FAILING_STEP_ERROR": failing_step_error,
        }

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut)
    def _extract_task_ref(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("taskRef"))
        if task_ref is not None:
            return self._crd_str(task_ref, "name", "unknown")
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_orig(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("taskRef"))
        if task_ref is not None:
            return self._crd_str(task_ref, "name", "unknown")
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_1(self, spec: Mapping[str, object] | None) -> str:
        if spec is not None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("taskRef"))
        if task_ref is not None:
            return self._crd_str(task_ref, "name", "unknown")
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_2(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "XXunknownXX"
        task_ref = self._crd_mapping(spec.get("taskRef"))
        if task_ref is not None:
            return self._crd_str(task_ref, "name", "unknown")
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_3(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "UNKNOWN"
        task_ref = self._crd_mapping(spec.get("taskRef"))
        if task_ref is not None:
            return self._crd_str(task_ref, "name", "unknown")
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_4(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = None
        if task_ref is not None:
            return self._crd_str(task_ref, "name", "unknown")
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_5(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(None)
        if task_ref is not None:
            return self._crd_str(task_ref, "name", "unknown")
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_6(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get(None))
        if task_ref is not None:
            return self._crd_str(task_ref, "name", "unknown")
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_7(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("XXtaskRefXX"))
        if task_ref is not None:
            return self._crd_str(task_ref, "name", "unknown")
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_8(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("taskref"))
        if task_ref is not None:
            return self._crd_str(task_ref, "name", "unknown")
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_9(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("TASKREF"))
        if task_ref is not None:
            return self._crd_str(task_ref, "name", "unknown")
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_10(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("taskRef"))
        if task_ref is None:
            return self._crd_str(task_ref, "name", "unknown")
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_11(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("taskRef"))
        if task_ref is not None:
            return self._crd_str(None, "name", "unknown")
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_12(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("taskRef"))
        if task_ref is not None:
            return self._crd_str(task_ref, None, "unknown")
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_13(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("taskRef"))
        if task_ref is not None:
            return self._crd_str(task_ref, "name", None)
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_14(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("taskRef"))
        if task_ref is not None:
            return self._crd_str("name", "unknown")
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_15(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("taskRef"))
        if task_ref is not None:
            return self._crd_str(task_ref, "unknown")
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_16(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("taskRef"))
        if task_ref is not None:
            return self._crd_str(task_ref, "name", )
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_17(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("taskRef"))
        if task_ref is not None:
            return self._crd_str(task_ref, "XXnameXX", "unknown")
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_18(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("taskRef"))
        if task_ref is not None:
            return self._crd_str(task_ref, "NAME", "unknown")
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_19(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("taskRef"))
        if task_ref is not None:
            return self._crd_str(task_ref, "name", "XXunknownXX")
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_20(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("taskRef"))
        if task_ref is not None:
            return self._crd_str(task_ref, "name", "UNKNOWN")
        return "unknown"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_21(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("taskRef"))
        if task_ref is not None:
            return self._crd_str(task_ref, "name", "unknown")
        return "XXunknownXX"

    def xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_22(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("taskRef"))
        if task_ref is not None:
            return self._crd_str(task_ref, "name", "unknown")
        return "UNKNOWN"

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut)
    def _task_run_status(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_orig(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_1(self, status: Mapping[str, object] | None) -> str:
        if status is not None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_2(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "XXNotStartedXX"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_3(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "notstarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_4(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NOTSTARTED"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_5(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = None
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_6(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get(None)
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_7(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("XXconditionsXX")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_8(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("CONDITIONS")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_9(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) and not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_10(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_11(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_12(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "XXNotStartedXX"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_13(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "notstarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_14(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NOTSTARTED"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_15(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = None
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_16(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[1]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_17(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_18(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "XXNotStartedXX"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_19(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "notstarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_20(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NOTSTARTED"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_21(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = None
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_22(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = None
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_23(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(None, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_24(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, None, "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_25(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", None)
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_26(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str("status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_27(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_28(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", )
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_29(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "XXstatusXX", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_30(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "STATUS", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_31(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "XXUnknownXX")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_32(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_33(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "UNKNOWN")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_34(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = None
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_35(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(None, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_36(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, None, "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_37(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", None)
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_38(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str("reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_39(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_40(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", )
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_41(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "XXreasonXX", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_42(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "REASON", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_43(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "XXXX")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_44(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded != "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_45(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "XXTrueXX":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_46(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "true":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_47(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "TRUE":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_48(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "XXSucceededXX"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_49(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_50(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "SUCCEEDED"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_51(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded != "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_52(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "XXFalseXX":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_53(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "false":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_54(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "FALSE":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_55(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason and "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_56(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "XXDeadlineExceededXX" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_57(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "deadlineexceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_58(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DEADLINEEXCEEDED" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_59(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" not in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_60(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "XXtimeoutXX" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_61(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "TIMEOUT" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_62(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" not in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_63(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.upper():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_64(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "XXTimeoutXX"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_65(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_66(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "TIMEOUT"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_67(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "XXFailedXX"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_68(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_69(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "FAILED"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_70(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" or reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_71(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded != "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_72(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "XXUnknownXX" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_73(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_74(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "UNKNOWN" and reason == "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_75(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason != "Running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_76(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "XXRunningXX":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_77(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "running":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_78(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "RUNNING":
            return "Running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_79(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "XXRunningXX"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_80(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "running"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_81(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "RUNNING"
        return "NotStarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_82(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "XXNotStartedXX"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_83(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "notstarted"

    def xǁVanillaTektonAdapterǁ_task_run_status__mutmut_84(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NOTSTARTED"

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_task_run_duration__mutmut)
    def _task_run_duration(
        self,
        status: Mapping[str, object] | None,
        start_time: str | None,
        run_status: str,
    ) -> str | None:
        if status is None or start_time is None:
            return None
        completion_time = self._crd_optional_str(status, "completionTime")
        if completion_time is None:
            return None
        return self._elapsed_between(start_time, completion_time)

    def xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_orig(
        self,
        status: Mapping[str, object] | None,
        start_time: str | None,
        run_status: str,
    ) -> str | None:
        if status is None or start_time is None:
            return None
        completion_time = self._crd_optional_str(status, "completionTime")
        if completion_time is None:
            return None
        return self._elapsed_between(start_time, completion_time)

    def xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_1(
        self,
        status: Mapping[str, object] | None,
        start_time: str | None,
        run_status: str,
    ) -> str | None:
        if status is None and start_time is None:
            return None
        completion_time = self._crd_optional_str(status, "completionTime")
        if completion_time is None:
            return None
        return self._elapsed_between(start_time, completion_time)

    def xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_2(
        self,
        status: Mapping[str, object] | None,
        start_time: str | None,
        run_status: str,
    ) -> str | None:
        if status is not None or start_time is None:
            return None
        completion_time = self._crd_optional_str(status, "completionTime")
        if completion_time is None:
            return None
        return self._elapsed_between(start_time, completion_time)

    def xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_3(
        self,
        status: Mapping[str, object] | None,
        start_time: str | None,
        run_status: str,
    ) -> str | None:
        if status is None or start_time is not None:
            return None
        completion_time = self._crd_optional_str(status, "completionTime")
        if completion_time is None:
            return None
        return self._elapsed_between(start_time, completion_time)

    def xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_4(
        self,
        status: Mapping[str, object] | None,
        start_time: str | None,
        run_status: str,
    ) -> str | None:
        if status is None or start_time is None:
            return None
        completion_time = None
        if completion_time is None:
            return None
        return self._elapsed_between(start_time, completion_time)

    def xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_5(
        self,
        status: Mapping[str, object] | None,
        start_time: str | None,
        run_status: str,
    ) -> str | None:
        if status is None or start_time is None:
            return None
        completion_time = self._crd_optional_str(None, "completionTime")
        if completion_time is None:
            return None
        return self._elapsed_between(start_time, completion_time)

    def xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_6(
        self,
        status: Mapping[str, object] | None,
        start_time: str | None,
        run_status: str,
    ) -> str | None:
        if status is None or start_time is None:
            return None
        completion_time = self._crd_optional_str(status, None)
        if completion_time is None:
            return None
        return self._elapsed_between(start_time, completion_time)

    def xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_7(
        self,
        status: Mapping[str, object] | None,
        start_time: str | None,
        run_status: str,
    ) -> str | None:
        if status is None or start_time is None:
            return None
        completion_time = self._crd_optional_str("completionTime")
        if completion_time is None:
            return None
        return self._elapsed_between(start_time, completion_time)

    def xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_8(
        self,
        status: Mapping[str, object] | None,
        start_time: str | None,
        run_status: str,
    ) -> str | None:
        if status is None or start_time is None:
            return None
        completion_time = self._crd_optional_str(status, )
        if completion_time is None:
            return None
        return self._elapsed_between(start_time, completion_time)

    def xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_9(
        self,
        status: Mapping[str, object] | None,
        start_time: str | None,
        run_status: str,
    ) -> str | None:
        if status is None or start_time is None:
            return None
        completion_time = self._crd_optional_str(status, "XXcompletionTimeXX")
        if completion_time is None:
            return None
        return self._elapsed_between(start_time, completion_time)

    def xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_10(
        self,
        status: Mapping[str, object] | None,
        start_time: str | None,
        run_status: str,
    ) -> str | None:
        if status is None or start_time is None:
            return None
        completion_time = self._crd_optional_str(status, "completiontime")
        if completion_time is None:
            return None
        return self._elapsed_between(start_time, completion_time)

    def xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_11(
        self,
        status: Mapping[str, object] | None,
        start_time: str | None,
        run_status: str,
    ) -> str | None:
        if status is None or start_time is None:
            return None
        completion_time = self._crd_optional_str(status, "COMPLETIONTIME")
        if completion_time is None:
            return None
        return self._elapsed_between(start_time, completion_time)

    def xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_12(
        self,
        status: Mapping[str, object] | None,
        start_time: str | None,
        run_status: str,
    ) -> str | None:
        if status is None or start_time is None:
            return None
        completion_time = self._crd_optional_str(status, "completionTime")
        if completion_time is not None:
            return None
        return self._elapsed_between(start_time, completion_time)

    def xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_13(
        self,
        status: Mapping[str, object] | None,
        start_time: str | None,
        run_status: str,
    ) -> str | None:
        if status is None or start_time is None:
            return None
        completion_time = self._crd_optional_str(status, "completionTime")
        if completion_time is None:
            return None
        return self._elapsed_between(None, completion_time)

    def xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_14(
        self,
        status: Mapping[str, object] | None,
        start_time: str | None,
        run_status: str,
    ) -> str | None:
        if status is None or start_time is None:
            return None
        completion_time = self._crd_optional_str(status, "completionTime")
        if completion_time is None:
            return None
        return self._elapsed_between(start_time, None)

    def xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_15(
        self,
        status: Mapping[str, object] | None,
        start_time: str | None,
        run_status: str,
    ) -> str | None:
        if status is None or start_time is None:
            return None
        completion_time = self._crd_optional_str(status, "completionTime")
        if completion_time is None:
            return None
        return self._elapsed_between(completion_time)

    def xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_16(
        self,
        status: Mapping[str, object] | None,
        start_time: str | None,
        run_status: str,
    ) -> str | None:
        if status is None or start_time is None:
            return None
        completion_time = self._crd_optional_str(status, "completionTime")
        if completion_time is None:
            return None
        return self._elapsed_between(start_time, )

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut)
    def _extract_failing_step(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_orig(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_1(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") and status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_2(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_3(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("XXFailedXX", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_4(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_5(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("FAILED", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_6(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "XXTimeoutXX") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_7(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_8(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "TIMEOUT") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_9(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is not None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_10(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = None
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_11(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get(None)
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_12(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("XXstepsXX")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_13(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("STEPS")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_14(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_15(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_16(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                break
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_17(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = None
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_18(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(None)
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_19(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get(None))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_20(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("XXterminatedXX"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_21(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("TERMINATED"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_22(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is not None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_23(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                break
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_24(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = None
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_25(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get(None)
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_26(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("XXexitCodeXX")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_27(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitcode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_28(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("EXITCODE")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_29(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) or exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_30(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code == 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_31(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 1:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_32(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(None, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_33(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, None, "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_34(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", None), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_35(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str("name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_36(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_37(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", ), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_38(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "XXnameXX", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_39(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "NAME", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_40(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "XXunknownXX"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_41(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "UNKNOWN"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_42(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    None, terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_43(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, None
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_44(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    terminated
                )
        return None, None

    def xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_45(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, )
        return None, None

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut)
    def _step_error(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", "")
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_orig(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", "")
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_1(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = None
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_2(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(None, "reason", "")
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_3(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, None, "")
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_4(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", None)
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_5(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str("reason", "")
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_6(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "")
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_7(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", )
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_8(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "XXreasonXX", "")
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_9(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "REASON", "")
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_10(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", "XXXX")
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_11(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", "")
        if "XXDeadlineExceededXX" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_12(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", "")
        if "deadlineexceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_13(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", "")
        if "DEADLINEEXCEEDED" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_14(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", "")
        if "DeadlineExceeded" not in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_15(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", "")
        if "DeadlineExceeded" in reason:
            return "XXTimeoutXX"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_16(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", "")
        if "DeadlineExceeded" in reason:
            return "timeout"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_17(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", "")
        if "DeadlineExceeded" in reason:
            return "TIMEOUT"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_18(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", "")
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = None
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_19(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", "")
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str(None, "message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_20(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", "")
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, None)
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_21(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", "")
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str("message")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_22(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", "")
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, )
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_23(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", "")
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, "XXmessageXX")
        return message if message else f"exit code {exit_code}"

    def xǁVanillaTektonAdapterǁ_step_error__mutmut_24(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", "")
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, "MESSAGE")
        return message if message else f"exit code {exit_code}"

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut)
    def _elapsed_between(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_orig(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_1(self, start: str, end: str) -> str:
        try:
            fmt = None
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_2(self, start: str, end: str) -> str:
        try:
            fmt = "XX%Y-%m-%dT%H:%M:%SZXX"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_3(self, start: str, end: str) -> str:
        try:
            fmt = "%y-%m-%dt%h:%m:%sz"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_4(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%M-%DT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_5(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = None
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_6(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) + datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_7(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(None, fmt) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_8(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, None) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_9(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(fmt) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_10(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, ) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_11(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(None, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_12(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, None)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_13(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_14(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, )
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_15(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            seconds = None
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_16(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            seconds = int(None)
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_17(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds > 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_18(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 61:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_19(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = None
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_20(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(None, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_21(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, None)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_22(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_23(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, )
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_24(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 61)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_25(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "XXunknownXX"

    def xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_26(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "UNKNOWN"

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_crd_items__mutmut)
    def _crd_items(self, raw: object) -> list[Mapping[str, object]]:
        mapping = self._crd_mapping(raw)
        if mapping is None:
            return []
        items = mapping.get("items", [])
        if not isinstance(items, list):
            return []
        return [item for item in items if isinstance(item, Mapping)]

    def xǁVanillaTektonAdapterǁ_crd_items__mutmut_orig(self, raw: object) -> list[Mapping[str, object]]:
        mapping = self._crd_mapping(raw)
        if mapping is None:
            return []
        items = mapping.get("items", [])
        if not isinstance(items, list):
            return []
        return [item for item in items if isinstance(item, Mapping)]

    def xǁVanillaTektonAdapterǁ_crd_items__mutmut_1(self, raw: object) -> list[Mapping[str, object]]:
        mapping = None
        if mapping is None:
            return []
        items = mapping.get("items", [])
        if not isinstance(items, list):
            return []
        return [item for item in items if isinstance(item, Mapping)]

    def xǁVanillaTektonAdapterǁ_crd_items__mutmut_2(self, raw: object) -> list[Mapping[str, object]]:
        mapping = self._crd_mapping(None)
        if mapping is None:
            return []
        items = mapping.get("items", [])
        if not isinstance(items, list):
            return []
        return [item for item in items if isinstance(item, Mapping)]

    def xǁVanillaTektonAdapterǁ_crd_items__mutmut_3(self, raw: object) -> list[Mapping[str, object]]:
        mapping = self._crd_mapping(raw)
        if mapping is not None:
            return []
        items = mapping.get("items", [])
        if not isinstance(items, list):
            return []
        return [item for item in items if isinstance(item, Mapping)]

    def xǁVanillaTektonAdapterǁ_crd_items__mutmut_4(self, raw: object) -> list[Mapping[str, object]]:
        mapping = self._crd_mapping(raw)
        if mapping is None:
            return []
        items = None
        if not isinstance(items, list):
            return []
        return [item for item in items if isinstance(item, Mapping)]

    def xǁVanillaTektonAdapterǁ_crd_items__mutmut_5(self, raw: object) -> list[Mapping[str, object]]:
        mapping = self._crd_mapping(raw)
        if mapping is None:
            return []
        items = mapping.get(None, [])
        if not isinstance(items, list):
            return []
        return [item for item in items if isinstance(item, Mapping)]

    def xǁVanillaTektonAdapterǁ_crd_items__mutmut_6(self, raw: object) -> list[Mapping[str, object]]:
        mapping = self._crd_mapping(raw)
        if mapping is None:
            return []
        items = mapping.get("items", None)
        if not isinstance(items, list):
            return []
        return [item for item in items if isinstance(item, Mapping)]

    def xǁVanillaTektonAdapterǁ_crd_items__mutmut_7(self, raw: object) -> list[Mapping[str, object]]:
        mapping = self._crd_mapping(raw)
        if mapping is None:
            return []
        items = mapping.get([])
        if not isinstance(items, list):
            return []
        return [item for item in items if isinstance(item, Mapping)]

    def xǁVanillaTektonAdapterǁ_crd_items__mutmut_8(self, raw: object) -> list[Mapping[str, object]]:
        mapping = self._crd_mapping(raw)
        if mapping is None:
            return []
        items = mapping.get("items", )
        if not isinstance(items, list):
            return []
        return [item for item in items if isinstance(item, Mapping)]

    def xǁVanillaTektonAdapterǁ_crd_items__mutmut_9(self, raw: object) -> list[Mapping[str, object]]:
        mapping = self._crd_mapping(raw)
        if mapping is None:
            return []
        items = mapping.get("XXitemsXX", [])
        if not isinstance(items, list):
            return []
        return [item for item in items if isinstance(item, Mapping)]

    def xǁVanillaTektonAdapterǁ_crd_items__mutmut_10(self, raw: object) -> list[Mapping[str, object]]:
        mapping = self._crd_mapping(raw)
        if mapping is None:
            return []
        items = mapping.get("ITEMS", [])
        if not isinstance(items, list):
            return []
        return [item for item in items if isinstance(item, Mapping)]

    def xǁVanillaTektonAdapterǁ_crd_items__mutmut_11(self, raw: object) -> list[Mapping[str, object]]:
        mapping = self._crd_mapping(raw)
        if mapping is None:
            return []
        items = mapping.get("items", [])
        if isinstance(items, list):
            return []
        return [item for item in items if isinstance(item, Mapping)]

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_crd_mapping__mutmut)
    def _crd_mapping(self, value: object) -> Mapping[str, object] | None:
        if isinstance(value, Mapping):
            return cast(Mapping[str, object], value)
        return None

    def xǁVanillaTektonAdapterǁ_crd_mapping__mutmut_orig(self, value: object) -> Mapping[str, object] | None:
        if isinstance(value, Mapping):
            return cast(Mapping[str, object], value)
        return None

    def xǁVanillaTektonAdapterǁ_crd_mapping__mutmut_1(self, value: object) -> Mapping[str, object] | None:
        if isinstance(value, Mapping):
            return cast(None, value)
        return None

    def xǁVanillaTektonAdapterǁ_crd_mapping__mutmut_2(self, value: object) -> Mapping[str, object] | None:
        if isinstance(value, Mapping):
            return cast(Mapping[str, object], None)
        return None

    def xǁVanillaTektonAdapterǁ_crd_mapping__mutmut_3(self, value: object) -> Mapping[str, object] | None:
        if isinstance(value, Mapping):
            return cast(value)
        return None

    def xǁVanillaTektonAdapterǁ_crd_mapping__mutmut_4(self, value: object) -> Mapping[str, object] | None:
        if isinstance(value, Mapping):
            return cast(Mapping[str, object], )
        return None

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_crd_str__mutmut)
    def _crd_str(
        self,
        data: Mapping[str, object] | None,
        key: str,
        default: str = "",
    ) -> str:
        if data is None:
            return default
        value = data.get(key, default)
        return value if isinstance(value, str) else default

    def xǁVanillaTektonAdapterǁ_crd_str__mutmut_orig(
        self,
        data: Mapping[str, object] | None,
        key: str,
        default: str = "",
    ) -> str:
        if data is None:
            return default
        value = data.get(key, default)
        return value if isinstance(value, str) else default

    def xǁVanillaTektonAdapterǁ_crd_str__mutmut_1(
        self,
        data: Mapping[str, object] | None,
        key: str,
        default: str = "XXXX",
    ) -> str:
        if data is None:
            return default
        value = data.get(key, default)
        return value if isinstance(value, str) else default

    def xǁVanillaTektonAdapterǁ_crd_str__mutmut_2(
        self,
        data: Mapping[str, object] | None,
        key: str,
        default: str = "",
    ) -> str:
        if data is not None:
            return default
        value = data.get(key, default)
        return value if isinstance(value, str) else default

    def xǁVanillaTektonAdapterǁ_crd_str__mutmut_3(
        self,
        data: Mapping[str, object] | None,
        key: str,
        default: str = "",
    ) -> str:
        if data is None:
            return default
        value = None
        return value if isinstance(value, str) else default

    def xǁVanillaTektonAdapterǁ_crd_str__mutmut_4(
        self,
        data: Mapping[str, object] | None,
        key: str,
        default: str = "",
    ) -> str:
        if data is None:
            return default
        value = data.get(None, default)
        return value if isinstance(value, str) else default

    def xǁVanillaTektonAdapterǁ_crd_str__mutmut_5(
        self,
        data: Mapping[str, object] | None,
        key: str,
        default: str = "",
    ) -> str:
        if data is None:
            return default
        value = data.get(key, None)
        return value if isinstance(value, str) else default

    def xǁVanillaTektonAdapterǁ_crd_str__mutmut_6(
        self,
        data: Mapping[str, object] | None,
        key: str,
        default: str = "",
    ) -> str:
        if data is None:
            return default
        value = data.get(default)
        return value if isinstance(value, str) else default

    def xǁVanillaTektonAdapterǁ_crd_str__mutmut_7(
        self,
        data: Mapping[str, object] | None,
        key: str,
        default: str = "",
    ) -> str:
        if data is None:
            return default
        value = data.get(key, )
        return value if isinstance(value, str) else default

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_crd_optional_str__mutmut)
    def _crd_optional_str(
        self,
        data: Mapping[str, object] | None,
        key: str,
    ) -> str | None:
        if data is None:
            return None
        value = data.get(key)
        return value if isinstance(value, str) else None

    def xǁVanillaTektonAdapterǁ_crd_optional_str__mutmut_orig(
        self,
        data: Mapping[str, object] | None,
        key: str,
    ) -> str | None:
        if data is None:
            return None
        value = data.get(key)
        return value if isinstance(value, str) else None

    def xǁVanillaTektonAdapterǁ_crd_optional_str__mutmut_1(
        self,
        data: Mapping[str, object] | None,
        key: str,
    ) -> str | None:
        if data is not None:
            return None
        value = data.get(key)
        return value if isinstance(value, str) else None

    def xǁVanillaTektonAdapterǁ_crd_optional_str__mutmut_2(
        self,
        data: Mapping[str, object] | None,
        key: str,
    ) -> str | None:
        if data is None:
            return None
        value = None
        return value if isinstance(value, str) else None

    def xǁVanillaTektonAdapterǁ_crd_optional_str__mutmut_3(
        self,
        data: Mapping[str, object] | None,
        key: str,
    ) -> str | None:
        if data is None:
            return None
        value = data.get(None)
        return value if isinstance(value, str) else None

    @_mutmut_mutated(mutants_xǁVanillaTektonAdapterǁ_crd_api_client__mutmut)
    def _crd_api_client(self) -> KubernetesCRDApi:
        if self._crd_api is None:
            self._crd_api = cast(KubernetesCRDApi, client.CustomObjectsApi())
        return self._crd_api

    def xǁVanillaTektonAdapterǁ_crd_api_client__mutmut_orig(self) -> KubernetesCRDApi:
        if self._crd_api is None:
            self._crd_api = cast(KubernetesCRDApi, client.CustomObjectsApi())
        return self._crd_api

    def xǁVanillaTektonAdapterǁ_crd_api_client__mutmut_1(self) -> KubernetesCRDApi:
        if self._crd_api is not None:
            self._crd_api = cast(KubernetesCRDApi, client.CustomObjectsApi())
        return self._crd_api

    def xǁVanillaTektonAdapterǁ_crd_api_client__mutmut_2(self) -> KubernetesCRDApi:
        if self._crd_api is None:
            self._crd_api = None
        return self._crd_api

    def xǁVanillaTektonAdapterǁ_crd_api_client__mutmut_3(self) -> KubernetesCRDApi:
        if self._crd_api is None:
            self._crd_api = cast(None, client.CustomObjectsApi())
        return self._crd_api

    def xǁVanillaTektonAdapterǁ_crd_api_client__mutmut_4(self) -> KubernetesCRDApi:
        if self._crd_api is None:
            self._crd_api = cast(KubernetesCRDApi, None)
        return self._crd_api

    def xǁVanillaTektonAdapterǁ_crd_api_client__mutmut_5(self) -> KubernetesCRDApi:
        if self._crd_api is None:
            self._crd_api = cast(client.CustomObjectsApi())
        return self._crd_api

    def xǁVanillaTektonAdapterǁ_crd_api_client__mutmut_6(self) -> KubernetesCRDApi:
        if self._crd_api is None:
            self._crd_api = cast(KubernetesCRDApi, )
        return self._crd_api

mutants_xǁVanillaTektonAdapterǁ__init____mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ__init____mutmut['xǁVanillaTektonAdapterǁ__init____mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁlist_task_runs__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_task_runs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_task_runs__mutmut['xǁVanillaTektonAdapterǁlist_task_runs__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_task_runs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_task_runs__mutmut['xǁVanillaTektonAdapterǁlist_task_runs__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_task_runs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_task_runs__mutmut['xǁVanillaTektonAdapterǁlist_task_runs__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_task_runs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_task_runs__mutmut['xǁVanillaTektonAdapterǁlist_task_runs__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_task_runs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_task_runs__mutmut['xǁVanillaTektonAdapterǁlist_task_runs__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_task_runs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_task_runs__mutmut['xǁVanillaTektonAdapterǁlist_task_runs__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_task_runs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_task_runs__mutmut['xǁVanillaTektonAdapterǁlist_task_runs__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_task_runs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_task_runs__mutmut['xǁVanillaTektonAdapterǁlist_task_runs__mutmut_8'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_task_runs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_task_runs__mutmut['xǁVanillaTektonAdapterǁlist_task_runs__mutmut_9'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_task_runs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_task_runs__mutmut['xǁVanillaTektonAdapterǁlist_task_runs__mutmut_10'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_task_runs__mutmut_10 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_8'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_9'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_10'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_pipeline_runs__mutmut_10 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁlist_pipeline_runs_in_namespace__mutmut_5 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_8'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_9'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_10'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_11'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_12'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_13'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_14'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_15'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_16'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_17'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_18'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_19'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_20'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_21'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_22'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_23'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_24'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs_in_namespace__mutmut_24 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_8'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_9'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_10'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_11'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_12'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_13'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_14'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_15'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_16'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_17'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_18'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_19'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_20'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_21'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_22'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_23'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_24'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_25'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_26'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_27'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_28'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_29'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_30'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_31'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_32'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_33'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_34'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_35'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_36'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_37'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_37 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_38'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_38 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_39'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_39 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_40'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_40 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_41'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_41 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_42'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_42 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_43'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_43 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_44'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_44 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_45'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_45 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_46'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_46 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_47'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_47 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_48'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_48 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_49'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_49 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_50'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_50 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_51'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_51 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_52'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_52 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_53'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_53 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_54'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_54 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_55'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_55 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_56'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_56 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_57'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_57 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_58'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_58 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_59'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_59 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_60'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_60 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_61'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_61 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_62'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_namespaced_pipeline_run_info__mutmut_62 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_8'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_9'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_10'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_11'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_12'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_13'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_14'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_15'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_16'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_17'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_18'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_19'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_20'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_21'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_22'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_23'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_24'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_25'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_26'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_27'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_28'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_pipeline_ref__mutmut_28 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_8'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_9'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_10'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_11'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_pipeline_runs__mutmut_11 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_8'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_9'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_10'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_11'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_12'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_13'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_14'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_15'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_16'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_17'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_18'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_19'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_20'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_21'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_22'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_23'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_24'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_25'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_26'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_27'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_28'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_29'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_30'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_31'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_32'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_33'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_34'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_35'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_36'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_37'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_37 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_38'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_38 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_39'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_39 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_40'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_40 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_41'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_41 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_42'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_42 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_43'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_43 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_44'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_44 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_45'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_45 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_46'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_46 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_47'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_47 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_48'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_48 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_49'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_49 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_50'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_50 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_51'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_51 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_52'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_52 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_53'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_53 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_54'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_54 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_55'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_55 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_56'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_56 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_57'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_pipeline_run_info__mutmut_57 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_8'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_9'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_10'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_11'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_12'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_13'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_14'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_15'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_16'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_17'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_18'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_19'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_20'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_21'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_22'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_23'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_24'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_25'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_26'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_27'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_28'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_29'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_30'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_31'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_32'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_33'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_34'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_35'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_36'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_37'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_37 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_38'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_38 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_39'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_39 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_40'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_40 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_41'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_41 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_42'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_42 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_43'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_43 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_44'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_44 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_45'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_45 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_46'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_46 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_47'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_47 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_48'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_48 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_49'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_49 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_50'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_50 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_51'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_51 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_52'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_52 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_53'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_53 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_54'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_54 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_55'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_55 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_56'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_56 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_57'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_57 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_58'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_58 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_59'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_59 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_60'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_60 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_61'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_61 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_62'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_62 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_63'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_63 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_64'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_64 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_65'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_65 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_66'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_66 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_67'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_67 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_68'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_68 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_69'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_69 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_70'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_70 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_71'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_71 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_72'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_72 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_73'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_73 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_74'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_74 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_75'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_75 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_76'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_76 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_77'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_77 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_78'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_78 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_79'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_79 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_80'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_80 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_81'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_81 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_82'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_status__mutmut_82 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_8'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_9'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_10'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_11'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_12'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_13'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_14'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_15'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_16'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_17'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_18'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_19'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_20'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_21'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_22'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut['xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_23'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_pipeline_run_duration_seconds__mutmut_23 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut['xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut['xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut['xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut['xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut['xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut['xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut['xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut['xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_8'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut['xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_9'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_seconds_to_human__mutmut_9 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_8'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_9'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_10'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_11'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_12'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_13'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_14'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_15'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_16'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_17'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_18'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_19'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_20'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_21'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_22'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_23'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_24'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_25'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_26'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut['xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_27'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_triggered_by__mutmut_27 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_8'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_9'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_10'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut['xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_11'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_fetch_task_runs__mutmut_11 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_8'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_9'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_10'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_11'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_12'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_13'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_14'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_15'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_16'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_17'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_18'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_19'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_20'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_21'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_22'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_23'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_24'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_25'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_26'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_27'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_28'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_29'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_30'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_31'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_32'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_33'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_34'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_35'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_36'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_37'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_37 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_38'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_38 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_39'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_39 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_40'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_40 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_41'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_41 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_42'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_42 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_43'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_43 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_44'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_44 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_45'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_45 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_46'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_46 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_47'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_47 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_48'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_48 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_49'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_49 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_50'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_50 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_51'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_51 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_52'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_52 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_53'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_53 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_54'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_54 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_55'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_55 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_56'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_56 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_57'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_57 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_58'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_58 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_59'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_59 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_60'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_60 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut['xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_61'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_to_task_run_info__mutmut_61 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_8'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_9'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_10'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_11'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_12'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_13'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_14'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_15'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_16'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_17'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_18'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_19'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_20'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_21'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut['xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_22'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_task_ref__mutmut_22 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_8'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_9'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_10'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_11'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_12'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_13'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_14'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_15'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_16'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_17'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_18'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_19'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_20'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_21'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_22'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_23'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_24'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_25'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_26'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_27'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_28'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_29'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_30'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_31'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_32'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_33'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_34'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_35'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_36'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_37'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_37 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_38'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_38 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_39'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_39 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_40'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_40 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_41'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_41 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_42'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_42 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_43'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_43 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_44'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_44 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_45'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_45 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_46'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_46 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_47'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_47 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_48'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_48 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_49'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_49 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_50'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_50 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_51'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_51 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_52'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_52 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_53'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_53 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_54'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_54 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_55'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_55 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_56'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_56 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_57'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_57 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_58'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_58 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_59'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_59 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_60'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_60 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_61'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_61 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_62'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_62 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_63'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_63 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_64'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_64 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_65'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_65 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_66'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_66 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_67'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_67 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_68'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_68 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_69'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_69 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_70'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_70 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_71'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_71 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_72'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_72 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_73'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_73 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_74'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_74 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_75'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_75 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_76'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_76 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_77'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_77 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_78'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_78 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_79'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_79 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_80'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_80 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_81'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_81 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_82'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_82 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_83'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_83 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_status__mutmut['xǁVanillaTektonAdapterǁ_task_run_status__mutmut_84'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_status__mutmut_84 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_task_run_duration__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_duration__mutmut['xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_duration__mutmut['xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_duration__mutmut['xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_duration__mutmut['xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_duration__mutmut['xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_duration__mutmut['xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_duration__mutmut['xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_duration__mutmut['xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_8'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_duration__mutmut['xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_9'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_duration__mutmut['xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_10'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_duration__mutmut['xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_11'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_duration__mutmut['xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_12'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_duration__mutmut['xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_13'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_duration__mutmut['xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_14'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_duration__mutmut['xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_15'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_task_run_duration__mutmut['xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_16'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_task_run_duration__mutmut_16 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_8'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_9'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_10'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_11'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_12'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_13'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_14'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_15'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_16'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_17'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_18'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_19'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_20'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_21'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_22'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_23'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_24'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_25'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_26'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_27'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_28'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_29'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_30'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_31'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_32'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_33'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_34'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_35'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_36'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_37'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_37 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_38'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_38 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_39'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_39 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_40'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_40 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_41'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_41 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_42'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_42 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_43'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_43 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_44'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_44 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut['xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_45'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_extract_failing_step__mutmut_45 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_8'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_9'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_10'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_11'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_12'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_13'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_14'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_15'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_16'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_17'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_18'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_19'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_20'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_21'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_22'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_23'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_step_error__mutmut['xǁVanillaTektonAdapterǁ_step_error__mutmut_24'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_step_error__mutmut_24 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_8'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_9'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_10'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_11'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_12'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_13'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_14'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_15'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_16'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_17'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_18'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_19'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_20'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_21'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_22'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_23'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_24'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_25'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_elapsed_between__mutmut['xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_26'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_elapsed_between__mutmut_26 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_crd_items__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_items__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_items__mutmut['xǁVanillaTektonAdapterǁ_crd_items__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_items__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_items__mutmut['xǁVanillaTektonAdapterǁ_crd_items__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_items__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_items__mutmut['xǁVanillaTektonAdapterǁ_crd_items__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_items__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_items__mutmut['xǁVanillaTektonAdapterǁ_crd_items__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_items__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_items__mutmut['xǁVanillaTektonAdapterǁ_crd_items__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_items__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_items__mutmut['xǁVanillaTektonAdapterǁ_crd_items__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_items__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_items__mutmut['xǁVanillaTektonAdapterǁ_crd_items__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_items__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_items__mutmut['xǁVanillaTektonAdapterǁ_crd_items__mutmut_8'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_items__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_items__mutmut['xǁVanillaTektonAdapterǁ_crd_items__mutmut_9'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_items__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_items__mutmut['xǁVanillaTektonAdapterǁ_crd_items__mutmut_10'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_items__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_items__mutmut['xǁVanillaTektonAdapterǁ_crd_items__mutmut_11'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_items__mutmut_11 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_crd_mapping__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_mapping__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_mapping__mutmut['xǁVanillaTektonAdapterǁ_crd_mapping__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_mapping__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_mapping__mutmut['xǁVanillaTektonAdapterǁ_crd_mapping__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_mapping__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_mapping__mutmut['xǁVanillaTektonAdapterǁ_crd_mapping__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_mapping__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_mapping__mutmut['xǁVanillaTektonAdapterǁ_crd_mapping__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_mapping__mutmut_4 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_crd_str__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_str__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_str__mutmut['xǁVanillaTektonAdapterǁ_crd_str__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_str__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_str__mutmut['xǁVanillaTektonAdapterǁ_crd_str__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_str__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_str__mutmut['xǁVanillaTektonAdapterǁ_crd_str__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_str__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_str__mutmut['xǁVanillaTektonAdapterǁ_crd_str__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_str__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_str__mutmut['xǁVanillaTektonAdapterǁ_crd_str__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_str__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_str__mutmut['xǁVanillaTektonAdapterǁ_crd_str__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_str__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_str__mutmut['xǁVanillaTektonAdapterǁ_crd_str__mutmut_7'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_str__mutmut_7 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_crd_optional_str__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_optional_str__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_optional_str__mutmut['xǁVanillaTektonAdapterǁ_crd_optional_str__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_optional_str__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_optional_str__mutmut['xǁVanillaTektonAdapterǁ_crd_optional_str__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_optional_str__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_optional_str__mutmut['xǁVanillaTektonAdapterǁ_crd_optional_str__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_optional_str__mutmut_3 # type: ignore # mutmut generated

mutants_xǁVanillaTektonAdapterǁ_crd_api_client__mutmut['_mutmut_orig'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_api_client__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_api_client__mutmut['xǁVanillaTektonAdapterǁ_crd_api_client__mutmut_1'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_api_client__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_api_client__mutmut['xǁVanillaTektonAdapterǁ_crd_api_client__mutmut_2'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_api_client__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_api_client__mutmut['xǁVanillaTektonAdapterǁ_crd_api_client__mutmut_3'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_api_client__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_api_client__mutmut['xǁVanillaTektonAdapterǁ_crd_api_client__mutmut_4'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_api_client__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_api_client__mutmut['xǁVanillaTektonAdapterǁ_crd_api_client__mutmut_5'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_api_client__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaTektonAdapterǁ_crd_api_client__mutmut['xǁVanillaTektonAdapterǁ_crd_api_client__mutmut_6'] = VanillaTektonAdapter.xǁVanillaTektonAdapterǁ_crd_api_client__mutmut_6 # type: ignore # mutmut generated
