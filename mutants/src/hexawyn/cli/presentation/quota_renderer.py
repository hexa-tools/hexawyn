from hexawyn.domain.models.quota import QuotaState

QUOTA_STATE_ICONS: dict[QuotaState, str] = {
    QuotaState.NORMAL: "",
    QuotaState.WARNING: "\u26a0\ufe0f ",
    QuotaState.CRITICAL: "\U0001f534 ",
    QuotaState.EXHAUSTED: "\u274c ",
    QuotaState.UNLIMITED: "",
    QuotaState.LOCKED: "\U0001f512 ",
}

QUOTA_RESOURCE_LABELS: dict[str, str] = {
    "investigations": "Investigations",
    "slack_alerts": "Slack alerts",
}

UPGRADE_URL = "https://hexawyn.com/pricing"

FILL_CHAR = chr(9608)
EMPTY_CHAR = chr(9617)
BAR_WIDTH = 20


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_bar_fill__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_bar_fill__mutmut)
def compute_bar_fill(used: int, limit: int, width: int = BAR_WIDTH) -> tuple[int, float]:
    pct = min(100.0, (used / limit) * 100) if limit > 0 else 0.0
    filled = int((pct / 100.0) * width)
    return filled, pct


def x_compute_bar_fill__mutmut_orig(used: int, limit: int, width: int = BAR_WIDTH) -> tuple[int, float]:
    pct = min(100.0, (used / limit) * 100) if limit > 0 else 0.0
    filled = int((pct / 100.0) * width)
    return filled, pct


def x_compute_bar_fill__mutmut_1(used: int, limit: int, width: int = BAR_WIDTH) -> tuple[int, float]:
    pct = None
    filled = int((pct / 100.0) * width)
    return filled, pct


def x_compute_bar_fill__mutmut_2(used: int, limit: int, width: int = BAR_WIDTH) -> tuple[int, float]:
    pct = min(None, (used / limit) * 100) if limit > 0 else 0.0
    filled = int((pct / 100.0) * width)
    return filled, pct


def x_compute_bar_fill__mutmut_3(used: int, limit: int, width: int = BAR_WIDTH) -> tuple[int, float]:
    pct = min(100.0, None) if limit > 0 else 0.0
    filled = int((pct / 100.0) * width)
    return filled, pct


def x_compute_bar_fill__mutmut_4(used: int, limit: int, width: int = BAR_WIDTH) -> tuple[int, float]:
    pct = min((used / limit) * 100) if limit > 0 else 0.0
    filled = int((pct / 100.0) * width)
    return filled, pct


def x_compute_bar_fill__mutmut_5(used: int, limit: int, width: int = BAR_WIDTH) -> tuple[int, float]:
    pct = min(100.0, ) if limit > 0 else 0.0
    filled = int((pct / 100.0) * width)
    return filled, pct


def x_compute_bar_fill__mutmut_6(used: int, limit: int, width: int = BAR_WIDTH) -> tuple[int, float]:
    pct = min(101.0, (used / limit) * 100) if limit > 0 else 0.0
    filled = int((pct / 100.0) * width)
    return filled, pct


def x_compute_bar_fill__mutmut_7(used: int, limit: int, width: int = BAR_WIDTH) -> tuple[int, float]:
    pct = min(100.0, (used / limit) / 100) if limit > 0 else 0.0
    filled = int((pct / 100.0) * width)
    return filled, pct


def x_compute_bar_fill__mutmut_8(used: int, limit: int, width: int = BAR_WIDTH) -> tuple[int, float]:
    pct = min(100.0, (used * limit) * 100) if limit > 0 else 0.0
    filled = int((pct / 100.0) * width)
    return filled, pct


def x_compute_bar_fill__mutmut_9(used: int, limit: int, width: int = BAR_WIDTH) -> tuple[int, float]:
    pct = min(100.0, (used / limit) * 101) if limit > 0 else 0.0
    filled = int((pct / 100.0) * width)
    return filled, pct


def x_compute_bar_fill__mutmut_10(used: int, limit: int, width: int = BAR_WIDTH) -> tuple[int, float]:
    pct = min(100.0, (used / limit) * 100) if limit >= 0 else 0.0
    filled = int((pct / 100.0) * width)
    return filled, pct


def x_compute_bar_fill__mutmut_11(used: int, limit: int, width: int = BAR_WIDTH) -> tuple[int, float]:
    pct = min(100.0, (used / limit) * 100) if limit > 1 else 0.0
    filled = int((pct / 100.0) * width)
    return filled, pct


def x_compute_bar_fill__mutmut_12(used: int, limit: int, width: int = BAR_WIDTH) -> tuple[int, float]:
    pct = min(100.0, (used / limit) * 100) if limit > 0 else 1.0
    filled = int((pct / 100.0) * width)
    return filled, pct


def x_compute_bar_fill__mutmut_13(used: int, limit: int, width: int = BAR_WIDTH) -> tuple[int, float]:
    pct = min(100.0, (used / limit) * 100) if limit > 0 else 0.0
    filled = None
    return filled, pct


def x_compute_bar_fill__mutmut_14(used: int, limit: int, width: int = BAR_WIDTH) -> tuple[int, float]:
    pct = min(100.0, (used / limit) * 100) if limit > 0 else 0.0
    filled = int(None)
    return filled, pct


def x_compute_bar_fill__mutmut_15(used: int, limit: int, width: int = BAR_WIDTH) -> tuple[int, float]:
    pct = min(100.0, (used / limit) * 100) if limit > 0 else 0.0
    filled = int((pct / 100.0) / width)
    return filled, pct


def x_compute_bar_fill__mutmut_16(used: int, limit: int, width: int = BAR_WIDTH) -> tuple[int, float]:
    pct = min(100.0, (used / limit) * 100) if limit > 0 else 0.0
    filled = int((pct * 100.0) * width)
    return filled, pct


def x_compute_bar_fill__mutmut_17(used: int, limit: int, width: int = BAR_WIDTH) -> tuple[int, float]:
    pct = min(100.0, (used / limit) * 100) if limit > 0 else 0.0
    filled = int((pct / 101.0) * width)
    return filled, pct

mutants_x_compute_bar_fill__mutmut['_mutmut_orig'] = x_compute_bar_fill__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_bar_fill__mutmut['x_compute_bar_fill__mutmut_1'] = x_compute_bar_fill__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_bar_fill__mutmut['x_compute_bar_fill__mutmut_2'] = x_compute_bar_fill__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_bar_fill__mutmut['x_compute_bar_fill__mutmut_3'] = x_compute_bar_fill__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_bar_fill__mutmut['x_compute_bar_fill__mutmut_4'] = x_compute_bar_fill__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_bar_fill__mutmut['x_compute_bar_fill__mutmut_5'] = x_compute_bar_fill__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_bar_fill__mutmut['x_compute_bar_fill__mutmut_6'] = x_compute_bar_fill__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_bar_fill__mutmut['x_compute_bar_fill__mutmut_7'] = x_compute_bar_fill__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_bar_fill__mutmut['x_compute_bar_fill__mutmut_8'] = x_compute_bar_fill__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_bar_fill__mutmut['x_compute_bar_fill__mutmut_9'] = x_compute_bar_fill__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_bar_fill__mutmut['x_compute_bar_fill__mutmut_10'] = x_compute_bar_fill__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_bar_fill__mutmut['x_compute_bar_fill__mutmut_11'] = x_compute_bar_fill__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_bar_fill__mutmut['x_compute_bar_fill__mutmut_12'] = x_compute_bar_fill__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_bar_fill__mutmut['x_compute_bar_fill__mutmut_13'] = x_compute_bar_fill__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_bar_fill__mutmut['x_compute_bar_fill__mutmut_14'] = x_compute_bar_fill__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_bar_fill__mutmut['x_compute_bar_fill__mutmut_15'] = x_compute_bar_fill__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_bar_fill__mutmut['x_compute_bar_fill__mutmut_16'] = x_compute_bar_fill__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_bar_fill__mutmut['x_compute_bar_fill__mutmut_17'] = x_compute_bar_fill__mutmut_17 # type: ignore # mutmut generated
mutants_x_format_quota_exceeded__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_format_quota_exceeded__mutmut)
def format_quota_exceeded(
    used: int,
    limit: int,
    *,
    resource: str = "investigations",
) -> str:
    """Build the CLI message shown when a quota is exceeded.

    CLI-only: the pricing link and the license-activation command are only
    actionable from a terminal. MCP tools surface the neutral exception
    message; the Slack adapter builds its own. Do not call this from the
    application core or the MCP/Slack adapters.
    """
    label = QUOTA_RESOURCE_LABELS.get(resource, resource)
    return (
        f"\u274c Quota exceeded \u2014 {label} ({used}/{limit})\n"
        f"Upgrade your plan: {UPGRADE_URL}\n"
        f"Activate: hexa license activate <YOUR-KEY>"
    )


def x_format_quota_exceeded__mutmut_orig(
    used: int,
    limit: int,
    *,
    resource: str = "investigations",
) -> str:
    """Build the CLI message shown when a quota is exceeded.

    CLI-only: the pricing link and the license-activation command are only
    actionable from a terminal. MCP tools surface the neutral exception
    message; the Slack adapter builds its own. Do not call this from the
    application core or the MCP/Slack adapters.
    """
    label = QUOTA_RESOURCE_LABELS.get(resource, resource)
    return (
        f"\u274c Quota exceeded \u2014 {label} ({used}/{limit})\n"
        f"Upgrade your plan: {UPGRADE_URL}\n"
        f"Activate: hexa license activate <YOUR-KEY>"
    )


def x_format_quota_exceeded__mutmut_1(
    used: int,
    limit: int,
    *,
    resource: str = "XXinvestigationsXX",
) -> str:
    """Build the CLI message shown when a quota is exceeded.

    CLI-only: the pricing link and the license-activation command are only
    actionable from a terminal. MCP tools surface the neutral exception
    message; the Slack adapter builds its own. Do not call this from the
    application core or the MCP/Slack adapters.
    """
    label = QUOTA_RESOURCE_LABELS.get(resource, resource)
    return (
        f"\u274c Quota exceeded \u2014 {label} ({used}/{limit})\n"
        f"Upgrade your plan: {UPGRADE_URL}\n"
        f"Activate: hexa license activate <YOUR-KEY>"
    )


def x_format_quota_exceeded__mutmut_2(
    used: int,
    limit: int,
    *,
    resource: str = "INVESTIGATIONS",
) -> str:
    """Build the CLI message shown when a quota is exceeded.

    CLI-only: the pricing link and the license-activation command are only
    actionable from a terminal. MCP tools surface the neutral exception
    message; the Slack adapter builds its own. Do not call this from the
    application core or the MCP/Slack adapters.
    """
    label = QUOTA_RESOURCE_LABELS.get(resource, resource)
    return (
        f"\u274c Quota exceeded \u2014 {label} ({used}/{limit})\n"
        f"Upgrade your plan: {UPGRADE_URL}\n"
        f"Activate: hexa license activate <YOUR-KEY>"
    )


def x_format_quota_exceeded__mutmut_3(
    used: int,
    limit: int,
    *,
    resource: str = "investigations",
) -> str:
    """Build the CLI message shown when a quota is exceeded.

    CLI-only: the pricing link and the license-activation command are only
    actionable from a terminal. MCP tools surface the neutral exception
    message; the Slack adapter builds its own. Do not call this from the
    application core or the MCP/Slack adapters.
    """
    label = None
    return (
        f"\u274c Quota exceeded \u2014 {label} ({used}/{limit})\n"
        f"Upgrade your plan: {UPGRADE_URL}\n"
        f"Activate: hexa license activate <YOUR-KEY>"
    )


def x_format_quota_exceeded__mutmut_4(
    used: int,
    limit: int,
    *,
    resource: str = "investigations",
) -> str:
    """Build the CLI message shown when a quota is exceeded.

    CLI-only: the pricing link and the license-activation command are only
    actionable from a terminal. MCP tools surface the neutral exception
    message; the Slack adapter builds its own. Do not call this from the
    application core or the MCP/Slack adapters.
    """
    label = QUOTA_RESOURCE_LABELS.get(None, resource)
    return (
        f"\u274c Quota exceeded \u2014 {label} ({used}/{limit})\n"
        f"Upgrade your plan: {UPGRADE_URL}\n"
        f"Activate: hexa license activate <YOUR-KEY>"
    )


def x_format_quota_exceeded__mutmut_5(
    used: int,
    limit: int,
    *,
    resource: str = "investigations",
) -> str:
    """Build the CLI message shown when a quota is exceeded.

    CLI-only: the pricing link and the license-activation command are only
    actionable from a terminal. MCP tools surface the neutral exception
    message; the Slack adapter builds its own. Do not call this from the
    application core or the MCP/Slack adapters.
    """
    label = QUOTA_RESOURCE_LABELS.get(resource, None)
    return (
        f"\u274c Quota exceeded \u2014 {label} ({used}/{limit})\n"
        f"Upgrade your plan: {UPGRADE_URL}\n"
        f"Activate: hexa license activate <YOUR-KEY>"
    )


def x_format_quota_exceeded__mutmut_6(
    used: int,
    limit: int,
    *,
    resource: str = "investigations",
) -> str:
    """Build the CLI message shown when a quota is exceeded.

    CLI-only: the pricing link and the license-activation command are only
    actionable from a terminal. MCP tools surface the neutral exception
    message; the Slack adapter builds its own. Do not call this from the
    application core or the MCP/Slack adapters.
    """
    label = QUOTA_RESOURCE_LABELS.get(resource)
    return (
        f"\u274c Quota exceeded \u2014 {label} ({used}/{limit})\n"
        f"Upgrade your plan: {UPGRADE_URL}\n"
        f"Activate: hexa license activate <YOUR-KEY>"
    )


def x_format_quota_exceeded__mutmut_7(
    used: int,
    limit: int,
    *,
    resource: str = "investigations",
) -> str:
    """Build the CLI message shown when a quota is exceeded.

    CLI-only: the pricing link and the license-activation command are only
    actionable from a terminal. MCP tools surface the neutral exception
    message; the Slack adapter builds its own. Do not call this from the
    application core or the MCP/Slack adapters.
    """
    label = QUOTA_RESOURCE_LABELS.get(resource, )
    return (
        f"\u274c Quota exceeded \u2014 {label} ({used}/{limit})\n"
        f"Upgrade your plan: {UPGRADE_URL}\n"
        f"Activate: hexa license activate <YOUR-KEY>"
    )

mutants_x_format_quota_exceeded__mutmut['_mutmut_orig'] = x_format_quota_exceeded__mutmut_orig # type: ignore # mutmut generated
mutants_x_format_quota_exceeded__mutmut['x_format_quota_exceeded__mutmut_1'] = x_format_quota_exceeded__mutmut_1 # type: ignore # mutmut generated
mutants_x_format_quota_exceeded__mutmut['x_format_quota_exceeded__mutmut_2'] = x_format_quota_exceeded__mutmut_2 # type: ignore # mutmut generated
mutants_x_format_quota_exceeded__mutmut['x_format_quota_exceeded__mutmut_3'] = x_format_quota_exceeded__mutmut_3 # type: ignore # mutmut generated
mutants_x_format_quota_exceeded__mutmut['x_format_quota_exceeded__mutmut_4'] = x_format_quota_exceeded__mutmut_4 # type: ignore # mutmut generated
mutants_x_format_quota_exceeded__mutmut['x_format_quota_exceeded__mutmut_5'] = x_format_quota_exceeded__mutmut_5 # type: ignore # mutmut generated
mutants_x_format_quota_exceeded__mutmut['x_format_quota_exceeded__mutmut_6'] = x_format_quota_exceeded__mutmut_6 # type: ignore # mutmut generated
mutants_x_format_quota_exceeded__mutmut['x_format_quota_exceeded__mutmut_7'] = x_format_quota_exceeded__mutmut_7 # type: ignore # mutmut generated
