from __future__ import annotations

from collections.abc import Callable
from dataclasses import replace

from hexawyn.domain.models.helm_values_diff import (
    DiffSeverity,
    HelmValuesDiffReport,
    ValueDiff,
)
from hexawyn.domain.services.helm_values_diff.severity_matrix import (
    classify_severity,
    is_secret_key,
)
from hexawyn.domain.services.helm_values_diff.values_deep_diff import deep_diff

_REDACTED = "[REDACTED]"
_CHRONIC_DIFF_DAYS = 7

DiffAgeProvider = Callable[[str], "int | None"]


class HelmValuesDiffService:
    """Domain service — turns two Helm values trees into a graded diff report.

    Enriches the structural diff with the authoritative severity matrix,
    redacts secret-bearing values, keeps the source→target direction explicit
    (source is the reference environment, e.g. staging), attaches
    human-readable discrepancy suggestions, and — when a diff-age provider is
    injected — flags critical differences that have persisted beyond a week.
    """

    def __init__(self, diff_age_provider: DiffAgeProvider | None = None) -> None:
        self._diff_age_provider = diff_age_provider

    def diff(
        self,
        release: str,
        source_env: str,
        target_env: str,
        source_values: dict[str, object],
        target_values: dict[str, object],
    ) -> HelmValuesDiffReport:
        enriched = [
            self._enrich(raw, source_env, target_env)
            for raw in deep_diff(source_values, target_values)
        ]

        critical = [diff for diff in enriched if diff.severity == "critical"]
        warning = [diff for diff in enriched if diff.severity == "warning"]
        informational = [diff for diff in enriched if diff.severity == "informational"]

        return HelmValuesDiffReport(
            release=release,
            source_env=source_env,
            target_env=target_env,
            critical=critical,
            warning=warning,
            informational=informational,
            total_differences=len(enriched),
            in_sync=len(enriched) == 0,
        )

    def _enrich(self, raw: ValueDiff, source_env: str, target_env: str) -> ValueDiff:
        secret = is_secret_key(raw.key_path)
        severity = classify_severity(raw.key_path)
        source_value = _REDACTED if secret and raw.source_value else raw.source_value
        target_value = _REDACTED if secret and raw.target_value else raw.target_value
        suggestion = self._suggest(raw, severity, source_env, target_env, secret)
        return replace(
            raw,
            source_value=source_value,
            target_value=target_value,
            severity=severity,
            is_secret=secret,
            suggestion=suggestion,
        )

    def _suggest(
        self,
        raw: ValueDiff,
        severity: DiffSeverity,
        source_env: str,
        target_env: str,
        secret: bool,
    ) -> str:
        parts = [self._base_suggestion(raw, source_env, target_env, secret)]
        if raw.type_mismatch:
            parts.append(
                "Type mismatch may cause runtime issues (e.g. a quoted number "
                "parsed as a string)."
            )
        age_note = self._age_note(raw, severity)
        if age_note:
            parts.append(age_note)
        return " ".join(part for part in parts if part)

    def _base_suggestion(
        self, raw: ValueDiff, source_env: str, target_env: str, secret: bool
    ) -> str:
        key = raw.key_path.lower()
        if secret:
            return f"Secret value differs between {source_env} and {target_env}."
        if key.endswith("image.tag") or key.endswith("image.repository"):
            return (
                f"Different code is running: {source_env} uses {raw.source_value!r}, "
                f"{target_env} uses {raw.target_value!r}."
            )
        if "replica" in key:
            return (
                f"Replica count differs, which affects availability and capacity "
                f"({source_env}={raw.source_value}, {target_env}={raw.target_value})."
            )
        if "resources.limits" in key or "resources.requests" in key:
            return "Resource sizing differs, which can change performance and OOM behaviour."
        if raw.change_type == "added":
            return f"Key present only in {target_env}."
        if raw.change_type == "removed":
            return f"Key present only in {source_env}."
        return f"Value differs between {source_env} and {target_env}."

    def _age_note(self, raw: ValueDiff, severity: DiffSeverity) -> str:
        if self._diff_age_provider is None or severity != "critical":
            return ""
        age_days = self._diff_age_provider(raw.key_path)
        if age_days is not None and age_days > _CHRONIC_DIFF_DAYS:
            return f"This critical difference has persisted for {age_days} days."
        return ""
