from __future__ import annotations

from hexawyn.application.ports.driven.budget_intelligence_port import (
    BudgetIntelligenceData,
)
from hexawyn.domain.models.budget_intelligence import (
    BudgetAlertRecommendation,
    BudgetIntelligenceReport,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_budget_intelligence__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_budget_intelligence__mutmut)
def compute_budget_intelligence(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_orig(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_1(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = None
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_2(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["XXbudget_monthly_eurXX"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_3(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["BUDGET_MONTHLY_EUR"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_4(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None and budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_5(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is not None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_6(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget < 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_7(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 1:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_8(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=None,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_9(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=None,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_10(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation=None,
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_11(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_12(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_13(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_14(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=True,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_15(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="XXConfigurez cloud_budget_monthly pour activer le suivi budgétaire.XX",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_16(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_17(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="CONFIGUREZ CLOUD_BUDGET_MONTHLY POUR ACTIVER LE SUIVI BUDGÉTAIRE.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_18(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = None
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_19(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["XXprojected_spend_eurXX"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_20(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["PROJECTED_SPEND_EUR"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_21(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = None
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_22(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["XXcurrent_spend_eurXX"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_23(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["CURRENT_SPEND_EUR"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_24(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = None
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_25(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round(None, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_26(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, None)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_27(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round(1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_28(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, )
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_29(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget / 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_30(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) * budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_31(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected + budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_32(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 101, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_33(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 2)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_34(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = None
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_35(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected >= budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_36(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = None

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_37(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(None, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_38(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, None)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_39(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_40(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, )

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_41(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=None,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_42(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=None,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_43(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=None,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_44(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=None,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_45(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=None,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_46(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=None,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_47(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=None,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_48(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=None,
    )


def x_compute_budget_intelligence__mutmut_49(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_50(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_51(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_52(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_53(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_54(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        recommendations=recommendations,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_55(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        config_available=True,
    )


def x_compute_budget_intelligence__mutmut_56(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        )


def x_compute_budget_intelligence__mutmut_57(
    data: BudgetIntelligenceData, period: str
) -> BudgetIntelligenceReport:
    budget = data["budget_monthly_eur"]
    if budget is None or budget <= 0:
        return BudgetIntelligenceReport(
            period_label=period,
            config_available=False,
            explanation="Configurez cloud_budget_monthly pour activer le suivi budgétaire.",
        )

    projected = data["projected_spend_eur"]
    current = data["current_spend_eur"]
    overshoot = round((projected - budget) / budget * 100, 1)
    exceeded = projected > budget
    recommendations = _build_recommendations(exceeded, overshoot)

    return BudgetIntelligenceReport(
        period_label=period,
        current_spend_eur=current,
        projected_spend_eur=projected,
        budget_monthly_eur=budget,
        overshoot_pct=overshoot,
        budget_exceeded=exceeded,
        recommendations=recommendations,
        config_available=False,
    )

mutants_x_compute_budget_intelligence__mutmut['_mutmut_orig'] = x_compute_budget_intelligence__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_1'] = x_compute_budget_intelligence__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_2'] = x_compute_budget_intelligence__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_3'] = x_compute_budget_intelligence__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_4'] = x_compute_budget_intelligence__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_5'] = x_compute_budget_intelligence__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_6'] = x_compute_budget_intelligence__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_7'] = x_compute_budget_intelligence__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_8'] = x_compute_budget_intelligence__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_9'] = x_compute_budget_intelligence__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_10'] = x_compute_budget_intelligence__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_11'] = x_compute_budget_intelligence__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_12'] = x_compute_budget_intelligence__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_13'] = x_compute_budget_intelligence__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_14'] = x_compute_budget_intelligence__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_15'] = x_compute_budget_intelligence__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_16'] = x_compute_budget_intelligence__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_17'] = x_compute_budget_intelligence__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_18'] = x_compute_budget_intelligence__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_19'] = x_compute_budget_intelligence__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_20'] = x_compute_budget_intelligence__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_21'] = x_compute_budget_intelligence__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_22'] = x_compute_budget_intelligence__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_23'] = x_compute_budget_intelligence__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_24'] = x_compute_budget_intelligence__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_25'] = x_compute_budget_intelligence__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_26'] = x_compute_budget_intelligence__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_27'] = x_compute_budget_intelligence__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_28'] = x_compute_budget_intelligence__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_29'] = x_compute_budget_intelligence__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_30'] = x_compute_budget_intelligence__mutmut_30 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_31'] = x_compute_budget_intelligence__mutmut_31 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_32'] = x_compute_budget_intelligence__mutmut_32 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_33'] = x_compute_budget_intelligence__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_34'] = x_compute_budget_intelligence__mutmut_34 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_35'] = x_compute_budget_intelligence__mutmut_35 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_36'] = x_compute_budget_intelligence__mutmut_36 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_37'] = x_compute_budget_intelligence__mutmut_37 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_38'] = x_compute_budget_intelligence__mutmut_38 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_39'] = x_compute_budget_intelligence__mutmut_39 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_40'] = x_compute_budget_intelligence__mutmut_40 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_41'] = x_compute_budget_intelligence__mutmut_41 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_42'] = x_compute_budget_intelligence__mutmut_42 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_43'] = x_compute_budget_intelligence__mutmut_43 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_44'] = x_compute_budget_intelligence__mutmut_44 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_45'] = x_compute_budget_intelligence__mutmut_45 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_46'] = x_compute_budget_intelligence__mutmut_46 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_47'] = x_compute_budget_intelligence__mutmut_47 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_48'] = x_compute_budget_intelligence__mutmut_48 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_49'] = x_compute_budget_intelligence__mutmut_49 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_50'] = x_compute_budget_intelligence__mutmut_50 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_51'] = x_compute_budget_intelligence__mutmut_51 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_52'] = x_compute_budget_intelligence__mutmut_52 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_53'] = x_compute_budget_intelligence__mutmut_53 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_54'] = x_compute_budget_intelligence__mutmut_54 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_55'] = x_compute_budget_intelligence__mutmut_55 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_56'] = x_compute_budget_intelligence__mutmut_56 # type: ignore # mutmut generated
mutants_x_compute_budget_intelligence__mutmut['x_compute_budget_intelligence__mutmut_57'] = x_compute_budget_intelligence__mutmut_57 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_recommendations__mutmut)
def _build_recommendations(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_orig(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_1(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_2(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action=None,
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_3(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description=None,
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_4(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_5(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_6(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="XXVerifier les workloads les plus couteuxXX",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_7(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_8(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="VERIFIER LES WORKLOADS LES PLUS COUTEUX",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_9(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="XXIdentifier les services consommant le plus de ressources.XX",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_10(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_11(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="IDENTIFIER LES SERVICES CONSOMMANT LE PLUS DE RESSOURCES.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_12(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action=None,
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_13(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description=None,
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_14(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_15(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_16(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="XXOptimiser les limites CPUXX",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_17(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="optimiser les limites cpu",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_18(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="OPTIMISER LES LIMITES CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_19(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="XXReduire les requests/limits sur-contraintes sans impact.XX",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_20(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_21(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="REDUIRE LES REQUESTS/LIMITS SUR-CONTRAINTES SANS IMPACT.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_22(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action=None,
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_23(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            description=None,
        ),
    ]


def x__build_recommendations__mutmut_24(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_25(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="Reporter les traitements non critiques",
            ),
    ]


def x__build_recommendations__mutmut_26(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="XXReporter les traitements non critiquesXX",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_27(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="reporter les traitements non critiques",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]


def x__build_recommendations__mutmut_28(exceeded: bool, overshoot_pct: float) -> list[BudgetAlertRecommendation]:
    if not exceeded:
        return []
    return [
        BudgetAlertRecommendation(
            action="Verifier les workloads les plus couteux",
            description="Identifier les services consommant le plus de ressources.",
        ),
        BudgetAlertRecommendation(
            action="Optimiser les limites CPU",
            description="Reduire les requests/limits sur-contraintes sans impact.",
        ),
        BudgetAlertRecommendation(
            action="REPORTER LES TRAITEMENTS NON CRITIQUES",
            description=f"Decaler les batch jobs hors pic (+{overshoot_pct}% projete).",
        ),
    ]

mutants_x__build_recommendations__mutmut['_mutmut_orig'] = x__build_recommendations__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_1'] = x__build_recommendations__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_2'] = x__build_recommendations__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_3'] = x__build_recommendations__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_4'] = x__build_recommendations__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_5'] = x__build_recommendations__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_6'] = x__build_recommendations__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_7'] = x__build_recommendations__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_8'] = x__build_recommendations__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_9'] = x__build_recommendations__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_10'] = x__build_recommendations__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_11'] = x__build_recommendations__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_12'] = x__build_recommendations__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_13'] = x__build_recommendations__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_14'] = x__build_recommendations__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_15'] = x__build_recommendations__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_16'] = x__build_recommendations__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_17'] = x__build_recommendations__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_18'] = x__build_recommendations__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_19'] = x__build_recommendations__mutmut_19 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_20'] = x__build_recommendations__mutmut_20 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_21'] = x__build_recommendations__mutmut_21 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_22'] = x__build_recommendations__mutmut_22 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_23'] = x__build_recommendations__mutmut_23 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_24'] = x__build_recommendations__mutmut_24 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_25'] = x__build_recommendations__mutmut_25 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_26'] = x__build_recommendations__mutmut_26 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_27'] = x__build_recommendations__mutmut_27 # type: ignore # mutmut generated
mutants_x__build_recommendations__mutmut['x__build_recommendations__mutmut_28'] = x__build_recommendations__mutmut_28 # type: ignore # mutmut generated
