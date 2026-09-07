from __future__ import annotations

from hexawyn.application.ports.driven.pipeline_run_logs_port import PipelineRunLogsPort
from hexawyn.domain.models.pipeline_run_logs import PipelineRunLogsRequest, StepLog
from kubernetes import client, config


class KubernetesPipelineRunLogsAdapter(PipelineRunLogsPort):
    def fetch_step_logs(self, request: PipelineRunLogsRequest) -> list[StepLog]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespace = request.namespace or "default"
            pipeline_run_name = request.pipeline_run_name

            pods = v1.list_namespaced_pod(
                namespace=namespace,
                label_selector=f"tekton.dev/pipelineRun={pipeline_run_name}",
            )

            result: list[StepLog] = []
            for pod in pods.items:
                if not pod.metadata:
                    continue

                for container in pod.spec.containers:
                    step_name = container.name
                    if step_name in ("prepare", "place-tools", "working-dir-init"):
                        continue

                    try:
                        logs = v1.read_namespaced_pod_log(
                            name=pod.metadata.name,
                            namespace=namespace,
                            container=step_name,
                            tail_lines=50,
                        )
                        result.append(
                            StepLog(
                                step_name=step_name,
                                log_lines=logs.split("\n") if logs else [],
                                status="completed",  # type: ignore
                                truncated=False,
                            )
                        )
                    except Exception:
                        result.append(
                            StepLog(
                                step_name=step_name,
                                log_lines=[],
                                status="pending",  # type: ignore
                                truncated=False,
                            )
                        )

            return result
        except Exception:
            return []
