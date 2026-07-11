from __future__ import annotations

from hexawyn.application.ports.driven.budget_intelligence_port import (
    BudgetIntelligenceData,
)
from hexawyn.domain.models.budget_intelligence import (
    BudgetAlertRecommendation,
    BudgetIntelligenceReport,
)


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
