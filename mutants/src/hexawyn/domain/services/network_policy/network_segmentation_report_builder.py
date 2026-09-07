from __future__ import annotations

from hexawyn.domain.models.network_policy import (
    ExcludedNamespace,
    NamespaceNetworkFinding,
    NetworkSegmentationReport,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_report__mutmut)
def build_report(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_orig(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_1(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = None
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_2(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(None)
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_3(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(2 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_4(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status != "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_5(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "XXopenXX")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_6(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "OPEN")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_7(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = None
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_8(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        None
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_9(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        2 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_10(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status != "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_11(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "XXpartially_restrictedXX"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_12(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "PARTIALLY_RESTRICTED"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_13(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = None

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_14(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(None)

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_15(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(2 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_16(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status != "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_17(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "XXrestrictedXX")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_18(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "RESTRICTED")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_19(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=None,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_20(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=None,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_21(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=None,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_22(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=None,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_23(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=None,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_24(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=None,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_25(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=None,
    )


def x_build_report__mutmut_26(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_27(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_28(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_29(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_30(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_31(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_32(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        )


def x_build_report__mutmut_33(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(None, total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_34(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, None, excluded_namespaces),
    )


def x_build_report__mutmut_35(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, None),
    )


def x_build_report__mutmut_36(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(total_namespaces_checked, excluded_namespaces),
    )


def x_build_report__mutmut_37(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, excluded_namespaces),
    )


def x_build_report__mutmut_38(
    findings: list[NamespaceNetworkFinding],
    excluded_namespaces: list[ExcludedNamespace],
    total_namespaces_checked: int,
) -> NetworkSegmentationReport:
    fully_open_count = sum(1 for finding in findings if finding.network_status == "open")
    partially_restricted_count = sum(
        1 for finding in findings if finding.network_status == "partially_restricted"
    )
    restricted_count = sum(1 for finding in findings if finding.network_status == "restricted")

    return NetworkSegmentationReport(
        findings=findings,
        excluded_namespaces=excluded_namespaces,
        total_namespaces_checked=total_namespaces_checked,
        fully_open_count=fully_open_count,
        partially_restricted_count=partially_restricted_count,
        restricted_count=restricted_count,
        summary=_build_summary(fully_open_count, total_namespaces_checked, ),
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
mutants_x_build_report__mutmut['x_build_report__mutmut_27'] = x_build_report__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_28'] = x_build_report__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_29'] = x_build_report__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_30'] = x_build_report__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_31'] = x_build_report__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_32'] = x_build_report__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_33'] = x_build_report__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_34'] = x_build_report__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_35'] = x_build_report__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_36'] = x_build_report__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_37'] = x_build_report__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_report__mutmut['x_build_report__mutmut_38'] = x_build_report__mutmut_38 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_summary__mutmut)
def _build_summary(
    fully_open_count: int,
    total_namespaces_checked: int,
    excluded_namespaces: list[ExcludedNamespace],
) -> str:
    if not fully_open_count:
        summary = f"No namespaces fully open out of {total_namespaces_checked} checked."
    else:
        summary = (
            f"{fully_open_count} namespace(s) fully open to east-west traffic "
            f"out of {total_namespaces_checked} checked."
        )
    if excluded_namespaces:
        summary += f" {len(excluded_namespaces)} system namespace(s) shown separately."
    return summary


def x__build_summary__mutmut_orig(
    fully_open_count: int,
    total_namespaces_checked: int,
    excluded_namespaces: list[ExcludedNamespace],
) -> str:
    if not fully_open_count:
        summary = f"No namespaces fully open out of {total_namespaces_checked} checked."
    else:
        summary = (
            f"{fully_open_count} namespace(s) fully open to east-west traffic "
            f"out of {total_namespaces_checked} checked."
        )
    if excluded_namespaces:
        summary += f" {len(excluded_namespaces)} system namespace(s) shown separately."
    return summary


def x__build_summary__mutmut_1(
    fully_open_count: int,
    total_namespaces_checked: int,
    excluded_namespaces: list[ExcludedNamespace],
) -> str:
    if fully_open_count:
        summary = f"No namespaces fully open out of {total_namespaces_checked} checked."
    else:
        summary = (
            f"{fully_open_count} namespace(s) fully open to east-west traffic "
            f"out of {total_namespaces_checked} checked."
        )
    if excluded_namespaces:
        summary += f" {len(excluded_namespaces)} system namespace(s) shown separately."
    return summary


def x__build_summary__mutmut_2(
    fully_open_count: int,
    total_namespaces_checked: int,
    excluded_namespaces: list[ExcludedNamespace],
) -> str:
    if not fully_open_count:
        summary = None
    else:
        summary = (
            f"{fully_open_count} namespace(s) fully open to east-west traffic "
            f"out of {total_namespaces_checked} checked."
        )
    if excluded_namespaces:
        summary += f" {len(excluded_namespaces)} system namespace(s) shown separately."
    return summary


def x__build_summary__mutmut_3(
    fully_open_count: int,
    total_namespaces_checked: int,
    excluded_namespaces: list[ExcludedNamespace],
) -> str:
    if not fully_open_count:
        summary = f"No namespaces fully open out of {total_namespaces_checked} checked."
    else:
        summary = None
    if excluded_namespaces:
        summary += f" {len(excluded_namespaces)} system namespace(s) shown separately."
    return summary


def x__build_summary__mutmut_4(
    fully_open_count: int,
    total_namespaces_checked: int,
    excluded_namespaces: list[ExcludedNamespace],
) -> str:
    if not fully_open_count:
        summary = f"No namespaces fully open out of {total_namespaces_checked} checked."
    else:
        summary = (
            f"{fully_open_count} namespace(s) fully open to east-west traffic "
            f"out of {total_namespaces_checked} checked."
        )
    if excluded_namespaces:
        summary = f" {len(excluded_namespaces)} system namespace(s) shown separately."
    return summary


def x__build_summary__mutmut_5(
    fully_open_count: int,
    total_namespaces_checked: int,
    excluded_namespaces: list[ExcludedNamespace],
) -> str:
    if not fully_open_count:
        summary = f"No namespaces fully open out of {total_namespaces_checked} checked."
    else:
        summary = (
            f"{fully_open_count} namespace(s) fully open to east-west traffic "
            f"out of {total_namespaces_checked} checked."
        )
    if excluded_namespaces:
        summary -= f" {len(excluded_namespaces)} system namespace(s) shown separately."
    return summary

mutants_x__build_summary__mutmut['_mutmut_orig'] = x__build_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_1'] = x__build_summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_2'] = x__build_summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_3'] = x__build_summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_4'] = x__build_summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_5'] = x__build_summary__mutmut_5 # type: ignore # mutmut generated
