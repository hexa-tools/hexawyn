from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class SaturationPrediction:
    days_to_saturation: int | None
    saturation_date: str | None
    capped_horizon: bool
mutants_x_predict_saturation__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_predict_saturation__mutmut)
def predict_saturation(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_orig(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_1(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day < 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_2(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 1:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_3(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=None
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_4(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_5(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_6(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_7(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_8(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = None
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_9(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(None, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_10(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, None)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_11(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max((ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_12(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, )
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_13(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(1.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_14(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) * growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_15(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling + current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_16(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days >= max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_17(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=None
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_18(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_19(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_20(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_21(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_22(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = None
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_23(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(None)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_24(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = None
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_25(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at - timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_26(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=None)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_27(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=None, saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_28(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=None, capped_horizon=False
    )


def x_predict_saturation__mutmut_29(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=None
    )


def x_predict_saturation__mutmut_30(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        saturation_date=saturation_date, capped_horizon=False
    )


def x_predict_saturation__mutmut_31(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, capped_horizon=False
    )


def x_predict_saturation__mutmut_32(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, )


def x_predict_saturation__mutmut_33(
    current: float,
    ceiling: float,
    growth_rate_per_day: float,
    observed_at: date,
    max_horizon_days: int,
) -> SaturationPrediction:
    """`(ceiling - current) / growth_rate` — mirrors `MemoryPrediction.compute`'s
    saturation formula. Growth at or below zero means capacity is stable or
    freeing, never a risk. A horizon beyond `max_horizon_days` is capped
    rather than reported as a literal (and practically meaningless) date."""
    if growth_rate_per_day <= 0:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=False
        )

    days = max(0.0, (ceiling - current) / growth_rate_per_day)
    if days > max_horizon_days:
        return SaturationPrediction(
            days_to_saturation=None, saturation_date=None, capped_horizon=True
        )

    days_rounded = round(days)
    saturation_date = (observed_at + timedelta(days=days_rounded)).isoformat()
    return SaturationPrediction(
        days_to_saturation=days_rounded, saturation_date=saturation_date, capped_horizon=True
    )

mutants_x_predict_saturation__mutmut['_mutmut_orig'] = x_predict_saturation__mutmut_orig # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_1'] = x_predict_saturation__mutmut_1 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_2'] = x_predict_saturation__mutmut_2 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_3'] = x_predict_saturation__mutmut_3 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_4'] = x_predict_saturation__mutmut_4 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_5'] = x_predict_saturation__mutmut_5 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_6'] = x_predict_saturation__mutmut_6 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_7'] = x_predict_saturation__mutmut_7 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_8'] = x_predict_saturation__mutmut_8 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_9'] = x_predict_saturation__mutmut_9 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_10'] = x_predict_saturation__mutmut_10 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_11'] = x_predict_saturation__mutmut_11 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_12'] = x_predict_saturation__mutmut_12 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_13'] = x_predict_saturation__mutmut_13 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_14'] = x_predict_saturation__mutmut_14 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_15'] = x_predict_saturation__mutmut_15 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_16'] = x_predict_saturation__mutmut_16 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_17'] = x_predict_saturation__mutmut_17 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_18'] = x_predict_saturation__mutmut_18 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_19'] = x_predict_saturation__mutmut_19 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_20'] = x_predict_saturation__mutmut_20 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_21'] = x_predict_saturation__mutmut_21 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_22'] = x_predict_saturation__mutmut_22 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_23'] = x_predict_saturation__mutmut_23 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_24'] = x_predict_saturation__mutmut_24 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_25'] = x_predict_saturation__mutmut_25 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_26'] = x_predict_saturation__mutmut_26 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_27'] = x_predict_saturation__mutmut_27 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_28'] = x_predict_saturation__mutmut_28 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_29'] = x_predict_saturation__mutmut_29 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_30'] = x_predict_saturation__mutmut_30 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_31'] = x_predict_saturation__mutmut_31 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_32'] = x_predict_saturation__mutmut_32 # type: ignore # mutmut generated
mutants_x_predict_saturation__mutmut['x_predict_saturation__mutmut_33'] = x_predict_saturation__mutmut_33 # type: ignore # mutmut generated
