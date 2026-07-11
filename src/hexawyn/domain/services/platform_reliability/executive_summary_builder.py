from __future__ import annotations

from hexawyn.domain.models.platform_reliability import IncidentSummary


def build_summary(
    uptime_pct: float,
    incidents: list[IncidentSummary],
    avg_resolution_minutes: int,
    resolution_delta_pct: float,
    resolution_trend: str,
    financial_impact_eur: float | None,
    pricing_configured: bool,
) -> str:
    """Build a deterministic, jargon-free executive summary (<= 5 sentences).

    Business language only — no Kubernetes terms. When a major incident
    occurred it is highlighted with its date and root cause. A financial figure
    is included only when pricing is configured, never fabricated.
    """
    if not incidents:
        return "Plateforme stable. Aucun incident ce mois."

    sentences = [_availability_sentence(uptime_pct, incidents)]
    major = _first_major(incidents)
    if major is not None:
        sentences.append(_major_sentence(major))
    sentences.append(
        _resolution_sentence(avg_resolution_minutes, resolution_delta_pct, resolution_trend)
    )
    if pricing_configured and financial_impact_eur is not None:
        sentences.append(_financial_sentence(financial_impact_eur))
    return " ".join(sentences)


def _availability_sentence(uptime_pct: float, incidents: list[IncidentSummary]) -> str:
    count = len(incidents)
    label = _severity_label(incidents)
    plural = "s" if count > 1 else ""
    uptime_text = f"{uptime_pct:.2f}".replace(".", ",")
    return f"{uptime_text}% de disponibilite, avec {count} incident{plural} {label} resolu{plural}."


def _major_sentence(major: IncidentSummary) -> str:
    cause = major.root_cause or "cause en cours d'analyse"
    hours = round(major.downtime_minutes / 60, 1)
    hours_text = f"{hours:.1f}".replace(".", ",")
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def _resolution_sentence(avg_minutes: int, delta_pct: float, trend: str) -> str:
    if trend == "stable":
        return f"Temps de resolution moyen : {avg_minutes} min."
    direction = "-" if delta_pct < 0 else "+"
    return (
        f"Temps de resolution moyen : {avg_minutes} min "
        f"({direction}{abs(round(delta_pct))}% vs mois dernier)."
    )


def _financial_sentence(financial_impact_eur: float) -> str:
    amount = f"{financial_impact_eur:.0f}".replace(".", ",")
    return f"Cout estime des interventions : {amount}\u20ac."


def _first_major(incidents: list[IncidentSummary]) -> IncidentSummary | None:
    for incident in incidents:
        if incident.severity == "major":
            return incident
    return None


def _severity_label(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "major" for incident in incidents):
        return "majeur" + ("s" if len(incidents) > 1 else "")
    return "mineur" + ("s" if len(incidents) > 1 else "")
