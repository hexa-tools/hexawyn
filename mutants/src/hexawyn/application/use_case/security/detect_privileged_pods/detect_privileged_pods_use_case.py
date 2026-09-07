from __future__ import annotations

from hexawyn.application.ports.driven.pod_security_context_audit_port import (
    PodSecurityContextAuditPort,
)
from hexawyn.application.use_case.security.detect_privileged_pods.command import (
    DetectPrivilegedPodsCommand,
)
from hexawyn.application.use_case.security.detect_privileged_pods.mapper import (
    to_domain_spec,
    to_response,
)
from hexawyn.application.use_case.security.detect_privileged_pods.response import (
    DetectPrivilegedPodsResponse,
)
from hexawyn.domain.models.pod_security import PodSecurityFinding
from hexawyn.domain.services.pod_security.pod_security_report_builder import (
    build_report,
)
from hexawyn.domain.services.pod_security.scanner import scan_pod

_KNOWN_SYSTEM_FRAGMENTS = ("kube-proxy", "calico", "cilium", "fluentd")


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDetectPrivilegedPodsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class DetectPrivilegedPodsUseCase:
    @_mutmut_mutated(mutants_xǁDetectPrivilegedPodsUseCaseǁ__init____mutmut)
    def __init__(self, port: PodSecurityContextAuditPort) -> None:
        self._port = port
    def xǁDetectPrivilegedPodsUseCaseǁ__init____mutmut_orig(self, port: PodSecurityContextAuditPort) -> None:
        self._port = port
    def xǁDetectPrivilegedPodsUseCaseǁ__init____mutmut_1(self, port: PodSecurityContextAuditPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut)
    def execute(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_orig(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_1(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = None
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_2(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = None

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_3(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = None
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_4(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = None

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_5(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 1

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_6(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces or raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_7(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["XXnamespaceXX"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_8(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["NAMESPACE"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_9(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_10(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                break

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_11(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = None
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_12(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(None)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_13(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = None

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_14(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(None)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_15(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_16(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count = 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_17(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count -= 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_18(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 2
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_19(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                break

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_20(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = ""
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_21(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" or any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_22(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind != "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_23(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "XXDaemonSetXX" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_24(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "daemonset" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_25(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DAEMONSET" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_26(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                None
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_27(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag not in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_28(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = None

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_29(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "XXsystem workload — exempt from PSSXX"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_30(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from pss"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_31(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "SYSTEM WORKLOAD — EXEMPT FROM PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_32(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                None
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_33(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=None,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_34(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=None,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_35(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=None,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_36(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=None,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_37(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=None,
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_38(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_39(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_40(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_41(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_42(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_43(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        None,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_44(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = None
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_45(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=None,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_46(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=None,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_47(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=None,
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_48(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_49(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_50(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            )
        return DetectPrivilegedPodsResponse(**to_response(report))  # type: ignore

    def xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_51(
        self,
        command: DetectPrivilegedPodsCommand,
    ) -> DetectPrivilegedPodsResponse:
        raw_pods = self._port.list_pod_security_specs()
        psa_levels = self._port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_count = 0

        for raw in raw_pods:
            if command.namespaces and raw["namespace"] not in command.namespaces:
                continue

            spec = to_domain_spec(raw)
            violations = scan_pod(spec)

            if not violations:
                compliant_count += 1
                continue

            note: str | None = None
            if spec.owner_kind == "DaemonSet" and any(
                frag in spec.pod_name for frag in _KNOWN_SYSTEM_FRAGMENTS
            ):
                note = "system workload — exempt from PSS"

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(
                        spec.namespace,
                    ),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_count,
            total_pods_checked=len(raw_pods),
        )
        return DetectPrivilegedPodsResponse(**to_response(None))  # type: ignore

mutants_xǁDetectPrivilegedPodsUseCaseǁ__init____mutmut['_mutmut_orig'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁ__init____mutmut['xǁDetectPrivilegedPodsUseCaseǁ__init____mutmut_1'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['_mutmut_orig'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_1'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_2'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_3'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_4'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_5'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_6'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_7'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_8'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_9'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_10'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_11'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_12'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_13'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_14'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_15'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_16'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_17'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_18'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_19'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_20'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_21'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_22'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_23'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_24'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_25'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_26'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_27'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_28'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_29'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_30'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_31'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_32'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_33'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_34'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_35'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_36'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_37'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_38'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_39'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_40'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_41'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_42'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_43'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_44'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_45'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_46'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_47'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_48'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_49'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_50'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut['xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_51'] = DetectPrivilegedPodsUseCase.xǁDetectPrivilegedPodsUseCaseǁexecute__mutmut_51 # type: ignore # mutmut generated
