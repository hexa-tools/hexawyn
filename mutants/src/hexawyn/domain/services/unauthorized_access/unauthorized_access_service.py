from __future__ import annotations

from hexawyn.application.ports.driven.unauthorized_access_port import UnauthorizedAccessRaw
from hexawyn.domain.models.unauthorized_access import UnauthorizedAccessReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_unauthorized_access_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_unauthorized_access_report__mutmut)
def compute_unauthorized_access_report(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_orig(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_1(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_2(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=None, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_3(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=None, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_4(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning=None
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_5(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_6(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_7(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_8(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=True, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_9(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="XXAucune donnee d'acces disponible.XX"
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_10(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_11(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="AUCUNE DONNEE D'ACCES DISPONIBLE."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_12(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = None
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_13(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["XXattempt_countXX"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_14(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["ATTEMPT_COUNT"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_15(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = None
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_16(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["XXsource_typeXX"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_17(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["SOURCE_TYPE"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_18(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = None

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_19(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(None, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_20(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, None)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_21(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_22(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, )

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_23(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=None,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_24(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=None,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_25(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=None,
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_26(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=None,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_27(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=None,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_28(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=None,
    )


def x_compute_unauthorized_access_report__mutmut_29(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_30(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_31(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_32(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_33(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_34(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        )


def x_compute_unauthorized_access_report__mutmut_35(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["XXwindow_minutesXX"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_36(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["WINDOW_MINUTES"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def x_compute_unauthorized_access_report__mutmut_37(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=False,
    )

mutants_x_compute_unauthorized_access_report__mutmut['_mutmut_orig'] = x_compute_unauthorized_access_report__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_1'] = x_compute_unauthorized_access_report__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_2'] = x_compute_unauthorized_access_report__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_3'] = x_compute_unauthorized_access_report__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_4'] = x_compute_unauthorized_access_report__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_5'] = x_compute_unauthorized_access_report__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_6'] = x_compute_unauthorized_access_report__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_7'] = x_compute_unauthorized_access_report__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_8'] = x_compute_unauthorized_access_report__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_9'] = x_compute_unauthorized_access_report__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_10'] = x_compute_unauthorized_access_report__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_11'] = x_compute_unauthorized_access_report__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_12'] = x_compute_unauthorized_access_report__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_13'] = x_compute_unauthorized_access_report__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_14'] = x_compute_unauthorized_access_report__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_15'] = x_compute_unauthorized_access_report__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_16'] = x_compute_unauthorized_access_report__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_17'] = x_compute_unauthorized_access_report__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_18'] = x_compute_unauthorized_access_report__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_19'] = x_compute_unauthorized_access_report__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_20'] = x_compute_unauthorized_access_report__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_21'] = x_compute_unauthorized_access_report__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_22'] = x_compute_unauthorized_access_report__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_23'] = x_compute_unauthorized_access_report__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_24'] = x_compute_unauthorized_access_report__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_25'] = x_compute_unauthorized_access_report__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_26'] = x_compute_unauthorized_access_report__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_27'] = x_compute_unauthorized_access_report__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_28'] = x_compute_unauthorized_access_report__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_29'] = x_compute_unauthorized_access_report__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_30'] = x_compute_unauthorized_access_report__mutmut_30 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_31'] = x_compute_unauthorized_access_report__mutmut_31 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_32'] = x_compute_unauthorized_access_report__mutmut_32 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_33'] = x_compute_unauthorized_access_report__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_34'] = x_compute_unauthorized_access_report__mutmut_34 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_35'] = x_compute_unauthorized_access_report__mutmut_35 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_36'] = x_compute_unauthorized_access_report__mutmut_36 # type: ignore # mutmut generated
mutants_x_compute_unauthorized_access_report__mutmut['x_compute_unauthorized_access_report__mutmut_37'] = x_compute_unauthorized_access_report__mutmut_37 # type: ignore # mutmut generated
mutants_x__alert_level__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__alert_level__mutmut)
def _alert_level(count: int, source: str) -> str:
    if source == "internal":
        return "medium" if count > 50 else "low"  # noqa: PLR2004
    if count > 20:  # noqa: PLR2004
        return "high"
    if count > 0:
        return "medium"
    return "low"


def x__alert_level__mutmut_orig(count: int, source: str) -> str:
    if source == "internal":
        return "medium" if count > 50 else "low"  # noqa: PLR2004
    if count > 20:  # noqa: PLR2004
        return "high"
    if count > 0:
        return "medium"
    return "low"


def x__alert_level__mutmut_1(count: int, source: str) -> str:
    if source != "internal":
        return "medium" if count > 50 else "low"  # noqa: PLR2004
    if count > 20:  # noqa: PLR2004
        return "high"
    if count > 0:
        return "medium"
    return "low"


def x__alert_level__mutmut_2(count: int, source: str) -> str:
    if source == "XXinternalXX":
        return "medium" if count > 50 else "low"  # noqa: PLR2004
    if count > 20:  # noqa: PLR2004
        return "high"
    if count > 0:
        return "medium"
    return "low"


def x__alert_level__mutmut_3(count: int, source: str) -> str:
    if source == "INTERNAL":
        return "medium" if count > 50 else "low"  # noqa: PLR2004
    if count > 20:  # noqa: PLR2004
        return "high"
    if count > 0:
        return "medium"
    return "low"


def x__alert_level__mutmut_4(count: int, source: str) -> str:
    if source == "internal":
        return "XXmediumXX" if count > 50 else "low"  # noqa: PLR2004
    if count > 20:  # noqa: PLR2004
        return "high"
    if count > 0:
        return "medium"
    return "low"


def x__alert_level__mutmut_5(count: int, source: str) -> str:
    if source == "internal":
        return "MEDIUM" if count > 50 else "low"  # noqa: PLR2004
    if count > 20:  # noqa: PLR2004
        return "high"
    if count > 0:
        return "medium"
    return "low"


def x__alert_level__mutmut_6(count: int, source: str) -> str:
    if source == "internal":
        return "medium" if count >= 50 else "low"  # noqa: PLR2004
    if count > 20:  # noqa: PLR2004
        return "high"
    if count > 0:
        return "medium"
    return "low"


def x__alert_level__mutmut_7(count: int, source: str) -> str:
    if source == "internal":
        return "medium" if count > 51 else "low"  # noqa: PLR2004
    if count > 20:  # noqa: PLR2004
        return "high"
    if count > 0:
        return "medium"
    return "low"


def x__alert_level__mutmut_8(count: int, source: str) -> str:
    if source == "internal":
        return "medium" if count > 50 else "XXlowXX"  # noqa: PLR2004
    if count > 20:  # noqa: PLR2004
        return "high"
    if count > 0:
        return "medium"
    return "low"


def x__alert_level__mutmut_9(count: int, source: str) -> str:
    if source == "internal":
        return "medium" if count > 50 else "LOW"  # noqa: PLR2004
    if count > 20:  # noqa: PLR2004
        return "high"
    if count > 0:
        return "medium"
    return "low"


def x__alert_level__mutmut_10(count: int, source: str) -> str:
    if source == "internal":
        return "medium" if count > 50 else "low"  # noqa: PLR2004
    if count >= 20:  # noqa: PLR2004
        return "high"
    if count > 0:
        return "medium"
    return "low"


def x__alert_level__mutmut_11(count: int, source: str) -> str:
    if source == "internal":
        return "medium" if count > 50 else "low"  # noqa: PLR2004
    if count > 21:  # noqa: PLR2004
        return "high"
    if count > 0:
        return "medium"
    return "low"


def x__alert_level__mutmut_12(count: int, source: str) -> str:
    if source == "internal":
        return "medium" if count > 50 else "low"  # noqa: PLR2004
    if count > 20:  # noqa: PLR2004
        return "XXhighXX"
    if count > 0:
        return "medium"
    return "low"


def x__alert_level__mutmut_13(count: int, source: str) -> str:
    if source == "internal":
        return "medium" if count > 50 else "low"  # noqa: PLR2004
    if count > 20:  # noqa: PLR2004
        return "HIGH"
    if count > 0:
        return "medium"
    return "low"


def x__alert_level__mutmut_14(count: int, source: str) -> str:
    if source == "internal":
        return "medium" if count > 50 else "low"  # noqa: PLR2004
    if count > 20:  # noqa: PLR2004
        return "high"
    if count >= 0:
        return "medium"
    return "low"


def x__alert_level__mutmut_15(count: int, source: str) -> str:
    if source == "internal":
        return "medium" if count > 50 else "low"  # noqa: PLR2004
    if count > 20:  # noqa: PLR2004
        return "high"
    if count > 1:
        return "medium"
    return "low"


def x__alert_level__mutmut_16(count: int, source: str) -> str:
    if source == "internal":
        return "medium" if count > 50 else "low"  # noqa: PLR2004
    if count > 20:  # noqa: PLR2004
        return "high"
    if count > 0:
        return "XXmediumXX"
    return "low"


def x__alert_level__mutmut_17(count: int, source: str) -> str:
    if source == "internal":
        return "medium" if count > 50 else "low"  # noqa: PLR2004
    if count > 20:  # noqa: PLR2004
        return "high"
    if count > 0:
        return "MEDIUM"
    return "low"


def x__alert_level__mutmut_18(count: int, source: str) -> str:
    if source == "internal":
        return "medium" if count > 50 else "low"  # noqa: PLR2004
    if count > 20:  # noqa: PLR2004
        return "high"
    if count > 0:
        return "medium"
    return "XXlowXX"


def x__alert_level__mutmut_19(count: int, source: str) -> str:
    if source == "internal":
        return "medium" if count > 50 else "low"  # noqa: PLR2004
    if count > 20:  # noqa: PLR2004
        return "high"
    if count > 0:
        return "medium"
    return "LOW"

mutants_x__alert_level__mutmut['_mutmut_orig'] = x__alert_level__mutmut_orig # type: ignore # mutmut generated
mutants_x__alert_level__mutmut['x__alert_level__mutmut_1'] = x__alert_level__mutmut_1 # type: ignore # mutmut generated
mutants_x__alert_level__mutmut['x__alert_level__mutmut_2'] = x__alert_level__mutmut_2 # type: ignore # mutmut generated
mutants_x__alert_level__mutmut['x__alert_level__mutmut_3'] = x__alert_level__mutmut_3 # type: ignore # mutmut generated
mutants_x__alert_level__mutmut['x__alert_level__mutmut_4'] = x__alert_level__mutmut_4 # type: ignore # mutmut generated
mutants_x__alert_level__mutmut['x__alert_level__mutmut_5'] = x__alert_level__mutmut_5 # type: ignore # mutmut generated
mutants_x__alert_level__mutmut['x__alert_level__mutmut_6'] = x__alert_level__mutmut_6 # type: ignore # mutmut generated
mutants_x__alert_level__mutmut['x__alert_level__mutmut_7'] = x__alert_level__mutmut_7 # type: ignore # mutmut generated
mutants_x__alert_level__mutmut['x__alert_level__mutmut_8'] = x__alert_level__mutmut_8 # type: ignore # mutmut generated
mutants_x__alert_level__mutmut['x__alert_level__mutmut_9'] = x__alert_level__mutmut_9 # type: ignore # mutmut generated
mutants_x__alert_level__mutmut['x__alert_level__mutmut_10'] = x__alert_level__mutmut_10 # type: ignore # mutmut generated
mutants_x__alert_level__mutmut['x__alert_level__mutmut_11'] = x__alert_level__mutmut_11 # type: ignore # mutmut generated
mutants_x__alert_level__mutmut['x__alert_level__mutmut_12'] = x__alert_level__mutmut_12 # type: ignore # mutmut generated
mutants_x__alert_level__mutmut['x__alert_level__mutmut_13'] = x__alert_level__mutmut_13 # type: ignore # mutmut generated
mutants_x__alert_level__mutmut['x__alert_level__mutmut_14'] = x__alert_level__mutmut_14 # type: ignore # mutmut generated
mutants_x__alert_level__mutmut['x__alert_level__mutmut_15'] = x__alert_level__mutmut_15 # type: ignore # mutmut generated
mutants_x__alert_level__mutmut['x__alert_level__mutmut_16'] = x__alert_level__mutmut_16 # type: ignore # mutmut generated
mutants_x__alert_level__mutmut['x__alert_level__mutmut_17'] = x__alert_level__mutmut_17 # type: ignore # mutmut generated
mutants_x__alert_level__mutmut['x__alert_level__mutmut_18'] = x__alert_level__mutmut_18 # type: ignore # mutmut generated
mutants_x__alert_level__mutmut['x__alert_level__mutmut_19'] = x__alert_level__mutmut_19 # type: ignore # mutmut generated
