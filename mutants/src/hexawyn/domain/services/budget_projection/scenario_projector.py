from __future__ import annotations

from hexawyn.domain.models.budget_projection import ProjectedMonth
from hexawyn.domain.services.budget_projection.growth_estimator import GrowthEstimate

_OPTIMISTIC_FACTOR = 0.5
_PESSIMISTIC_FACTOR = 1.5
_EXPONENTIAL_PESSIMISTIC_FACTOR = 2.0


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_project_months__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_project_months__mutmut)
def project_months(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_orig(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_1(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = None
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_2(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct * 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_3(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 101
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_4(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = None
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_5(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate / _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_6(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = None
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_7(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate / _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_8(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(None)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_9(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = None

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_10(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = None
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_11(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(None, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_12(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, None):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_13(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_14(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, ):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_15(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(2, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_16(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon - 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_17(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 2):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_18(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = None
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_19(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(None, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_20(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, None, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_21(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, None)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_22(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_23(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_24(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, )
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_25(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            None
        )
    return months


def x_project_months__mutmut_26(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=None,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_27(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=None,
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_28(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=None,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_29(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=None,
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_30(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=None,
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_31(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=None,
            )
        )
    return months


def x_project_months__mutmut_32(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_33(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_34(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_35(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_36(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_37(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                )
        )
    return months


def x_project_months__mutmut_38(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(None, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_39(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, None),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_40(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_41(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, ),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_42(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(None, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_43(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, None, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_44(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, None),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_45(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_46(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_47(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, ),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_48(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(None, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_49(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, None, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_50(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, None),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_51(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_52(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_53(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, ),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def x_project_months__mutmut_54(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(None, category_mix),
            )
        )
    return months


def x_project_months__mutmut_55(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, None),
            )
        )
    return months


def x_project_months__mutmut_56(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(category_mix),
            )
        )
    return months


def x_project_months__mutmut_57(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, ),
            )
        )
    return months

mutants_x_project_months__mutmut['_mutmut_orig'] = x_project_months__mutmut_orig # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_1'] = x_project_months__mutmut_1 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_2'] = x_project_months__mutmut_2 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_3'] = x_project_months__mutmut_3 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_4'] = x_project_months__mutmut_4 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_5'] = x_project_months__mutmut_5 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_6'] = x_project_months__mutmut_6 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_7'] = x_project_months__mutmut_7 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_8'] = x_project_months__mutmut_8 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_9'] = x_project_months__mutmut_9 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_10'] = x_project_months__mutmut_10 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_11'] = x_project_months__mutmut_11 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_12'] = x_project_months__mutmut_12 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_13'] = x_project_months__mutmut_13 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_14'] = x_project_months__mutmut_14 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_15'] = x_project_months__mutmut_15 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_16'] = x_project_months__mutmut_16 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_17'] = x_project_months__mutmut_17 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_18'] = x_project_months__mutmut_18 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_19'] = x_project_months__mutmut_19 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_20'] = x_project_months__mutmut_20 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_21'] = x_project_months__mutmut_21 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_22'] = x_project_months__mutmut_22 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_23'] = x_project_months__mutmut_23 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_24'] = x_project_months__mutmut_24 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_25'] = x_project_months__mutmut_25 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_26'] = x_project_months__mutmut_26 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_27'] = x_project_months__mutmut_27 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_28'] = x_project_months__mutmut_28 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_29'] = x_project_months__mutmut_29 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_30'] = x_project_months__mutmut_30 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_31'] = x_project_months__mutmut_31 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_32'] = x_project_months__mutmut_32 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_33'] = x_project_months__mutmut_33 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_34'] = x_project_months__mutmut_34 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_35'] = x_project_months__mutmut_35 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_36'] = x_project_months__mutmut_36 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_37'] = x_project_months__mutmut_37 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_38'] = x_project_months__mutmut_38 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_39'] = x_project_months__mutmut_39 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_40'] = x_project_months__mutmut_40 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_41'] = x_project_months__mutmut_41 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_42'] = x_project_months__mutmut_42 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_43'] = x_project_months__mutmut_43 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_44'] = x_project_months__mutmut_44 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_45'] = x_project_months__mutmut_45 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_46'] = x_project_months__mutmut_46 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_47'] = x_project_months__mutmut_47 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_48'] = x_project_months__mutmut_48 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_49'] = x_project_months__mutmut_49 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_50'] = x_project_months__mutmut_50 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_51'] = x_project_months__mutmut_51 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_52'] = x_project_months__mutmut_52 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_53'] = x_project_months__mutmut_53 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_54'] = x_project_months__mutmut_54 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_55'] = x_project_months__mutmut_55 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_56'] = x_project_months__mutmut_56 # type: ignore # mutmut generated
mutants_x_project_months__mutmut['x_project_months__mutmut_57'] = x_project_months__mutmut_57 # type: ignore # mutmut generated
mutants_x__pessimistic_factor__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__pessimistic_factor__mutmut)
def _pessimistic_factor(model: str) -> float:
    if model == "exponential":
        return _EXPONENTIAL_PESSIMISTIC_FACTOR
    return _PESSIMISTIC_FACTOR


def x__pessimistic_factor__mutmut_orig(model: str) -> float:
    if model == "exponential":
        return _EXPONENTIAL_PESSIMISTIC_FACTOR
    return _PESSIMISTIC_FACTOR


def x__pessimistic_factor__mutmut_1(model: str) -> float:
    if model != "exponential":
        return _EXPONENTIAL_PESSIMISTIC_FACTOR
    return _PESSIMISTIC_FACTOR


def x__pessimistic_factor__mutmut_2(model: str) -> float:
    if model == "XXexponentialXX":
        return _EXPONENTIAL_PESSIMISTIC_FACTOR
    return _PESSIMISTIC_FACTOR


def x__pessimistic_factor__mutmut_3(model: str) -> float:
    if model == "EXPONENTIAL":
        return _EXPONENTIAL_PESSIMISTIC_FACTOR
    return _PESSIMISTIC_FACTOR

mutants_x__pessimistic_factor__mutmut['_mutmut_orig'] = x__pessimistic_factor__mutmut_orig # type: ignore # mutmut generated
mutants_x__pessimistic_factor__mutmut['x__pessimistic_factor__mutmut_1'] = x__pessimistic_factor__mutmut_1 # type: ignore # mutmut generated
mutants_x__pessimistic_factor__mutmut['x__pessimistic_factor__mutmut_2'] = x__pessimistic_factor__mutmut_2 # type: ignore # mutmut generated
mutants_x__pessimistic_factor__mutmut['x__pessimistic_factor__mutmut_3'] = x__pessimistic_factor__mutmut_3 # type: ignore # mutmut generated
mutants_x__compound__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compound__mutmut)
def _compound(base: float, rate: float, offset: int) -> float:
    return round(base * (1 + rate) ** offset, 2)


def x__compound__mutmut_orig(base: float, rate: float, offset: int) -> float:
    return round(base * (1 + rate) ** offset, 2)


def x__compound__mutmut_1(base: float, rate: float, offset: int) -> float:
    return round(None, 2)


def x__compound__mutmut_2(base: float, rate: float, offset: int) -> float:
    return round(base * (1 + rate) ** offset, None)


def x__compound__mutmut_3(base: float, rate: float, offset: int) -> float:
    return round(2)


def x__compound__mutmut_4(base: float, rate: float, offset: int) -> float:
    return round(base * (1 + rate) ** offset, )


def x__compound__mutmut_5(base: float, rate: float, offset: int) -> float:
    return round(base / (1 + rate) ** offset, 2)


def x__compound__mutmut_6(base: float, rate: float, offset: int) -> float:
    return round(base * (1 + rate) * offset, 2)


def x__compound__mutmut_7(base: float, rate: float, offset: int) -> float:
    return round(base * (1 - rate) ** offset, 2)


def x__compound__mutmut_8(base: float, rate: float, offset: int) -> float:
    return round(base * (2 + rate) ** offset, 2)


def x__compound__mutmut_9(base: float, rate: float, offset: int) -> float:
    return round(base * (1 + rate) ** offset, 3)

mutants_x__compound__mutmut['_mutmut_orig'] = x__compound__mutmut_orig # type: ignore # mutmut generated
mutants_x__compound__mutmut['x__compound__mutmut_1'] = x__compound__mutmut_1 # type: ignore # mutmut generated
mutants_x__compound__mutmut['x__compound__mutmut_2'] = x__compound__mutmut_2 # type: ignore # mutmut generated
mutants_x__compound__mutmut['x__compound__mutmut_3'] = x__compound__mutmut_3 # type: ignore # mutmut generated
mutants_x__compound__mutmut['x__compound__mutmut_4'] = x__compound__mutmut_4 # type: ignore # mutmut generated
mutants_x__compound__mutmut['x__compound__mutmut_5'] = x__compound__mutmut_5 # type: ignore # mutmut generated
mutants_x__compound__mutmut['x__compound__mutmut_6'] = x__compound__mutmut_6 # type: ignore # mutmut generated
mutants_x__compound__mutmut['x__compound__mutmut_7'] = x__compound__mutmut_7 # type: ignore # mutmut generated
mutants_x__compound__mutmut['x__compound__mutmut_8'] = x__compound__mutmut_8 # type: ignore # mutmut generated
mutants_x__compound__mutmut['x__compound__mutmut_9'] = x__compound__mutmut_9 # type: ignore # mutmut generated
mutants_x__split_categories__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__split_categories__mutmut)
def _split_categories(total: float, category_mix: dict[str, float]) -> dict[str, float]:
    return {category: round(total * share, 2) for category, share in category_mix.items()}


def x__split_categories__mutmut_orig(total: float, category_mix: dict[str, float]) -> dict[str, float]:
    return {category: round(total * share, 2) for category, share in category_mix.items()}


def x__split_categories__mutmut_1(total: float, category_mix: dict[str, float]) -> dict[str, float]:
    return {category: round(None, 2) for category, share in category_mix.items()}


def x__split_categories__mutmut_2(total: float, category_mix: dict[str, float]) -> dict[str, float]:
    return {category: round(total * share, None) for category, share in category_mix.items()}


def x__split_categories__mutmut_3(total: float, category_mix: dict[str, float]) -> dict[str, float]:
    return {category: round(2) for category, share in category_mix.items()}


def x__split_categories__mutmut_4(total: float, category_mix: dict[str, float]) -> dict[str, float]:
    return {category: round(total * share, ) for category, share in category_mix.items()}


def x__split_categories__mutmut_5(total: float, category_mix: dict[str, float]) -> dict[str, float]:
    return {category: round(total / share, 2) for category, share in category_mix.items()}


def x__split_categories__mutmut_6(total: float, category_mix: dict[str, float]) -> dict[str, float]:
    return {category: round(total * share, 3) for category, share in category_mix.items()}

mutants_x__split_categories__mutmut['_mutmut_orig'] = x__split_categories__mutmut_orig # type: ignore # mutmut generated
mutants_x__split_categories__mutmut['x__split_categories__mutmut_1'] = x__split_categories__mutmut_1 # type: ignore # mutmut generated
mutants_x__split_categories__mutmut['x__split_categories__mutmut_2'] = x__split_categories__mutmut_2 # type: ignore # mutmut generated
mutants_x__split_categories__mutmut['x__split_categories__mutmut_3'] = x__split_categories__mutmut_3 # type: ignore # mutmut generated
mutants_x__split_categories__mutmut['x__split_categories__mutmut_4'] = x__split_categories__mutmut_4 # type: ignore # mutmut generated
mutants_x__split_categories__mutmut['x__split_categories__mutmut_5'] = x__split_categories__mutmut_5 # type: ignore # mutmut generated
mutants_x__split_categories__mutmut['x__split_categories__mutmut_6'] = x__split_categories__mutmut_6 # type: ignore # mutmut generated
mutants_x__add_months__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__add_months__mutmut)
def _add_months(start_month: str, offset: int) -> str:
    year, month = (int(part) for part in start_month.split("-"))
    zero_based = (month - 1) + offset
    new_year = year + zero_based // 12
    new_month = zero_based % 12 + 1
    return f"{new_year:04d}-{new_month:02d}"


def x__add_months__mutmut_orig(start_month: str, offset: int) -> str:
    year, month = (int(part) for part in start_month.split("-"))
    zero_based = (month - 1) + offset
    new_year = year + zero_based // 12
    new_month = zero_based % 12 + 1
    return f"{new_year:04d}-{new_month:02d}"


def x__add_months__mutmut_1(start_month: str, offset: int) -> str:
    year, month = None
    zero_based = (month - 1) + offset
    new_year = year + zero_based // 12
    new_month = zero_based % 12 + 1
    return f"{new_year:04d}-{new_month:02d}"


def x__add_months__mutmut_2(start_month: str, offset: int) -> str:
    year, month = (int(None) for part in start_month.split("-"))
    zero_based = (month - 1) + offset
    new_year = year + zero_based // 12
    new_month = zero_based % 12 + 1
    return f"{new_year:04d}-{new_month:02d}"


def x__add_months__mutmut_3(start_month: str, offset: int) -> str:
    year, month = (int(part) for part in start_month.split(None))
    zero_based = (month - 1) + offset
    new_year = year + zero_based // 12
    new_month = zero_based % 12 + 1
    return f"{new_year:04d}-{new_month:02d}"


def x__add_months__mutmut_4(start_month: str, offset: int) -> str:
    year, month = (int(part) for part in start_month.split("XX-XX"))
    zero_based = (month - 1) + offset
    new_year = year + zero_based // 12
    new_month = zero_based % 12 + 1
    return f"{new_year:04d}-{new_month:02d}"


def x__add_months__mutmut_5(start_month: str, offset: int) -> str:
    year, month = (int(part) for part in start_month.split("-"))
    zero_based = None
    new_year = year + zero_based // 12
    new_month = zero_based % 12 + 1
    return f"{new_year:04d}-{new_month:02d}"


def x__add_months__mutmut_6(start_month: str, offset: int) -> str:
    year, month = (int(part) for part in start_month.split("-"))
    zero_based = (month - 1) - offset
    new_year = year + zero_based // 12
    new_month = zero_based % 12 + 1
    return f"{new_year:04d}-{new_month:02d}"


def x__add_months__mutmut_7(start_month: str, offset: int) -> str:
    year, month = (int(part) for part in start_month.split("-"))
    zero_based = (month + 1) + offset
    new_year = year + zero_based // 12
    new_month = zero_based % 12 + 1
    return f"{new_year:04d}-{new_month:02d}"


def x__add_months__mutmut_8(start_month: str, offset: int) -> str:
    year, month = (int(part) for part in start_month.split("-"))
    zero_based = (month - 2) + offset
    new_year = year + zero_based // 12
    new_month = zero_based % 12 + 1
    return f"{new_year:04d}-{new_month:02d}"


def x__add_months__mutmut_9(start_month: str, offset: int) -> str:
    year, month = (int(part) for part in start_month.split("-"))
    zero_based = (month - 1) + offset
    new_year = None
    new_month = zero_based % 12 + 1
    return f"{new_year:04d}-{new_month:02d}"


def x__add_months__mutmut_10(start_month: str, offset: int) -> str:
    year, month = (int(part) for part in start_month.split("-"))
    zero_based = (month - 1) + offset
    new_year = year - zero_based // 12
    new_month = zero_based % 12 + 1
    return f"{new_year:04d}-{new_month:02d}"


def x__add_months__mutmut_11(start_month: str, offset: int) -> str:
    year, month = (int(part) for part in start_month.split("-"))
    zero_based = (month - 1) + offset
    new_year = year + zero_based / 12
    new_month = zero_based % 12 + 1
    return f"{new_year:04d}-{new_month:02d}"


def x__add_months__mutmut_12(start_month: str, offset: int) -> str:
    year, month = (int(part) for part in start_month.split("-"))
    zero_based = (month - 1) + offset
    new_year = year + zero_based // 13
    new_month = zero_based % 12 + 1
    return f"{new_year:04d}-{new_month:02d}"


def x__add_months__mutmut_13(start_month: str, offset: int) -> str:
    year, month = (int(part) for part in start_month.split("-"))
    zero_based = (month - 1) + offset
    new_year = year + zero_based // 12
    new_month = None
    return f"{new_year:04d}-{new_month:02d}"


def x__add_months__mutmut_14(start_month: str, offset: int) -> str:
    year, month = (int(part) for part in start_month.split("-"))
    zero_based = (month - 1) + offset
    new_year = year + zero_based // 12
    new_month = zero_based % 12 - 1
    return f"{new_year:04d}-{new_month:02d}"


def x__add_months__mutmut_15(start_month: str, offset: int) -> str:
    year, month = (int(part) for part in start_month.split("-"))
    zero_based = (month - 1) + offset
    new_year = year + zero_based // 12
    new_month = zero_based / 12 + 1
    return f"{new_year:04d}-{new_month:02d}"


def x__add_months__mutmut_16(start_month: str, offset: int) -> str:
    year, month = (int(part) for part in start_month.split("-"))
    zero_based = (month - 1) + offset
    new_year = year + zero_based // 12
    new_month = zero_based % 13 + 1
    return f"{new_year:04d}-{new_month:02d}"


def x__add_months__mutmut_17(start_month: str, offset: int) -> str:
    year, month = (int(part) for part in start_month.split("-"))
    zero_based = (month - 1) + offset
    new_year = year + zero_based // 12
    new_month = zero_based % 12 + 2
    return f"{new_year:04d}-{new_month:02d}"

mutants_x__add_months__mutmut['_mutmut_orig'] = x__add_months__mutmut_orig # type: ignore # mutmut generated
mutants_x__add_months__mutmut['x__add_months__mutmut_1'] = x__add_months__mutmut_1 # type: ignore # mutmut generated
mutants_x__add_months__mutmut['x__add_months__mutmut_2'] = x__add_months__mutmut_2 # type: ignore # mutmut generated
mutants_x__add_months__mutmut['x__add_months__mutmut_3'] = x__add_months__mutmut_3 # type: ignore # mutmut generated
mutants_x__add_months__mutmut['x__add_months__mutmut_4'] = x__add_months__mutmut_4 # type: ignore # mutmut generated
mutants_x__add_months__mutmut['x__add_months__mutmut_5'] = x__add_months__mutmut_5 # type: ignore # mutmut generated
mutants_x__add_months__mutmut['x__add_months__mutmut_6'] = x__add_months__mutmut_6 # type: ignore # mutmut generated
mutants_x__add_months__mutmut['x__add_months__mutmut_7'] = x__add_months__mutmut_7 # type: ignore # mutmut generated
mutants_x__add_months__mutmut['x__add_months__mutmut_8'] = x__add_months__mutmut_8 # type: ignore # mutmut generated
mutants_x__add_months__mutmut['x__add_months__mutmut_9'] = x__add_months__mutmut_9 # type: ignore # mutmut generated
mutants_x__add_months__mutmut['x__add_months__mutmut_10'] = x__add_months__mutmut_10 # type: ignore # mutmut generated
mutants_x__add_months__mutmut['x__add_months__mutmut_11'] = x__add_months__mutmut_11 # type: ignore # mutmut generated
mutants_x__add_months__mutmut['x__add_months__mutmut_12'] = x__add_months__mutmut_12 # type: ignore # mutmut generated
mutants_x__add_months__mutmut['x__add_months__mutmut_13'] = x__add_months__mutmut_13 # type: ignore # mutmut generated
mutants_x__add_months__mutmut['x__add_months__mutmut_14'] = x__add_months__mutmut_14 # type: ignore # mutmut generated
mutants_x__add_months__mutmut['x__add_months__mutmut_15'] = x__add_months__mutmut_15 # type: ignore # mutmut generated
mutants_x__add_months__mutmut['x__add_months__mutmut_16'] = x__add_months__mutmut_16 # type: ignore # mutmut generated
mutants_x__add_months__mutmut['x__add_months__mutmut_17'] = x__add_months__mutmut_17 # type: ignore # mutmut generated
