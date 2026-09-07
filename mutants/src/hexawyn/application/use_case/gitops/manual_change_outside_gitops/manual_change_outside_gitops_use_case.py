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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁManualChangeOutsideGitopsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut: MutantDict = {}  # type: ignore


class ManualChangeOutsideGitopsUseCase:
    @_mutmut_mutated(mutants_xǁManualChangeOutsideGitopsUseCaseǁ__init____mutmut)
    def __init__(self, audit_port: GitopsDriftAuditPort) -> None:  # noqa: F821  # type: ignore
        self._audit_port = audit_port
    def xǁManualChangeOutsideGitopsUseCaseǁ__init____mutmut_orig(self, audit_port: GitopsDriftAuditPort) -> None:  # noqa: F821  # type: ignore
        self._audit_port = audit_port
    def xǁManualChangeOutsideGitopsUseCaseǁ__init____mutmut_1(self, audit_port: GitopsDriftAuditPort) -> None:  # noqa: F821  # type: ignore
        self._audit_port = None

    @_mutmut_mutated(mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut)
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_orig(
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_1(
        self, command: ManualChangeOutsideGitopsCommand
    ) -> ManualChangeOutsideGitopsResponse:
        resources = None
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_2(
        self, command: ManualChangeOutsideGitopsCommand
    ) -> ManualChangeOutsideGitopsResponse:
        resources = self._audit_port.list_live_config_resources(None)
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_3(
        self, command: ManualChangeOutsideGitopsCommand
    ) -> ManualChangeOutsideGitopsResponse:
        resources = self._audit_port.list_live_config_resources(command.namespace)
        audit_result = None
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_4(
        self, command: ManualChangeOutsideGitopsCommand
    ) -> ManualChangeOutsideGitopsResponse:
        resources = self._audit_port.list_live_config_resources(command.namespace)
        audit_result = self._audit_port.fetch_audit_log_events(
            None, command.window_days
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_5(
        self, command: ManualChangeOutsideGitopsCommand
    ) -> ManualChangeOutsideGitopsResponse:
        resources = self._audit_port.list_live_config_resources(command.namespace)
        audit_result = self._audit_port.fetch_audit_log_events(
            command.namespace, None
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_6(
        self, command: ManualChangeOutsideGitopsCommand
    ) -> ManualChangeOutsideGitopsResponse:
        resources = self._audit_port.list_live_config_resources(command.namespace)
        audit_result = self._audit_port.fetch_audit_log_events(
            command.window_days
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_7(
        self, command: ManualChangeOutsideGitopsCommand
    ) -> ManualChangeOutsideGitopsResponse:
        resources = self._audit_port.list_live_config_resources(command.namespace)
        audit_result = self._audit_port.fetch_audit_log_events(
            command.namespace, )
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_8(
        self, command: ManualChangeOutsideGitopsCommand
    ) -> ManualChangeOutsideGitopsResponse:
        resources = self._audit_port.list_live_config_resources(command.namespace)
        audit_result = self._audit_port.fetch_audit_log_events(
            command.namespace, command.window_days
        )
        audit_index = None
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_9(
        self, command: ManualChangeOutsideGitopsCommand
    ) -> ManualChangeOutsideGitopsResponse:
        resources = self._audit_port.list_live_config_resources(command.namespace)
        audit_result = self._audit_port.fetch_audit_log_events(
            command.namespace, command.window_days
        )
        audit_index = _index_audit_events(None)
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_10(
        self, command: ManualChangeOutsideGitopsCommand
    ) -> ManualChangeOutsideGitopsResponse:
        resources = self._audit_port.list_live_config_resources(command.namespace)
        audit_result = self._audit_port.fetch_audit_log_events(
            command.namespace, command.window_days
        )
        audit_index = _index_audit_events(audit_result["XXeventsXX"])
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_11(
        self, command: ManualChangeOutsideGitopsCommand
    ) -> ManualChangeOutsideGitopsResponse:
        resources = self._audit_port.list_live_config_resources(command.namespace)
        audit_result = self._audit_port.fetch_audit_log_events(
            command.namespace, command.window_days
        )
        audit_index = _index_audit_events(audit_result["EVENTS"])
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_12(
        self, command: ManualChangeOutsideGitopsCommand
    ) -> ManualChangeOutsideGitopsResponse:
        resources = self._audit_port.list_live_config_resources(command.namespace)
        audit_result = self._audit_port.fetch_audit_log_events(
            command.namespace, command.window_days
        )
        audit_index = _index_audit_events(audit_result["events"])
        now = None

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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_13(
        self, command: ManualChangeOutsideGitopsCommand
    ) -> ManualChangeOutsideGitopsResponse:
        resources = self._audit_port.list_live_config_resources(command.namespace)
        audit_result = self._audit_port.fetch_audit_log_events(
            command.namespace, command.window_days
        )
        audit_index = _index_audit_events(audit_result["events"])
        now = datetime.now(None)

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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_14(
        self, command: ManualChangeOutsideGitopsCommand
    ) -> ManualChangeOutsideGitopsResponse:
        resources = self._audit_port.list_live_config_resources(command.namespace)
        audit_result = self._audit_port.fetch_audit_log_events(
            command.namespace, command.window_days
        )
        audit_index = _index_audit_events(audit_result["events"])
        now = datetime.now(UTC)

        changes: list[ManualChange] = None
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_15(
        self, command: ManualChangeOutsideGitopsCommand
    ) -> ManualChangeOutsideGitopsResponse:
        resources = self._audit_port.list_live_config_resources(command.namespace)
        audit_result = self._audit_port.fetch_audit_log_events(
            command.namespace, command.window_days
        )
        audit_index = _index_audit_events(audit_result["events"])
        now = datetime.now(UTC)

        changes: list[ManualChange] = []
        excluded_count = None
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_16(
        self, command: ManualChangeOutsideGitopsCommand
    ) -> ManualChangeOutsideGitopsResponse:
        resources = self._audit_port.list_live_config_resources(command.namespace)
        audit_result = self._audit_port.fetch_audit_log_events(
            command.namespace, command.window_days
        )
        audit_index = _index_audit_events(audit_result["events"])
        now = datetime.now(UTC)

        changes: list[ManualChange] = []
        excluded_count = 1
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_17(
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
            for entry in resource["XXmanaged_fieldsXX"]:
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_18(
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
            for entry in resource["MANAGED_FIELDS"]:
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_19(
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
                if is_within_window(entry["time"], command.window_days, now):
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_20(
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
                if not is_within_window(None, command.window_days, now):
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_21(
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
                if not is_within_window(entry["time"], None, now):
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_22(
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
                if not is_within_window(entry["time"], command.window_days, None):
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_23(
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
                if not is_within_window(command.window_days, now):
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_24(
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
                if not is_within_window(entry["time"], now):
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_25(
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
                if not is_within_window(entry["time"], command.window_days, ):
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_26(
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
                if not is_within_window(entry["XXtimeXX"], command.window_days, now):
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_27(
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
                if not is_within_window(entry["TIME"], command.window_days, now):
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_28(
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
                    break
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_29(
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
                key = None
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_30(
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
                key = (resource["XXkindXX"], resource["name"], resource["namespace"], entry["time"])
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_31(
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
                key = (resource["KIND"], resource["name"], resource["namespace"], entry["time"])
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_32(
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
                key = (resource["kind"], resource["XXnameXX"], resource["namespace"], entry["time"])
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_33(
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
                key = (resource["kind"], resource["NAME"], resource["namespace"], entry["time"])
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_34(
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
                key = (resource["kind"], resource["name"], resource["XXnamespaceXX"], entry["time"])
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_35(
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
                key = (resource["kind"], resource["name"], resource["NAMESPACE"], entry["time"])
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_36(
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
                key = (resource["kind"], resource["name"], resource["namespace"], entry["XXtimeXX"])
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_37(
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
                key = (resource["kind"], resource["name"], resource["namespace"], entry["TIME"])
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_38(
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
                real_actor = None
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_39(
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
                real_actor = audit_index.get(None)
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_40(
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
                actor = None
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_41(
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
                actor = real_actor if real_actor is None else entry["manager"]
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_42(
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
                actor = real_actor if real_actor is not None else entry["XXmanagerXX"]
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_43(
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
                actor = real_actor if real_actor is not None else entry["MANAGER"]
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_44(
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
                actor_type = None
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_45(
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
                actor_type = classify_actor(None, _cfg.gitops_controllers)
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_46(
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
                actor_type = classify_actor(actor, None)
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_47(
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
                actor_type = classify_actor(_cfg.gitops_controllers)
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_48(
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
                actor_type = classify_actor(actor, )
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_49(
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
                if is_manual_change(actor_type):
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_50(
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
                if not is_manual_change(None):
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_51(
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
                    excluded_count = 1
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_52(
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
                    excluded_count -= 1
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_53(
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
                    excluded_count += 2
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_54(
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
                    break
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_55(
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
                severity = None
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_56(
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
                    None, resource["name"], _cfg.sensitive_configmap_keywords
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_57(
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
                    resource["kind"], None, _cfg.sensitive_configmap_keywords
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_58(
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
                    resource["kind"], resource["name"], None
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_59(
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
                    resource["name"], _cfg.sensitive_configmap_keywords
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_60(
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
                    resource["kind"], _cfg.sensitive_configmap_keywords
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_61(
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
                    resource["kind"], resource["name"], )
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_62(
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
                    resource["XXkindXX"], resource["name"], _cfg.sensitive_configmap_keywords
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_63(
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
                    resource["KIND"], resource["name"], _cfg.sensitive_configmap_keywords
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_64(
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
                    resource["kind"], resource["XXnameXX"], _cfg.sensitive_configmap_keywords
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_65(
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
                    resource["kind"], resource["NAME"], _cfg.sensitive_configmap_keywords
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_66(
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
                    None
                )

        used_fallback = not audit_result["available"]
        partial_window = audit_result["available"] and is_partial_window(
            audit_result["earliest_timestamp"], command.window_days, now
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_67(
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
                        kind=None,
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_68(
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
                        name=None,
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_69(
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
                        namespace=None,
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_70(
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
                        timestamp=None,
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_71(
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
                        actor=None,
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_72(
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
                        actor_type=None,
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_73(
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
                        changed_fields=None,
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_74(
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
                        severity=None,
                        is_limited_actor_info=real_actor is None,
                    )
                )

        used_fallback = not audit_result["available"]
        partial_window = audit_result["available"] and is_partial_window(
            audit_result["earliest_timestamp"], command.window_days, now
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_75(
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
                        is_limited_actor_info=None,
                    )
                )

        used_fallback = not audit_result["available"]
        partial_window = audit_result["available"] and is_partial_window(
            audit_result["earliest_timestamp"], command.window_days, now
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_76(
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_77(
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_78(
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_79(
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_80(
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_81(
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_82(
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_83(
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
                        is_limited_actor_info=real_actor is None,
                    )
                )

        used_fallback = not audit_result["available"]
        partial_window = audit_result["available"] and is_partial_window(
            audit_result["earliest_timestamp"], command.window_days, now
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_84(
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
                        )
                )

        used_fallback = not audit_result["available"]
        partial_window = audit_result["available"] and is_partial_window(
            audit_result["earliest_timestamp"], command.window_days, now
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_85(
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
                        kind=resource["XXkindXX"],
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_86(
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
                        kind=resource["KIND"],
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_87(
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
                        name=resource["XXnameXX"],
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_88(
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
                        name=resource["NAME"],
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_89(
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
                        namespace=resource["XXnamespaceXX"],
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_90(
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
                        namespace=resource["NAMESPACE"],
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_91(
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
                        timestamp=entry["XXtimeXX"],
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_92(
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
                        timestamp=entry["TIME"],
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_93(
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
                        changed_fields=extract_field_paths(None),
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_94(
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
                        changed_fields=extract_field_paths(entry["XXfields_v1_rawXX"]),
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_95(
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
                        changed_fields=extract_field_paths(entry["FIELDS_V1_RAW"]),
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

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_96(
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
                        is_limited_actor_info=real_actor is not None,
                    )
                )

        used_fallback = not audit_result["available"]
        partial_window = audit_result["available"] and is_partial_window(
            audit_result["earliest_timestamp"], command.window_days, now
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_97(
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

        used_fallback = None
        partial_window = audit_result["available"] and is_partial_window(
            audit_result["earliest_timestamp"], command.window_days, now
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_98(
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

        used_fallback = audit_result["available"]
        partial_window = audit_result["available"] and is_partial_window(
            audit_result["earliest_timestamp"], command.window_days, now
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_99(
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

        used_fallback = not audit_result["XXavailableXX"]
        partial_window = audit_result["available"] and is_partial_window(
            audit_result["earliest_timestamp"], command.window_days, now
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_100(
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

        used_fallback = not audit_result["AVAILABLE"]
        partial_window = audit_result["available"] and is_partial_window(
            audit_result["earliest_timestamp"], command.window_days, now
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_101(
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
        partial_window = None
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_102(
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
        partial_window = audit_result["available"] or is_partial_window(
            audit_result["earliest_timestamp"], command.window_days, now
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_103(
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
        partial_window = audit_result["XXavailableXX"] and is_partial_window(
            audit_result["earliest_timestamp"], command.window_days, now
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_104(
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
        partial_window = audit_result["AVAILABLE"] and is_partial_window(
            audit_result["earliest_timestamp"], command.window_days, now
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_105(
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
            None, command.window_days, now
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_106(
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
            audit_result["earliest_timestamp"], None, now
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_107(
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
            audit_result["earliest_timestamp"], command.window_days, None
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_108(
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
            command.window_days, now
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_109(
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
            audit_result["earliest_timestamp"], now
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_110(
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
            audit_result["earliest_timestamp"], command.window_days, )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_111(
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
            audit_result["XXearliest_timestampXX"], command.window_days, now
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_112(
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
            audit_result["EARLIEST_TIMESTAMP"], command.window_days, now
        )
        report = build_report(changes, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_113(
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
        report = None
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_114(
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
        report = build_report(None, excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_115(
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
        report = build_report(changes, None, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_116(
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
        report = build_report(changes, excluded_count, None, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_117(
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
        report = build_report(changes, excluded_count, used_fallback, None)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_118(
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
        report = build_report(excluded_count, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_119(
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
        report = build_report(changes, used_fallback, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_120(
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
        report = build_report(changes, excluded_count, partial_window)
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_121(
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
        report = build_report(changes, excluded_count, used_fallback, )
        return _to_response(report)

    def xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_122(
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
        return _to_response(None)

mutants_xǁManualChangeOutsideGitopsUseCaseǁ__init____mutmut['_mutmut_orig'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁ__init____mutmut['xǁManualChangeOutsideGitopsUseCaseǁ__init____mutmut_1'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['_mutmut_orig'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_orig # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_1'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_1 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_2'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_2 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_3'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_3 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_4'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_4 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_5'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_5 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_6'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_6 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_7'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_7 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_8'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_8 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_9'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_9 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_10'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_10 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_11'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_11 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_12'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_12 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_13'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_13 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_14'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_14 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_15'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_15 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_16'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_16 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_17'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_17 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_18'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_18 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_19'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_19 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_20'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_20 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_21'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_21 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_22'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_22 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_23'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_23 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_24'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_24 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_25'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_25 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_26'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_26 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_27'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_27 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_28'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_28 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_29'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_29 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_30'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_30 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_31'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_31 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_32'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_32 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_33'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_33 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_34'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_34 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_35'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_35 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_36'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_36 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_37'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_37 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_38'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_38 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_39'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_39 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_40'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_40 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_41'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_41 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_42'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_42 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_43'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_43 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_44'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_44 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_45'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_45 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_46'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_46 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_47'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_47 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_48'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_48 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_49'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_49 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_50'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_50 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_51'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_51 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_52'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_52 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_53'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_53 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_54'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_54 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_55'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_55 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_56'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_56 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_57'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_57 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_58'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_58 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_59'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_59 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_60'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_60 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_61'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_61 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_62'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_62 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_63'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_63 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_64'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_64 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_65'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_65 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_66'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_66 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_67'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_67 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_68'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_68 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_69'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_69 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_70'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_70 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_71'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_71 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_72'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_72 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_73'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_73 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_74'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_74 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_75'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_75 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_76'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_76 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_77'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_77 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_78'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_78 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_79'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_79 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_80'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_80 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_81'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_81 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_82'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_82 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_83'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_83 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_84'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_84 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_85'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_85 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_86'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_86 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_87'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_87 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_88'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_88 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_89'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_89 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_90'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_90 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_91'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_91 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_92'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_92 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_93'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_93 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_94'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_94 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_95'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_95 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_96'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_96 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_97'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_97 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_98'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_98 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_99'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_99 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_100'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_100 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_101'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_101 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_102'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_102 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_103'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_103 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_104'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_104 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_105'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_105 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_106'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_106 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_107'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_107 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_108'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_108 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_109'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_109 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_110'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_110 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_111'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_111 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_112'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_112 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_113'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_113 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_114'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_114 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_115'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_115 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_116'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_116 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_117'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_117 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_118'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_118 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_119'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_119 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_120'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_120 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_121'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_121 # type: ignore # mutmut generated
mutants_xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut['xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_122'] = ManualChangeOutsideGitopsUseCase.xǁManualChangeOutsideGitopsUseCaseǁdetect_manual_changes__mutmut_122 # type: ignore # mutmut generated
mutants_x__index_audit_events__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__index_audit_events__mutmut)
def _index_audit_events(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["name"], event["namespace"], event["timestamp"]): event["actor"]
        for event in events
    }


def x__index_audit_events__mutmut_orig(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["name"], event["namespace"], event["timestamp"]): event["actor"]
        for event in events
    }


def x__index_audit_events__mutmut_1(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["XXkindXX"], event["name"], event["namespace"], event["timestamp"]): event["actor"]
        for event in events
    }


def x__index_audit_events__mutmut_2(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["KIND"], event["name"], event["namespace"], event["timestamp"]): event["actor"]
        for event in events
    }


def x__index_audit_events__mutmut_3(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["XXnameXX"], event["namespace"], event["timestamp"]): event["actor"]
        for event in events
    }


def x__index_audit_events__mutmut_4(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["NAME"], event["namespace"], event["timestamp"]): event["actor"]
        for event in events
    }


def x__index_audit_events__mutmut_5(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["name"], event["XXnamespaceXX"], event["timestamp"]): event["actor"]
        for event in events
    }


def x__index_audit_events__mutmut_6(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["name"], event["NAMESPACE"], event["timestamp"]): event["actor"]
        for event in events
    }


def x__index_audit_events__mutmut_7(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["name"], event["namespace"], event["XXtimestampXX"]): event["actor"]
        for event in events
    }


def x__index_audit_events__mutmut_8(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["name"], event["namespace"], event["TIMESTAMP"]): event["actor"]
        for event in events
    }


def x__index_audit_events__mutmut_9(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["name"], event["namespace"], event["timestamp"]): event["XXactorXX"]
        for event in events
    }


def x__index_audit_events__mutmut_10(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["name"], event["namespace"], event["timestamp"]): event["ACTOR"]
        for event in events
    }

mutants_x__index_audit_events__mutmut['_mutmut_orig'] = x__index_audit_events__mutmut_orig # type: ignore # mutmut generated
mutants_x__index_audit_events__mutmut['x__index_audit_events__mutmut_1'] = x__index_audit_events__mutmut_1 # type: ignore # mutmut generated
mutants_x__index_audit_events__mutmut['x__index_audit_events__mutmut_2'] = x__index_audit_events__mutmut_2 # type: ignore # mutmut generated
mutants_x__index_audit_events__mutmut['x__index_audit_events__mutmut_3'] = x__index_audit_events__mutmut_3 # type: ignore # mutmut generated
mutants_x__index_audit_events__mutmut['x__index_audit_events__mutmut_4'] = x__index_audit_events__mutmut_4 # type: ignore # mutmut generated
mutants_x__index_audit_events__mutmut['x__index_audit_events__mutmut_5'] = x__index_audit_events__mutmut_5 # type: ignore # mutmut generated
mutants_x__index_audit_events__mutmut['x__index_audit_events__mutmut_6'] = x__index_audit_events__mutmut_6 # type: ignore # mutmut generated
mutants_x__index_audit_events__mutmut['x__index_audit_events__mutmut_7'] = x__index_audit_events__mutmut_7 # type: ignore # mutmut generated
mutants_x__index_audit_events__mutmut['x__index_audit_events__mutmut_8'] = x__index_audit_events__mutmut_8 # type: ignore # mutmut generated
mutants_x__index_audit_events__mutmut['x__index_audit_events__mutmut_9'] = x__index_audit_events__mutmut_9 # type: ignore # mutmut generated
mutants_x__index_audit_events__mutmut['x__index_audit_events__mutmut_10'] = x__index_audit_events__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_response__mutmut)
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


def x__to_response__mutmut_orig(report: ManualChangeOutsideGitopsReport) -> ManualChangeOutsideGitopsResponse:  # noqa: F821  # type: ignore
    return ManualChangeOutsideGitopsResponse(
        manual_changes=[_to_change_dict(change) for change in report.manual_changes],
        total_manual_changes=report.total_manual_changes,
        excluded_gitops_change_count=report.excluded_gitops_change_count,
        used_managed_fields_fallback=report.used_managed_fields_fallback,
        partial_window=report.partial_window,
        notes=report.notes,
        error=None,
    )


def x__to_response__mutmut_1(report: ManualChangeOutsideGitopsReport) -> ManualChangeOutsideGitopsResponse:  # noqa: F821  # type: ignore
    return ManualChangeOutsideGitopsResponse(
        manual_changes=None,
        total_manual_changes=report.total_manual_changes,
        excluded_gitops_change_count=report.excluded_gitops_change_count,
        used_managed_fields_fallback=report.used_managed_fields_fallback,
        partial_window=report.partial_window,
        notes=report.notes,
        error=None,
    )


def x__to_response__mutmut_2(report: ManualChangeOutsideGitopsReport) -> ManualChangeOutsideGitopsResponse:  # noqa: F821  # type: ignore
    return ManualChangeOutsideGitopsResponse(
        manual_changes=[_to_change_dict(change) for change in report.manual_changes],
        total_manual_changes=None,
        excluded_gitops_change_count=report.excluded_gitops_change_count,
        used_managed_fields_fallback=report.used_managed_fields_fallback,
        partial_window=report.partial_window,
        notes=report.notes,
        error=None,
    )


def x__to_response__mutmut_3(report: ManualChangeOutsideGitopsReport) -> ManualChangeOutsideGitopsResponse:  # noqa: F821  # type: ignore
    return ManualChangeOutsideGitopsResponse(
        manual_changes=[_to_change_dict(change) for change in report.manual_changes],
        total_manual_changes=report.total_manual_changes,
        excluded_gitops_change_count=None,
        used_managed_fields_fallback=report.used_managed_fields_fallback,
        partial_window=report.partial_window,
        notes=report.notes,
        error=None,
    )


def x__to_response__mutmut_4(report: ManualChangeOutsideGitopsReport) -> ManualChangeOutsideGitopsResponse:  # noqa: F821  # type: ignore
    return ManualChangeOutsideGitopsResponse(
        manual_changes=[_to_change_dict(change) for change in report.manual_changes],
        total_manual_changes=report.total_manual_changes,
        excluded_gitops_change_count=report.excluded_gitops_change_count,
        used_managed_fields_fallback=None,
        partial_window=report.partial_window,
        notes=report.notes,
        error=None,
    )


def x__to_response__mutmut_5(report: ManualChangeOutsideGitopsReport) -> ManualChangeOutsideGitopsResponse:  # noqa: F821  # type: ignore
    return ManualChangeOutsideGitopsResponse(
        manual_changes=[_to_change_dict(change) for change in report.manual_changes],
        total_manual_changes=report.total_manual_changes,
        excluded_gitops_change_count=report.excluded_gitops_change_count,
        used_managed_fields_fallback=report.used_managed_fields_fallback,
        partial_window=None,
        notes=report.notes,
        error=None,
    )


def x__to_response__mutmut_6(report: ManualChangeOutsideGitopsReport) -> ManualChangeOutsideGitopsResponse:  # noqa: F821  # type: ignore
    return ManualChangeOutsideGitopsResponse(
        manual_changes=[_to_change_dict(change) for change in report.manual_changes],
        total_manual_changes=report.total_manual_changes,
        excluded_gitops_change_count=report.excluded_gitops_change_count,
        used_managed_fields_fallback=report.used_managed_fields_fallback,
        partial_window=report.partial_window,
        notes=None,
        error=None,
    )


def x__to_response__mutmut_7(report: ManualChangeOutsideGitopsReport) -> ManualChangeOutsideGitopsResponse:  # noqa: F821  # type: ignore
    return ManualChangeOutsideGitopsResponse(
        total_manual_changes=report.total_manual_changes,
        excluded_gitops_change_count=report.excluded_gitops_change_count,
        used_managed_fields_fallback=report.used_managed_fields_fallback,
        partial_window=report.partial_window,
        notes=report.notes,
        error=None,
    )


def x__to_response__mutmut_8(report: ManualChangeOutsideGitopsReport) -> ManualChangeOutsideGitopsResponse:  # noqa: F821  # type: ignore
    return ManualChangeOutsideGitopsResponse(
        manual_changes=[_to_change_dict(change) for change in report.manual_changes],
        excluded_gitops_change_count=report.excluded_gitops_change_count,
        used_managed_fields_fallback=report.used_managed_fields_fallback,
        partial_window=report.partial_window,
        notes=report.notes,
        error=None,
    )


def x__to_response__mutmut_9(report: ManualChangeOutsideGitopsReport) -> ManualChangeOutsideGitopsResponse:  # noqa: F821  # type: ignore
    return ManualChangeOutsideGitopsResponse(
        manual_changes=[_to_change_dict(change) for change in report.manual_changes],
        total_manual_changes=report.total_manual_changes,
        used_managed_fields_fallback=report.used_managed_fields_fallback,
        partial_window=report.partial_window,
        notes=report.notes,
        error=None,
    )


def x__to_response__mutmut_10(report: ManualChangeOutsideGitopsReport) -> ManualChangeOutsideGitopsResponse:  # noqa: F821  # type: ignore
    return ManualChangeOutsideGitopsResponse(
        manual_changes=[_to_change_dict(change) for change in report.manual_changes],
        total_manual_changes=report.total_manual_changes,
        excluded_gitops_change_count=report.excluded_gitops_change_count,
        partial_window=report.partial_window,
        notes=report.notes,
        error=None,
    )


def x__to_response__mutmut_11(report: ManualChangeOutsideGitopsReport) -> ManualChangeOutsideGitopsResponse:  # noqa: F821  # type: ignore
    return ManualChangeOutsideGitopsResponse(
        manual_changes=[_to_change_dict(change) for change in report.manual_changes],
        total_manual_changes=report.total_manual_changes,
        excluded_gitops_change_count=report.excluded_gitops_change_count,
        used_managed_fields_fallback=report.used_managed_fields_fallback,
        notes=report.notes,
        error=None,
    )


def x__to_response__mutmut_12(report: ManualChangeOutsideGitopsReport) -> ManualChangeOutsideGitopsResponse:  # noqa: F821  # type: ignore
    return ManualChangeOutsideGitopsResponse(
        manual_changes=[_to_change_dict(change) for change in report.manual_changes],
        total_manual_changes=report.total_manual_changes,
        excluded_gitops_change_count=report.excluded_gitops_change_count,
        used_managed_fields_fallback=report.used_managed_fields_fallback,
        partial_window=report.partial_window,
        error=None,
    )


def x__to_response__mutmut_13(report: ManualChangeOutsideGitopsReport) -> ManualChangeOutsideGitopsResponse:  # noqa: F821  # type: ignore
    return ManualChangeOutsideGitopsResponse(
        manual_changes=[_to_change_dict(change) for change in report.manual_changes],
        total_manual_changes=report.total_manual_changes,
        excluded_gitops_change_count=report.excluded_gitops_change_count,
        used_managed_fields_fallback=report.used_managed_fields_fallback,
        partial_window=report.partial_window,
        notes=report.notes,
        )


def x__to_response__mutmut_14(report: ManualChangeOutsideGitopsReport) -> ManualChangeOutsideGitopsResponse:  # noqa: F821  # type: ignore
    return ManualChangeOutsideGitopsResponse(
        manual_changes=[_to_change_dict(None) for change in report.manual_changes],
        total_manual_changes=report.total_manual_changes,
        excluded_gitops_change_count=report.excluded_gitops_change_count,
        used_managed_fields_fallback=report.used_managed_fields_fallback,
        partial_window=report.partial_window,
        notes=report.notes,
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
mutants_x__to_response__mutmut['x__to_response__mutmut_11'] = x__to_response__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_12'] = x__to_response__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_13'] = x__to_response__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_14'] = x__to_response__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_change_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_change_dict__mutmut)
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


def x__to_change_dict__mutmut_orig(change: ManualChange) -> ManualChangeDict:
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


def x__to_change_dict__mutmut_1(change: ManualChange) -> ManualChangeDict:
    return ManualChangeDict(
        kind=None,
        name=change.name,
        namespace=change.namespace,
        timestamp=change.timestamp,
        actor=change.actor,
        actor_type=change.actor_type,
        changed_fields=change.changed_fields,
        severity=change.severity,
        is_limited_actor_info=change.is_limited_actor_info,
    )


def x__to_change_dict__mutmut_2(change: ManualChange) -> ManualChangeDict:
    return ManualChangeDict(
        kind=change.kind,
        name=None,
        namespace=change.namespace,
        timestamp=change.timestamp,
        actor=change.actor,
        actor_type=change.actor_type,
        changed_fields=change.changed_fields,
        severity=change.severity,
        is_limited_actor_info=change.is_limited_actor_info,
    )


def x__to_change_dict__mutmut_3(change: ManualChange) -> ManualChangeDict:
    return ManualChangeDict(
        kind=change.kind,
        name=change.name,
        namespace=None,
        timestamp=change.timestamp,
        actor=change.actor,
        actor_type=change.actor_type,
        changed_fields=change.changed_fields,
        severity=change.severity,
        is_limited_actor_info=change.is_limited_actor_info,
    )


def x__to_change_dict__mutmut_4(change: ManualChange) -> ManualChangeDict:
    return ManualChangeDict(
        kind=change.kind,
        name=change.name,
        namespace=change.namespace,
        timestamp=None,
        actor=change.actor,
        actor_type=change.actor_type,
        changed_fields=change.changed_fields,
        severity=change.severity,
        is_limited_actor_info=change.is_limited_actor_info,
    )


def x__to_change_dict__mutmut_5(change: ManualChange) -> ManualChangeDict:
    return ManualChangeDict(
        kind=change.kind,
        name=change.name,
        namespace=change.namespace,
        timestamp=change.timestamp,
        actor=None,
        actor_type=change.actor_type,
        changed_fields=change.changed_fields,
        severity=change.severity,
        is_limited_actor_info=change.is_limited_actor_info,
    )


def x__to_change_dict__mutmut_6(change: ManualChange) -> ManualChangeDict:
    return ManualChangeDict(
        kind=change.kind,
        name=change.name,
        namespace=change.namespace,
        timestamp=change.timestamp,
        actor=change.actor,
        actor_type=None,
        changed_fields=change.changed_fields,
        severity=change.severity,
        is_limited_actor_info=change.is_limited_actor_info,
    )


def x__to_change_dict__mutmut_7(change: ManualChange) -> ManualChangeDict:
    return ManualChangeDict(
        kind=change.kind,
        name=change.name,
        namespace=change.namespace,
        timestamp=change.timestamp,
        actor=change.actor,
        actor_type=change.actor_type,
        changed_fields=None,
        severity=change.severity,
        is_limited_actor_info=change.is_limited_actor_info,
    )


def x__to_change_dict__mutmut_8(change: ManualChange) -> ManualChangeDict:
    return ManualChangeDict(
        kind=change.kind,
        name=change.name,
        namespace=change.namespace,
        timestamp=change.timestamp,
        actor=change.actor,
        actor_type=change.actor_type,
        changed_fields=change.changed_fields,
        severity=None,
        is_limited_actor_info=change.is_limited_actor_info,
    )


def x__to_change_dict__mutmut_9(change: ManualChange) -> ManualChangeDict:
    return ManualChangeDict(
        kind=change.kind,
        name=change.name,
        namespace=change.namespace,
        timestamp=change.timestamp,
        actor=change.actor,
        actor_type=change.actor_type,
        changed_fields=change.changed_fields,
        severity=change.severity,
        is_limited_actor_info=None,
    )


def x__to_change_dict__mutmut_10(change: ManualChange) -> ManualChangeDict:
    return ManualChangeDict(
        name=change.name,
        namespace=change.namespace,
        timestamp=change.timestamp,
        actor=change.actor,
        actor_type=change.actor_type,
        changed_fields=change.changed_fields,
        severity=change.severity,
        is_limited_actor_info=change.is_limited_actor_info,
    )


def x__to_change_dict__mutmut_11(change: ManualChange) -> ManualChangeDict:
    return ManualChangeDict(
        kind=change.kind,
        namespace=change.namespace,
        timestamp=change.timestamp,
        actor=change.actor,
        actor_type=change.actor_type,
        changed_fields=change.changed_fields,
        severity=change.severity,
        is_limited_actor_info=change.is_limited_actor_info,
    )


def x__to_change_dict__mutmut_12(change: ManualChange) -> ManualChangeDict:
    return ManualChangeDict(
        kind=change.kind,
        name=change.name,
        timestamp=change.timestamp,
        actor=change.actor,
        actor_type=change.actor_type,
        changed_fields=change.changed_fields,
        severity=change.severity,
        is_limited_actor_info=change.is_limited_actor_info,
    )


def x__to_change_dict__mutmut_13(change: ManualChange) -> ManualChangeDict:
    return ManualChangeDict(
        kind=change.kind,
        name=change.name,
        namespace=change.namespace,
        actor=change.actor,
        actor_type=change.actor_type,
        changed_fields=change.changed_fields,
        severity=change.severity,
        is_limited_actor_info=change.is_limited_actor_info,
    )


def x__to_change_dict__mutmut_14(change: ManualChange) -> ManualChangeDict:
    return ManualChangeDict(
        kind=change.kind,
        name=change.name,
        namespace=change.namespace,
        timestamp=change.timestamp,
        actor_type=change.actor_type,
        changed_fields=change.changed_fields,
        severity=change.severity,
        is_limited_actor_info=change.is_limited_actor_info,
    )


def x__to_change_dict__mutmut_15(change: ManualChange) -> ManualChangeDict:
    return ManualChangeDict(
        kind=change.kind,
        name=change.name,
        namespace=change.namespace,
        timestamp=change.timestamp,
        actor=change.actor,
        changed_fields=change.changed_fields,
        severity=change.severity,
        is_limited_actor_info=change.is_limited_actor_info,
    )


def x__to_change_dict__mutmut_16(change: ManualChange) -> ManualChangeDict:
    return ManualChangeDict(
        kind=change.kind,
        name=change.name,
        namespace=change.namespace,
        timestamp=change.timestamp,
        actor=change.actor,
        actor_type=change.actor_type,
        severity=change.severity,
        is_limited_actor_info=change.is_limited_actor_info,
    )


def x__to_change_dict__mutmut_17(change: ManualChange) -> ManualChangeDict:
    return ManualChangeDict(
        kind=change.kind,
        name=change.name,
        namespace=change.namespace,
        timestamp=change.timestamp,
        actor=change.actor,
        actor_type=change.actor_type,
        changed_fields=change.changed_fields,
        is_limited_actor_info=change.is_limited_actor_info,
    )


def x__to_change_dict__mutmut_18(change: ManualChange) -> ManualChangeDict:
    return ManualChangeDict(
        kind=change.kind,
        name=change.name,
        namespace=change.namespace,
        timestamp=change.timestamp,
        actor=change.actor,
        actor_type=change.actor_type,
        changed_fields=change.changed_fields,
        severity=change.severity,
        )

mutants_x__to_change_dict__mutmut['_mutmut_orig'] = x__to_change_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_change_dict__mutmut['x__to_change_dict__mutmut_1'] = x__to_change_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_change_dict__mutmut['x__to_change_dict__mutmut_2'] = x__to_change_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_change_dict__mutmut['x__to_change_dict__mutmut_3'] = x__to_change_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_change_dict__mutmut['x__to_change_dict__mutmut_4'] = x__to_change_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_change_dict__mutmut['x__to_change_dict__mutmut_5'] = x__to_change_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_change_dict__mutmut['x__to_change_dict__mutmut_6'] = x__to_change_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_change_dict__mutmut['x__to_change_dict__mutmut_7'] = x__to_change_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_change_dict__mutmut['x__to_change_dict__mutmut_8'] = x__to_change_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_change_dict__mutmut['x__to_change_dict__mutmut_9'] = x__to_change_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_change_dict__mutmut['x__to_change_dict__mutmut_10'] = x__to_change_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_change_dict__mutmut['x__to_change_dict__mutmut_11'] = x__to_change_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_change_dict__mutmut['x__to_change_dict__mutmut_12'] = x__to_change_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_change_dict__mutmut['x__to_change_dict__mutmut_13'] = x__to_change_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_change_dict__mutmut['x__to_change_dict__mutmut_14'] = x__to_change_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_change_dict__mutmut['x__to_change_dict__mutmut_15'] = x__to_change_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_change_dict__mutmut['x__to_change_dict__mutmut_16'] = x__to_change_dict__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_change_dict__mutmut['x__to_change_dict__mutmut_17'] = x__to_change_dict__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_change_dict__mutmut['x__to_change_dict__mutmut_18'] = x__to_change_dict__mutmut_18 # type: ignore # mutmut generated
