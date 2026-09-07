# mypy: ignore-errors
from __future__ import annotations

from hexawyn.application.ports.driven.pod_security_context_audit_port import (
    ContainerSecurityContextRaw,
    PodSecuritySpecRaw,
)
from hexawyn.application.use_case.governance.pod_security_standards_audit.command import (
    PodSecurityStandardsAuditCommand,
)
from hexawyn.application.use_case.governance.pod_security_standards_audit.response import (
    PodSecurityStandardsAuditResponse,
)
from hexawyn.application.use_case.security.detect_privileged_pods.response import (
    PodSecurityFindingDict,
    SecurityViolationDict,
)
from hexawyn.domain.models.constants import PodSecurityConstants
from hexawyn.domain.models.pod_security import (
    ContainerSecurityContext,
    PodSecurityAuditReport,
    PodSecurityFinding,
    PodSecuritySpec,
    SecurityViolation,
    ViolationType,
)
from hexawyn.domain.services.pod_security.fix_recommender import recommend_fix
from hexawyn.domain.services.pod_security.pod_security_report_builder import build_report
from hexawyn.domain.services.pod_security.security_context_parser import (
    allows_privilege_escalation,
    is_privileged,
    resolves_to_root,
)
from hexawyn.domain.services.pod_security.system_workload import is_known_system_daemonset
from hexawyn.domain.services.pod_security.violation_classifier import (
    classify_pss_level,
    classify_severity,
)

_cfg = PodSecurityConstants()
_SYSTEM_WORKLOAD_NOTE = "expected system workload (known system DaemonSet)"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPodSecurityStandardsAuditUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut: MutantDict = {}  # type: ignore


class PodSecurityStandardsAuditUseCase:
    @_mutmut_mutated(mutants_xǁPodSecurityStandardsAuditUseCaseǁ__init____mutmut)
    def __init__(self, pod_security_port: PodSecurityContextAuditPort) -> None:  # noqa: F821  # type: ignore
        self._pod_security_port = pod_security_port
    def xǁPodSecurityStandardsAuditUseCaseǁ__init____mutmut_orig(self, pod_security_port: PodSecurityContextAuditPort) -> None:  # noqa: F821  # type: ignore
        self._pod_security_port = pod_security_port
    def xǁPodSecurityStandardsAuditUseCaseǁ__init____mutmut_1(self, pod_security_port: PodSecurityContextAuditPort) -> None:  # noqa: F821  # type: ignore
        self._pod_security_port = None

    @_mutmut_mutated(mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut)
    def audit_pod_security(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_orig(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_1(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = None
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_2(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_3(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = None
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_4(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(None)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_5(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = None
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_6(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["XXnamespaceXX"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_7(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["NAMESPACE"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_8(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] not in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_9(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = None

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_10(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = None
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_11(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = None

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_12(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 1

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_13(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = None
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_14(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(None)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_15(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = None
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_16(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(None)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_17(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_18(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count = 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_19(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count -= 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_20(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 2
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_21(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                break

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_22(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = ""
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_23(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                None, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_24(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, None, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_25(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, None
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_26(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_27(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_28(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_29(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = None

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_30(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                None
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_31(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=None,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_32(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=None,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_33(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=None,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_34(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=None,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_35(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

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
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_36(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_37(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_38(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_39(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_40(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

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
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_41(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(None),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_42(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = None
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_43(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=None,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_44(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=None,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_45(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=None,
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_46(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_47(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_48(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            )
        return _to_response(report)

    def xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_49(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(None)

mutants_xǁPodSecurityStandardsAuditUseCaseǁ__init____mutmut['_mutmut_orig'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁ__init____mutmut['xǁPodSecurityStandardsAuditUseCaseǁ__init____mutmut_1'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['_mutmut_orig'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_1'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_2'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_3'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_4'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_5'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_6'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_7'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_8'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_9'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_10'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_11'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_12'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_13'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_14'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_15'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_16'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_17'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_18'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_19'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_20'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_21'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_22'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_23'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_23 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_24'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_24 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_25'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_25 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_26'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_26 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_27'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_27 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_28'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_28 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_29'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_29 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_30'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_30 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_31'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_31 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_32'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_32 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_33'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_33 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_34'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_34 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_35'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_35 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_36'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_36 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_37'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_37 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_38'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_38 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_39'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_39 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_40'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_40 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_41'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_41 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_42'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_42 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_43'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_43 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_44'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_44 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_45'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_45 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_46'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_46 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_47'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_47 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_48'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_48 # type: ignore # mutmut generated
mutants_xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut['xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_49'] = PodSecurityStandardsAuditUseCase.xǁPodSecurityStandardsAuditUseCaseǁaudit_pod_security__mutmut_49 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__scan_pod__mutmut)
def _scan_pod(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_orig(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_1(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = None
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_2(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(None)
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_3(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation(None, None))
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_4(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation(None))
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_5(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", ))
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_6(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("XXhost_pidXX", None))
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_7(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("HOST_PID", None))
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_8(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(None)
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_9(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(_build_violation(None, None))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_10(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(_build_violation(None))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_11(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(_build_violation("host_network", ))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_12(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(_build_violation("XXhost_networkXX", None))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_13(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(_build_violation("HOST_NETWORK", None))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_14(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(None)
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_15(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(_build_violation(None, None))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_16(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(_build_violation(None))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_17(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", ))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_18(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(_build_violation("XXhost_ipcXX", None))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_19(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(_build_violation("HOST_IPC", None))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_20(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(None)
    return violations


def x__scan_pod__mutmut_21(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(_scan_container(None, spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_22(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(_scan_container(container, None))
    return violations


def x__scan_pod__mutmut_23(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(_scan_container(spec.pod_run_as_non_root))
    return violations


def x__scan_pod__mutmut_24(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(_scan_container(container, ))
    return violations

mutants_x__scan_pod__mutmut['_mutmut_orig'] = x__scan_pod__mutmut_orig # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_1'] = x__scan_pod__mutmut_1 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_2'] = x__scan_pod__mutmut_2 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_3'] = x__scan_pod__mutmut_3 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_4'] = x__scan_pod__mutmut_4 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_5'] = x__scan_pod__mutmut_5 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_6'] = x__scan_pod__mutmut_6 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_7'] = x__scan_pod__mutmut_7 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_8'] = x__scan_pod__mutmut_8 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_9'] = x__scan_pod__mutmut_9 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_10'] = x__scan_pod__mutmut_10 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_11'] = x__scan_pod__mutmut_11 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_12'] = x__scan_pod__mutmut_12 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_13'] = x__scan_pod__mutmut_13 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_14'] = x__scan_pod__mutmut_14 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_15'] = x__scan_pod__mutmut_15 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_16'] = x__scan_pod__mutmut_16 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_17'] = x__scan_pod__mutmut_17 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_18'] = x__scan_pod__mutmut_18 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_19'] = x__scan_pod__mutmut_19 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_20'] = x__scan_pod__mutmut_20 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_21'] = x__scan_pod__mutmut_21 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_22'] = x__scan_pod__mutmut_22 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_23'] = x__scan_pod__mutmut_23 # type: ignore # mutmut generated
mutants_x__scan_pod__mutmut['x__scan_pod__mutmut_24'] = x__scan_pod__mutmut_24 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__scan_container__mutmut)
def _scan_container(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_orig(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_1(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = None
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_2(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(None):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_3(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(None)
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_4(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation(None, container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_5(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", None))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_6(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation(container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_7(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", ))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_8(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("XXprivilegedXX", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_9(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("PRIVILEGED", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_10(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(None, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_11(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, None):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_12(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_13(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, ):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_14(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(None)
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_15(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation(None, container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_16(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", None))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_17(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation(container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_18(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", ))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_19(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("XXrun_as_rootXX", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_20(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("RUN_AS_ROOT", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_21(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(None):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_22(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(None)
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_23(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation(None, container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_24(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", None))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_25(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation(container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_26(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", ))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_27(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("XXallow_privilege_escalationXX", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_28(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("ALLOW_PRIVILEGE_ESCALATION", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_29(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            None
        )
    return violations


def x__scan_container__mutmut_30(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation(None, container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_31(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", None, capability)
        )
    return violations


def x__scan_container__mutmut_32(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, None)
        )
    return violations


def x__scan_container__mutmut_33(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation(container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_34(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", capability)
        )
    return violations


def x__scan_container__mutmut_35(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, )
        )
    return violations


def x__scan_container__mutmut_36(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("XXdangerous_capabilityXX", container.container_name, capability)
        )
    return violations


def x__scan_container__mutmut_37(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("DANGEROUS_CAPABILITY", container.container_name, capability)
        )
    return violations

mutants_x__scan_container__mutmut['_mutmut_orig'] = x__scan_container__mutmut_orig # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_1'] = x__scan_container__mutmut_1 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_2'] = x__scan_container__mutmut_2 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_3'] = x__scan_container__mutmut_3 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_4'] = x__scan_container__mutmut_4 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_5'] = x__scan_container__mutmut_5 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_6'] = x__scan_container__mutmut_6 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_7'] = x__scan_container__mutmut_7 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_8'] = x__scan_container__mutmut_8 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_9'] = x__scan_container__mutmut_9 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_10'] = x__scan_container__mutmut_10 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_11'] = x__scan_container__mutmut_11 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_12'] = x__scan_container__mutmut_12 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_13'] = x__scan_container__mutmut_13 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_14'] = x__scan_container__mutmut_14 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_15'] = x__scan_container__mutmut_15 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_16'] = x__scan_container__mutmut_16 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_17'] = x__scan_container__mutmut_17 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_18'] = x__scan_container__mutmut_18 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_19'] = x__scan_container__mutmut_19 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_20'] = x__scan_container__mutmut_20 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_21'] = x__scan_container__mutmut_21 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_22'] = x__scan_container__mutmut_22 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_23'] = x__scan_container__mutmut_23 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_24'] = x__scan_container__mutmut_24 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_25'] = x__scan_container__mutmut_25 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_26'] = x__scan_container__mutmut_26 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_27'] = x__scan_container__mutmut_27 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_28'] = x__scan_container__mutmut_28 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_29'] = x__scan_container__mutmut_29 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_30'] = x__scan_container__mutmut_30 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_31'] = x__scan_container__mutmut_31 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_32'] = x__scan_container__mutmut_32 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_33'] = x__scan_container__mutmut_33 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_34'] = x__scan_container__mutmut_34 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_35'] = x__scan_container__mutmut_35 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_36'] = x__scan_container__mutmut_36 # type: ignore # mutmut generated
mutants_x__scan_container__mutmut['x__scan_container__mutmut_37'] = x__scan_container__mutmut_37 # type: ignore # mutmut generated
mutants_x__build_violation__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_violation__mutmut)
def _build_violation(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x__build_violation__mutmut_orig(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x__build_violation__mutmut_1(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=None,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x__build_violation__mutmut_2(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=None,
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x__build_violation__mutmut_3(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=None,
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x__build_violation__mutmut_4(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=None,
        recommendation=recommend_fix(violation_type, capability),
    )


def x__build_violation__mutmut_5(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=None,
    )


def x__build_violation__mutmut_6(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x__build_violation__mutmut_7(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x__build_violation__mutmut_8(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x__build_violation__mutmut_9(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        recommendation=recommend_fix(violation_type, capability),
    )


def x__build_violation__mutmut_10(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        )


def x__build_violation__mutmut_11(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(None, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x__build_violation__mutmut_12(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, None),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x__build_violation__mutmut_13(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x__build_violation__mutmut_14(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, ),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x__build_violation__mutmut_15(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(None),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x__build_violation__mutmut_16(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(None, capability),
    )


def x__build_violation__mutmut_17(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, None),
    )


def x__build_violation__mutmut_18(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(capability),
    )


def x__build_violation__mutmut_19(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, ),
    )

mutants_x__build_violation__mutmut['_mutmut_orig'] = x__build_violation__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_violation__mutmut['x__build_violation__mutmut_1'] = x__build_violation__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_violation__mutmut['x__build_violation__mutmut_2'] = x__build_violation__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_violation__mutmut['x__build_violation__mutmut_3'] = x__build_violation__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_violation__mutmut['x__build_violation__mutmut_4'] = x__build_violation__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_violation__mutmut['x__build_violation__mutmut_5'] = x__build_violation__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_violation__mutmut['x__build_violation__mutmut_6'] = x__build_violation__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_violation__mutmut['x__build_violation__mutmut_7'] = x__build_violation__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_violation__mutmut['x__build_violation__mutmut_8'] = x__build_violation__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_violation__mutmut['x__build_violation__mutmut_9'] = x__build_violation__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_violation__mutmut['x__build_violation__mutmut_10'] = x__build_violation__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_violation__mutmut['x__build_violation__mutmut_11'] = x__build_violation__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_violation__mutmut['x__build_violation__mutmut_12'] = x__build_violation__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_violation__mutmut['x__build_violation__mutmut_13'] = x__build_violation__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_violation__mutmut['x__build_violation__mutmut_14'] = x__build_violation__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_violation__mutmut['x__build_violation__mutmut_15'] = x__build_violation__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_violation__mutmut['x__build_violation__mutmut_16'] = x__build_violation__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_violation__mutmut['x__build_violation__mutmut_17'] = x__build_violation__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_violation__mutmut['x__build_violation__mutmut_18'] = x__build_violation__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_violation__mutmut['x__build_violation__mutmut_19'] = x__build_violation__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_domain_spec__mutmut)
def _to_domain_spec(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_orig(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_1(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=None,
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_2(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=None,
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_3(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=None,
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_4(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=None,
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_5(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=None,
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_6(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=None,
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_7(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=None,
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_8(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=None,
    )


def x__to_domain_spec__mutmut_9(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_10(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_11(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_12(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_13(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_14(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_15(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_16(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        )


def x__to_domain_spec__mutmut_17(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["XXpod_nameXX"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_18(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["POD_NAME"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_19(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["XXnamespaceXX"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_20(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["NAMESPACE"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_21(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["XXowner_kindXX"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_22(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["OWNER_KIND"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_23(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["XXpod_run_as_non_rootXX"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_24(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["POD_RUN_AS_NON_ROOT"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_25(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["XXhost_pidXX"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_26(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["HOST_PID"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_27(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["XXhost_networkXX"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_28(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["HOST_NETWORK"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_29(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["XXhost_ipcXX"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_30(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["HOST_IPC"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_31(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(None) for container in raw["containers"]],
    )


def x__to_domain_spec__mutmut_32(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["XXcontainersXX"]],
    )


def x__to_domain_spec__mutmut_33(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["CONTAINERS"]],
    )

mutants_x__to_domain_spec__mutmut['_mutmut_orig'] = x__to_domain_spec__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_1'] = x__to_domain_spec__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_2'] = x__to_domain_spec__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_3'] = x__to_domain_spec__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_4'] = x__to_domain_spec__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_5'] = x__to_domain_spec__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_6'] = x__to_domain_spec__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_7'] = x__to_domain_spec__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_8'] = x__to_domain_spec__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_9'] = x__to_domain_spec__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_10'] = x__to_domain_spec__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_11'] = x__to_domain_spec__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_12'] = x__to_domain_spec__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_13'] = x__to_domain_spec__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_14'] = x__to_domain_spec__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_15'] = x__to_domain_spec__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_16'] = x__to_domain_spec__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_17'] = x__to_domain_spec__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_18'] = x__to_domain_spec__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_19'] = x__to_domain_spec__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_20'] = x__to_domain_spec__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_21'] = x__to_domain_spec__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_22'] = x__to_domain_spec__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_23'] = x__to_domain_spec__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_24'] = x__to_domain_spec__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_25'] = x__to_domain_spec__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_26'] = x__to_domain_spec__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_27'] = x__to_domain_spec__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_28'] = x__to_domain_spec__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_29'] = x__to_domain_spec__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_30'] = x__to_domain_spec__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_31'] = x__to_domain_spec__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_32'] = x__to_domain_spec__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_domain_spec__mutmut['x__to_domain_spec__mutmut_33'] = x__to_domain_spec__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_domain_container__mutmut)
def _to_domain_container(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_orig(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_1(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=None,
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_2(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=None,
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_3(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=None,
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_4(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=None,
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_5(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=None,
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_6(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=None,
    )


def x__to_domain_container__mutmut_7(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_8(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_9(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_10(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_11(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_12(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        )


def x__to_domain_container__mutmut_13(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["XXcontainer_nameXX"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_14(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["CONTAINER_NAME"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_15(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["XXcontainer_kindXX"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_16(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["CONTAINER_KIND"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_17(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["XXprivilegedXX"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_18(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["PRIVILEGED"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_19(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["XXallow_privilege_escalationXX"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_20(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["ALLOW_PRIVILEGE_ESCALATION"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_21(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["XXrun_as_non_rootXX"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_22(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["RUN_AS_NON_ROOT"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_23(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["XXadded_capabilitiesXX"],
    )


def x__to_domain_container__mutmut_24(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["ADDED_CAPABILITIES"],
    )

mutants_x__to_domain_container__mutmut['_mutmut_orig'] = x__to_domain_container__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_1'] = x__to_domain_container__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_2'] = x__to_domain_container__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_3'] = x__to_domain_container__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_4'] = x__to_domain_container__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_5'] = x__to_domain_container__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_6'] = x__to_domain_container__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_7'] = x__to_domain_container__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_8'] = x__to_domain_container__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_9'] = x__to_domain_container__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_10'] = x__to_domain_container__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_11'] = x__to_domain_container__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_12'] = x__to_domain_container__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_13'] = x__to_domain_container__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_14'] = x__to_domain_container__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_15'] = x__to_domain_container__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_16'] = x__to_domain_container__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_17'] = x__to_domain_container__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_18'] = x__to_domain_container__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_19'] = x__to_domain_container__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_20'] = x__to_domain_container__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_21'] = x__to_domain_container__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_22'] = x__to_domain_container__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_23'] = x__to_domain_container__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_24'] = x__to_domain_container__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_response__mutmut)
def _to_response(report: PodSecurityAuditReport) -> PodSecurityStandardsAuditResponse:
    return PodSecurityStandardsAuditResponse(
        findings=[_to_finding_dict(finding) for finding in report.findings],
        compliant_pod_count=report.compliant_pod_count,
        total_pods_checked=report.total_pods_checked,
        summary=report.summary,
        error=None,
    )


def x__to_response__mutmut_orig(report: PodSecurityAuditReport) -> PodSecurityStandardsAuditResponse:
    return PodSecurityStandardsAuditResponse(
        findings=[_to_finding_dict(finding) for finding in report.findings],
        compliant_pod_count=report.compliant_pod_count,
        total_pods_checked=report.total_pods_checked,
        summary=report.summary,
        error=None,
    )


def x__to_response__mutmut_1(report: PodSecurityAuditReport) -> PodSecurityStandardsAuditResponse:
    return PodSecurityStandardsAuditResponse(
        findings=None,
        compliant_pod_count=report.compliant_pod_count,
        total_pods_checked=report.total_pods_checked,
        summary=report.summary,
        error=None,
    )


def x__to_response__mutmut_2(report: PodSecurityAuditReport) -> PodSecurityStandardsAuditResponse:
    return PodSecurityStandardsAuditResponse(
        findings=[_to_finding_dict(finding) for finding in report.findings],
        compliant_pod_count=None,
        total_pods_checked=report.total_pods_checked,
        summary=report.summary,
        error=None,
    )


def x__to_response__mutmut_3(report: PodSecurityAuditReport) -> PodSecurityStandardsAuditResponse:
    return PodSecurityStandardsAuditResponse(
        findings=[_to_finding_dict(finding) for finding in report.findings],
        compliant_pod_count=report.compliant_pod_count,
        total_pods_checked=None,
        summary=report.summary,
        error=None,
    )


def x__to_response__mutmut_4(report: PodSecurityAuditReport) -> PodSecurityStandardsAuditResponse:
    return PodSecurityStandardsAuditResponse(
        findings=[_to_finding_dict(finding) for finding in report.findings],
        compliant_pod_count=report.compliant_pod_count,
        total_pods_checked=report.total_pods_checked,
        summary=None,
        error=None,
    )


def x__to_response__mutmut_5(report: PodSecurityAuditReport) -> PodSecurityStandardsAuditResponse:
    return PodSecurityStandardsAuditResponse(
        compliant_pod_count=report.compliant_pod_count,
        total_pods_checked=report.total_pods_checked,
        summary=report.summary,
        error=None,
    )


def x__to_response__mutmut_6(report: PodSecurityAuditReport) -> PodSecurityStandardsAuditResponse:
    return PodSecurityStandardsAuditResponse(
        findings=[_to_finding_dict(finding) for finding in report.findings],
        total_pods_checked=report.total_pods_checked,
        summary=report.summary,
        error=None,
    )


def x__to_response__mutmut_7(report: PodSecurityAuditReport) -> PodSecurityStandardsAuditResponse:
    return PodSecurityStandardsAuditResponse(
        findings=[_to_finding_dict(finding) for finding in report.findings],
        compliant_pod_count=report.compliant_pod_count,
        summary=report.summary,
        error=None,
    )


def x__to_response__mutmut_8(report: PodSecurityAuditReport) -> PodSecurityStandardsAuditResponse:
    return PodSecurityStandardsAuditResponse(
        findings=[_to_finding_dict(finding) for finding in report.findings],
        compliant_pod_count=report.compliant_pod_count,
        total_pods_checked=report.total_pods_checked,
        error=None,
    )


def x__to_response__mutmut_9(report: PodSecurityAuditReport) -> PodSecurityStandardsAuditResponse:
    return PodSecurityStandardsAuditResponse(
        findings=[_to_finding_dict(finding) for finding in report.findings],
        compliant_pod_count=report.compliant_pod_count,
        total_pods_checked=report.total_pods_checked,
        summary=report.summary,
        )


def x__to_response__mutmut_10(report: PodSecurityAuditReport) -> PodSecurityStandardsAuditResponse:
    return PodSecurityStandardsAuditResponse(
        findings=[_to_finding_dict(None) for finding in report.findings],
        compliant_pod_count=report.compliant_pod_count,
        total_pods_checked=report.total_pods_checked,
        summary=report.summary,
        error=None,
    )

mutants_x__to_response__mutmut['_mutmut_orig'] = x__to_response__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_1'] = x__to_response__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_2'] = x__to_response__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_3'] = x__to_response__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_4'] = x__to_response__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_5'] = x__to_response__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_6'] = x__to_response__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_7'] = x__to_response__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_8'] = x__to_response__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_9'] = x__to_response__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_10'] = x__to_response__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_finding_dict__mutmut)
def _to_finding_dict(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[_to_violation_dict(violation) for violation in finding.violations],
        note=finding.note,  # type: ignore
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_orig(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[_to_violation_dict(violation) for violation in finding.violations],
        note=finding.note,  # type: ignore
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_1(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=None,
        namespace=finding.namespace,
        violations=[_to_violation_dict(violation) for violation in finding.violations],
        note=finding.note,  # type: ignore
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_2(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=None,
        violations=[_to_violation_dict(violation) for violation in finding.violations],
        note=finding.note,  # type: ignore
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_3(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=None,
        note=finding.note,  # type: ignore
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_4(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[_to_violation_dict(violation) for violation in finding.violations],
        note=None,  # type: ignore
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_5(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[_to_violation_dict(violation) for violation in finding.violations],
        note=finding.note,  # type: ignore
        namespace_psa_enforce_level=None,
    )


def x__to_finding_dict__mutmut_6(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        namespace=finding.namespace,
        violations=[_to_violation_dict(violation) for violation in finding.violations],
        note=finding.note,  # type: ignore
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_7(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        violations=[_to_violation_dict(violation) for violation in finding.violations],
        note=finding.note,  # type: ignore
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_8(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        note=finding.note,  # type: ignore
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_9(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[_to_violation_dict(violation) for violation in finding.violations],
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_10(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[_to_violation_dict(violation) for violation in finding.violations],
        note=finding.note,  # type: ignore
        )


def x__to_finding_dict__mutmut_11(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[_to_violation_dict(None) for violation in finding.violations],
        note=finding.note,  # type: ignore
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )

mutants_x__to_finding_dict__mutmut['_mutmut_orig'] = x__to_finding_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_1'] = x__to_finding_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_2'] = x__to_finding_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_3'] = x__to_finding_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_4'] = x__to_finding_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_5'] = x__to_finding_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_6'] = x__to_finding_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_7'] = x__to_finding_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_8'] = x__to_finding_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_9'] = x__to_finding_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_10'] = x__to_finding_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_11'] = x__to_finding_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_violation_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_violation_dict__mutmut)
def _to_violation_dict(violation: SecurityViolation) -> SecurityViolationDict:
    return SecurityViolationDict(
        violation_type=violation.violation_type,
        severity=violation.severity,
        pss_level=violation.pss_level,
        container_name=violation.container_name,  # type: ignore
        recommendation=violation.recommendation,
    )


def x__to_violation_dict__mutmut_orig(violation: SecurityViolation) -> SecurityViolationDict:
    return SecurityViolationDict(
        violation_type=violation.violation_type,
        severity=violation.severity,
        pss_level=violation.pss_level,
        container_name=violation.container_name,  # type: ignore
        recommendation=violation.recommendation,
    )


def x__to_violation_dict__mutmut_1(violation: SecurityViolation) -> SecurityViolationDict:
    return SecurityViolationDict(
        violation_type=None,
        severity=violation.severity,
        pss_level=violation.pss_level,
        container_name=violation.container_name,  # type: ignore
        recommendation=violation.recommendation,
    )


def x__to_violation_dict__mutmut_2(violation: SecurityViolation) -> SecurityViolationDict:
    return SecurityViolationDict(
        violation_type=violation.violation_type,
        severity=None,
        pss_level=violation.pss_level,
        container_name=violation.container_name,  # type: ignore
        recommendation=violation.recommendation,
    )


def x__to_violation_dict__mutmut_3(violation: SecurityViolation) -> SecurityViolationDict:
    return SecurityViolationDict(
        violation_type=violation.violation_type,
        severity=violation.severity,
        pss_level=None,
        container_name=violation.container_name,  # type: ignore
        recommendation=violation.recommendation,
    )


def x__to_violation_dict__mutmut_4(violation: SecurityViolation) -> SecurityViolationDict:
    return SecurityViolationDict(
        violation_type=violation.violation_type,
        severity=violation.severity,
        pss_level=violation.pss_level,
        container_name=None,  # type: ignore
        recommendation=violation.recommendation,
    )


def x__to_violation_dict__mutmut_5(violation: SecurityViolation) -> SecurityViolationDict:
    return SecurityViolationDict(
        violation_type=violation.violation_type,
        severity=violation.severity,
        pss_level=violation.pss_level,
        container_name=violation.container_name,  # type: ignore
        recommendation=None,
    )


def x__to_violation_dict__mutmut_6(violation: SecurityViolation) -> SecurityViolationDict:
    return SecurityViolationDict(
        severity=violation.severity,
        pss_level=violation.pss_level,
        container_name=violation.container_name,  # type: ignore
        recommendation=violation.recommendation,
    )


def x__to_violation_dict__mutmut_7(violation: SecurityViolation) -> SecurityViolationDict:
    return SecurityViolationDict(
        violation_type=violation.violation_type,
        pss_level=violation.pss_level,
        container_name=violation.container_name,  # type: ignore
        recommendation=violation.recommendation,
    )


def x__to_violation_dict__mutmut_8(violation: SecurityViolation) -> SecurityViolationDict:
    return SecurityViolationDict(
        violation_type=violation.violation_type,
        severity=violation.severity,
        container_name=violation.container_name,  # type: ignore
        recommendation=violation.recommendation,
    )


def x__to_violation_dict__mutmut_9(violation: SecurityViolation) -> SecurityViolationDict:
    return SecurityViolationDict(
        violation_type=violation.violation_type,
        severity=violation.severity,
        pss_level=violation.pss_level,
        recommendation=violation.recommendation,
    )


def x__to_violation_dict__mutmut_10(violation: SecurityViolation) -> SecurityViolationDict:
    return SecurityViolationDict(
        violation_type=violation.violation_type,
        severity=violation.severity,
        pss_level=violation.pss_level,
        container_name=violation.container_name,  # type: ignore
        )

mutants_x__to_violation_dict__mutmut['_mutmut_orig'] = x__to_violation_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_violation_dict__mutmut['x__to_violation_dict__mutmut_1'] = x__to_violation_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_violation_dict__mutmut['x__to_violation_dict__mutmut_2'] = x__to_violation_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_violation_dict__mutmut['x__to_violation_dict__mutmut_3'] = x__to_violation_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_violation_dict__mutmut['x__to_violation_dict__mutmut_4'] = x__to_violation_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_violation_dict__mutmut['x__to_violation_dict__mutmut_5'] = x__to_violation_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_violation_dict__mutmut['x__to_violation_dict__mutmut_6'] = x__to_violation_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_violation_dict__mutmut['x__to_violation_dict__mutmut_7'] = x__to_violation_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_violation_dict__mutmut['x__to_violation_dict__mutmut_8'] = x__to_violation_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_violation_dict__mutmut['x__to_violation_dict__mutmut_9'] = x__to_violation_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_violation_dict__mutmut['x__to_violation_dict__mutmut_10'] = x__to_violation_dict__mutmut_10 # type: ignore # mutmut generated
