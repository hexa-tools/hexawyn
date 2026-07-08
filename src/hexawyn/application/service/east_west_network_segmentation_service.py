from __future__ import annotations

from hexawyn.application.ports.driven.network_policy_audit_port import (
    NetworkPolicyAuditPort,
    NetworkPolicyRaw,
)
from hexawyn.application.ports.driving.detect_network_segmentation_gaps.detect_network_segmentation_gaps_command import (
    DetectNetworkSegmentationGapsCommand,
)
from hexawyn.application.ports.driving.detect_network_segmentation_gaps.detect_network_segmentation_gaps_response import (
    DetectNetworkSegmentationGapsResponse,
    ExcludedNamespaceDict,
    NamespaceNetworkFindingDict,
)
from hexawyn.application.ports.driving.detect_network_segmentation_gaps.detect_network_segmentation_gaps_service_port import (
    DetectNetworkSegmentationGapsServicePort,
)
from hexawyn.domain.models.constants import NetworkPolicyConstants
from hexawyn.domain.models.network_policy import (
    ExcludedNamespace,
    NamespaceNetworkFinding,
    NetworkSegmentationReport,
    NetworkStatus,
)
from hexawyn.domain.services.network_policy.namespace_status_classifier import (
    classify_network_status,
)
from hexawyn.domain.services.network_policy.network_segmentation_report_builder import (
    build_report,
)
from hexawyn.domain.services.network_policy.policy_coverage_analyzer import (
    provides_egress_restriction,
    provides_ingress_restriction,
)
from hexawyn.domain.services.network_policy.recommendation_builder import build_recommendation
from hexawyn.domain.services.network_policy.risk_classifier import classify_risk_level

_cfg = NetworkPolicyConstants()
_ISTIO_NOTE = "Istio mTLS provides equivalent protection"
_CALICO_NOTE = (
    "Calico GlobalNetworkPolicy detected — may provide protection beyond "
    "vanilla NetworkPolicy visibility"
)


class EastWestNetworkSegmentationService(DetectNetworkSegmentationGapsServicePort):
    def __init__(self, network_policy_port: NetworkPolicyAuditPort) -> None:
        self._network_policy_port = network_policy_port

    def detect_segmentation_gaps(
        self, command: DetectNetworkSegmentationGapsCommand
    ) -> DetectNetworkSegmentationGapsResponse:
        namespaces_raw = self._network_policy_port.list_namespaces_with_pod_counts()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            namespaces_raw = [ns for ns in namespaces_raw if ns["name"] in allowed_namespaces]

        policies_by_namespace = _group_policies_by_namespace(
            self._network_policy_port.list_network_policies()
        )
        has_calico = self._network_policy_port.has_calico_global_network_policies()
        has_istio_strict = self._network_policy_port.has_istio_strict_peer_authentication()

        findings: list[NamespaceNetworkFinding] = []
        excluded: list[ExcludedNamespace] = []

        for namespace in namespaces_raw:
            if namespace["name"] in _cfg.system_namespaces:
                excluded.append(
                    ExcludedNamespace(namespace=namespace["name"], reason="system namespace")
                )
                continue

            ns_policies = policies_by_namespace.get(namespace["name"], [])
            ingress_policies = sum(
                1
                for policy in ns_policies
                if provides_ingress_restriction(policy["ingress_rule_count"])
            )
            egress_policies = sum(
                1
                for policy in ns_policies
                if provides_egress_restriction(policy["egress_rule_count"])
            )

            network_status = classify_network_status(ingress_policies, egress_policies)
            risk_level = classify_risk_level(network_status, namespace["pod_count"])
            recommendation = build_recommendation(network_status, ingress_policies, egress_policies)
            note = _build_note(has_calico, has_istio_strict, network_status, ns_policies)

            findings.append(
                NamespaceNetworkFinding(
                    namespace=namespace["name"],
                    ingress_policies=ingress_policies,
                    egress_policies=egress_policies,
                    pod_count=namespace["pod_count"],
                    network_status=network_status,
                    risk_level=risk_level,
                    recommendation=recommendation,
                    note=note,
                )
            )

        report = build_report(
            findings=findings,
            excluded_namespaces=excluded,
            total_namespaces_checked=len(namespaces_raw),
        )
        return _to_response(report)


def _group_policies_by_namespace(
    policies_raw: list[NetworkPolicyRaw],
) -> dict[str, list[NetworkPolicyRaw]]:
    grouped: dict[str, list[NetworkPolicyRaw]] = {}
    for policy in policies_raw:
        grouped.setdefault(policy["namespace"], []).append(policy)
    return grouped


def _build_note(
    has_calico: bool,
    has_istio_strict: bool,
    network_status: NetworkStatus,
    ns_policies: list[NetworkPolicyRaw],
) -> str | None:
    notes: list[str] = []
    if network_status != "restricted":
        if has_calico:
            notes.append(_CALICO_NOTE)
        if has_istio_strict:
            notes.append(_ISTIO_NOTE)

    broad_policies = [
        policy
        for policy in ns_policies
        if policy["has_empty_pod_selector"]
        and (policy["ingress_rule_count"] > 0 or policy["egress_rule_count"] > 0)
    ]
    if broad_policies:
        notes.append(
            f"{len(broad_policies)} polic(ies) apply to all pods in this namespace (empty podSelector)"
        )

    return "; ".join(notes) if notes else None


def _to_response(report: NetworkSegmentationReport) -> DetectNetworkSegmentationGapsResponse:
    return DetectNetworkSegmentationGapsResponse(
        findings=[_to_finding_dict(finding) for finding in report.findings],
        excluded_namespaces=[
            _to_excluded_dict(excluded) for excluded in report.excluded_namespaces
        ],
        total_namespaces_checked=report.total_namespaces_checked,
        fully_open_count=report.fully_open_count,
        partially_restricted_count=report.partially_restricted_count,
        restricted_count=report.restricted_count,
        summary=report.summary,
        error=None,
    )


def _to_finding_dict(finding: NamespaceNetworkFinding) -> NamespaceNetworkFindingDict:
    return NamespaceNetworkFindingDict(
        namespace=finding.namespace,
        ingress_policies=finding.ingress_policies,
        egress_policies=finding.egress_policies,
        pod_count=finding.pod_count,
        network_status=finding.network_status,
        risk_level=finding.risk_level,
        recommendation=finding.recommendation,
        note=finding.note,
    )


def _to_excluded_dict(excluded: ExcludedNamespace) -> ExcludedNamespaceDict:
    return ExcludedNamespaceDict(namespace=excluded.namespace, reason=excluded.reason)
