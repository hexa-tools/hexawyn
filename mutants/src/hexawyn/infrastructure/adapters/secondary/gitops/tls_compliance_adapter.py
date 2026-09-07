from __future__ import annotations

from hexawyn.application.ports.driven.tls_compliance_port import (
    TLSCompliancePort,
    TLSServiceRawData,
)
from kubernetes import client, config


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut: MutantDict = {}  # type: ignore


class TLSComplianceAdapter(TLSCompliancePort):
    @_mutmut_mutated(mutants_xǁTLSComplianceAdapterǁscan_services__mutmut)
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_orig(self) -> list[TLSServiceRawData]:
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_1(self) -> list[TLSServiceRawData]:
        try:
            config.load_kube_config()
            v1 = None

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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_2(self) -> list[TLSServiceRawData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            secrets = None
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_3(self) -> list[TLSServiceRawData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            secrets = v1.list_secret_for_all_namespaces()
            services = None

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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_4(self) -> list[TLSServiceRawData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            secrets = v1.list_secret_for_all_namespaces()
            services = v1.list_service_for_all_namespaces()

            tls_services: set[str] = None
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_5(self) -> list[TLSServiceRawData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            secrets = v1.list_secret_for_all_namespaces()
            services = v1.list_service_for_all_namespaces()

            tls_services: set[str] = set()
            for secret in secrets.items:
                if secret.metadata:
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_6(self) -> list[TLSServiceRawData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            secrets = v1.list_secret_for_all_namespaces()
            services = v1.list_service_for_all_namespaces()

            tls_services: set[str] = set()
            for secret in secrets.items:
                if not secret.metadata:
                    break
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_7(self) -> list[TLSServiceRawData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            secrets = v1.list_secret_for_all_namespaces()
            services = v1.list_service_for_all_namespaces()

            tls_services: set[str] = set()
            for secret in secrets.items:
                if not secret.metadata:
                    continue
                if secret.type != "kubernetes.io/tls":
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_8(self) -> list[TLSServiceRawData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            secrets = v1.list_secret_for_all_namespaces()
            services = v1.list_service_for_all_namespaces()

            tls_services: set[str] = set()
            for secret in secrets.items:
                if not secret.metadata:
                    continue
                if secret.type == "XXkubernetes.io/tlsXX":
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_9(self) -> list[TLSServiceRawData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            secrets = v1.list_secret_for_all_namespaces()
            services = v1.list_service_for_all_namespaces()

            tls_services: set[str] = set()
            for secret in secrets.items:
                if not secret.metadata:
                    continue
                if secret.type == "KUBERNETES.IO/TLS":
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_10(self) -> list[TLSServiceRawData]:
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
                    tls_services.add(None)

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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_11(self) -> list[TLSServiceRawData]:
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

            result: list[TLSServiceRawData] = None
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_12(self) -> list[TLSServiceRawData]:
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
                if svc.metadata:
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_13(self) -> list[TLSServiceRawData]:
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
                    break
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_14(self) -> list[TLSServiceRawData]:
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
                uses_tls = None
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_15(self) -> list[TLSServiceRawData]:
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
                    None
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_16(self) -> list[TLSServiceRawData]:
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
                    f"{svc.metadata.namespace}/{s}" in tls_services and svc.metadata.name
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_17(self) -> list[TLSServiceRawData]:
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
                    f"{svc.metadata.namespace}/{s}" not in tls_services
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_18(self) -> list[TLSServiceRawData]:
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
                    or svc.metadata.name not in str(getattr(getattr(svc.spec, "ports", [{}])[0], "name", ""))
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_19(self) -> list[TLSServiceRawData]:
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
                    in str(None)
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_20(self) -> list[TLSServiceRawData]:
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
                    in str(getattr(None, "name", ""))
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_21(self) -> list[TLSServiceRawData]:
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
                    in str(getattr(getattr(svc.spec, "ports", [{}])[0], None, ""))
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_22(self) -> list[TLSServiceRawData]:
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
                    in str(getattr(getattr(svc.spec, "ports", [{}])[0], "name", None))
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_23(self) -> list[TLSServiceRawData]:
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
                    in str(getattr("name", ""))
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_24(self) -> list[TLSServiceRawData]:
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
                    in str(getattr(getattr(svc.spec, "ports", [{}])[0], ""))
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_25(self) -> list[TLSServiceRawData]:
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
                    in str(getattr(getattr(svc.spec, "ports", [{}])[0], "name", ))
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_26(self) -> list[TLSServiceRawData]:
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
                    in str(getattr(getattr(None, "ports", [{}])[0], "name", ""))
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_27(self) -> list[TLSServiceRawData]:
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
                    in str(getattr(getattr(svc.spec, None, [{}])[0], "name", ""))
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_28(self) -> list[TLSServiceRawData]:
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
                    in str(getattr(getattr(svc.spec, "ports", None)[0], "name", ""))
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_29(self) -> list[TLSServiceRawData]:
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
                    in str(getattr(getattr("ports", [{}])[0], "name", ""))
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_30(self) -> list[TLSServiceRawData]:
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
                    in str(getattr(getattr(svc.spec, [{}])[0], "name", ""))
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_31(self) -> list[TLSServiceRawData]:
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
                    in str(getattr(getattr(svc.spec, "ports", )[0], "name", ""))
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_32(self) -> list[TLSServiceRawData]:
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
                    in str(getattr(getattr(svc.spec, "XXportsXX", [{}])[0], "name", ""))
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_33(self) -> list[TLSServiceRawData]:
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
                    in str(getattr(getattr(svc.spec, "PORTS", [{}])[0], "name", ""))
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_34(self) -> list[TLSServiceRawData]:
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
                    in str(getattr(getattr(svc.spec, "ports", [{}])[1], "name", ""))
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_35(self) -> list[TLSServiceRawData]:
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
                    in str(getattr(getattr(svc.spec, "ports", [{}])[0], "XXnameXX", ""))
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_36(self) -> list[TLSServiceRawData]:
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
                    in str(getattr(getattr(svc.spec, "ports", [{}])[0], "NAME", ""))
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_37(self) -> list[TLSServiceRawData]:
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
                    in str(getattr(getattr(svc.spec, "ports", [{}])[0], "name", "XXXX"))
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
    def xǁTLSComplianceAdapterǁscan_services__mutmut_38(self) -> list[TLSServiceRawData]:
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
                    None
                )
            return result
        except Exception:
            return []
    def xǁTLSComplianceAdapterǁscan_services__mutmut_39(self) -> list[TLSServiceRawData]:
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
                        name=None,
                        namespace=svc.metadata.namespace or "",
                        tls_enabled=uses_tls,
                    )
                )
            return result
        except Exception:
            return []
    def xǁTLSComplianceAdapterǁscan_services__mutmut_40(self) -> list[TLSServiceRawData]:
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
                        namespace=None,
                        tls_enabled=uses_tls,
                    )
                )
            return result
        except Exception:
            return []
    def xǁTLSComplianceAdapterǁscan_services__mutmut_41(self) -> list[TLSServiceRawData]:
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
                        tls_enabled=None,
                    )
                )
            return result
        except Exception:
            return []
    def xǁTLSComplianceAdapterǁscan_services__mutmut_42(self) -> list[TLSServiceRawData]:
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
                        namespace=svc.metadata.namespace or "",
                        tls_enabled=uses_tls,
                    )
                )
            return result
        except Exception:
            return []
    def xǁTLSComplianceAdapterǁscan_services__mutmut_43(self) -> list[TLSServiceRawData]:
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
                        tls_enabled=uses_tls,
                    )
                )
            return result
        except Exception:
            return []
    def xǁTLSComplianceAdapterǁscan_services__mutmut_44(self) -> list[TLSServiceRawData]:
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
                        )
                )
            return result
        except Exception:
            return []
    def xǁTLSComplianceAdapterǁscan_services__mutmut_45(self) -> list[TLSServiceRawData]:
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
                        name=svc.metadata.name and "",
                        namespace=svc.metadata.namespace or "",
                        tls_enabled=uses_tls,
                    )
                )
            return result
        except Exception:
            return []
    def xǁTLSComplianceAdapterǁscan_services__mutmut_46(self) -> list[TLSServiceRawData]:
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
                        name=svc.metadata.name or "XXXX",
                        namespace=svc.metadata.namespace or "",
                        tls_enabled=uses_tls,
                    )
                )
            return result
        except Exception:
            return []
    def xǁTLSComplianceAdapterǁscan_services__mutmut_47(self) -> list[TLSServiceRawData]:
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
                        namespace=svc.metadata.namespace and "",
                        tls_enabled=uses_tls,
                    )
                )
            return result
        except Exception:
            return []
    def xǁTLSComplianceAdapterǁscan_services__mutmut_48(self) -> list[TLSServiceRawData]:
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
                        namespace=svc.metadata.namespace or "XXXX",
                        tls_enabled=uses_tls,
                    )
                )
            return result
        except Exception:
            return []

mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['_mutmut_orig'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_1'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_2'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_3'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_4'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_5'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_6'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_7'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_8'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_9'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_10'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_11'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_12'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_13'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_14'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_15'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_16'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_17'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_18'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_19'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_20'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_21'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_22'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_22 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_23'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_23 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_24'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_24 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_25'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_25 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_26'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_26 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_27'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_27 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_28'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_28 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_29'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_29 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_30'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_30 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_31'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_31 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_32'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_32 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_33'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_33 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_34'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_34 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_35'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_35 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_36'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_36 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_37'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_37 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_38'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_38 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_39'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_39 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_40'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_40 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_41'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_41 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_42'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_42 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_43'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_43 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_44'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_44 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_45'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_45 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_46'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_46 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_47'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_47 # type: ignore # mutmut generated
mutants_xǁTLSComplianceAdapterǁscan_services__mutmut['xǁTLSComplianceAdapterǁscan_services__mutmut_48'] = TLSComplianceAdapter.xǁTLSComplianceAdapterǁscan_services__mutmut_48 # type: ignore # mutmut generated
