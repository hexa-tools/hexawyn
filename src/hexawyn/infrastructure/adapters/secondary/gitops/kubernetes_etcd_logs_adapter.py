from __future__ import annotations

from hexawyn.application.ports.driven.etcd_logs_port import ETCDLogsPort
from hexawyn.domain.models.etcd_logs import ETCDLogLine, ETCDLogsRequest
from kubernetes import client, config


class KubernetesETCDLogsAdapter(ETCDLogsPort):
    def fetch_logs(self, request: ETCDLogsRequest) -> list[ETCDLogLine]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            pods = v1.list_pod_for_all_namespaces(
                label_selector="component=etcd,tier=control-plane"
            )
            result: list[ETCDLogLine] = []
            for pod in pods.items:
                if pod.metadata and pod.metadata.namespace:
                    try:
                        logs = v1.read_namespaced_pod_log(
                            name=pod.metadata.name,
                            namespace=pod.metadata.namespace,
                            tail_lines=50,
                        )
                        for i, line in enumerate(logs.split("\n")):
                            if line.strip():
                                result.append(
                                    ETCDLogLine(
                                        timestamp="",
                                        level="info",
                                        message=line[:200],
                                    )
                                )
                    except Exception:
                        continue
            return result
        except Exception:
            return []
