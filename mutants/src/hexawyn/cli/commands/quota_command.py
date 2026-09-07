import click

from hexawyn.application.use_case.cluster.get_quota_usage.command import (
    GetQuotaUsageCommand,
)
from hexawyn.application.use_case.cluster.get_quota_usage.get_quota_usage_use_case import (
    GetQuotaUsageUseCase,
)
from hexawyn.cli.presentation.quota_renderer import (
    BAR_WIDTH,
    EMPTY_CHAR,
    FILL_CHAR,
    QUOTA_RESOURCE_LABELS,
    QUOTA_STATE_ICONS,
    UPGRADE_URL,
    compute_bar_fill,
    format_quota_exceeded,
)
from hexawyn.domain.models.quota import QuotaState, QuotaUsage

TIER_LABELS: dict[str, str] = {
    "starter": "\U0001f1eb\U0001f1f7 Starter ($1/month)",
    "team": "\U0001f680 Team ($99/month)",
    "scale_up": "\U0001f680 Scale-up ($199/month)",
}

_BAR_COLORS: dict[str, str] = {
    "normal": "green",
    "warning": "yellow",
    "critical": "red",
    "exhausted": "red",
}


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__render_bar__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__render_bar__mutmut)
def _render_bar(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_orig(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_1(used: int, limit: int | None, state: QuotaState) -> str:
    if state not in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_2(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "XX\u221e Illimit\u00e9XX"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_3(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_4(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221E ILLIMIT\u00E9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_5(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state != QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_6(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return "XXXX"
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_7(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None and limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_8(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is not None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_9(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit < 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_10(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 1:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_11(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return "XXXX"
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_12(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = None
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_13(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(None, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_14(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, None, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_15(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, None)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_16(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_17(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_18(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, )
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_19(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = None
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_20(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(None, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_21(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, None)
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_22(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(_BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_23(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, )
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_24(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["XXnormalXX"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_25(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["NORMAL"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_26(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = None
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_27(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR / (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_28(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH + filled)
    return f"{click.style(FILL_CHAR * filled, fg=color)}{empty_part}"


def x__render_bar__mutmut_29(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(None, fg=color)}{empty_part}"


def x__render_bar__mutmut_30(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, fg=None)}{empty_part}"


def x__render_bar__mutmut_31(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(fg=color)}{empty_part}"


def x__render_bar__mutmut_32(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR * filled, )}{empty_part}"


def x__render_bar__mutmut_33(used: int, limit: int | None, state: QuotaState) -> str:
    if state in (QuotaState.UNLIMITED,):
        return "\u221e Illimit\u00e9"
    if state == QuotaState.LOCKED:
        return ""
    if limit is None or limit <= 0:
        return ""
    filled, _ = compute_bar_fill(used, limit, BAR_WIDTH)
    color = _BAR_COLORS.get(state.value, _BAR_COLORS["normal"])
    empty_part = EMPTY_CHAR * (BAR_WIDTH - filled)
    return f"{click.style(FILL_CHAR / filled, fg=color)}{empty_part}"

mutants_x__render_bar__mutmut['_mutmut_orig'] = x__render_bar__mutmut_orig # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_1'] = x__render_bar__mutmut_1 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_2'] = x__render_bar__mutmut_2 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_3'] = x__render_bar__mutmut_3 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_4'] = x__render_bar__mutmut_4 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_5'] = x__render_bar__mutmut_5 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_6'] = x__render_bar__mutmut_6 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_7'] = x__render_bar__mutmut_7 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_8'] = x__render_bar__mutmut_8 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_9'] = x__render_bar__mutmut_9 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_10'] = x__render_bar__mutmut_10 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_11'] = x__render_bar__mutmut_11 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_12'] = x__render_bar__mutmut_12 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_13'] = x__render_bar__mutmut_13 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_14'] = x__render_bar__mutmut_14 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_15'] = x__render_bar__mutmut_15 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_16'] = x__render_bar__mutmut_16 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_17'] = x__render_bar__mutmut_17 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_18'] = x__render_bar__mutmut_18 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_19'] = x__render_bar__mutmut_19 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_20'] = x__render_bar__mutmut_20 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_21'] = x__render_bar__mutmut_21 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_22'] = x__render_bar__mutmut_22 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_23'] = x__render_bar__mutmut_23 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_24'] = x__render_bar__mutmut_24 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_25'] = x__render_bar__mutmut_25 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_26'] = x__render_bar__mutmut_26 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_27'] = x__render_bar__mutmut_27 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_28'] = x__render_bar__mutmut_28 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_29'] = x__render_bar__mutmut_29 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_30'] = x__render_bar__mutmut_30 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_31'] = x__render_bar__mutmut_31 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_32'] = x__render_bar__mutmut_32 # type: ignore # mutmut generated
mutants_x__render_bar__mutmut['x__render_bar__mutmut_33'] = x__render_bar__mutmut_33 # type: ignore # mutmut generated
mutants_x__render_line__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__render_line__mutmut)
def _render_line(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_orig(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_1(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = None
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_2(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(None, "")
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_3(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, None)
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_4(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get("")
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_5(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, )
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_6(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "XXXX")
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_7(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = None

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_8(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(None, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_9(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, None, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_10(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, limit, None)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_11(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_12(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_13(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, limit, )

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_14(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, limit, state)

    if state != QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_15(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = None
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_16(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "XX\u221e Illimit\u00e9XX"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_17(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_18(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221E ILLIMIT\u00E9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_19(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state != QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_20(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = None
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_21(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "XX\U0001f512 UnavailableXX"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_22(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 unavailable"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_23(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001F512 UNAVAILABLE"
    else:
        remaining = (limit or 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_24(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = None
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_25(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) + used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_26(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit and 0) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_27(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 1) - used
        extra = f"{used}/{limit}  {bar}  {remaining} remaining"

    return f"{label}: {icon}{extra}"


def x__render_line__mutmut_28(
    label: str,
    used: int,
    limit: int | None,
    state: QuotaState,
) -> str:
    icon = QUOTA_STATE_ICONS.get(state, "")
    bar = _render_bar(used, limit, state)

    if state == QuotaState.UNLIMITED:
        extra = "\u221e Illimit\u00e9"
    elif state == QuotaState.LOCKED:
        extra = "\U0001f512 Unavailable"
    else:
        remaining = (limit or 0) - used
        extra = None

    return f"{label}: {icon}{extra}"

mutants_x__render_line__mutmut['_mutmut_orig'] = x__render_line__mutmut_orig # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_1'] = x__render_line__mutmut_1 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_2'] = x__render_line__mutmut_2 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_3'] = x__render_line__mutmut_3 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_4'] = x__render_line__mutmut_4 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_5'] = x__render_line__mutmut_5 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_6'] = x__render_line__mutmut_6 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_7'] = x__render_line__mutmut_7 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_8'] = x__render_line__mutmut_8 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_9'] = x__render_line__mutmut_9 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_10'] = x__render_line__mutmut_10 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_11'] = x__render_line__mutmut_11 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_12'] = x__render_line__mutmut_12 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_13'] = x__render_line__mutmut_13 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_14'] = x__render_line__mutmut_14 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_15'] = x__render_line__mutmut_15 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_16'] = x__render_line__mutmut_16 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_17'] = x__render_line__mutmut_17 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_18'] = x__render_line__mutmut_18 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_19'] = x__render_line__mutmut_19 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_20'] = x__render_line__mutmut_20 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_21'] = x__render_line__mutmut_21 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_22'] = x__render_line__mutmut_22 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_23'] = x__render_line__mutmut_23 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_24'] = x__render_line__mutmut_24 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_25'] = x__render_line__mutmut_25 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_26'] = x__render_line__mutmut_26 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_27'] = x__render_line__mutmut_27 # type: ignore # mutmut generated
mutants_x__render_line__mutmut['x__render_line__mutmut_28'] = x__render_line__mutmut_28 # type: ignore # mutmut generated
mutants_x__get_tier_label__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__get_tier_label__mutmut)
def _get_tier_label() -> str:
    try:
        from hexawyn.infrastructure.config.license_manager import get_license_tier

        tier = get_license_tier()
        return TIER_LABELS.get(tier.value, TIER_LABELS["starter"])
    except ImportError:
        return TIER_LABELS["starter"]


def x__get_tier_label__mutmut_orig() -> str:
    try:
        from hexawyn.infrastructure.config.license_manager import get_license_tier

        tier = get_license_tier()
        return TIER_LABELS.get(tier.value, TIER_LABELS["starter"])
    except ImportError:
        return TIER_LABELS["starter"]


def x__get_tier_label__mutmut_1() -> str:
    try:
        from hexawyn.infrastructure.config.license_manager import get_license_tier

        tier = None
        return TIER_LABELS.get(tier.value, TIER_LABELS["starter"])
    except ImportError:
        return TIER_LABELS["starter"]


def x__get_tier_label__mutmut_2() -> str:
    try:
        from hexawyn.infrastructure.config.license_manager import get_license_tier

        tier = get_license_tier()
        return TIER_LABELS.get(None, TIER_LABELS["starter"])
    except ImportError:
        return TIER_LABELS["starter"]


def x__get_tier_label__mutmut_3() -> str:
    try:
        from hexawyn.infrastructure.config.license_manager import get_license_tier

        tier = get_license_tier()
        return TIER_LABELS.get(tier.value, None)
    except ImportError:
        return TIER_LABELS["starter"]


def x__get_tier_label__mutmut_4() -> str:
    try:
        from hexawyn.infrastructure.config.license_manager import get_license_tier

        tier = get_license_tier()
        return TIER_LABELS.get(TIER_LABELS["starter"])
    except ImportError:
        return TIER_LABELS["starter"]


def x__get_tier_label__mutmut_5() -> str:
    try:
        from hexawyn.infrastructure.config.license_manager import get_license_tier

        tier = get_license_tier()
        return TIER_LABELS.get(tier.value, )
    except ImportError:
        return TIER_LABELS["starter"]


def x__get_tier_label__mutmut_6() -> str:
    try:
        from hexawyn.infrastructure.config.license_manager import get_license_tier

        tier = get_license_tier()
        return TIER_LABELS.get(tier.value, TIER_LABELS["XXstarterXX"])
    except ImportError:
        return TIER_LABELS["starter"]


def x__get_tier_label__mutmut_7() -> str:
    try:
        from hexawyn.infrastructure.config.license_manager import get_license_tier

        tier = get_license_tier()
        return TIER_LABELS.get(tier.value, TIER_LABELS["STARTER"])
    except ImportError:
        return TIER_LABELS["starter"]


def x__get_tier_label__mutmut_8() -> str:
    try:
        from hexawyn.infrastructure.config.license_manager import get_license_tier

        tier = get_license_tier()
        return TIER_LABELS.get(tier.value, TIER_LABELS["starter"])
    except ImportError:
        return TIER_LABELS["XXstarterXX"]


def x__get_tier_label__mutmut_9() -> str:
    try:
        from hexawyn.infrastructure.config.license_manager import get_license_tier

        tier = get_license_tier()
        return TIER_LABELS.get(tier.value, TIER_LABELS["starter"])
    except ImportError:
        return TIER_LABELS["STARTER"]

mutants_x__get_tier_label__mutmut['_mutmut_orig'] = x__get_tier_label__mutmut_orig # type: ignore # mutmut generated
mutants_x__get_tier_label__mutmut['x__get_tier_label__mutmut_1'] = x__get_tier_label__mutmut_1 # type: ignore # mutmut generated
mutants_x__get_tier_label__mutmut['x__get_tier_label__mutmut_2'] = x__get_tier_label__mutmut_2 # type: ignore # mutmut generated
mutants_x__get_tier_label__mutmut['x__get_tier_label__mutmut_3'] = x__get_tier_label__mutmut_3 # type: ignore # mutmut generated
mutants_x__get_tier_label__mutmut['x__get_tier_label__mutmut_4'] = x__get_tier_label__mutmut_4 # type: ignore # mutmut generated
mutants_x__get_tier_label__mutmut['x__get_tier_label__mutmut_5'] = x__get_tier_label__mutmut_5 # type: ignore # mutmut generated
mutants_x__get_tier_label__mutmut['x__get_tier_label__mutmut_6'] = x__get_tier_label__mutmut_6 # type: ignore # mutmut generated
mutants_x__get_tier_label__mutmut['x__get_tier_label__mutmut_7'] = x__get_tier_label__mutmut_7 # type: ignore # mutmut generated
mutants_x__get_tier_label__mutmut['x__get_tier_label__mutmut_8'] = x__get_tier_label__mutmut_8 # type: ignore # mutmut generated
mutants_x__get_tier_label__mutmut['x__get_tier_label__mutmut_9'] = x__get_tier_label__mutmut_9 # type: ignore # mutmut generated


@click.command()
def quota() -> None:
    """Show your monthly usage quota per resource with progress bars."""
    from hexawyn.application.service.runtime_adapter import get_runtime
    from hexawyn.infrastructure.adapters.secondary.runtime_quota_source import RuntimeQuotaSource
    from hexawyn.infrastructure.config.quota_manager import _get_current_month

    quota_source = RuntimeQuotaSource(runtime=get_runtime())
    month = _get_current_month()

    use_case = GetQuotaUsageUseCase(plan_port=quota_source, usage_meter=quota_source)
    response = use_case.execute(GetQuotaUsageCommand())

    tier_label = _get_tier_label()

    click.echo(f"\nhexawyn Usage \u2014 {month}")
    click.echo("\u2500" * 52)
    click.echo(f"Tier          : {tier_label}")

    any_exhausted = False
    any_above_normal = False
    exhausted_quota: QuotaUsage | None = None

    for quota_usage in response.quotas:
        if quota_usage.state == QuotaState.UNLIMITED:
            continue
        label = QUOTA_RESOURCE_LABELS.get(quota_usage.resource, quota_usage.resource)

        if quota_usage.state == QuotaState.EXHAUSTED:
            any_exhausted = True
            exhausted_quota = quota_usage
        if quota_usage.state in (QuotaState.WARNING, QuotaState.CRITICAL):
            any_above_normal = True

        click.echo(
            _render_line(
                label=label,
                used=quota_usage.used,
                limit=quota_usage.limit,
                state=quota_usage.state,
            )
        )

    from hexawyn.infrastructure.config.quota_manager import get_history_days

    history_days = get_history_days()
    if history_days == -1:
        click.echo("History       : \u221e Unlimited")
    else:
        click.echo(f"History       : {history_days} days")

    click.echo("Reset         : 1st of next month")

    if any_exhausted and exhausted_quota is not None:
        click.echo(
            "\n"
            + format_quota_exceeded(
                used=exhausted_quota.used,
                limit=exhausted_quota.limit or 0,
                resource=exhausted_quota.resource,
            )
        )
    elif any_above_normal:
        click.echo(f"\n\U0001f680 Running low on quota! Upgrade: {UPGRADE_URL}")
