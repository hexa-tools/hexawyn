from __future__ import annotations

from hexawyn.application.ports.driven.tls_compliance_port import (
    TLSCompliancePort,
    TLSServiceRawData,
)
from kubernetes import client, config


class TLSComplianceAdapter(TLSCompliancePort):
    def scan_services(self) -> list[TLSServiceRawData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            secrets = v1.list_secret_for_all_namespaces()
            services = v1.list_service_for_all_namespaces()

            tls_services: set[str] = set()
            for secret in secrets.items:
                if not secret.metadata:
                    continue
                if secret.type == "kubernetes.io/tls":
                    tls_services.add(f"{secret.metadata.namespace}/{secret.metadata.name}")

            result: list[TLSServiceRawData] = []
            for svc in services.items:
                if not svc.metadata:
                    continue
                uses_tls = any(
                    f"{svc.metadata.namespace}/{s}" in tls_services
                    or svc.metadata.name
                    in str(getattr(getattr(svc.spec, "ports", [{}])[0], "name", ""))
                    for s in [svc.metadata.name]
                    if s
                )
                result.append(
                    TLSServiceRawData(  # type: ignore
                        name=svc.metadata.name or "",
                        namespace=svc.metadata.namespace or "",
                        tls_enabled=uses_tls,
                    )
                )
            return result
        except Exception:
            return []
