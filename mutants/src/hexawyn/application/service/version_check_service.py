from __future__ import annotations

from hexawyn.application.ports.driven.version_check_port import VersionCheckPort
from hexawyn.domain.models.version_info import VersionCheckResult

_UP_TO_DATE = "up_to_date"
_UPDATE_AVAILABLE = "update_available"
_UNKNOWN = "unknown"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_check_for_update__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_check_for_update__mutmut)
def check_for_update(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_orig(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_1(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = None

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_2(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_3(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=None,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_4(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=None,
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_5(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=None,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_6(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error=None,
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_7(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_8(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_9(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_10(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_11(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="XXXX",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_12(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="XXcould not fetch latest versionXX",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_13(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="COULD NOT FETCH LATEST VERSION",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_14(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = None
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_15(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(None, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_16(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, None)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_17(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_18(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, )
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_19(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is not None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_20(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=None,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_21(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=None,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_22(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=None,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_23(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=None,
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_24(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_25(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_26(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_27(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_28(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison <= 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_29(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 1:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_30(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=None,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_31(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=None,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_32(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=None,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_33(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_34(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_35(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_36(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=None,
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_37(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=None,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_38(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        status=None,
    )


def x_check_for_update__mutmut_39(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        latest_version=latest,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_40(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        status=_UP_TO_DATE,
    )


def x_check_for_update__mutmut_41(current_version: str, port: VersionCheckPort) -> VersionCheckResult:
    latest = port.fetch_latest_version()

    if not latest:
        return VersionCheckResult(
            current_version=current_version,
            latest_version="",
            status=_UNKNOWN,
            error="could not fetch latest version",
        )

    comparison = _compare_versions(current_version, latest)
    if comparison is None:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UNKNOWN,
            error=f"invalid version: {latest}",
        )

    if comparison < 0:
        return VersionCheckResult(
            current_version=current_version,
            latest_version=latest,
            status=_UPDATE_AVAILABLE,
        )

    return VersionCheckResult(
        current_version=current_version,
        latest_version=latest,
        )

mutants_x_check_for_update__mutmut['_mutmut_orig'] = x_check_for_update__mutmut_orig # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_1'] = x_check_for_update__mutmut_1 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_2'] = x_check_for_update__mutmut_2 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_3'] = x_check_for_update__mutmut_3 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_4'] = x_check_for_update__mutmut_4 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_5'] = x_check_for_update__mutmut_5 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_6'] = x_check_for_update__mutmut_6 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_7'] = x_check_for_update__mutmut_7 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_8'] = x_check_for_update__mutmut_8 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_9'] = x_check_for_update__mutmut_9 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_10'] = x_check_for_update__mutmut_10 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_11'] = x_check_for_update__mutmut_11 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_12'] = x_check_for_update__mutmut_12 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_13'] = x_check_for_update__mutmut_13 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_14'] = x_check_for_update__mutmut_14 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_15'] = x_check_for_update__mutmut_15 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_16'] = x_check_for_update__mutmut_16 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_17'] = x_check_for_update__mutmut_17 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_18'] = x_check_for_update__mutmut_18 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_19'] = x_check_for_update__mutmut_19 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_20'] = x_check_for_update__mutmut_20 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_21'] = x_check_for_update__mutmut_21 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_22'] = x_check_for_update__mutmut_22 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_23'] = x_check_for_update__mutmut_23 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_24'] = x_check_for_update__mutmut_24 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_25'] = x_check_for_update__mutmut_25 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_26'] = x_check_for_update__mutmut_26 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_27'] = x_check_for_update__mutmut_27 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_28'] = x_check_for_update__mutmut_28 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_29'] = x_check_for_update__mutmut_29 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_30'] = x_check_for_update__mutmut_30 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_31'] = x_check_for_update__mutmut_31 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_32'] = x_check_for_update__mutmut_32 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_33'] = x_check_for_update__mutmut_33 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_34'] = x_check_for_update__mutmut_34 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_35'] = x_check_for_update__mutmut_35 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_36'] = x_check_for_update__mutmut_36 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_37'] = x_check_for_update__mutmut_37 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_38'] = x_check_for_update__mutmut_38 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_39'] = x_check_for_update__mutmut_39 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_40'] = x_check_for_update__mutmut_40 # type: ignore # mutmut generated
mutants_x_check_for_update__mutmut['x_check_for_update__mutmut_41'] = x_check_for_update__mutmut_41 # type: ignore # mutmut generated
mutants_x__compare_versions__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compare_versions__mutmut)
def _compare_versions(current: str, latest: str) -> int | None:
    """Return -1 when latest is newer, 0 when equal, 1 when current is newer.

    Returns None when either version cannot be parsed.
    """
    current_parts = _parse_version(current)
    latest_parts = _parse_version(latest)

    if current_parts is None or latest_parts is None:
        return None

    if current_parts == latest_parts:
        return 0
    return -1 if _is_newer(latest_parts, current_parts) else 1


def x__compare_versions__mutmut_orig(current: str, latest: str) -> int | None:
    """Return -1 when latest is newer, 0 when equal, 1 when current is newer.

    Returns None when either version cannot be parsed.
    """
    current_parts = _parse_version(current)
    latest_parts = _parse_version(latest)

    if current_parts is None or latest_parts is None:
        return None

    if current_parts == latest_parts:
        return 0
    return -1 if _is_newer(latest_parts, current_parts) else 1


def x__compare_versions__mutmut_1(current: str, latest: str) -> int | None:
    """Return -1 when latest is newer, 0 when equal, 1 when current is newer.

    Returns None when either version cannot be parsed.
    """
    current_parts = None
    latest_parts = _parse_version(latest)

    if current_parts is None or latest_parts is None:
        return None

    if current_parts == latest_parts:
        return 0
    return -1 if _is_newer(latest_parts, current_parts) else 1


def x__compare_versions__mutmut_2(current: str, latest: str) -> int | None:
    """Return -1 when latest is newer, 0 when equal, 1 when current is newer.

    Returns None when either version cannot be parsed.
    """
    current_parts = _parse_version(None)
    latest_parts = _parse_version(latest)

    if current_parts is None or latest_parts is None:
        return None

    if current_parts == latest_parts:
        return 0
    return -1 if _is_newer(latest_parts, current_parts) else 1


def x__compare_versions__mutmut_3(current: str, latest: str) -> int | None:
    """Return -1 when latest is newer, 0 when equal, 1 when current is newer.

    Returns None when either version cannot be parsed.
    """
    current_parts = _parse_version(current)
    latest_parts = None

    if current_parts is None or latest_parts is None:
        return None

    if current_parts == latest_parts:
        return 0
    return -1 if _is_newer(latest_parts, current_parts) else 1


def x__compare_versions__mutmut_4(current: str, latest: str) -> int | None:
    """Return -1 when latest is newer, 0 when equal, 1 when current is newer.

    Returns None when either version cannot be parsed.
    """
    current_parts = _parse_version(current)
    latest_parts = _parse_version(None)

    if current_parts is None or latest_parts is None:
        return None

    if current_parts == latest_parts:
        return 0
    return -1 if _is_newer(latest_parts, current_parts) else 1


def x__compare_versions__mutmut_5(current: str, latest: str) -> int | None:
    """Return -1 when latest is newer, 0 when equal, 1 when current is newer.

    Returns None when either version cannot be parsed.
    """
    current_parts = _parse_version(current)
    latest_parts = _parse_version(latest)

    if current_parts is None and latest_parts is None:
        return None

    if current_parts == latest_parts:
        return 0
    return -1 if _is_newer(latest_parts, current_parts) else 1


def x__compare_versions__mutmut_6(current: str, latest: str) -> int | None:
    """Return -1 when latest is newer, 0 when equal, 1 when current is newer.

    Returns None when either version cannot be parsed.
    """
    current_parts = _parse_version(current)
    latest_parts = _parse_version(latest)

    if current_parts is not None or latest_parts is None:
        return None

    if current_parts == latest_parts:
        return 0
    return -1 if _is_newer(latest_parts, current_parts) else 1


def x__compare_versions__mutmut_7(current: str, latest: str) -> int | None:
    """Return -1 when latest is newer, 0 when equal, 1 when current is newer.

    Returns None when either version cannot be parsed.
    """
    current_parts = _parse_version(current)
    latest_parts = _parse_version(latest)

    if current_parts is None or latest_parts is not None:
        return None

    if current_parts == latest_parts:
        return 0
    return -1 if _is_newer(latest_parts, current_parts) else 1


def x__compare_versions__mutmut_8(current: str, latest: str) -> int | None:
    """Return -1 when latest is newer, 0 when equal, 1 when current is newer.

    Returns None when either version cannot be parsed.
    """
    current_parts = _parse_version(current)
    latest_parts = _parse_version(latest)

    if current_parts is None or latest_parts is None:
        return None

    if current_parts != latest_parts:
        return 0
    return -1 if _is_newer(latest_parts, current_parts) else 1


def x__compare_versions__mutmut_9(current: str, latest: str) -> int | None:
    """Return -1 when latest is newer, 0 when equal, 1 when current is newer.

    Returns None when either version cannot be parsed.
    """
    current_parts = _parse_version(current)
    latest_parts = _parse_version(latest)

    if current_parts is None or latest_parts is None:
        return None

    if current_parts == latest_parts:
        return 1
    return -1 if _is_newer(latest_parts, current_parts) else 1


def x__compare_versions__mutmut_10(current: str, latest: str) -> int | None:
    """Return -1 when latest is newer, 0 when equal, 1 when current is newer.

    Returns None when either version cannot be parsed.
    """
    current_parts = _parse_version(current)
    latest_parts = _parse_version(latest)

    if current_parts is None or latest_parts is None:
        return None

    if current_parts == latest_parts:
        return 0
    return +1 if _is_newer(latest_parts, current_parts) else 1


def x__compare_versions__mutmut_11(current: str, latest: str) -> int | None:
    """Return -1 when latest is newer, 0 when equal, 1 when current is newer.

    Returns None when either version cannot be parsed.
    """
    current_parts = _parse_version(current)
    latest_parts = _parse_version(latest)

    if current_parts is None or latest_parts is None:
        return None

    if current_parts == latest_parts:
        return 0
    return -2 if _is_newer(latest_parts, current_parts) else 1


def x__compare_versions__mutmut_12(current: str, latest: str) -> int | None:
    """Return -1 when latest is newer, 0 when equal, 1 when current is newer.

    Returns None when either version cannot be parsed.
    """
    current_parts = _parse_version(current)
    latest_parts = _parse_version(latest)

    if current_parts is None or latest_parts is None:
        return None

    if current_parts == latest_parts:
        return 0
    return -1 if _is_newer(None, current_parts) else 1


def x__compare_versions__mutmut_13(current: str, latest: str) -> int | None:
    """Return -1 when latest is newer, 0 when equal, 1 when current is newer.

    Returns None when either version cannot be parsed.
    """
    current_parts = _parse_version(current)
    latest_parts = _parse_version(latest)

    if current_parts is None or latest_parts is None:
        return None

    if current_parts == latest_parts:
        return 0
    return -1 if _is_newer(latest_parts, None) else 1


def x__compare_versions__mutmut_14(current: str, latest: str) -> int | None:
    """Return -1 when latest is newer, 0 when equal, 1 when current is newer.

    Returns None when either version cannot be parsed.
    """
    current_parts = _parse_version(current)
    latest_parts = _parse_version(latest)

    if current_parts is None or latest_parts is None:
        return None

    if current_parts == latest_parts:
        return 0
    return -1 if _is_newer(current_parts) else 1


def x__compare_versions__mutmut_15(current: str, latest: str) -> int | None:
    """Return -1 when latest is newer, 0 when equal, 1 when current is newer.

    Returns None when either version cannot be parsed.
    """
    current_parts = _parse_version(current)
    latest_parts = _parse_version(latest)

    if current_parts is None or latest_parts is None:
        return None

    if current_parts == latest_parts:
        return 0
    return -1 if _is_newer(latest_parts, ) else 1


def x__compare_versions__mutmut_16(current: str, latest: str) -> int | None:
    """Return -1 when latest is newer, 0 when equal, 1 when current is newer.

    Returns None when either version cannot be parsed.
    """
    current_parts = _parse_version(current)
    latest_parts = _parse_version(latest)

    if current_parts is None or latest_parts is None:
        return None

    if current_parts == latest_parts:
        return 0
    return -1 if _is_newer(latest_parts, current_parts) else 2

mutants_x__compare_versions__mutmut['_mutmut_orig'] = x__compare_versions__mutmut_orig # type: ignore # mutmut generated
mutants_x__compare_versions__mutmut['x__compare_versions__mutmut_1'] = x__compare_versions__mutmut_1 # type: ignore # mutmut generated
mutants_x__compare_versions__mutmut['x__compare_versions__mutmut_2'] = x__compare_versions__mutmut_2 # type: ignore # mutmut generated
mutants_x__compare_versions__mutmut['x__compare_versions__mutmut_3'] = x__compare_versions__mutmut_3 # type: ignore # mutmut generated
mutants_x__compare_versions__mutmut['x__compare_versions__mutmut_4'] = x__compare_versions__mutmut_4 # type: ignore # mutmut generated
mutants_x__compare_versions__mutmut['x__compare_versions__mutmut_5'] = x__compare_versions__mutmut_5 # type: ignore # mutmut generated
mutants_x__compare_versions__mutmut['x__compare_versions__mutmut_6'] = x__compare_versions__mutmut_6 # type: ignore # mutmut generated
mutants_x__compare_versions__mutmut['x__compare_versions__mutmut_7'] = x__compare_versions__mutmut_7 # type: ignore # mutmut generated
mutants_x__compare_versions__mutmut['x__compare_versions__mutmut_8'] = x__compare_versions__mutmut_8 # type: ignore # mutmut generated
mutants_x__compare_versions__mutmut['x__compare_versions__mutmut_9'] = x__compare_versions__mutmut_9 # type: ignore # mutmut generated
mutants_x__compare_versions__mutmut['x__compare_versions__mutmut_10'] = x__compare_versions__mutmut_10 # type: ignore # mutmut generated
mutants_x__compare_versions__mutmut['x__compare_versions__mutmut_11'] = x__compare_versions__mutmut_11 # type: ignore # mutmut generated
mutants_x__compare_versions__mutmut['x__compare_versions__mutmut_12'] = x__compare_versions__mutmut_12 # type: ignore # mutmut generated
mutants_x__compare_versions__mutmut['x__compare_versions__mutmut_13'] = x__compare_versions__mutmut_13 # type: ignore # mutmut generated
mutants_x__compare_versions__mutmut['x__compare_versions__mutmut_14'] = x__compare_versions__mutmut_14 # type: ignore # mutmut generated
mutants_x__compare_versions__mutmut['x__compare_versions__mutmut_15'] = x__compare_versions__mutmut_15 # type: ignore # mutmut generated
mutants_x__compare_versions__mutmut['x__compare_versions__mutmut_16'] = x__compare_versions__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_version__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_version__mutmut)
def _parse_version(version: str) -> tuple[int, int, int, int | None] | None:
    import re

    match = re.match(r"(\d+)\.(\d+)\.(\d+)(?:b(\d+))?", version)
    if not match:
        return None
    major, minor, patch = (int(part) for part in match.groups()[:3])
    beta = int(match.group(4)) if match.group(4) else None
    return (major, minor, patch, beta)


def x__parse_version__mutmut_orig(version: str) -> tuple[int, int, int, int | None] | None:
    import re

    match = re.match(r"(\d+)\.(\d+)\.(\d+)(?:b(\d+))?", version)
    if not match:
        return None
    major, minor, patch = (int(part) for part in match.groups()[:3])
    beta = int(match.group(4)) if match.group(4) else None
    return (major, minor, patch, beta)


def x__parse_version__mutmut_1(version: str) -> tuple[int, int, int, int | None] | None:
    import re

    match = None
    if not match:
        return None
    major, minor, patch = (int(part) for part in match.groups()[:3])
    beta = int(match.group(4)) if match.group(4) else None
    return (major, minor, patch, beta)


def x__parse_version__mutmut_2(version: str) -> tuple[int, int, int, int | None] | None:
    import re

    match = re.match(None, version)
    if not match:
        return None
    major, minor, patch = (int(part) for part in match.groups()[:3])
    beta = int(match.group(4)) if match.group(4) else None
    return (major, minor, patch, beta)


def x__parse_version__mutmut_3(version: str) -> tuple[int, int, int, int | None] | None:
    import re

    match = re.match(r"(\d+)\.(\d+)\.(\d+)(?:b(\d+))?", None)
    if not match:
        return None
    major, minor, patch = (int(part) for part in match.groups()[:3])
    beta = int(match.group(4)) if match.group(4) else None
    return (major, minor, patch, beta)


def x__parse_version__mutmut_4(version: str) -> tuple[int, int, int, int | None] | None:
    import re

    match = re.match(version)
    if not match:
        return None
    major, minor, patch = (int(part) for part in match.groups()[:3])
    beta = int(match.group(4)) if match.group(4) else None
    return (major, minor, patch, beta)


def x__parse_version__mutmut_5(version: str) -> tuple[int, int, int, int | None] | None:
    import re

    match = re.match(r"(\d+)\.(\d+)\.(\d+)(?:b(\d+))?", )
    if not match:
        return None
    major, minor, patch = (int(part) for part in match.groups()[:3])
    beta = int(match.group(4)) if match.group(4) else None
    return (major, minor, patch, beta)


def x__parse_version__mutmut_6(version: str) -> tuple[int, int, int, int | None] | None:
    import re

    match = re.match(r"XX(\d+)\.(\d+)\.(\d+)(?:b(\d+))?XX", version)
    if not match:
        return None
    major, minor, patch = (int(part) for part in match.groups()[:3])
    beta = int(match.group(4)) if match.group(4) else None
    return (major, minor, patch, beta)


def x__parse_version__mutmut_7(version: str) -> tuple[int, int, int, int | None] | None:
    import re

    match = re.match(r"(\d+)\.(\d+)\.(\d+)(?:B(\d+))?", version)
    if not match:
        return None
    major, minor, patch = (int(part) for part in match.groups()[:3])
    beta = int(match.group(4)) if match.group(4) else None
    return (major, minor, patch, beta)


def x__parse_version__mutmut_8(version: str) -> tuple[int, int, int, int | None] | None:
    import re

    match = re.match(r"(\d+)\.(\d+)\.(\d+)(?:b(\d+))?", version)
    if match:
        return None
    major, minor, patch = (int(part) for part in match.groups()[:3])
    beta = int(match.group(4)) if match.group(4) else None
    return (major, minor, patch, beta)


def x__parse_version__mutmut_9(version: str) -> tuple[int, int, int, int | None] | None:
    import re

    match = re.match(r"(\d+)\.(\d+)\.(\d+)(?:b(\d+))?", version)
    if not match:
        return None
    major, minor, patch = None
    beta = int(match.group(4)) if match.group(4) else None
    return (major, minor, patch, beta)


def x__parse_version__mutmut_10(version: str) -> tuple[int, int, int, int | None] | None:
    import re

    match = re.match(r"(\d+)\.(\d+)\.(\d+)(?:b(\d+))?", version)
    if not match:
        return None
    major, minor, patch = (int(None) for part in match.groups()[:3])
    beta = int(match.group(4)) if match.group(4) else None
    return (major, minor, patch, beta)


def x__parse_version__mutmut_11(version: str) -> tuple[int, int, int, int | None] | None:
    import re

    match = re.match(r"(\d+)\.(\d+)\.(\d+)(?:b(\d+))?", version)
    if not match:
        return None
    major, minor, patch = (int(part) for part in match.groups()[:4])
    beta = int(match.group(4)) if match.group(4) else None
    return (major, minor, patch, beta)


def x__parse_version__mutmut_12(version: str) -> tuple[int, int, int, int | None] | None:
    import re

    match = re.match(r"(\d+)\.(\d+)\.(\d+)(?:b(\d+))?", version)
    if not match:
        return None
    major, minor, patch = (int(part) for part in match.groups()[:3])
    beta = None
    return (major, minor, patch, beta)


def x__parse_version__mutmut_13(version: str) -> tuple[int, int, int, int | None] | None:
    import re

    match = re.match(r"(\d+)\.(\d+)\.(\d+)(?:b(\d+))?", version)
    if not match:
        return None
    major, minor, patch = (int(part) for part in match.groups()[:3])
    beta = int(None) if match.group(4) else None
    return (major, minor, patch, beta)


def x__parse_version__mutmut_14(version: str) -> tuple[int, int, int, int | None] | None:
    import re

    match = re.match(r"(\d+)\.(\d+)\.(\d+)(?:b(\d+))?", version)
    if not match:
        return None
    major, minor, patch = (int(part) for part in match.groups()[:3])
    beta = int(match.group(None)) if match.group(4) else None
    return (major, minor, patch, beta)


def x__parse_version__mutmut_15(version: str) -> tuple[int, int, int, int | None] | None:
    import re

    match = re.match(r"(\d+)\.(\d+)\.(\d+)(?:b(\d+))?", version)
    if not match:
        return None
    major, minor, patch = (int(part) for part in match.groups()[:3])
    beta = int(match.group(5)) if match.group(4) else None
    return (major, minor, patch, beta)


def x__parse_version__mutmut_16(version: str) -> tuple[int, int, int, int | None] | None:
    import re

    match = re.match(r"(\d+)\.(\d+)\.(\d+)(?:b(\d+))?", version)
    if not match:
        return None
    major, minor, patch = (int(part) for part in match.groups()[:3])
    beta = int(match.group(4)) if match.group(None) else None
    return (major, minor, patch, beta)


def x__parse_version__mutmut_17(version: str) -> tuple[int, int, int, int | None] | None:
    import re

    match = re.match(r"(\d+)\.(\d+)\.(\d+)(?:b(\d+))?", version)
    if not match:
        return None
    major, minor, patch = (int(part) for part in match.groups()[:3])
    beta = int(match.group(4)) if match.group(5) else None
    return (major, minor, patch, beta)

mutants_x__parse_version__mutmut['_mutmut_orig'] = x__parse_version__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_version__mutmut['x__parse_version__mutmut_1'] = x__parse_version__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_version__mutmut['x__parse_version__mutmut_2'] = x__parse_version__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_version__mutmut['x__parse_version__mutmut_3'] = x__parse_version__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_version__mutmut['x__parse_version__mutmut_4'] = x__parse_version__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_version__mutmut['x__parse_version__mutmut_5'] = x__parse_version__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_version__mutmut['x__parse_version__mutmut_6'] = x__parse_version__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_version__mutmut['x__parse_version__mutmut_7'] = x__parse_version__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_version__mutmut['x__parse_version__mutmut_8'] = x__parse_version__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_version__mutmut['x__parse_version__mutmut_9'] = x__parse_version__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_version__mutmut['x__parse_version__mutmut_10'] = x__parse_version__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_version__mutmut['x__parse_version__mutmut_11'] = x__parse_version__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_version__mutmut['x__parse_version__mutmut_12'] = x__parse_version__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_version__mutmut['x__parse_version__mutmut_13'] = x__parse_version__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_version__mutmut['x__parse_version__mutmut_14'] = x__parse_version__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_version__mutmut['x__parse_version__mutmut_15'] = x__parse_version__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_version__mutmut['x__parse_version__mutmut_16'] = x__parse_version__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_version__mutmut['x__parse_version__mutmut_17'] = x__parse_version__mutmut_17 # type: ignore # mutmut generated
mutants_x__is_newer__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__is_newer__mutmut)
def _is_newer(
    candidate: tuple[int, int, int, int | None],
    baseline: tuple[int, int, int, int | None],
) -> bool:
    for candidate_part, baseline_part in zip(candidate, baseline):
        if candidate_part == baseline_part:
            continue
        if candidate_part is None:
            return True
        if baseline_part is None:
            return False
        return candidate_part > baseline_part
    return False


def x__is_newer__mutmut_orig(
    candidate: tuple[int, int, int, int | None],
    baseline: tuple[int, int, int, int | None],
) -> bool:
    for candidate_part, baseline_part in zip(candidate, baseline):
        if candidate_part == baseline_part:
            continue
        if candidate_part is None:
            return True
        if baseline_part is None:
            return False
        return candidate_part > baseline_part
    return False


def x__is_newer__mutmut_1(
    candidate: tuple[int, int, int, int | None],
    baseline: tuple[int, int, int, int | None],
) -> bool:
    for candidate_part, baseline_part in zip(None, baseline):
        if candidate_part == baseline_part:
            continue
        if candidate_part is None:
            return True
        if baseline_part is None:
            return False
        return candidate_part > baseline_part
    return False


def x__is_newer__mutmut_2(
    candidate: tuple[int, int, int, int | None],
    baseline: tuple[int, int, int, int | None],
) -> bool:
    for candidate_part, baseline_part in zip(candidate, None):
        if candidate_part == baseline_part:
            continue
        if candidate_part is None:
            return True
        if baseline_part is None:
            return False
        return candidate_part > baseline_part
    return False


def x__is_newer__mutmut_3(
    candidate: tuple[int, int, int, int | None],
    baseline: tuple[int, int, int, int | None],
) -> bool:
    for candidate_part, baseline_part in zip(baseline):
        if candidate_part == baseline_part:
            continue
        if candidate_part is None:
            return True
        if baseline_part is None:
            return False
        return candidate_part > baseline_part
    return False


def x__is_newer__mutmut_4(
    candidate: tuple[int, int, int, int | None],
    baseline: tuple[int, int, int, int | None],
) -> bool:
    for candidate_part, baseline_part in zip(candidate, ):
        if candidate_part == baseline_part:
            continue
        if candidate_part is None:
            return True
        if baseline_part is None:
            return False
        return candidate_part > baseline_part
    return False


def x__is_newer__mutmut_5(
    candidate: tuple[int, int, int, int | None],
    baseline: tuple[int, int, int, int | None],
) -> bool:
    for candidate_part, baseline_part in zip(candidate, baseline):
        if candidate_part != baseline_part:
            continue
        if candidate_part is None:
            return True
        if baseline_part is None:
            return False
        return candidate_part > baseline_part
    return False


def x__is_newer__mutmut_6(
    candidate: tuple[int, int, int, int | None],
    baseline: tuple[int, int, int, int | None],
) -> bool:
    for candidate_part, baseline_part in zip(candidate, baseline):
        if candidate_part == baseline_part:
            break
        if candidate_part is None:
            return True
        if baseline_part is None:
            return False
        return candidate_part > baseline_part
    return False


def x__is_newer__mutmut_7(
    candidate: tuple[int, int, int, int | None],
    baseline: tuple[int, int, int, int | None],
) -> bool:
    for candidate_part, baseline_part in zip(candidate, baseline):
        if candidate_part == baseline_part:
            continue
        if candidate_part is not None:
            return True
        if baseline_part is None:
            return False
        return candidate_part > baseline_part
    return False


def x__is_newer__mutmut_8(
    candidate: tuple[int, int, int, int | None],
    baseline: tuple[int, int, int, int | None],
) -> bool:
    for candidate_part, baseline_part in zip(candidate, baseline):
        if candidate_part == baseline_part:
            continue
        if candidate_part is None:
            return False
        if baseline_part is None:
            return False
        return candidate_part > baseline_part
    return False


def x__is_newer__mutmut_9(
    candidate: tuple[int, int, int, int | None],
    baseline: tuple[int, int, int, int | None],
) -> bool:
    for candidate_part, baseline_part in zip(candidate, baseline):
        if candidate_part == baseline_part:
            continue
        if candidate_part is None:
            return True
        if baseline_part is not None:
            return False
        return candidate_part > baseline_part
    return False


def x__is_newer__mutmut_10(
    candidate: tuple[int, int, int, int | None],
    baseline: tuple[int, int, int, int | None],
) -> bool:
    for candidate_part, baseline_part in zip(candidate, baseline):
        if candidate_part == baseline_part:
            continue
        if candidate_part is None:
            return True
        if baseline_part is None:
            return True
        return candidate_part > baseline_part
    return False


def x__is_newer__mutmut_11(
    candidate: tuple[int, int, int, int | None],
    baseline: tuple[int, int, int, int | None],
) -> bool:
    for candidate_part, baseline_part in zip(candidate, baseline):
        if candidate_part == baseline_part:
            continue
        if candidate_part is None:
            return True
        if baseline_part is None:
            return False
        return candidate_part >= baseline_part
    return False


def x__is_newer__mutmut_12(
    candidate: tuple[int, int, int, int | None],
    baseline: tuple[int, int, int, int | None],
) -> bool:
    for candidate_part, baseline_part in zip(candidate, baseline):
        if candidate_part == baseline_part:
            continue
        if candidate_part is None:
            return True
        if baseline_part is None:
            return False
        return candidate_part > baseline_part
    return True

mutants_x__is_newer__mutmut['_mutmut_orig'] = x__is_newer__mutmut_orig # type: ignore # mutmut generated
mutants_x__is_newer__mutmut['x__is_newer__mutmut_1'] = x__is_newer__mutmut_1 # type: ignore # mutmut generated
mutants_x__is_newer__mutmut['x__is_newer__mutmut_2'] = x__is_newer__mutmut_2 # type: ignore # mutmut generated
mutants_x__is_newer__mutmut['x__is_newer__mutmut_3'] = x__is_newer__mutmut_3 # type: ignore # mutmut generated
mutants_x__is_newer__mutmut['x__is_newer__mutmut_4'] = x__is_newer__mutmut_4 # type: ignore # mutmut generated
mutants_x__is_newer__mutmut['x__is_newer__mutmut_5'] = x__is_newer__mutmut_5 # type: ignore # mutmut generated
mutants_x__is_newer__mutmut['x__is_newer__mutmut_6'] = x__is_newer__mutmut_6 # type: ignore # mutmut generated
mutants_x__is_newer__mutmut['x__is_newer__mutmut_7'] = x__is_newer__mutmut_7 # type: ignore # mutmut generated
mutants_x__is_newer__mutmut['x__is_newer__mutmut_8'] = x__is_newer__mutmut_8 # type: ignore # mutmut generated
mutants_x__is_newer__mutmut['x__is_newer__mutmut_9'] = x__is_newer__mutmut_9 # type: ignore # mutmut generated
mutants_x__is_newer__mutmut['x__is_newer__mutmut_10'] = x__is_newer__mutmut_10 # type: ignore # mutmut generated
mutants_x__is_newer__mutmut['x__is_newer__mutmut_11'] = x__is_newer__mutmut_11 # type: ignore # mutmut generated
mutants_x__is_newer__mutmut['x__is_newer__mutmut_12'] = x__is_newer__mutmut_12 # type: ignore # mutmut generated
