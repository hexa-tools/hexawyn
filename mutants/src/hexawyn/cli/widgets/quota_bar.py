from textual.widgets import Static

from hexawyn.cli.presentation.quota_renderer import (
    EMPTY_CHAR,
    FILL_CHAR,
    QUOTA_RESOURCE_LABELS,
    QUOTA_STATE_ICONS,
    UPGRADE_URL,
    compute_bar_fill,
)
from hexawyn.domain.models.quota import QuotaState, QuotaUsage

_BAR_COLORS: dict[str, str] = {
    "normal": "#22c55e",
    "warning": "#f97316",
    "critical": "#ef4444",
    "exhausted": "#ef4444",
}


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__quota_bar__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__quota_bar__mutmut)
def _quota_bar(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_orig(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_1(quota: QuotaUsage, width: int = 21) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_2(quota: QuotaUsage, width: int = 20) -> str:
    label = None

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_3(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(None, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_4(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, None)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_5(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_6(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, )

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_7(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state != QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_8(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state != QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_9(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = None
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_10(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier and "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_11(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "XXunknownXX"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_12(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "UNKNOWN"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_13(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = None
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_14(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit and 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_15(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 1
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_16(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = None

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_17(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(None, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_18(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, None, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_19(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, None)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_20(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_21(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_22(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, )

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_23(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = None
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_24(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(None, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_25(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, None)
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_26(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(_BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_27(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, )
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_28(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["XXnormalXX"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_29(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["NORMAL"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_30(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = None

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_31(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR / filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_32(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR / (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_33(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width + filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_34(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = None
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_35(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(None, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_36(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, None)
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_37(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get("")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_38(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, )
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


def x__quota_bar__mutmut_39(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "XXXX")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"

mutants_x__quota_bar__mutmut['_mutmut_orig'] = x__quota_bar__mutmut_orig # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_1'] = x__quota_bar__mutmut_1 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_2'] = x__quota_bar__mutmut_2 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_3'] = x__quota_bar__mutmut_3 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_4'] = x__quota_bar__mutmut_4 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_5'] = x__quota_bar__mutmut_5 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_6'] = x__quota_bar__mutmut_6 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_7'] = x__quota_bar__mutmut_7 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_8'] = x__quota_bar__mutmut_8 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_9'] = x__quota_bar__mutmut_9 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_10'] = x__quota_bar__mutmut_10 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_11'] = x__quota_bar__mutmut_11 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_12'] = x__quota_bar__mutmut_12 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_13'] = x__quota_bar__mutmut_13 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_14'] = x__quota_bar__mutmut_14 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_15'] = x__quota_bar__mutmut_15 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_16'] = x__quota_bar__mutmut_16 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_17'] = x__quota_bar__mutmut_17 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_18'] = x__quota_bar__mutmut_18 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_19'] = x__quota_bar__mutmut_19 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_20'] = x__quota_bar__mutmut_20 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_21'] = x__quota_bar__mutmut_21 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_22'] = x__quota_bar__mutmut_22 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_23'] = x__quota_bar__mutmut_23 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_24'] = x__quota_bar__mutmut_24 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_25'] = x__quota_bar__mutmut_25 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_26'] = x__quota_bar__mutmut_26 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_27'] = x__quota_bar__mutmut_27 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_28'] = x__quota_bar__mutmut_28 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_29'] = x__quota_bar__mutmut_29 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_30'] = x__quota_bar__mutmut_30 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_31'] = x__quota_bar__mutmut_31 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_32'] = x__quota_bar__mutmut_32 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_33'] = x__quota_bar__mutmut_33 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_34'] = x__quota_bar__mutmut_34 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_35'] = x__quota_bar__mutmut_35 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_36'] = x__quota_bar__mutmut_36 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_37'] = x__quota_bar__mutmut_37 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_38'] = x__quota_bar__mutmut_38 # type: ignore # mutmut generated
mutants_x__quota_bar__mutmut['x__quota_bar__mutmut_39'] = x__quota_bar__mutmut_39 # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut: MutantDict = {}  # type: ignore


class QuotaProgressBar(Static):
    @_mutmut_mutated(mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut)
    def update_quotas(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = ["\n[bold]Quota Usage[/bold]", "\u2500" * 52]
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("\n".join(lines))
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_orig(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = ["\n[bold]Quota Usage[/bold]", "\u2500" * 52]
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("\n".join(lines))
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_1(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = None
        lines = ["\n[bold]Quota Usage[/bold]", "\u2500" * 52]
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("\n".join(lines))
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_2(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state == QuotaState.UNLIMITED]
        lines = ["\n[bold]Quota Usage[/bold]", "\u2500" * 52]
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("\n".join(lines))
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_3(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = None
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("\n".join(lines))
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_4(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = ["XX\n[bold]Quota Usage[/bold]XX", "\u2500" * 52]
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("\n".join(lines))
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_5(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = ["\n[bold]quota usage[/bold]", "\u2500" * 52]
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("\n".join(lines))
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_6(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = ["\n[BOLD]QUOTA USAGE[/BOLD]", "\u2500" * 52]
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("\n".join(lines))
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_7(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = ["\n[bold]Quota Usage[/bold]", "\u2500" / 52]
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("\n".join(lines))
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_8(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = ["\n[bold]Quota Usage[/bold]", "XX\u2500XX" * 52]
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("\n".join(lines))
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_9(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = ["\n[bold]Quota Usage[/bold]", "\u2500" * 53]
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("\n".join(lines))
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_10(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = ["\n[bold]Quota Usage[/bold]", "\u2500" * 52]
        any_above_normal = None

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("\n".join(lines))
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_11(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = ["\n[bold]Quota Usage[/bold]", "\u2500" * 52]
        any_above_normal = True

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("\n".join(lines))
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_12(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = ["\n[bold]Quota Usage[/bold]", "\u2500" * 52]
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(None)
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("\n".join(lines))
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_13(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = ["\n[bold]Quota Usage[/bold]", "\u2500" * 52]
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(_quota_bar(None))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("\n".join(lines))
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_14(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = ["\n[bold]Quota Usage[/bold]", "\u2500" * 52]
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state not in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("\n".join(lines))
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_15(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = ["\n[bold]Quota Usage[/bold]", "\u2500" * 52]
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = None

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("\n".join(lines))
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_16(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = ["\n[bold]Quota Usage[/bold]", "\u2500" * 52]
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = False

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("\n".join(lines))
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_17(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = ["\n[bold]Quota Usage[/bold]", "\u2500" * 52]
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(None)

        self.update("\n".join(lines))
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_18(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = ["\n[bold]Quota Usage[/bold]", "\u2500" * 52]
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update(None)
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_19(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = ["\n[bold]Quota Usage[/bold]", "\u2500" * 52]
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("\n".join(None))
    def xǁQuotaProgressBarǁupdate_quotas__mutmut_20(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = ["\n[bold]Quota Usage[/bold]", "\u2500" * 52]
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("XX\nXX".join(lines))

mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['_mutmut_orig'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_orig # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['xǁQuotaProgressBarǁupdate_quotas__mutmut_1'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_1 # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['xǁQuotaProgressBarǁupdate_quotas__mutmut_2'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_2 # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['xǁQuotaProgressBarǁupdate_quotas__mutmut_3'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_3 # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['xǁQuotaProgressBarǁupdate_quotas__mutmut_4'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_4 # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['xǁQuotaProgressBarǁupdate_quotas__mutmut_5'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_5 # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['xǁQuotaProgressBarǁupdate_quotas__mutmut_6'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_6 # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['xǁQuotaProgressBarǁupdate_quotas__mutmut_7'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_7 # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['xǁQuotaProgressBarǁupdate_quotas__mutmut_8'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_8 # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['xǁQuotaProgressBarǁupdate_quotas__mutmut_9'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_9 # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['xǁQuotaProgressBarǁupdate_quotas__mutmut_10'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_10 # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['xǁQuotaProgressBarǁupdate_quotas__mutmut_11'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_11 # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['xǁQuotaProgressBarǁupdate_quotas__mutmut_12'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_12 # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['xǁQuotaProgressBarǁupdate_quotas__mutmut_13'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_13 # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['xǁQuotaProgressBarǁupdate_quotas__mutmut_14'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_14 # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['xǁQuotaProgressBarǁupdate_quotas__mutmut_15'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_15 # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['xǁQuotaProgressBarǁupdate_quotas__mutmut_16'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_16 # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['xǁQuotaProgressBarǁupdate_quotas__mutmut_17'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_17 # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['xǁQuotaProgressBarǁupdate_quotas__mutmut_18'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_18 # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['xǁQuotaProgressBarǁupdate_quotas__mutmut_19'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_19 # type: ignore # mutmut generated
mutants_xǁQuotaProgressBarǁupdate_quotas__mutmut['xǁQuotaProgressBarǁupdate_quotas__mutmut_20'] = QuotaProgressBar.xǁQuotaProgressBarǁupdate_quotas__mutmut_20 # type: ignore # mutmut generated
