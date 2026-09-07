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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAuditSecretRotationUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class AuditSecretRotationUseCase:
    @_mutmut_mutated(mutants_xǁAuditSecretRotationUseCaseǁ__init____mutmut)
    def __init__(self, port: SecretRotationAuditPort) -> None:
        self._port = port
    def xǁAuditSecretRotationUseCaseǁ__init____mutmut_orig(self, port: SecretRotationAuditPort) -> None:
        self._port = port
    def xǁAuditSecretRotationUseCaseǁ__init____mutmut_1(self, port: SecretRotationAuditPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut)
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_orig(
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_1(
        self,
        command: AuditSecretRotationCommand,
    ) -> AuditSecretRotationResponse:
        secrets_raw = None
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_2(
        self,
        command: AuditSecretRotationCommand,
    ) -> AuditSecretRotationResponse:
        secrets_raw = self._port.list_secrets()
        references_raw = None
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_3(
        self,
        command: AuditSecretRotationCommand,
    ) -> AuditSecretRotationResponse:
        secrets_raw = self._port.list_secrets()
        references_raw = self._port.list_secret_references()
        exempt_ns = None

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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_4(
        self,
        command: AuditSecretRotationCommand,
    ) -> AuditSecretRotationResponse:
        secrets_raw = self._port.list_secrets()
        references_raw = self._port.list_secret_references()
        exempt_ns = self._port.get_namespace_rotation_exemptions()

        refs_by_secret = None
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_5(
        self,
        command: AuditSecretRotationCommand,
    ) -> AuditSecretRotationResponse:
        secrets_raw = self._port.list_secrets()
        references_raw = self._port.list_secret_references()
        exempt_ns = self._port.get_namespace_rotation_exemptions()

        refs_by_secret = index_references(None)
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_6(
        self,
        command: AuditSecretRotationCommand,
    ) -> AuditSecretRotationResponse:
        secrets_raw = self._port.list_secrets()
        references_raw = self._port.list_secret_references()
        exempt_ns = self._port.get_namespace_rotation_exemptions()

        refs_by_secret = index_references(references_raw)
        today = None

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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_7(
        self,
        command: AuditSecretRotationCommand,
    ) -> AuditSecretRotationResponse:
        secrets_raw = self._port.list_secrets()
        references_raw = self._port.list_secret_references()
        exempt_ns = self._port.get_namespace_rotation_exemptions()

        refs_by_secret = index_references(references_raw)
        today = date.today()

        findings: list[StaleSecretFinding] = None
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_8(
        self,
        command: AuditSecretRotationCommand,
    ) -> AuditSecretRotationResponse:
        secrets_raw = self._port.list_secrets()
        references_raw = self._port.list_secret_references()
        exempt_ns = self._port.get_namespace_rotation_exemptions()

        refs_by_secret = index_references(references_raw)
        today = date.today()

        findings: list[StaleSecretFinding] = []
        excluded: list[ExcludedSecret] = None

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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_9(
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
            reason = None
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_10(
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
            reason = exclusion_reason(None, exempt_ns)
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_11(
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
            reason = exclusion_reason(secret, None)
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_12(
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
            reason = exclusion_reason(exempt_ns)
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_13(
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
            reason = exclusion_reason(secret, )
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_14(
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
            if reason is None:
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_15(
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
                    None
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_16(
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
                        name=None,
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_17(
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
                        namespace=None,
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_18(
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
                        reason=None,
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_19(
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_20(
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_21(
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_22(
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
                        name=secret["XXnameXX"],
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_23(
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
                        name=secret["NAME"],
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_24(
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
                        namespace=secret["XXnamespaceXX"],
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_25(
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
                        namespace=secret["NAMESPACE"],
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_26(
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
                break

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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_27(
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

            managed_fields = None
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_28(
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

            managed_fields = [to_domain_entry(None) for raw in secret["managed_fields"]]
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_29(
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

            managed_fields = [to_domain_entry(raw) for raw in secret["XXmanaged_fieldsXX"]]
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_30(
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

            managed_fields = [to_domain_entry(raw) for raw in secret["MANAGED_FIELDS"]]
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_31(
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
            last_modified_raw = None
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_32(
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
                find_last_data_change_time(managed_fields) and secret["creation_timestamp"]
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_33(
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
                find_last_data_change_time(None) or secret["creation_timestamp"]
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_34(
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
                find_last_data_change_time(managed_fields) or secret["XXcreation_timestampXX"]
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_35(
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
                find_last_data_change_time(managed_fields) or secret["CREATION_TIMESTAMP"]
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_36(
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
            last_modified_date = None
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_37(
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
            last_modified_date = parse_date(None)
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_38(
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
            age_days = None
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_39(
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
            age_days = calculate_age_days(None, today)
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_40(
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
            age_days = calculate_age_days(last_modified_date, None)
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_41(
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
            age_days = calculate_age_days(today)
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_42(
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
            age_days = calculate_age_days(last_modified_date, )
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_43(
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
            if is_stale(age_days, command.rotation_threshold_days):
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_44(
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
            if not is_stale(None, command.rotation_threshold_days):
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_45(
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
            if not is_stale(age_days, None):
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_46(
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
            if not is_stale(command.rotation_threshold_days):
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_47(
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
            if not is_stale(age_days, ):
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_48(
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
                break

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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_49(
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

            referenced_by = None
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_50(
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
                None
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_51(
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
                    None,
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_52(
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
                    None,
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_53(
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_54(
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_55(
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
                    (secret["XXnamespaceXX"], secret["name"]),
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_56(
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
                    (secret["NAMESPACE"], secret["name"]),
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_57(
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
                    (secret["namespace"], secret["XXnameXX"]),
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_58(
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
                    (secret["namespace"], secret["NAME"]),
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_59(
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
            risk = None
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_60(
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
                None,
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_61(
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
                None,
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_62(
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_63(
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_64(
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
                secret["XXsecret_typeXX"],
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_65(
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
                secret["SECRET_TYPE"],
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_66(
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
                secret["XXdata_keysXX"],
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_67(
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
                secret["DATA_KEYS"],
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_68(
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
            urgency = None

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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_69(
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
            urgency = compute_urgency_score(None, age_days)

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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_70(
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
            urgency = compute_urgency_score(risk, None)

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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_71(
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
            urgency = compute_urgency_score(age_days)

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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_72(
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
            urgency = compute_urgency_score(risk, )

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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_73(
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
                None
            )

        findings = sort_by_urgency(findings)
        report = build_report(
            findings=findings,
            excluded_secrets=excluded,
            total_secrets_checked=len(secrets_raw),
            rotation_threshold_days=command.rotation_threshold_days,
        )
        return to_response(report)

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_74(
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
                    name=None,
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_75(
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
                    namespace=None,
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_76(
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
                    secret_type=None,
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_77(
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
                    age_days=None,
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_78(
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
                    last_modified=None,
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_79(
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
                    referenced_by=None,
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_80(
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
                    risk_level=None,
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_81(
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
                    urgency_score=None,
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_82(
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
                    note=None,
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_83(
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_84(
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_85(
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_86(
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_87(
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_88(
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_89(
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_90(
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_91(
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_92(
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
                    name=secret["XXnameXX"],
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_93(
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
                    name=secret["NAME"],
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_94(
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
                    namespace=secret["XXnamespaceXX"],
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_95(
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
                    namespace=secret["NAMESPACE"],
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_96(
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
                    secret_type=secret["XXsecret_typeXX"],
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_97(
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
                    secret_type=secret["SECRET_TYPE"],
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_98(
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
                    note=_UNUSED_NOTE if is_unused(None) else None,
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

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_99(
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

        findings = None
        report = build_report(
            findings=findings,
            excluded_secrets=excluded,
            total_secrets_checked=len(secrets_raw),
            rotation_threshold_days=command.rotation_threshold_days,
        )
        return to_response(report)

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_100(
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

        findings = sort_by_urgency(None)
        report = build_report(
            findings=findings,
            excluded_secrets=excluded,
            total_secrets_checked=len(secrets_raw),
            rotation_threshold_days=command.rotation_threshold_days,
        )
        return to_response(report)

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_101(
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
        report = None
        return to_response(report)

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_102(
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
            findings=None,
            excluded_secrets=excluded,
            total_secrets_checked=len(secrets_raw),
            rotation_threshold_days=command.rotation_threshold_days,
        )
        return to_response(report)

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_103(
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
            excluded_secrets=None,
            total_secrets_checked=len(secrets_raw),
            rotation_threshold_days=command.rotation_threshold_days,
        )
        return to_response(report)

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_104(
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
            total_secrets_checked=None,
            rotation_threshold_days=command.rotation_threshold_days,
        )
        return to_response(report)

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_105(
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
            rotation_threshold_days=None,
        )
        return to_response(report)

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_106(
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
            excluded_secrets=excluded,
            total_secrets_checked=len(secrets_raw),
            rotation_threshold_days=command.rotation_threshold_days,
        )
        return to_response(report)

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_107(
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
            total_secrets_checked=len(secrets_raw),
            rotation_threshold_days=command.rotation_threshold_days,
        )
        return to_response(report)

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_108(
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
            rotation_threshold_days=command.rotation_threshold_days,
        )
        return to_response(report)

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_109(
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
            )
        return to_response(report)

    def xǁAuditSecretRotationUseCaseǁexecute__mutmut_110(
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
        return to_response(None)

mutants_xǁAuditSecretRotationUseCaseǁ__init____mutmut['_mutmut_orig'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁ__init____mutmut['xǁAuditSecretRotationUseCaseǁ__init____mutmut_1'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['_mutmut_orig'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_1'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_2'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_3'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_4'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_5'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_6'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_7'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_8'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_9'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_10'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_11'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_12'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_13'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_14'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_15'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_16'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_17'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_18'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_19'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_20'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_21'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_22'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_23'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_24'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_25'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_26'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_27'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_28'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_29'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_30'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_31'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_32'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_33'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_34'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_35'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_36'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_37'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_38'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_39'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_40'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_41'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_42'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_43'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_44'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_45'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_46'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_47'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_48'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_49'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_50'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_51'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_51 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_52'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_52 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_53'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_53 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_54'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_54 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_55'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_55 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_56'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_56 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_57'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_57 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_58'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_58 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_59'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_59 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_60'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_60 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_61'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_61 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_62'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_62 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_63'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_63 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_64'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_64 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_65'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_65 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_66'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_66 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_67'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_67 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_68'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_68 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_69'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_69 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_70'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_70 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_71'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_71 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_72'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_72 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_73'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_73 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_74'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_74 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_75'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_75 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_76'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_76 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_77'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_77 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_78'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_78 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_79'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_79 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_80'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_80 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_81'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_81 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_82'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_82 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_83'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_83 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_84'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_84 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_85'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_85 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_86'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_86 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_87'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_87 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_88'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_88 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_89'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_89 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_90'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_90 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_91'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_91 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_92'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_92 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_93'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_93 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_94'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_94 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_95'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_95 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_96'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_96 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_97'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_97 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_98'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_98 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_99'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_99 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_100'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_100 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_101'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_101 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_102'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_102 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_103'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_103 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_104'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_104 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_105'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_105 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_106'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_106 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_107'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_107 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_108'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_108 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_109'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_109 # type: ignore # mutmut generated
mutants_xǁAuditSecretRotationUseCaseǁexecute__mutmut['xǁAuditSecretRotationUseCaseǁexecute__mutmut_110'] = AuditSecretRotationUseCase.xǁAuditSecretRotationUseCaseǁexecute__mutmut_110 # type: ignore # mutmut generated
