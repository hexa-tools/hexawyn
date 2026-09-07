from __future__ import annotations

from hexawyn.application.ports.driven.pipeline_for_service_port import (
    PipelineForServicePort,
)
from hexawyn.domain.models.pipeline_for_service import (
    PipelineForServiceRequest,
    ServicePipeline,
)
from kubernetes import client, config


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut: MutantDict = {}  # type: ignore


class KubernetesPipelineForServiceAdapter(PipelineForServicePort):
    @_mutmut_mutated(mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut)
    def find_pipelines(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_orig(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_1(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = None

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_2(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = None
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_3(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = None

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_4(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "XXdefaultXX"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_5(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "DEFAULT"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_6(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = None
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_7(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group=None,
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_8(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version=None,
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_9(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=None,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_10(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural=None,
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_11(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_12(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_13(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_14(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_15(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="XXtekton.devXX",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_16(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="TEKTON.DEV",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_17(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="XXv1XX",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_18(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="V1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_19(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="XXpipelinerunsXX",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_20(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="PIPELINERUNS",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_21(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get(None, []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_22(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", None):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_23(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get([]):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_24(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", ):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_25(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("XXitemsXX", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_26(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("ITEMS", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_27(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = None
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_28(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get(None, {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_29(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", None)
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_30(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get({})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_31(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", )
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_32(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("XXmetadataXX", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_33(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("METADATA", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_34(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = None
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_35(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get(None, "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_36(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", None)
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_37(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_38(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", )
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_39(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("XXnameXX", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_40(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("NAME", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_41(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "XXXX")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_42(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = None

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_43(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get(None, {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_44(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", None)

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_45(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get({})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_46(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", )

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_47(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("XXlabelsXX", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_48(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("LABELS", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_49(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = None
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_50(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get(None, "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_51(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", None)
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_52(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_53(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", )
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_54(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("XXapp.kubernetes.io/nameXX", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_55(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("APP.KUBERNETES.IO/NAME", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_56(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "XXXX")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_57(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = None

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_58(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get(None, "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_59(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", None)

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_60(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_61(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", )

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_62(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get(None, {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_63(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", None).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_64(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get({}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_65(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", ).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_66(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get(None, {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_67(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", None).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_68(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get({}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_69(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", ).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_70(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("XXspecXX", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_71(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("SPEC", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_72(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("XXpipelineRefXX", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_73(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineref", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_74(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("PIPELINEREF", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_75(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("XXnameXX", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_76(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("NAME", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_77(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "XXXX")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_78(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name or request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_79(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_80(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        break

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_81(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = None
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_82(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = "XXXX"
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_83(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = None
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_84(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get(None, [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_85(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", None)
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_86(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get([])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_87(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", )
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_88(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get(None, {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_89(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", None).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_90(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get({}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_91(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", ).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_92(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("XXstatusXX", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_93(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("STATUS", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_94(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("XXconditionsXX", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_95(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("CONDITIONS", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_96(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get(None) == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_97(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("XXtypeXX") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_98(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("TYPE") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_99(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") != "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_100(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "XXSucceededXX":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_101(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_102(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "SUCCEEDED":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_103(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = None
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_104(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(None)
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_105(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get(None, "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_106(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", None))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_107(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_108(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", ))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_109(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("XXstatusXX", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_110(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("STATUS", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_111(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "XXUnknownXX"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_112(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_113(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "UNKNOWN"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_114(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            return

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_115(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        None
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_116(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=None,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_117(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=None,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_118(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url=None,
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_119(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch=None,
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_120(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger=None,
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_121(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=None,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_122(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=None,
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_123(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_124(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_125(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_126(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_127(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_128(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_129(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_130(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref and name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_131(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="XXXX",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_132(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="XXXX",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_133(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="XXmanualXX",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_134(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="MANUAL",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_135(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(None),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_136(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get(None, "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_137(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", None)),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_138(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_139(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", )),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_140(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get(None, {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_141(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", None).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_142(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get({}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_143(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", ).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_144(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("XXstatusXX", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_145(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("STATUS", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_146(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("XXstartTimeXX", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_147(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("starttime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_148(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("STARTTIME", "")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_149(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "XXXX")),
                        )
                    )
            except Exception:
                pass

            return result[:10]
        except Exception:
            return []
    def xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_150(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        try:
            config.load_kube_config()
            crd = client.CustomObjectsApi()

            result: list[ServicePipeline] = []
            namespace = "default"

            try:
                pipelineruns = crd.list_namespaced_custom_object(
                    group="tekton.dev",
                    version="v1",
                    namespace=namespace,
                    plural="pipelineruns",
                )
                for pr in pipelineruns.get("items", []):
                    metadata = pr.get("metadata", {})
                    name = metadata.get("name", "")
                    labels = metadata.get("labels", {})

                    service_label = labels.get("app.kubernetes.io/name", "")
                    pipeline_ref = pr.get("spec", {}).get("pipelineRef", {}).get("name", "")

                    if request.service_name and request.service_name not in (
                        name,
                        service_label,
                        pipeline_ref,
                    ):
                        continue

                    status = ""
                    conditions = pr.get("status", {}).get("conditions", [])
                    for cond in conditions:
                        if cond.get("type") == "Succeeded":
                            status = str(cond.get("status", "Unknown"))
                            break

                    result.append(
                        ServicePipeline(
                            pipeline_name=pipeline_ref or name,
                            namespace=namespace,
                            repo_url="",
                            branch="",
                            trigger="manual",
                            last_run_status=status,
                            last_run_timestamp=str(pr.get("status", {}).get("startTime", "")),
                        )
                    )
            except Exception:
                pass

            return result[:11]
        except Exception:
            return []

mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['_mutmut_orig'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_1'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_2'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_3'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_4'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_5'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_6'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_7'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_8'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_9'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_10'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_11'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_12'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_13'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_14'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_15'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_16'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_17'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_18'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_19'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_20'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_21'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_22'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_23'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_24'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_25'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_26'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_27'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_28'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_29'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_30'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_31'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_32'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_32 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_33'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_33 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_34'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_34 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_35'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_35 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_36'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_36 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_37'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_37 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_38'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_38 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_39'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_39 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_40'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_40 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_41'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_41 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_42'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_42 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_43'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_43 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_44'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_44 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_45'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_45 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_46'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_46 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_47'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_47 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_48'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_48 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_49'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_49 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_50'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_50 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_51'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_51 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_52'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_52 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_53'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_53 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_54'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_54 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_55'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_55 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_56'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_56 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_57'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_57 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_58'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_58 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_59'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_59 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_60'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_60 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_61'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_61 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_62'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_62 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_63'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_63 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_64'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_64 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_65'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_65 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_66'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_66 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_67'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_67 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_68'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_68 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_69'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_69 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_70'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_70 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_71'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_71 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_72'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_72 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_73'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_73 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_74'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_74 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_75'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_75 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_76'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_76 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_77'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_77 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_78'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_78 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_79'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_79 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_80'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_80 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_81'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_81 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_82'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_82 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_83'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_83 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_84'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_84 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_85'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_85 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_86'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_86 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_87'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_87 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_88'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_88 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_89'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_89 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_90'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_90 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_91'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_91 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_92'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_92 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_93'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_93 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_94'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_94 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_95'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_95 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_96'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_96 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_97'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_97 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_98'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_98 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_99'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_99 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_100'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_100 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_101'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_101 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_102'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_102 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_103'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_103 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_104'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_104 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_105'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_105 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_106'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_106 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_107'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_107 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_108'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_108 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_109'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_109 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_110'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_110 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_111'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_111 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_112'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_112 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_113'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_113 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_114'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_114 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_115'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_115 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_116'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_116 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_117'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_117 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_118'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_118 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_119'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_119 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_120'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_120 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_121'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_121 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_122'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_122 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_123'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_123 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_124'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_124 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_125'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_125 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_126'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_126 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_127'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_127 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_128'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_128 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_129'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_129 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_130'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_130 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_131'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_131 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_132'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_132 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_133'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_133 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_134'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_134 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_135'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_135 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_136'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_136 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_137'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_137 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_138'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_138 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_139'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_139 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_140'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_140 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_141'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_141 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_142'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_142 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_143'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_143 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_144'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_144 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_145'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_145 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_146'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_146 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_147'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_147 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_148'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_148 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_149'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_149 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut['xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_150'] = KubernetesPipelineForServiceAdapter.xǁKubernetesPipelineForServiceAdapterǁfind_pipelines__mutmut_150 # type: ignore # mutmut generated
