from __future__ import annotations

from datetime import UTC, date, datetime

from hexawyn.application.ports.driven.secret_rotation_audit_port import (
    ManagedFieldsEntryRaw,
    SecretRaw,
    SecretReferenceRaw,
)
from hexawyn.application.use_case.security.audit_secret_rotation.response import (
    AuditSecretRotationResponse,
    ExcludedSecretDict,
    StaleSecretFindingDict,
)
from hexawyn.domain.models.constants import SecretRotationConstants
from hexawyn.domain.models.secret_rotation import (
    ExcludedSecret,
    ManagedFieldsEntry,
    SecretRotationReport,
    StaleSecretFinding,
)

_cfg = SecretRotationConstants()
_ExcludedSecretKey = tuple[str, str]


def exclusion_reason(
    secret: SecretRaw,
    exempt_namespaces: set[str],
) -> str | None:
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


def index_references(
    references_raw: list[SecretReferenceRaw],
) -> dict[_ExcludedSecretKey, list[str]]:
    index: dict[_ExcludedSecretKey, list[str]] = {}
    for ref in references_raw:
        key = (ref["namespace"], ref["secret_name"])
        index.setdefault(key, []).append(ref["workload_name"])
    return index


def to_domain_entry(raw: ManagedFieldsEntryRaw) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        manager=raw["manager"],
        operation=raw["operation"],
        time=raw["time"],
        fields_v1_raw=raw["fields_v1_raw"],
    )


def parse_date(value: str) -> date:
    return datetime.fromisoformat(value).astimezone(UTC).date()


def to_response(report: SecretRotationReport) -> AuditSecretRotationResponse:
    return AuditSecretRotationResponse(
        findings=[_to_finding_dict(f) for f in report.findings],
        excluded_secrets=[_to_excluded_dict(e) for e in report.excluded_secrets],
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
        name=excluded.name,
        namespace=excluded.namespace,
        reason=excluded.reason,
    )
