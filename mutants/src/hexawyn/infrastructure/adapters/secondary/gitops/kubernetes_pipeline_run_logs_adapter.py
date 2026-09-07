from __future__ import annotations

from hexawyn.application.ports.driven.pipeline_run_logs_port import PipelineRunLogsPort
from hexawyn.domain.models.pipeline_run_logs import PipelineRunLogsRequest, StepLog
from kubernetes import client, config


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut: MutantDict = {}  # type: ignore


class KubernetesPipelineRunLogsAdapter(PipelineRunLogsPort):
    @_mutmut_mutated(mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut)
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_orig(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_1(self, request: PipelineRunLogsRequest) -> list[StepLog]:
        try:
            config.load_kube_config()
            v1 = None

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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_2(self, request: PipelineRunLogsRequest) -> list[StepLog]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespace = None
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_3(self, request: PipelineRunLogsRequest) -> list[StepLog]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespace = request.namespace and "default"
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_4(self, request: PipelineRunLogsRequest) -> list[StepLog]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespace = request.namespace or "XXdefaultXX"
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_5(self, request: PipelineRunLogsRequest) -> list[StepLog]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespace = request.namespace or "DEFAULT"
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_6(self, request: PipelineRunLogsRequest) -> list[StepLog]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespace = request.namespace or "default"
            pipeline_run_name = None

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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_7(self, request: PipelineRunLogsRequest) -> list[StepLog]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespace = request.namespace or "default"
            pipeline_run_name = request.pipeline_run_name

            pods = None

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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_8(self, request: PipelineRunLogsRequest) -> list[StepLog]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespace = request.namespace or "default"
            pipeline_run_name = request.pipeline_run_name

            pods = v1.list_namespaced_pod(
                namespace=None,
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_9(self, request: PipelineRunLogsRequest) -> list[StepLog]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespace = request.namespace or "default"
            pipeline_run_name = request.pipeline_run_name

            pods = v1.list_namespaced_pod(
                namespace=namespace,
                label_selector=None,
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_10(self, request: PipelineRunLogsRequest) -> list[StepLog]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespace = request.namespace or "default"
            pipeline_run_name = request.pipeline_run_name

            pods = v1.list_namespaced_pod(
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_11(self, request: PipelineRunLogsRequest) -> list[StepLog]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespace = request.namespace or "default"
            pipeline_run_name = request.pipeline_run_name

            pods = v1.list_namespaced_pod(
                namespace=namespace,
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_12(self, request: PipelineRunLogsRequest) -> list[StepLog]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespace = request.namespace or "default"
            pipeline_run_name = request.pipeline_run_name

            pods = v1.list_namespaced_pod(
                namespace=namespace,
                label_selector=f"tekton.dev/pipelineRun={pipeline_run_name}",
            )

            result: list[StepLog] = None
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_13(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                if pod.metadata:
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_14(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                    break

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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_15(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                    step_name = None
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_16(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                    if step_name not in ("prepare", "place-tools", "working-dir-init"):
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_17(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                    if step_name in ("XXprepareXX", "place-tools", "working-dir-init"):
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_18(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                    if step_name in ("PREPARE", "place-tools", "working-dir-init"):
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_19(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                    if step_name in ("prepare", "XXplace-toolsXX", "working-dir-init"):
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_20(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                    if step_name in ("prepare", "PLACE-TOOLS", "working-dir-init"):
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_21(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                    if step_name in ("prepare", "place-tools", "XXworking-dir-initXX"):
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_22(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                    if step_name in ("prepare", "place-tools", "WORKING-DIR-INIT"):
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_23(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                        break

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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_24(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                        logs = None
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_25(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                            name=None,
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_26(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                            namespace=None,
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_27(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                            container=None,
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_28(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                            tail_lines=None,
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_29(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_30(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_31(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_32(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_33(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                            tail_lines=51,
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_34(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                            None
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_35(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                                step_name=None,
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_36(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                                log_lines=None,
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_37(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                                status=None,  # type: ignore
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_38(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                                truncated=None,
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_39(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_40(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_41(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_42(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_43(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                                log_lines=logs.split(None) if logs else [],
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_44(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                                log_lines=logs.split("XX\nXX") if logs else [],
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_45(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                                status="XXcompletedXX",  # type: ignore
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_46(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                                status="COMPLETED",  # type: ignore
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_47(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                                truncated=True,
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
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_48(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                            None
                        )

            return result
        except Exception:
            return []
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_49(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                                step_name=None,
                                log_lines=[],
                                status="pending",  # type: ignore
                                truncated=False,
                            )
                        )

            return result
        except Exception:
            return []
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_50(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                                log_lines=None,
                                status="pending",  # type: ignore
                                truncated=False,
                            )
                        )

            return result
        except Exception:
            return []
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_51(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                                status=None,  # type: ignore
                                truncated=False,
                            )
                        )

            return result
        except Exception:
            return []
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_52(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                                truncated=None,
                            )
                        )

            return result
        except Exception:
            return []
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_53(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                                log_lines=[],
                                status="pending",  # type: ignore
                                truncated=False,
                            )
                        )

            return result
        except Exception:
            return []
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_54(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                                status="pending",  # type: ignore
                                truncated=False,
                            )
                        )

            return result
        except Exception:
            return []
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_55(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                                truncated=False,
                            )
                        )

            return result
        except Exception:
            return []
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_56(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                                )
                        )

            return result
        except Exception:
            return []
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_57(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                                status="XXpendingXX",  # type: ignore
                                truncated=False,
                            )
                        )

            return result
        except Exception:
            return []
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_58(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                                status="PENDING",  # type: ignore
                                truncated=False,
                            )
                        )

            return result
        except Exception:
            return []
    def xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_59(self, request: PipelineRunLogsRequest) -> list[StepLog]:
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
                                truncated=True,
                            )
                        )

            return result
        except Exception:
            return []

mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['_mutmut_orig'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_1'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_2'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_3'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_4'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_5'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_6'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_7'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_8'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_9'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_10'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_11'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_12'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_13'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_14'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_15'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_16'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_17'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_18'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_19'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_20'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_21'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_22'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_23'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_24'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_25'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_26'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_27'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_28'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_29'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_30'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_31'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_32'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_32 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_33'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_33 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_34'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_34 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_35'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_35 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_36'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_36 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_37'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_37 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_38'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_38 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_39'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_39 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_40'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_40 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_41'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_41 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_42'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_42 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_43'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_43 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_44'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_44 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_45'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_45 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_46'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_46 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_47'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_47 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_48'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_48 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_49'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_49 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_50'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_50 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_51'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_51 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_52'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_52 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_53'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_53 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_54'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_54 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_55'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_55 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_56'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_56 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_57'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_57 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_58'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_58 # type: ignore # mutmut generated
mutants_xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut['xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_59'] = KubernetesPipelineRunLogsAdapter.xǁKubernetesPipelineRunLogsAdapterǁfetch_step_logs__mutmut_59 # type: ignore # mutmut generated
