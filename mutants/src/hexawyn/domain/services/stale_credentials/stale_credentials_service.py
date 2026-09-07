from __future__ import annotations

from hexawyn.application.ports.driven.stale_credentials_port import StaleCredentialRaw
from hexawyn.domain.models.stale_credentials import StaleCredential, StaleCredentialsReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_stale_credentials_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_stale_credentials_report__mutmut)
def compute_stale_credentials_report(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_orig(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_1(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_2(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=None, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_3(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=None, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_4(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning=None
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_5(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_6(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_7(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_8(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=True, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_9(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="XXAucune donnee de rotation disponible.XX"
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_10(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_11(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="AUCUNE DONNEE DE ROTATION DISPONIBLE."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_12(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = None  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_13(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["XXdays_unrotatedXX"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_14(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["DAYS_UNROTATED"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_15(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] > 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_16(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 91]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_17(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = None
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_18(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(None)
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_19(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(2 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_20(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["XXrisk_levelXX"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_21(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["RISK_LEVEL"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_22(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] != "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_23(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "XXcriticalXX")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_24(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "CRITICAL")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_25(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=None,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_26(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=None,
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_27(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=None,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_28(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=None,
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_29(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=None,
    )


def x_compute_stale_credentials_report__mutmut_30(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_31(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_32(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_33(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        has_data=True,
    )


def x_compute_stale_credentials_report__mutmut_34(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        )


def x_compute_stale_credentials_report__mutmut_35(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]  # noqa: PLR2004
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=False,
    )

mutants_x_compute_stale_credentials_report__mutmut['_mutmut_orig'] = x_compute_stale_credentials_report__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_1'] = x_compute_stale_credentials_report__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_2'] = x_compute_stale_credentials_report__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_3'] = x_compute_stale_credentials_report__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_4'] = x_compute_stale_credentials_report__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_5'] = x_compute_stale_credentials_report__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_6'] = x_compute_stale_credentials_report__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_7'] = x_compute_stale_credentials_report__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_8'] = x_compute_stale_credentials_report__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_9'] = x_compute_stale_credentials_report__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_10'] = x_compute_stale_credentials_report__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_11'] = x_compute_stale_credentials_report__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_12'] = x_compute_stale_credentials_report__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_13'] = x_compute_stale_credentials_report__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_14'] = x_compute_stale_credentials_report__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_15'] = x_compute_stale_credentials_report__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_16'] = x_compute_stale_credentials_report__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_17'] = x_compute_stale_credentials_report__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_18'] = x_compute_stale_credentials_report__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_19'] = x_compute_stale_credentials_report__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_20'] = x_compute_stale_credentials_report__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_21'] = x_compute_stale_credentials_report__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_22'] = x_compute_stale_credentials_report__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_23'] = x_compute_stale_credentials_report__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_24'] = x_compute_stale_credentials_report__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_25'] = x_compute_stale_credentials_report__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_26'] = x_compute_stale_credentials_report__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_27'] = x_compute_stale_credentials_report__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_28'] = x_compute_stale_credentials_report__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_29'] = x_compute_stale_credentials_report__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_30'] = x_compute_stale_credentials_report__mutmut_30 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_31'] = x_compute_stale_credentials_report__mutmut_31 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_32'] = x_compute_stale_credentials_report__mutmut_32 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_33'] = x_compute_stale_credentials_report__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_34'] = x_compute_stale_credentials_report__mutmut_34 # type: ignore # mutmut generated
mutants_x_compute_stale_credentials_report__mutmut['x_compute_stale_credentials_report__mutmut_35'] = x_compute_stale_credentials_report__mutmut_35 # type: ignore # mutmut generated
