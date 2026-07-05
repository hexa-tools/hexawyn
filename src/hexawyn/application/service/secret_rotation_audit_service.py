from __future__ import annotations

from datetime import UTC, date, datetime

from hexawyn.application.ports.driven.secret_rotation_audit_port import (
    ManagedFieldsEntryRaw,
    SecretRaw,
    SecretReferenceRaw,
    SecretRotationAuditPort,
)
from hexawyn.application.ports.driving.audit_secret_rotation.audit_secret_rotation_command import (
    AuditSecretRotationCommand,
)
from hexawyn.application.ports.driving.audit_secret_rotation.audit_secret_rotation_response import (
    AuditSecretRotationResponse,
    ExcludedSecretDict,
    StaleSecretFindingDict,
)
from hexawyn.application.ports.driving.audit_secret_rotation.audit_secret_rotation_service_port import (
    AuditSecretRotationServicePort,
)
from hexawyn.domain.models.constants import SecretRotationConstants
from hexawyn.domain.models.secret_rotation import (
    ExcludedSecret,
    ManagedFieldsEntry,
    SecretRotationReport,
    StaleSecretFinding,
)
from hexawyn.domain.services.secret_rotation.age_calculator import calculate_age_days, is_stale
from hexawyn.domain.services.secret_rotation.managed_fields_analyzer import (
    find_last_data_change_time,
)
from hexawyn.domain.services.secret_rotation.risk_classifier import classify_risk_level
from hexawyn.domain.services.secret_rotation.rotation_report_builder import build_report
from hexawyn.domain.services.secret_rotation.urgency_scorer import (
    compute_urgency_score,
    sort_by_urgency,
)
from hexawyn.domain.services.secret_rotation.usage_mapper import deduplicate_references, is_unused

_cfg = SecretRotationConstants()
_UNUSED_NOTE = "unused by any pod or deployment — safe to delete"
_ExcludedSecretKey = tuple[str, str]


class SecretRotationAuditService(AuditSecretRotationServicePort):
    def __init__(self, secret_rotation_port: SecretRotationAuditPort) -> None:
        self._secret_rotation_port = secret_rotation_port

    def audit_secret_rotation(
        self, command: AuditSecretRotationCommand
    ) -> AuditSecretRotationResponse:
        secrets_raw = self._secret_rotation_port.list_secrets()
        references_raw = self._secret_rotation_port.list_secret_references()
        exempt_namespaces = self._secret_rotation_port.get_namespace_rotation_exemptions()

        references_by_secret = _index_references(references_raw)
        today = date.today()

        findings: list[StaleSecretFinding] = []
        excluded: list[ExcludedSecret] = []

        for secret in secrets_raw:
            exclusion_reason = _exclusion_reason(secret, exempt_namespaces)
            if exclusion_reason is not None:
                excluded.append(
                    ExcludedSecret(
                        name=secret["name"], namespace=secret["namespace"], reason=exclusion_reason
                    )
                )
                continue

            managed_fields = [_to_domain_entry(raw) for raw in secret["managed_fields"]]
            last_modified_raw = (
                find_last_data_change_time(managed_fields) or secret["creation_timestamp"]
            )
            last_modified_date = _parse_date(last_modified_raw)
            age_days = calculate_age_days(last_modified_date, today)
            if not is_stale(age_days, command.rotation_threshold_days):
                continue

            referenced_by = deduplicate_references(
                references_by_secret.get((secret["namespace"], secret["name"]), [])
            )
            risk_level = classify_risk_level(secret["secret_type"], secret["data_keys"])
            urgency_score = compute_urgency_score(risk_level, age_days)

            findings.append(
                StaleSecretFinding(
                    name=secret["name"],
                    namespace=secret["namespace"],
                    secret_type=secret["secret_type"],
                    age_days=age_days,
                    last_modified=last_modified_date.isoformat(),
                    referenced_by=referenced_by,
                    risk_level=risk_level,
                    urgency_score=urgency_score,
                    note=_UNUSED_NOTE if is_unused(referenced_by) else None,
                )
            )

        findings = sort_by_urgency(findings)
        report = build_report(
            findings=findings,
            excluded_secrets=excluded,
            total_secrets_checked=len(secrets_raw),
            rotation_threshold_days=command.rotation_threshold_days,
        )
        return _to_response(report)


def _exclusion_reason(secret: SecretRaw, exempt_namespaces: set[str]) -> str | None:
    if secret["namespace"] in exempt_namespaces:
        return "namespace exempt from rotation policy"
    annotations = secret["annotations"]
    if _cfg.external_secrets_annotation_key in annotations:
        return "externally managed (External Secrets Operator)"
    if (
        secret["secret_type"] in _cfg.critical_secret_types
        and _cfg.cert_manager_annotation_key in annotations
    ):
        return "auto-rotated (cert-manager)"
    return None


def _index_references(
    references_raw: list[SecretReferenceRaw],
) -> dict[_ExcludedSecretKey, list[str]]:
    index: dict[_ExcludedSecretKey, list[str]] = {}
    for reference in references_raw:
        key = (reference["namespace"], reference["secret_name"])
        index.setdefault(key, []).append(reference["workload_name"])
    return index


def _to_domain_entry(raw: ManagedFieldsEntryRaw) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        manager=raw["manager"],
        operation=raw["operation"],
        time=raw["time"],
        fields_v1_raw=raw["fields_v1_raw"],
    )


def _parse_date(value: str) -> date:
    return datetime.fromisoformat(value).astimezone(UTC).date()


def _to_response(report: SecretRotationReport) -> AuditSecretRotationResponse:
    return AuditSecretRotationResponse(
        findings=[_to_finding_dict(finding) for finding in report.findings],
        excluded_secrets=[_to_excluded_dict(excluded) for excluded in report.excluded_secrets],
        total_secrets_checked=report.total_secrets_checked,
        rotation_threshold_days=report.rotation_threshold_days,
        summary=report.summary,
        error=None,
    )


def _to_finding_dict(finding: StaleSecretFinding) -> StaleSecretFindingDict:
    return StaleSecretFindingDict(
        name=finding.name,
        namespace=finding.namespace,
        secret_type=finding.secret_type,
        age_days=finding.age_days,
        last_modified=finding.last_modified,
        referenced_by=finding.referenced_by,
        risk_level=finding.risk_level,
        urgency_score=finding.urgency_score,
        note=finding.note,
    )


def _to_excluded_dict(excluded: ExcludedSecret) -> ExcludedSecretDict:
    return ExcludedSecretDict(
        name=excluded.name, namespace=excluded.namespace, reason=excluded.reason
    )
