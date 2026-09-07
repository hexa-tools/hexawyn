"""Startup-scan business logic — interpreting the control-plane scan result."""

from __future__ import annotations

_ERROR_NARRATIVE_SKIP = [
    "not available",
    "unavailable",
    "install hexawyn",
    "is down",
    "no node",
    "no pods",
    "0 pods",
    "Runtime not available",
    "startup scan requires",
    "empty and inactive",
]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_is_error_narrative__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_error_narrative__mutmut)
def is_error_narrative(text: str) -> bool:
    """Return True when a narrative reads as an error/unavailable state."""
    text_lower = text.lower()
    return any(p.lower() in text_lower for p in _ERROR_NARRATIVE_SKIP)


def x_is_error_narrative__mutmut_orig(text: str) -> bool:
    """Return True when a narrative reads as an error/unavailable state."""
    text_lower = text.lower()
    return any(p.lower() in text_lower for p in _ERROR_NARRATIVE_SKIP)


def x_is_error_narrative__mutmut_1(text: str) -> bool:
    """Return True when a narrative reads as an error/unavailable state."""
    text_lower = None
    return any(p.lower() in text_lower for p in _ERROR_NARRATIVE_SKIP)


def x_is_error_narrative__mutmut_2(text: str) -> bool:
    """Return True when a narrative reads as an error/unavailable state."""
    text_lower = text.upper()
    return any(p.lower() in text_lower for p in _ERROR_NARRATIVE_SKIP)


def x_is_error_narrative__mutmut_3(text: str) -> bool:
    """Return True when a narrative reads as an error/unavailable state."""
    text_lower = text.lower()
    return any(None)


def x_is_error_narrative__mutmut_4(text: str) -> bool:
    """Return True when a narrative reads as an error/unavailable state."""
    text_lower = text.lower()
    return any(p.upper() in text_lower for p in _ERROR_NARRATIVE_SKIP)


def x_is_error_narrative__mutmut_5(text: str) -> bool:
    """Return True when a narrative reads as an error/unavailable state."""
    text_lower = text.lower()
    return any(p.lower() not in text_lower for p in _ERROR_NARRATIVE_SKIP)

mutants_x_is_error_narrative__mutmut['_mutmut_orig'] = x_is_error_narrative__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_error_narrative__mutmut['x_is_error_narrative__mutmut_1'] = x_is_error_narrative__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_error_narrative__mutmut['x_is_error_narrative__mutmut_2'] = x_is_error_narrative__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_error_narrative__mutmut['x_is_error_narrative__mutmut_3'] = x_is_error_narrative__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_error_narrative__mutmut['x_is_error_narrative__mutmut_4'] = x_is_error_narrative__mutmut_4 # type: ignore # mutmut generated
mutants_x_is_error_narrative__mutmut['x_is_error_narrative__mutmut_5'] = x_is_error_narrative__mutmut_5 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_valid_startup_result__mutmut)
def is_valid_startup_result(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_orig(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_1(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = None
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_2(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get(None, 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_3(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", None)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_4(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get(0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_5(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", )
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_6(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("XXhealth_scoreXX", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_7(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("HEALTH_SCORE", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_8(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 1)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_9(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = None
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_10(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(None)
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_11(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get(None, ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_12(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", None))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_13(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get(""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_14(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_15(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("XXnarrative_summaryXX", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_16(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("NARRATIVE_SUMMARY", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_17(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", "XXXX"))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_18(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = None

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_19(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get(None, {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_20(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", None)

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_21(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get({})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_22(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", )

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_23(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("XXcluster_summaryXX", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_24(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("CLUSTER_SUMMARY", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_25(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) and health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_26(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_27(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score < 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_28(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 1:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_29(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return True

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_30(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = None
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_31(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get(None, 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_32(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", None) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_33(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get(0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_34(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", ) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_35(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("XXtotal_podsXX", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_36(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("TOTAL_PODS", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_37(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 1) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_38(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 1
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_39(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods < 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_40(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 1:
        return False

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_41(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return True

    if is_error_narrative(narrative):
        return False

    return True


def x_is_valid_startup_result__mutmut_42(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(None):
        return False

    return True


def x_is_valid_startup_result__mutmut_43(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return True

    return True


def x_is_valid_startup_result__mutmut_44(result_dict: dict[str, object]) -> bool:
    """Return True when a startup-scan result represents a usable dashboard.

    A result is only treated as valid when it carries a positive health score,
    reports pods, and its narrative is not an error/unavailable state.
    """
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return False

mutants_x_is_valid_startup_result__mutmut['_mutmut_orig'] = x_is_valid_startup_result__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_1'] = x_is_valid_startup_result__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_2'] = x_is_valid_startup_result__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_3'] = x_is_valid_startup_result__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_4'] = x_is_valid_startup_result__mutmut_4 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_5'] = x_is_valid_startup_result__mutmut_5 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_6'] = x_is_valid_startup_result__mutmut_6 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_7'] = x_is_valid_startup_result__mutmut_7 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_8'] = x_is_valid_startup_result__mutmut_8 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_9'] = x_is_valid_startup_result__mutmut_9 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_10'] = x_is_valid_startup_result__mutmut_10 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_11'] = x_is_valid_startup_result__mutmut_11 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_12'] = x_is_valid_startup_result__mutmut_12 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_13'] = x_is_valid_startup_result__mutmut_13 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_14'] = x_is_valid_startup_result__mutmut_14 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_15'] = x_is_valid_startup_result__mutmut_15 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_16'] = x_is_valid_startup_result__mutmut_16 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_17'] = x_is_valid_startup_result__mutmut_17 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_18'] = x_is_valid_startup_result__mutmut_18 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_19'] = x_is_valid_startup_result__mutmut_19 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_20'] = x_is_valid_startup_result__mutmut_20 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_21'] = x_is_valid_startup_result__mutmut_21 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_22'] = x_is_valid_startup_result__mutmut_22 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_23'] = x_is_valid_startup_result__mutmut_23 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_24'] = x_is_valid_startup_result__mutmut_24 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_25'] = x_is_valid_startup_result__mutmut_25 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_26'] = x_is_valid_startup_result__mutmut_26 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_27'] = x_is_valid_startup_result__mutmut_27 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_28'] = x_is_valid_startup_result__mutmut_28 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_29'] = x_is_valid_startup_result__mutmut_29 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_30'] = x_is_valid_startup_result__mutmut_30 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_31'] = x_is_valid_startup_result__mutmut_31 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_32'] = x_is_valid_startup_result__mutmut_32 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_33'] = x_is_valid_startup_result__mutmut_33 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_34'] = x_is_valid_startup_result__mutmut_34 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_35'] = x_is_valid_startup_result__mutmut_35 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_36'] = x_is_valid_startup_result__mutmut_36 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_37'] = x_is_valid_startup_result__mutmut_37 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_38'] = x_is_valid_startup_result__mutmut_38 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_39'] = x_is_valid_startup_result__mutmut_39 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_40'] = x_is_valid_startup_result__mutmut_40 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_41'] = x_is_valid_startup_result__mutmut_41 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_42'] = x_is_valid_startup_result__mutmut_42 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_43'] = x_is_valid_startup_result__mutmut_43 # type: ignore # mutmut generated
mutants_x_is_valid_startup_result__mutmut['x_is_valid_startup_result__mutmut_44'] = x_is_valid_startup_result__mutmut_44 # type: ignore # mutmut generated
