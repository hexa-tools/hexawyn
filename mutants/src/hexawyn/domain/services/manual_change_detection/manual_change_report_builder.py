from __future__ import annotations

from hexawyn.domain.models.manual_change import ManualChange, ManualChangeOutsideGitOpsReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_report__mutmut)
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


def x_build_report__mutmut_orig(
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


def x_build_report__mutmut_1(
    changes: list[ManualChange],
    excluded_count: int,
    used_fallback: bool,
    partial_window: bool,
) -> ManualChangeOutsideGitOpsReport:
    notes: list[str] = None
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


def x_build_report__mutmut_2(
    changes: list[ManualChange],
    excluded_count: int,
    used_fallback: bool,
    partial_window: bool,
) -> ManualChangeOutsideGitOpsReport:
    notes: list[str] = []
    if used_fallback:
        notes.append(
            None
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


def x_build_report__mutmut_3(
    changes: list[ManualChange],
    excluded_count: int,
    used_fallback: bool,
    partial_window: bool,
) -> ManualChangeOutsideGitOpsReport:
    notes: list[str] = []
    if used_fallback:
        notes.append(
            "XXKubernetes audit logs are not configured; falling back to managedFields XX"
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


def x_build_report__mutmut_4(
    changes: list[ManualChange],
    excluded_count: int,
    used_fallback: bool,
    partial_window: bool,
) -> ManualChangeOutsideGitOpsReport:
    notes: list[str] = []
    if used_fallback:
        notes.append(
            "kubernetes audit logs are not configured; falling back to managedfields "
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


def x_build_report__mutmut_5(
    changes: list[ManualChange],
    excluded_count: int,
    used_fallback: bool,
    partial_window: bool,
) -> ManualChangeOutsideGitOpsReport:
    notes: list[str] = []
    if used_fallback:
        notes.append(
            "KUBERNETES AUDIT LOGS ARE NOT CONFIGURED; FALLING BACK TO MANAGEDFIELDS "
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


def x_build_report__mutmut_6(
    changes: list[ManualChange],
    excluded_count: int,
    used_fallback: bool,
    partial_window: bool,
) -> ManualChangeOutsideGitOpsReport:
    notes: list[str] = []
    if used_fallback:
        notes.append(
            "Kubernetes audit logs are not configured; falling back to managedFields "
            "XXanalysis with limited actor info.XX"
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


def x_build_report__mutmut_7(
    changes: list[ManualChange],
    excluded_count: int,
    used_fallback: bool,
    partial_window: bool,
) -> ManualChangeOutsideGitOpsReport:
    notes: list[str] = []
    if used_fallback:
        notes.append(
            "Kubernetes audit logs are not configured; falling back to managedFields "
            "ANALYSIS WITH LIMITED ACTOR INFO."
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


def x_build_report__mutmut_8(
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
            None
        )
    return ManualChangeOutsideGitOpsReport(
        manual_changes=changes,
        total_manual_changes=len(changes),
        excluded_gitops_change_count=excluded_count,
        used_managed_fields_fallback=used_fallback,
        partial_window=partial_window,
        notes=notes,
    )


def x_build_report__mutmut_9(
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
            "XXAudit log data does not cover the full requested window — older entries XX"
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


def x_build_report__mutmut_10(
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
            "audit log data does not cover the full requested window — older entries "
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


def x_build_report__mutmut_11(
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
            "AUDIT LOG DATA DOES NOT COVER THE FULL REQUESTED WINDOW — OLDER ENTRIES "
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


def x_build_report__mutmut_12(
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
            "XXmay have been pruned or rotated away. Partial data returned.XX"
        )
    return ManualChangeOutsideGitOpsReport(
        manual_changes=changes,
        total_manual_changes=len(changes),
        excluded_gitops_change_count=excluded_count,
        used_managed_fields_fallback=used_fallback,
        partial_window=partial_window,
        notes=notes,
    )


def x_build_report__mutmut_13(
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
            "may have been pruned or rotated away. partial data returned."
        )
    return ManualChangeOutsideGitOpsReport(
        manual_changes=changes,
        total_manual_changes=len(changes),
        excluded_gitops_change_count=excluded_count,
        used_managed_fields_fallback=used_fallback,
        partial_window=partial_window,
        notes=notes,
    )


def x_build_report__mutmut_14(
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
            "MAY HAVE BEEN PRUNED OR ROTATED AWAY. PARTIAL DATA RETURNED."
        )
    return ManualChangeOutsideGitOpsReport(
        manual_changes=changes,
        total_manual_changes=len(changes),
        excluded_gitops_change_count=excluded_count,
        used_managed_fields_fallback=used_fallback,
        partial_window=partial_window,
        notes=notes,
    )


def x_build_report__mutmut_15(
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
        manual_changes=None,
        total_manual_changes=len(changes),
        excluded_gitops_change_count=excluded_count,
        used_managed_fields_fallback=used_fallback,
        partial_window=partial_window,
        notes=notes,
    )


def x_build_report__mutmut_16(
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
        total_manual_changes=None,
        excluded_gitops_change_count=excluded_count,
        used_managed_fields_fallback=used_fallback,
        partial_window=partial_window,
        notes=notes,
    )


def x_build_report__mutmut_17(
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
        excluded_gitops_change_count=None,
        used_managed_fields_fallback=used_fallback,
        partial_window=partial_window,
        notes=notes,
    )


def x_build_report__mutmut_18(
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
        used_managed_fields_fallback=None,
        partial_window=partial_window,
        notes=notes,
    )


def x_build_report__mutmut_19(
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
        partial_window=None,
        notes=notes,
    )


def x_build_report__mutmut_20(
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
        notes=None,
    )


def x_build_report__mutmut_21(
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
        total_manual_changes=len(changes),
        excluded_gitops_change_count=excluded_count,
        used_managed_fields_fallback=used_fallback,
        partial_window=partial_window,
        notes=notes,
    )


def x_build_report__mutmut_22(
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
        excluded_gitops_change_count=excluded_count,
        used_managed_fields_fallback=used_fallback,
        partial_window=partial_window,
        notes=notes,
    )


def x_build_report__mutmut_23(
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
        used_managed_fields_fallback=used_fallback,
        partial_window=partial_window,
        notes=notes,
    )


def x_build_report__mutmut_24(
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
        partial_window=partial_window,
        notes=notes,
    )


def x_build_report__mutmut_25(
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
        notes=notes,
    )


def x_build_report__mutmut_26(
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
        )

mutants_x_build_report__mutmut['_mutmut_orig'] = x_build_report__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_1'] = x_build_report__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_2'] = x_build_report__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_3'] = x_build_report__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_4'] = x_build_report__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_5'] = x_build_report__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_6'] = x_build_report__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_7'] = x_build_report__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_8'] = x_build_report__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_9'] = x_build_report__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_10'] = x_build_report__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_11'] = x_build_report__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_12'] = x_build_report__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_13'] = x_build_report__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_14'] = x_build_report__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_15'] = x_build_report__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_16'] = x_build_report__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_17'] = x_build_report__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_18'] = x_build_report__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_19'] = x_build_report__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_20'] = x_build_report__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_21'] = x_build_report__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_22'] = x_build_report__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_23'] = x_build_report__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_24'] = x_build_report__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_25'] = x_build_report__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_26'] = x_build_report__mutmut_26 # type: ignore # mutmut generated
