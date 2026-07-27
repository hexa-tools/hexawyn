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


class DetectPrivilegedPodsUseCase:
    def __init__(self, port: PodSecurityContextAuditPort) -> None:
        self._port = port

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
