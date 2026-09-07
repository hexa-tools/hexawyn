from __future__ import annotations


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_financial_impact__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_financial_impact__mutmut)
def compute_financial_impact(
    total_downtime_minutes: int, cost_per_minute: float | None
) -> float | None:
    """Estimate the financial impact of downtime.

    Returns None when pricing is not configured (``cost_per_minute is None``),
    so no financial figure is ever fabricated. A configured cost of 0.0 yields
    0.0 — a real, meaningful figure — not None.
    """
    if cost_per_minute is None:
        return None
    return round(total_downtime_minutes * cost_per_minute, 2)


def x_compute_financial_impact__mutmut_orig(
    total_downtime_minutes: int, cost_per_minute: float | None
) -> float | None:
    """Estimate the financial impact of downtime.

    Returns None when pricing is not configured (``cost_per_minute is None``),
    so no financial figure is ever fabricated. A configured cost of 0.0 yields
    0.0 — a real, meaningful figure — not None.
    """
    if cost_per_minute is None:
        return None
    return round(total_downtime_minutes * cost_per_minute, 2)


def x_compute_financial_impact__mutmut_1(
    total_downtime_minutes: int, cost_per_minute: float | None
) -> float | None:
    """Estimate the financial impact of downtime.

    Returns None when pricing is not configured (``cost_per_minute is None``),
    so no financial figure is ever fabricated. A configured cost of 0.0 yields
    0.0 — a real, meaningful figure — not None.
    """
    if cost_per_minute is not None:
        return None
    return round(total_downtime_minutes * cost_per_minute, 2)


def x_compute_financial_impact__mutmut_2(
    total_downtime_minutes: int, cost_per_minute: float | None
) -> float | None:
    """Estimate the financial impact of downtime.

    Returns None when pricing is not configured (``cost_per_minute is None``),
    so no financial figure is ever fabricated. A configured cost of 0.0 yields
    0.0 — a real, meaningful figure — not None.
    """
    if cost_per_minute is None:
        return None
    return round(None, 2)


def x_compute_financial_impact__mutmut_3(
    total_downtime_minutes: int, cost_per_minute: float | None
) -> float | None:
    """Estimate the financial impact of downtime.

    Returns None when pricing is not configured (``cost_per_minute is None``),
    so no financial figure is ever fabricated. A configured cost of 0.0 yields
    0.0 — a real, meaningful figure — not None.
    """
    if cost_per_minute is None:
        return None
    return round(total_downtime_minutes * cost_per_minute, None)


def x_compute_financial_impact__mutmut_4(
    total_downtime_minutes: int, cost_per_minute: float | None
) -> float | None:
    """Estimate the financial impact of downtime.

    Returns None when pricing is not configured (``cost_per_minute is None``),
    so no financial figure is ever fabricated. A configured cost of 0.0 yields
    0.0 — a real, meaningful figure — not None.
    """
    if cost_per_minute is None:
        return None
    return round(2)


def x_compute_financial_impact__mutmut_5(
    total_downtime_minutes: int, cost_per_minute: float | None
) -> float | None:
    """Estimate the financial impact of downtime.

    Returns None when pricing is not configured (``cost_per_minute is None``),
    so no financial figure is ever fabricated. A configured cost of 0.0 yields
    0.0 — a real, meaningful figure — not None.
    """
    if cost_per_minute is None:
        return None
    return round(total_downtime_minutes * cost_per_minute, )


def x_compute_financial_impact__mutmut_6(
    total_downtime_minutes: int, cost_per_minute: float | None
) -> float | None:
    """Estimate the financial impact of downtime.

    Returns None when pricing is not configured (``cost_per_minute is None``),
    so no financial figure is ever fabricated. A configured cost of 0.0 yields
    0.0 — a real, meaningful figure — not None.
    """
    if cost_per_minute is None:
        return None
    return round(total_downtime_minutes / cost_per_minute, 2)


def x_compute_financial_impact__mutmut_7(
    total_downtime_minutes: int, cost_per_minute: float | None
) -> float | None:
    """Estimate the financial impact of downtime.

    Returns None when pricing is not configured (``cost_per_minute is None``),
    so no financial figure is ever fabricated. A configured cost of 0.0 yields
    0.0 — a real, meaningful figure — not None.
    """
    if cost_per_minute is None:
        return None
    return round(total_downtime_minutes * cost_per_minute, 3)

mutants_x_compute_financial_impact__mutmut['_mutmut_orig'] = x_compute_financial_impact__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_financial_impact__mutmut['x_compute_financial_impact__mutmut_1'] = x_compute_financial_impact__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_financial_impact__mutmut['x_compute_financial_impact__mutmut_2'] = x_compute_financial_impact__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_financial_impact__mutmut['x_compute_financial_impact__mutmut_3'] = x_compute_financial_impact__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_financial_impact__mutmut['x_compute_financial_impact__mutmut_4'] = x_compute_financial_impact__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_financial_impact__mutmut['x_compute_financial_impact__mutmut_5'] = x_compute_financial_impact__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_financial_impact__mutmut['x_compute_financial_impact__mutmut_6'] = x_compute_financial_impact__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_financial_impact__mutmut['x_compute_financial_impact__mutmut_7'] = x_compute_financial_impact__mutmut_7 # type: ignore # mutmut generated
