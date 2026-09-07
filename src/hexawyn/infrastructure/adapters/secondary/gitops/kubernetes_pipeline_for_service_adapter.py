from __future__ import annotations

from hexawyn.application.ports.driven.pipeline_for_service_port import (
    PipelineForServicePort,
)
from hexawyn.domain.models.pipeline_for_service import (
    PipelineForServiceRequest,
    ServicePipeline,
)
from kubernetes import client, config


class KubernetesPipelineForServiceAdapter(PipelineForServicePort):
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
