# mypy: ignore-errors
from __future__ import annotations

from datetime import UTC, datetime

from hexawyn.application.ports.driven.gitops_drift_audit_port import (
    AuditEventRaw,
)
from hexawyn.application.use_case.gitops.manual_change_outside_gitops.command import (
    ManualChangeOutsideGitopsCommand,
)
from hexawyn.application.use_case.gitops.manual_change_outside_gitops.response import (
    ManualChangeDict,
    ManualChangeOutsideGitopsResponse,
)
from hexawyn.domain.models.constants import ManualChangeDetectionConstants
from hexawyn.domain.models.manual_change import (  # noqa: F401
    ManualChange,
    ManualChangeOutsideGitOpsReport,
)
from hexawyn.domain.services.manual_change_detection.actor_classifier import classify_actor
from hexawyn.domain.services.manual_change_detection.audit_event_filter import (
    is_manual_change,
    is_partial_window,
    is_within_window,
)
from hexawyn.domain.services.manual_change_detection.managed_fields_parser import (
    extract_field_paths,
)
from hexawyn.domain.services.manual_change_detection.manual_change_report_builder import (
    build_report,
)
from hexawyn.domain.services.manual_change_detection.sensitive_change_classifier import (
    classify_severity,
)

_cfg = ManualChangeDetectionConstants()


class ManualChangeOutsideGitopsUseCase:
    def __init__(self, audit_port: GitopsDriftAuditPort) -> None:  # noqa: F821  # type: ignore
        self._audit_port = audit_port

    def detect_manual_changes(
        self, command: ManualChangeOutsideGitopsCommand
    ) -> ManualChangeOutsideGitopsResponse:
        resources = self._audit_port.list_live_config_resources(command.namespace)
        audit_result = self._audit_port.fetch_audit_log_events(
            command.namespace, command.window_days
        )
        audit_index = _index_audit_events(audit_result["events"])
        now = datetime.now(UTC)

        changes: list[ManualChange] = []
        excluded_count = 0
        for resource in resources:
            for entry in resource["managed_fields"]:
                if not is_within_window(entry["time"], command.window_days, now):
                    continue
                key = (resource["kind"], resource["name"], resource["namespace"], entry["time"])
                real_actor = audit_index.get(key)
                actor = real_actor if real_actor is not None else entry["manager"]
                actor_type = classify_actor(actor, _cfg.gitops_controllers)
                if not is_manual_change(actor_type):
                    excluded_count += 1
                    continue
                severity = classify_severity(
                    resource["kind"], resource["name"], _cfg.sensitive_configmap_keywords
                )
                changes.append(
                    ManualChange(
                        kind=resource["kind"],
                        name=resource["name"],
                        namespace=resource["namespace"],
                        timestamp=entry["time"],
                        actor=actor,
                        actor_type=actor_type,
                        changed_fields=extract_field_paths(entry["fields_v1_raw"]),
                        severity=severity,
                        is_limited_actor_info=real_actor is None,
                    )
                )

        used_fallback = not audit_result["available"]
        partial_window = audit_result["available"] and is_partial_window(
            audit_result["earliest_timestamp"], command.window_days, now
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)


def _index_audit_events(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["name"], event["namespace"], event["timestamp"]): event["actor"]
        for event in events
    }


def _to_response(report: ManualChangeOutsideGitopsReport) -> ManualChangeOutsideGitopsResponse:  # noqa: F821  # type: ignore
    return ManualChangeOutsideGitopsResponse(
        manual_changes=[_to_change_dict(change) for change in report.manual_changes],
        total_manual_changes=report.total_manual_changes,
        excluded_gitops_change_count=report.excluded_gitops_change_count,
        used_managed_fields_fallback=report.used_managed_fields_fallback,
        partial_window=report.partial_window,
        notes=report.notes,
        error=None,
    )


def _to_change_dict(change: ManualChange) -> ManualChangeDict:
    return ManualChangeDict(
        kind=change.kind,
        name=change.name,
        namespace=change.namespace,
        timestamp=change.timestamp,
        actor=change.actor,
        actor_type=change.actor_type,
        changed_fields=change.changed_fields,
        severity=change.severity,
        is_limited_actor_info=change.is_limited_actor_info,
    )
