from __future__ import annotations

from hexawyn.domain.models.manual_change import ManualChange, ManualChangeOutsideGitOpsReport


def build_report(
    changes: list[ManualChange],
    excluded_count: int,
    used_fallback: bool,
    partial_window: bool,
) -> ManualChangeOutsideGitOpsReport:
    notes: list[str] = []
    if used_fallback:
        notes.append(
            "Kubernetes audit logs are not configured; falling back to managedFields "
            "analysis with limited actor info."
        )
    if partial_window:
        notes.append(
            "Audit log data does not cover the full requested window — older entries "
            "may have been pruned or rotated away. Partial data returned."
        )
    return ManualChangeOutsideGitOpsReport(
        manual_changes=changes,
        total_manual_changes=len(changes),
        excluded_gitops_change_count=excluded_count,
        used_managed_fields_fallback=used_fallback,
        partial_window=partial_window,
        notes=notes,
    )
