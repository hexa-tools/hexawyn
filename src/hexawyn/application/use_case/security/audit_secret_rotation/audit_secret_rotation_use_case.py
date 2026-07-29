from __future__ import annotations

from datetime import date

from hexawyn.application.ports.driven.secret_rotation_audit_port import (
    SecretRotationAuditPort,
)
from hexawyn.application.use_case.security.audit_secret_rotation.command import (
    AuditSecretRotationCommand,
)
from hexawyn.application.use_case.security.audit_secret_rotation.mapper import (
    exclusion_reason,
    index_references,
    parse_date,
    to_domain_entry,
    to_response,
)
from hexawyn.application.use_case.security.audit_secret_rotation.response import (
    AuditSecretRotationResponse,
)
from hexawyn.domain.models.secret_rotation import (
    ExcludedSecret,
    StaleSecretFinding,
)
from hexawyn.domain.services.secret_rotation.age_calculator import (
    calculate_age_days,
    is_stale,
)
from hexawyn.domain.services.secret_rotation.managed_fields_analyzer import (
    find_last_data_change_time,
)
from hexawyn.domain.services.secret_rotation.risk_classifier import classify_risk_level
from hexawyn.domain.services.secret_rotation.rotation_report_builder import (
    build_report,
)
from hexawyn.domain.services.secret_rotation.urgency_scorer import (
    compute_urgency_score,
    sort_by_urgency,
)
from hexawyn.domain.services.secret_rotation.usage_mapper import (
    deduplicate_references,
    is_unused,
)

_UNUSED_NOTE = "unused by any pod or deployment — safe to delete"


class AuditSecretRotationUseCase:
    def __init__(self, port: SecretRotationAuditPort) -> None:
        self._port = port

    def execute(
        self,
        command: AuditSecretRotationCommand,
    ) -> AuditSecretRotationResponse:
        secrets_raw = self._port.list_secrets()
        references_raw = self._port.list_secret_references()
        exempt_ns = self._port.get_namespace_rotation_exemptions()

        refs_by_secret = index_references(references_raw)
        today = date.today()

        findings: list[StaleSecretFinding] = []
        excluded: list[ExcludedSecret] = []

        for secret in secrets_raw:
            reason = exclusion_reason(secret, exempt_ns)
            if reason is not None:
                excluded.append(
                    ExcludedSecret(
                        name=secret["name"],
                        namespace=secret["namespace"],
                        reason=reason,
                    )
                )
                continue

            managed_fields = [to_domain_entry(raw) for raw in secret["managed_fields"]]
            last_modified_raw = (
                find_last_data_change_time(managed_fields) or secret["creation_timestamp"]
            )
            last_modified_date = parse_date(last_modified_raw)
            age_days = calculate_age_days(last_modified_date, today)
            if not is_stale(age_days, command.rotation_threshold_days):
                continue

            referenced_by = deduplicate_references(
                refs_by_secret.get(
                    (secret["namespace"], secret["name"]),
                    [],
                )
            )
            risk = classify_risk_level(
                secret["secret_type"],
                secret["data_keys"],
            )
            urgency = compute_urgency_score(risk, age_days)

            findings.append(
                StaleSecretFinding(
                    name=secret["name"],
                    namespace=secret["namespace"],
                    secret_type=secret["secret_type"],
                    age_days=age_days,
                    last_modified=last_modified_date.isoformat(),
                    referenced_by=referenced_by,
                    risk_level=risk,
                    urgency_score=urgency,
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
        return to_response(report)
