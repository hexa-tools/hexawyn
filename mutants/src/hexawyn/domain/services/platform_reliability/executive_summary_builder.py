from __future__ import annotations

from hexawyn.domain.models.platform_reliability import IncidentSummary


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_summary__mutmut)
def build_summary(  # noqa: PLR0913
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


def x_build_summary__mutmut_orig(  # noqa: PLR0913
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


def x_build_summary__mutmut_1(  # noqa: PLR0913
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
    if incidents:
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


def x_build_summary__mutmut_2(  # noqa: PLR0913
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
        return "XXPlateforme stable. Aucun incident ce mois.XX"

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


def x_build_summary__mutmut_3(  # noqa: PLR0913
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
        return "plateforme stable. aucun incident ce mois."

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


def x_build_summary__mutmut_4(  # noqa: PLR0913
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
        return "PLATEFORME STABLE. AUCUN INCIDENT CE MOIS."

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


def x_build_summary__mutmut_5(  # noqa: PLR0913
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

    sentences = None
    major = _first_major(incidents)
    if major is not None:
        sentences.append(_major_sentence(major))
    sentences.append(
        _resolution_sentence(avg_resolution_minutes, resolution_delta_pct, resolution_trend)
    )
    if pricing_configured and financial_impact_eur is not None:
        sentences.append(_financial_sentence(financial_impact_eur))
    return " ".join(sentences)


def x_build_summary__mutmut_6(  # noqa: PLR0913
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

    sentences = [_availability_sentence(None, incidents)]
    major = _first_major(incidents)
    if major is not None:
        sentences.append(_major_sentence(major))
    sentences.append(
        _resolution_sentence(avg_resolution_minutes, resolution_delta_pct, resolution_trend)
    )
    if pricing_configured and financial_impact_eur is not None:
        sentences.append(_financial_sentence(financial_impact_eur))
    return " ".join(sentences)


def x_build_summary__mutmut_7(  # noqa: PLR0913
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

    sentences = [_availability_sentence(uptime_pct, None)]
    major = _first_major(incidents)
    if major is not None:
        sentences.append(_major_sentence(major))
    sentences.append(
        _resolution_sentence(avg_resolution_minutes, resolution_delta_pct, resolution_trend)
    )
    if pricing_configured and financial_impact_eur is not None:
        sentences.append(_financial_sentence(financial_impact_eur))
    return " ".join(sentences)


def x_build_summary__mutmut_8(  # noqa: PLR0913
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

    sentences = [_availability_sentence(incidents)]
    major = _first_major(incidents)
    if major is not None:
        sentences.append(_major_sentence(major))
    sentences.append(
        _resolution_sentence(avg_resolution_minutes, resolution_delta_pct, resolution_trend)
    )
    if pricing_configured and financial_impact_eur is not None:
        sentences.append(_financial_sentence(financial_impact_eur))
    return " ".join(sentences)


def x_build_summary__mutmut_9(  # noqa: PLR0913
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

    sentences = [_availability_sentence(uptime_pct, )]
    major = _first_major(incidents)
    if major is not None:
        sentences.append(_major_sentence(major))
    sentences.append(
        _resolution_sentence(avg_resolution_minutes, resolution_delta_pct, resolution_trend)
    )
    if pricing_configured and financial_impact_eur is not None:
        sentences.append(_financial_sentence(financial_impact_eur))
    return " ".join(sentences)


def x_build_summary__mutmut_10(  # noqa: PLR0913
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
    major = None
    if major is not None:
        sentences.append(_major_sentence(major))
    sentences.append(
        _resolution_sentence(avg_resolution_minutes, resolution_delta_pct, resolution_trend)
    )
    if pricing_configured and financial_impact_eur is not None:
        sentences.append(_financial_sentence(financial_impact_eur))
    return " ".join(sentences)


def x_build_summary__mutmut_11(  # noqa: PLR0913
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
    major = _first_major(None)
    if major is not None:
        sentences.append(_major_sentence(major))
    sentences.append(
        _resolution_sentence(avg_resolution_minutes, resolution_delta_pct, resolution_trend)
    )
    if pricing_configured and financial_impact_eur is not None:
        sentences.append(_financial_sentence(financial_impact_eur))
    return " ".join(sentences)


def x_build_summary__mutmut_12(  # noqa: PLR0913
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
    if major is None:
        sentences.append(_major_sentence(major))
    sentences.append(
        _resolution_sentence(avg_resolution_minutes, resolution_delta_pct, resolution_trend)
    )
    if pricing_configured and financial_impact_eur is not None:
        sentences.append(_financial_sentence(financial_impact_eur))
    return " ".join(sentences)


def x_build_summary__mutmut_13(  # noqa: PLR0913
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
        sentences.append(None)
    sentences.append(
        _resolution_sentence(avg_resolution_minutes, resolution_delta_pct, resolution_trend)
    )
    if pricing_configured and financial_impact_eur is not None:
        sentences.append(_financial_sentence(financial_impact_eur))
    return " ".join(sentences)


def x_build_summary__mutmut_14(  # noqa: PLR0913
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
        sentences.append(_major_sentence(None))
    sentences.append(
        _resolution_sentence(avg_resolution_minutes, resolution_delta_pct, resolution_trend)
    )
    if pricing_configured and financial_impact_eur is not None:
        sentences.append(_financial_sentence(financial_impact_eur))
    return " ".join(sentences)


def x_build_summary__mutmut_15(  # noqa: PLR0913
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
        None
    )
    if pricing_configured and financial_impact_eur is not None:
        sentences.append(_financial_sentence(financial_impact_eur))
    return " ".join(sentences)


def x_build_summary__mutmut_16(  # noqa: PLR0913
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
        _resolution_sentence(None, resolution_delta_pct, resolution_trend)
    )
    if pricing_configured and financial_impact_eur is not None:
        sentences.append(_financial_sentence(financial_impact_eur))
    return " ".join(sentences)


def x_build_summary__mutmut_17(  # noqa: PLR0913
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
        _resolution_sentence(avg_resolution_minutes, None, resolution_trend)
    )
    if pricing_configured and financial_impact_eur is not None:
        sentences.append(_financial_sentence(financial_impact_eur))
    return " ".join(sentences)


def x_build_summary__mutmut_18(  # noqa: PLR0913
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
        _resolution_sentence(avg_resolution_minutes, resolution_delta_pct, None)
    )
    if pricing_configured and financial_impact_eur is not None:
        sentences.append(_financial_sentence(financial_impact_eur))
    return " ".join(sentences)


def x_build_summary__mutmut_19(  # noqa: PLR0913
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
        _resolution_sentence(resolution_delta_pct, resolution_trend)
    )
    if pricing_configured and financial_impact_eur is not None:
        sentences.append(_financial_sentence(financial_impact_eur))
    return " ".join(sentences)


def x_build_summary__mutmut_20(  # noqa: PLR0913
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
        _resolution_sentence(avg_resolution_minutes, resolution_trend)
    )
    if pricing_configured and financial_impact_eur is not None:
        sentences.append(_financial_sentence(financial_impact_eur))
    return " ".join(sentences)


def x_build_summary__mutmut_21(  # noqa: PLR0913
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
        _resolution_sentence(avg_resolution_minutes, resolution_delta_pct, )
    )
    if pricing_configured and financial_impact_eur is not None:
        sentences.append(_financial_sentence(financial_impact_eur))
    return " ".join(sentences)


def x_build_summary__mutmut_22(  # noqa: PLR0913
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
    if pricing_configured or financial_impact_eur is not None:
        sentences.append(_financial_sentence(financial_impact_eur))
    return " ".join(sentences)


def x_build_summary__mutmut_23(  # noqa: PLR0913
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
    if pricing_configured and financial_impact_eur is None:
        sentences.append(_financial_sentence(financial_impact_eur))
    return " ".join(sentences)


def x_build_summary__mutmut_24(  # noqa: PLR0913
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
        sentences.append(None)
    return " ".join(sentences)


def x_build_summary__mutmut_25(  # noqa: PLR0913
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
        sentences.append(_financial_sentence(None))
    return " ".join(sentences)


def x_build_summary__mutmut_26(  # noqa: PLR0913
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
    return " ".join(None)


def x_build_summary__mutmut_27(  # noqa: PLR0913
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
    return "XX XX".join(sentences)

mutants_x_build_summary__mutmut['_mutmut_orig'] = x_build_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_1'] = x_build_summary__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_2'] = x_build_summary__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_3'] = x_build_summary__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_4'] = x_build_summary__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_5'] = x_build_summary__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_6'] = x_build_summary__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_7'] = x_build_summary__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_8'] = x_build_summary__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_9'] = x_build_summary__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_10'] = x_build_summary__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_11'] = x_build_summary__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_12'] = x_build_summary__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_13'] = x_build_summary__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_14'] = x_build_summary__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_15'] = x_build_summary__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_16'] = x_build_summary__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_17'] = x_build_summary__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_18'] = x_build_summary__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_19'] = x_build_summary__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_20'] = x_build_summary__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_21'] = x_build_summary__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_22'] = x_build_summary__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_23'] = x_build_summary__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_24'] = x_build_summary__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_25'] = x_build_summary__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_26'] = x_build_summary__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_summary__mutmut['x_build_summary__mutmut_27'] = x_build_summary__mutmut_27 # type: ignore # mutmut generated
mutants_x__availability_sentence__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__availability_sentence__mutmut)
def _availability_sentence(uptime_pct: float, incidents: list[IncidentSummary]) -> str:
    count = len(incidents)
    label = _severity_label(incidents)
    plural = "s" if count > 1 else ""
    uptime_text = f"{uptime_pct:.2f}".replace(".", ",")
    return f"{uptime_text}% de disponibilite, avec {count} incident{plural} {label} resolu{plural}."


def x__availability_sentence__mutmut_orig(uptime_pct: float, incidents: list[IncidentSummary]) -> str:
    count = len(incidents)
    label = _severity_label(incidents)
    plural = "s" if count > 1 else ""
    uptime_text = f"{uptime_pct:.2f}".replace(".", ",")
    return f"{uptime_text}% de disponibilite, avec {count} incident{plural} {label} resolu{plural}."


def x__availability_sentence__mutmut_1(uptime_pct: float, incidents: list[IncidentSummary]) -> str:
    count = None
    label = _severity_label(incidents)
    plural = "s" if count > 1 else ""
    uptime_text = f"{uptime_pct:.2f}".replace(".", ",")
    return f"{uptime_text}% de disponibilite, avec {count} incident{plural} {label} resolu{plural}."


def x__availability_sentence__mutmut_2(uptime_pct: float, incidents: list[IncidentSummary]) -> str:
    count = len(incidents)
    label = None
    plural = "s" if count > 1 else ""
    uptime_text = f"{uptime_pct:.2f}".replace(".", ",")
    return f"{uptime_text}% de disponibilite, avec {count} incident{plural} {label} resolu{plural}."


def x__availability_sentence__mutmut_3(uptime_pct: float, incidents: list[IncidentSummary]) -> str:
    count = len(incidents)
    label = _severity_label(None)
    plural = "s" if count > 1 else ""
    uptime_text = f"{uptime_pct:.2f}".replace(".", ",")
    return f"{uptime_text}% de disponibilite, avec {count} incident{plural} {label} resolu{plural}."


def x__availability_sentence__mutmut_4(uptime_pct: float, incidents: list[IncidentSummary]) -> str:
    count = len(incidents)
    label = _severity_label(incidents)
    plural = None
    uptime_text = f"{uptime_pct:.2f}".replace(".", ",")
    return f"{uptime_text}% de disponibilite, avec {count} incident{plural} {label} resolu{plural}."


def x__availability_sentence__mutmut_5(uptime_pct: float, incidents: list[IncidentSummary]) -> str:
    count = len(incidents)
    label = _severity_label(incidents)
    plural = "XXsXX" if count > 1 else ""
    uptime_text = f"{uptime_pct:.2f}".replace(".", ",")
    return f"{uptime_text}% de disponibilite, avec {count} incident{plural} {label} resolu{plural}."


def x__availability_sentence__mutmut_6(uptime_pct: float, incidents: list[IncidentSummary]) -> str:
    count = len(incidents)
    label = _severity_label(incidents)
    plural = "S" if count > 1 else ""
    uptime_text = f"{uptime_pct:.2f}".replace(".", ",")
    return f"{uptime_text}% de disponibilite, avec {count} incident{plural} {label} resolu{plural}."


def x__availability_sentence__mutmut_7(uptime_pct: float, incidents: list[IncidentSummary]) -> str:
    count = len(incidents)
    label = _severity_label(incidents)
    plural = "s" if count >= 1 else ""
    uptime_text = f"{uptime_pct:.2f}".replace(".", ",")
    return f"{uptime_text}% de disponibilite, avec {count} incident{plural} {label} resolu{plural}."


def x__availability_sentence__mutmut_8(uptime_pct: float, incidents: list[IncidentSummary]) -> str:
    count = len(incidents)
    label = _severity_label(incidents)
    plural = "s" if count > 2 else ""
    uptime_text = f"{uptime_pct:.2f}".replace(".", ",")
    return f"{uptime_text}% de disponibilite, avec {count} incident{plural} {label} resolu{plural}."


def x__availability_sentence__mutmut_9(uptime_pct: float, incidents: list[IncidentSummary]) -> str:
    count = len(incidents)
    label = _severity_label(incidents)
    plural = "s" if count > 1 else "XXXX"
    uptime_text = f"{uptime_pct:.2f}".replace(".", ",")
    return f"{uptime_text}% de disponibilite, avec {count} incident{plural} {label} resolu{plural}."


def x__availability_sentence__mutmut_10(uptime_pct: float, incidents: list[IncidentSummary]) -> str:
    count = len(incidents)
    label = _severity_label(incidents)
    plural = "s" if count > 1 else ""
    uptime_text = None
    return f"{uptime_text}% de disponibilite, avec {count} incident{plural} {label} resolu{plural}."


def x__availability_sentence__mutmut_11(uptime_pct: float, incidents: list[IncidentSummary]) -> str:
    count = len(incidents)
    label = _severity_label(incidents)
    plural = "s" if count > 1 else ""
    uptime_text = f"{uptime_pct:.2f}".replace(None, ",")
    return f"{uptime_text}% de disponibilite, avec {count} incident{plural} {label} resolu{plural}."


def x__availability_sentence__mutmut_12(uptime_pct: float, incidents: list[IncidentSummary]) -> str:
    count = len(incidents)
    label = _severity_label(incidents)
    plural = "s" if count > 1 else ""
    uptime_text = f"{uptime_pct:.2f}".replace(".", None)
    return f"{uptime_text}% de disponibilite, avec {count} incident{plural} {label} resolu{plural}."


def x__availability_sentence__mutmut_13(uptime_pct: float, incidents: list[IncidentSummary]) -> str:
    count = len(incidents)
    label = _severity_label(incidents)
    plural = "s" if count > 1 else ""
    uptime_text = f"{uptime_pct:.2f}".replace(",")
    return f"{uptime_text}% de disponibilite, avec {count} incident{plural} {label} resolu{plural}."


def x__availability_sentence__mutmut_14(uptime_pct: float, incidents: list[IncidentSummary]) -> str:
    count = len(incidents)
    label = _severity_label(incidents)
    plural = "s" if count > 1 else ""
    uptime_text = f"{uptime_pct:.2f}".replace(".", )
    return f"{uptime_text}% de disponibilite, avec {count} incident{plural} {label} resolu{plural}."


def x__availability_sentence__mutmut_15(uptime_pct: float, incidents: list[IncidentSummary]) -> str:
    count = len(incidents)
    label = _severity_label(incidents)
    plural = "s" if count > 1 else ""
    uptime_text = f"{uptime_pct:.2f}".replace("XX.XX", ",")
    return f"{uptime_text}% de disponibilite, avec {count} incident{plural} {label} resolu{plural}."


def x__availability_sentence__mutmut_16(uptime_pct: float, incidents: list[IncidentSummary]) -> str:
    count = len(incidents)
    label = _severity_label(incidents)
    plural = "s" if count > 1 else ""
    uptime_text = f"{uptime_pct:.2f}".replace(".", "XX,XX")
    return f"{uptime_text}% de disponibilite, avec {count} incident{plural} {label} resolu{plural}."

mutants_x__availability_sentence__mutmut['_mutmut_orig'] = x__availability_sentence__mutmut_orig # type: ignore # mutmut generated
mutants_x__availability_sentence__mutmut['x__availability_sentence__mutmut_1'] = x__availability_sentence__mutmut_1 # type: ignore # mutmut generated
mutants_x__availability_sentence__mutmut['x__availability_sentence__mutmut_2'] = x__availability_sentence__mutmut_2 # type: ignore # mutmut generated
mutants_x__availability_sentence__mutmut['x__availability_sentence__mutmut_3'] = x__availability_sentence__mutmut_3 # type: ignore # mutmut generated
mutants_x__availability_sentence__mutmut['x__availability_sentence__mutmut_4'] = x__availability_sentence__mutmut_4 # type: ignore # mutmut generated
mutants_x__availability_sentence__mutmut['x__availability_sentence__mutmut_5'] = x__availability_sentence__mutmut_5 # type: ignore # mutmut generated
mutants_x__availability_sentence__mutmut['x__availability_sentence__mutmut_6'] = x__availability_sentence__mutmut_6 # type: ignore # mutmut generated
mutants_x__availability_sentence__mutmut['x__availability_sentence__mutmut_7'] = x__availability_sentence__mutmut_7 # type: ignore # mutmut generated
mutants_x__availability_sentence__mutmut['x__availability_sentence__mutmut_8'] = x__availability_sentence__mutmut_8 # type: ignore # mutmut generated
mutants_x__availability_sentence__mutmut['x__availability_sentence__mutmut_9'] = x__availability_sentence__mutmut_9 # type: ignore # mutmut generated
mutants_x__availability_sentence__mutmut['x__availability_sentence__mutmut_10'] = x__availability_sentence__mutmut_10 # type: ignore # mutmut generated
mutants_x__availability_sentence__mutmut['x__availability_sentence__mutmut_11'] = x__availability_sentence__mutmut_11 # type: ignore # mutmut generated
mutants_x__availability_sentence__mutmut['x__availability_sentence__mutmut_12'] = x__availability_sentence__mutmut_12 # type: ignore # mutmut generated
mutants_x__availability_sentence__mutmut['x__availability_sentence__mutmut_13'] = x__availability_sentence__mutmut_13 # type: ignore # mutmut generated
mutants_x__availability_sentence__mutmut['x__availability_sentence__mutmut_14'] = x__availability_sentence__mutmut_14 # type: ignore # mutmut generated
mutants_x__availability_sentence__mutmut['x__availability_sentence__mutmut_15'] = x__availability_sentence__mutmut_15 # type: ignore # mutmut generated
mutants_x__availability_sentence__mutmut['x__availability_sentence__mutmut_16'] = x__availability_sentence__mutmut_16 # type: ignore # mutmut generated
mutants_x__major_sentence__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__major_sentence__mutmut)
def _major_sentence(major: IncidentSummary) -> str:
    cause = major.root_cause or "cause en cours d'analyse"
    hours = round(major.downtime_minutes / 60, 1)
    hours_text = f"{hours:.1f}".replace(".", ",")
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def x__major_sentence__mutmut_orig(major: IncidentSummary) -> str:
    cause = major.root_cause or "cause en cours d'analyse"
    hours = round(major.downtime_minutes / 60, 1)
    hours_text = f"{hours:.1f}".replace(".", ",")
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def x__major_sentence__mutmut_1(major: IncidentSummary) -> str:
    cause = None
    hours = round(major.downtime_minutes / 60, 1)
    hours_text = f"{hours:.1f}".replace(".", ",")
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def x__major_sentence__mutmut_2(major: IncidentSummary) -> str:
    cause = major.root_cause and "cause en cours d'analyse"
    hours = round(major.downtime_minutes / 60, 1)
    hours_text = f"{hours:.1f}".replace(".", ",")
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def x__major_sentence__mutmut_3(major: IncidentSummary) -> str:
    cause = major.root_cause or "XXcause en cours d'analyseXX"
    hours = round(major.downtime_minutes / 60, 1)
    hours_text = f"{hours:.1f}".replace(".", ",")
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def x__major_sentence__mutmut_4(major: IncidentSummary) -> str:
    cause = major.root_cause or "CAUSE EN COURS D'ANALYSE"
    hours = round(major.downtime_minutes / 60, 1)
    hours_text = f"{hours:.1f}".replace(".", ",")
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def x__major_sentence__mutmut_5(major: IncidentSummary) -> str:
    cause = major.root_cause or "cause en cours d'analyse"
    hours = None
    hours_text = f"{hours:.1f}".replace(".", ",")
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def x__major_sentence__mutmut_6(major: IncidentSummary) -> str:
    cause = major.root_cause or "cause en cours d'analyse"
    hours = round(None, 1)
    hours_text = f"{hours:.1f}".replace(".", ",")
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def x__major_sentence__mutmut_7(major: IncidentSummary) -> str:
    cause = major.root_cause or "cause en cours d'analyse"
    hours = round(major.downtime_minutes / 60, None)
    hours_text = f"{hours:.1f}".replace(".", ",")
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def x__major_sentence__mutmut_8(major: IncidentSummary) -> str:
    cause = major.root_cause or "cause en cours d'analyse"
    hours = round(1)
    hours_text = f"{hours:.1f}".replace(".", ",")
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def x__major_sentence__mutmut_9(major: IncidentSummary) -> str:
    cause = major.root_cause or "cause en cours d'analyse"
    hours = round(major.downtime_minutes / 60, )
    hours_text = f"{hours:.1f}".replace(".", ",")
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def x__major_sentence__mutmut_10(major: IncidentSummary) -> str:
    cause = major.root_cause or "cause en cours d'analyse"
    hours = round(major.downtime_minutes * 60, 1)
    hours_text = f"{hours:.1f}".replace(".", ",")
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def x__major_sentence__mutmut_11(major: IncidentSummary) -> str:
    cause = major.root_cause or "cause en cours d'analyse"
    hours = round(major.downtime_minutes / 61, 1)
    hours_text = f"{hours:.1f}".replace(".", ",")
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def x__major_sentence__mutmut_12(major: IncidentSummary) -> str:
    cause = major.root_cause or "cause en cours d'analyse"
    hours = round(major.downtime_minutes / 60, 2)
    hours_text = f"{hours:.1f}".replace(".", ",")
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def x__major_sentence__mutmut_13(major: IncidentSummary) -> str:
    cause = major.root_cause or "cause en cours d'analyse"
    hours = round(major.downtime_minutes / 60, 1)
    hours_text = None
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def x__major_sentence__mutmut_14(major: IncidentSummary) -> str:
    cause = major.root_cause or "cause en cours d'analyse"
    hours = round(major.downtime_minutes / 60, 1)
    hours_text = f"{hours:.1f}".replace(None, ",")
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def x__major_sentence__mutmut_15(major: IncidentSummary) -> str:
    cause = major.root_cause or "cause en cours d'analyse"
    hours = round(major.downtime_minutes / 60, 1)
    hours_text = f"{hours:.1f}".replace(".", None)
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def x__major_sentence__mutmut_16(major: IncidentSummary) -> str:
    cause = major.root_cause or "cause en cours d'analyse"
    hours = round(major.downtime_minutes / 60, 1)
    hours_text = f"{hours:.1f}".replace(",")
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def x__major_sentence__mutmut_17(major: IncidentSummary) -> str:
    cause = major.root_cause or "cause en cours d'analyse"
    hours = round(major.downtime_minutes / 60, 1)
    hours_text = f"{hours:.1f}".replace(".", )
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def x__major_sentence__mutmut_18(major: IncidentSummary) -> str:
    cause = major.root_cause or "cause en cours d'analyse"
    hours = round(major.downtime_minutes / 60, 1)
    hours_text = f"{hours:.1f}".replace("XX.XX", ",")
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )


def x__major_sentence__mutmut_19(major: IncidentSummary) -> str:
    cause = major.root_cause or "cause en cours d'analyse"
    hours = round(major.downtime_minutes / 60, 1)
    hours_text = f"{hours:.1f}".replace(".", "XX,XX")
    return (
        f"Incident critique le {major.date} : {hours_text}h d'indisponibilite. "
        f"Cause racine : {cause}. Corrige."
    )

mutants_x__major_sentence__mutmut['_mutmut_orig'] = x__major_sentence__mutmut_orig # type: ignore # mutmut generated
mutants_x__major_sentence__mutmut['x__major_sentence__mutmut_1'] = x__major_sentence__mutmut_1 # type: ignore # mutmut generated
mutants_x__major_sentence__mutmut['x__major_sentence__mutmut_2'] = x__major_sentence__mutmut_2 # type: ignore # mutmut generated
mutants_x__major_sentence__mutmut['x__major_sentence__mutmut_3'] = x__major_sentence__mutmut_3 # type: ignore # mutmut generated
mutants_x__major_sentence__mutmut['x__major_sentence__mutmut_4'] = x__major_sentence__mutmut_4 # type: ignore # mutmut generated
mutants_x__major_sentence__mutmut['x__major_sentence__mutmut_5'] = x__major_sentence__mutmut_5 # type: ignore # mutmut generated
mutants_x__major_sentence__mutmut['x__major_sentence__mutmut_6'] = x__major_sentence__mutmut_6 # type: ignore # mutmut generated
mutants_x__major_sentence__mutmut['x__major_sentence__mutmut_7'] = x__major_sentence__mutmut_7 # type: ignore # mutmut generated
mutants_x__major_sentence__mutmut['x__major_sentence__mutmut_8'] = x__major_sentence__mutmut_8 # type: ignore # mutmut generated
mutants_x__major_sentence__mutmut['x__major_sentence__mutmut_9'] = x__major_sentence__mutmut_9 # type: ignore # mutmut generated
mutants_x__major_sentence__mutmut['x__major_sentence__mutmut_10'] = x__major_sentence__mutmut_10 # type: ignore # mutmut generated
mutants_x__major_sentence__mutmut['x__major_sentence__mutmut_11'] = x__major_sentence__mutmut_11 # type: ignore # mutmut generated
mutants_x__major_sentence__mutmut['x__major_sentence__mutmut_12'] = x__major_sentence__mutmut_12 # type: ignore # mutmut generated
mutants_x__major_sentence__mutmut['x__major_sentence__mutmut_13'] = x__major_sentence__mutmut_13 # type: ignore # mutmut generated
mutants_x__major_sentence__mutmut['x__major_sentence__mutmut_14'] = x__major_sentence__mutmut_14 # type: ignore # mutmut generated
mutants_x__major_sentence__mutmut['x__major_sentence__mutmut_15'] = x__major_sentence__mutmut_15 # type: ignore # mutmut generated
mutants_x__major_sentence__mutmut['x__major_sentence__mutmut_16'] = x__major_sentence__mutmut_16 # type: ignore # mutmut generated
mutants_x__major_sentence__mutmut['x__major_sentence__mutmut_17'] = x__major_sentence__mutmut_17 # type: ignore # mutmut generated
mutants_x__major_sentence__mutmut['x__major_sentence__mutmut_18'] = x__major_sentence__mutmut_18 # type: ignore # mutmut generated
mutants_x__major_sentence__mutmut['x__major_sentence__mutmut_19'] = x__major_sentence__mutmut_19 # type: ignore # mutmut generated
mutants_x__resolution_sentence__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__resolution_sentence__mutmut)
def _resolution_sentence(avg_minutes: int, delta_pct: float, trend: str) -> str:
    if trend == "stable":
        return f"Temps de resolution moyen : {avg_minutes} min."
    direction = "-" if delta_pct < 0 else "+"
    return (
        f"Temps de resolution moyen : {avg_minutes} min "
        f"({direction}{abs(round(delta_pct))}% vs mois dernier)."
    )


def x__resolution_sentence__mutmut_orig(avg_minutes: int, delta_pct: float, trend: str) -> str:
    if trend == "stable":
        return f"Temps de resolution moyen : {avg_minutes} min."
    direction = "-" if delta_pct < 0 else "+"
    return (
        f"Temps de resolution moyen : {avg_minutes} min "
        f"({direction}{abs(round(delta_pct))}% vs mois dernier)."
    )


def x__resolution_sentence__mutmut_1(avg_minutes: int, delta_pct: float, trend: str) -> str:
    if trend != "stable":
        return f"Temps de resolution moyen : {avg_minutes} min."
    direction = "-" if delta_pct < 0 else "+"
    return (
        f"Temps de resolution moyen : {avg_minutes} min "
        f"({direction}{abs(round(delta_pct))}% vs mois dernier)."
    )


def x__resolution_sentence__mutmut_2(avg_minutes: int, delta_pct: float, trend: str) -> str:
    if trend == "XXstableXX":
        return f"Temps de resolution moyen : {avg_minutes} min."
    direction = "-" if delta_pct < 0 else "+"
    return (
        f"Temps de resolution moyen : {avg_minutes} min "
        f"({direction}{abs(round(delta_pct))}% vs mois dernier)."
    )


def x__resolution_sentence__mutmut_3(avg_minutes: int, delta_pct: float, trend: str) -> str:
    if trend == "STABLE":
        return f"Temps de resolution moyen : {avg_minutes} min."
    direction = "-" if delta_pct < 0 else "+"
    return (
        f"Temps de resolution moyen : {avg_minutes} min "
        f"({direction}{abs(round(delta_pct))}% vs mois dernier)."
    )


def x__resolution_sentence__mutmut_4(avg_minutes: int, delta_pct: float, trend: str) -> str:
    if trend == "stable":
        return f"Temps de resolution moyen : {avg_minutes} min."
    direction = None
    return (
        f"Temps de resolution moyen : {avg_minutes} min "
        f"({direction}{abs(round(delta_pct))}% vs mois dernier)."
    )


def x__resolution_sentence__mutmut_5(avg_minutes: int, delta_pct: float, trend: str) -> str:
    if trend == "stable":
        return f"Temps de resolution moyen : {avg_minutes} min."
    direction = "XX-XX" if delta_pct < 0 else "+"
    return (
        f"Temps de resolution moyen : {avg_minutes} min "
        f"({direction}{abs(round(delta_pct))}% vs mois dernier)."
    )


def x__resolution_sentence__mutmut_6(avg_minutes: int, delta_pct: float, trend: str) -> str:
    if trend == "stable":
        return f"Temps de resolution moyen : {avg_minutes} min."
    direction = "-" if delta_pct <= 0 else "+"
    return (
        f"Temps de resolution moyen : {avg_minutes} min "
        f"({direction}{abs(round(delta_pct))}% vs mois dernier)."
    )


def x__resolution_sentence__mutmut_7(avg_minutes: int, delta_pct: float, trend: str) -> str:
    if trend == "stable":
        return f"Temps de resolution moyen : {avg_minutes} min."
    direction = "-" if delta_pct < 1 else "+"
    return (
        f"Temps de resolution moyen : {avg_minutes} min "
        f"({direction}{abs(round(delta_pct))}% vs mois dernier)."
    )


def x__resolution_sentence__mutmut_8(avg_minutes: int, delta_pct: float, trend: str) -> str:
    if trend == "stable":
        return f"Temps de resolution moyen : {avg_minutes} min."
    direction = "-" if delta_pct < 0 else "XX+XX"
    return (
        f"Temps de resolution moyen : {avg_minutes} min "
        f"({direction}{abs(round(delta_pct))}% vs mois dernier)."
    )


def x__resolution_sentence__mutmut_9(avg_minutes: int, delta_pct: float, trend: str) -> str:
    if trend == "stable":
        return f"Temps de resolution moyen : {avg_minutes} min."
    direction = "-" if delta_pct < 0 else "+"
    return (
        f"Temps de resolution moyen : {avg_minutes} min "
        f"({direction}{abs(None)}% vs mois dernier)."
    )


def x__resolution_sentence__mutmut_10(avg_minutes: int, delta_pct: float, trend: str) -> str:
    if trend == "stable":
        return f"Temps de resolution moyen : {avg_minutes} min."
    direction = "-" if delta_pct < 0 else "+"
    return (
        f"Temps de resolution moyen : {avg_minutes} min "
        f"({direction}{abs(round(None))}% vs mois dernier)."
    )

mutants_x__resolution_sentence__mutmut['_mutmut_orig'] = x__resolution_sentence__mutmut_orig # type: ignore # mutmut generated
mutants_x__resolution_sentence__mutmut['x__resolution_sentence__mutmut_1'] = x__resolution_sentence__mutmut_1 # type: ignore # mutmut generated
mutants_x__resolution_sentence__mutmut['x__resolution_sentence__mutmut_2'] = x__resolution_sentence__mutmut_2 # type: ignore # mutmut generated
mutants_x__resolution_sentence__mutmut['x__resolution_sentence__mutmut_3'] = x__resolution_sentence__mutmut_3 # type: ignore # mutmut generated
mutants_x__resolution_sentence__mutmut['x__resolution_sentence__mutmut_4'] = x__resolution_sentence__mutmut_4 # type: ignore # mutmut generated
mutants_x__resolution_sentence__mutmut['x__resolution_sentence__mutmut_5'] = x__resolution_sentence__mutmut_5 # type: ignore # mutmut generated
mutants_x__resolution_sentence__mutmut['x__resolution_sentence__mutmut_6'] = x__resolution_sentence__mutmut_6 # type: ignore # mutmut generated
mutants_x__resolution_sentence__mutmut['x__resolution_sentence__mutmut_7'] = x__resolution_sentence__mutmut_7 # type: ignore # mutmut generated
mutants_x__resolution_sentence__mutmut['x__resolution_sentence__mutmut_8'] = x__resolution_sentence__mutmut_8 # type: ignore # mutmut generated
mutants_x__resolution_sentence__mutmut['x__resolution_sentence__mutmut_9'] = x__resolution_sentence__mutmut_9 # type: ignore # mutmut generated
mutants_x__resolution_sentence__mutmut['x__resolution_sentence__mutmut_10'] = x__resolution_sentence__mutmut_10 # type: ignore # mutmut generated
mutants_x__financial_sentence__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__financial_sentence__mutmut)
def _financial_sentence(financial_impact_eur: float) -> str:
    amount = f"{financial_impact_eur:.0f}".replace(".", ",")
    return f"Cout estime des interventions : {amount}\u20ac."


def x__financial_sentence__mutmut_orig(financial_impact_eur: float) -> str:
    amount = f"{financial_impact_eur:.0f}".replace(".", ",")
    return f"Cout estime des interventions : {amount}\u20ac."


def x__financial_sentence__mutmut_1(financial_impact_eur: float) -> str:
    amount = None
    return f"Cout estime des interventions : {amount}\u20ac."


def x__financial_sentence__mutmut_2(financial_impact_eur: float) -> str:
    amount = f"{financial_impact_eur:.0f}".replace(None, ",")
    return f"Cout estime des interventions : {amount}\u20ac."


def x__financial_sentence__mutmut_3(financial_impact_eur: float) -> str:
    amount = f"{financial_impact_eur:.0f}".replace(".", None)
    return f"Cout estime des interventions : {amount}\u20ac."


def x__financial_sentence__mutmut_4(financial_impact_eur: float) -> str:
    amount = f"{financial_impact_eur:.0f}".replace(",")
    return f"Cout estime des interventions : {amount}\u20ac."


def x__financial_sentence__mutmut_5(financial_impact_eur: float) -> str:
    amount = f"{financial_impact_eur:.0f}".replace(".", )
    return f"Cout estime des interventions : {amount}\u20ac."


def x__financial_sentence__mutmut_6(financial_impact_eur: float) -> str:
    amount = f"{financial_impact_eur:.0f}".replace("XX.XX", ",")
    return f"Cout estime des interventions : {amount}\u20ac."


def x__financial_sentence__mutmut_7(financial_impact_eur: float) -> str:
    amount = f"{financial_impact_eur:.0f}".replace(".", "XX,XX")
    return f"Cout estime des interventions : {amount}\u20ac."

mutants_x__financial_sentence__mutmut['_mutmut_orig'] = x__financial_sentence__mutmut_orig # type: ignore # mutmut generated
mutants_x__financial_sentence__mutmut['x__financial_sentence__mutmut_1'] = x__financial_sentence__mutmut_1 # type: ignore # mutmut generated
mutants_x__financial_sentence__mutmut['x__financial_sentence__mutmut_2'] = x__financial_sentence__mutmut_2 # type: ignore # mutmut generated
mutants_x__financial_sentence__mutmut['x__financial_sentence__mutmut_3'] = x__financial_sentence__mutmut_3 # type: ignore # mutmut generated
mutants_x__financial_sentence__mutmut['x__financial_sentence__mutmut_4'] = x__financial_sentence__mutmut_4 # type: ignore # mutmut generated
mutants_x__financial_sentence__mutmut['x__financial_sentence__mutmut_5'] = x__financial_sentence__mutmut_5 # type: ignore # mutmut generated
mutants_x__financial_sentence__mutmut['x__financial_sentence__mutmut_6'] = x__financial_sentence__mutmut_6 # type: ignore # mutmut generated
mutants_x__financial_sentence__mutmut['x__financial_sentence__mutmut_7'] = x__financial_sentence__mutmut_7 # type: ignore # mutmut generated
mutants_x__first_major__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__first_major__mutmut)
def _first_major(incidents: list[IncidentSummary]) -> IncidentSummary | None:
    for incident in incidents:
        if incident.severity == "major":
            return incident
    return None


def x__first_major__mutmut_orig(incidents: list[IncidentSummary]) -> IncidentSummary | None:
    for incident in incidents:
        if incident.severity == "major":
            return incident
    return None


def x__first_major__mutmut_1(incidents: list[IncidentSummary]) -> IncidentSummary | None:
    for incident in incidents:
        if incident.severity != "major":
            return incident
    return None


def x__first_major__mutmut_2(incidents: list[IncidentSummary]) -> IncidentSummary | None:
    for incident in incidents:
        if incident.severity == "XXmajorXX":
            return incident
    return None


def x__first_major__mutmut_3(incidents: list[IncidentSummary]) -> IncidentSummary | None:
    for incident in incidents:
        if incident.severity == "MAJOR":
            return incident
    return None

mutants_x__first_major__mutmut['_mutmut_orig'] = x__first_major__mutmut_orig # type: ignore # mutmut generated
mutants_x__first_major__mutmut['x__first_major__mutmut_1'] = x__first_major__mutmut_1 # type: ignore # mutmut generated
mutants_x__first_major__mutmut['x__first_major__mutmut_2'] = x__first_major__mutmut_2 # type: ignore # mutmut generated
mutants_x__first_major__mutmut['x__first_major__mutmut_3'] = x__first_major__mutmut_3 # type: ignore # mutmut generated
mutants_x__severity_label__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__severity_label__mutmut)
def _severity_label(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "major" for incident in incidents):
        return "majeur" + ("s" if len(incidents) > 1 else "")
    return "mineur" + ("s" if len(incidents) > 1 else "")


def x__severity_label__mutmut_orig(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "major" for incident in incidents):
        return "majeur" + ("s" if len(incidents) > 1 else "")
    return "mineur" + ("s" if len(incidents) > 1 else "")


def x__severity_label__mutmut_1(incidents: list[IncidentSummary]) -> str:
    if any(None):
        return "majeur" + ("s" if len(incidents) > 1 else "")
    return "mineur" + ("s" if len(incidents) > 1 else "")


def x__severity_label__mutmut_2(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity != "major" for incident in incidents):
        return "majeur" + ("s" if len(incidents) > 1 else "")
    return "mineur" + ("s" if len(incidents) > 1 else "")


def x__severity_label__mutmut_3(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "XXmajorXX" for incident in incidents):
        return "majeur" + ("s" if len(incidents) > 1 else "")
    return "mineur" + ("s" if len(incidents) > 1 else "")


def x__severity_label__mutmut_4(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "MAJOR" for incident in incidents):
        return "majeur" + ("s" if len(incidents) > 1 else "")
    return "mineur" + ("s" if len(incidents) > 1 else "")


def x__severity_label__mutmut_5(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "major" for incident in incidents):
        return "majeur" - ("s" if len(incidents) > 1 else "")
    return "mineur" + ("s" if len(incidents) > 1 else "")


def x__severity_label__mutmut_6(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "major" for incident in incidents):
        return "XXmajeurXX" + ("s" if len(incidents) > 1 else "")
    return "mineur" + ("s" if len(incidents) > 1 else "")


def x__severity_label__mutmut_7(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "major" for incident in incidents):
        return "MAJEUR" + ("s" if len(incidents) > 1 else "")
    return "mineur" + ("s" if len(incidents) > 1 else "")


def x__severity_label__mutmut_8(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "major" for incident in incidents):
        return "majeur" + ("XXsXX" if len(incidents) > 1 else "")
    return "mineur" + ("s" if len(incidents) > 1 else "")


def x__severity_label__mutmut_9(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "major" for incident in incidents):
        return "majeur" + ("S" if len(incidents) > 1 else "")
    return "mineur" + ("s" if len(incidents) > 1 else "")


def x__severity_label__mutmut_10(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "major" for incident in incidents):
        return "majeur" + ("s" if len(incidents) >= 1 else "")
    return "mineur" + ("s" if len(incidents) > 1 else "")


def x__severity_label__mutmut_11(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "major" for incident in incidents):
        return "majeur" + ("s" if len(incidents) > 2 else "")
    return "mineur" + ("s" if len(incidents) > 1 else "")


def x__severity_label__mutmut_12(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "major" for incident in incidents):
        return "majeur" + ("s" if len(incidents) > 1 else "XXXX")
    return "mineur" + ("s" if len(incidents) > 1 else "")


def x__severity_label__mutmut_13(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "major" for incident in incidents):
        return "majeur" + ("s" if len(incidents) > 1 else "")
    return "mineur" - ("s" if len(incidents) > 1 else "")


def x__severity_label__mutmut_14(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "major" for incident in incidents):
        return "majeur" + ("s" if len(incidents) > 1 else "")
    return "XXmineurXX" + ("s" if len(incidents) > 1 else "")


def x__severity_label__mutmut_15(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "major" for incident in incidents):
        return "majeur" + ("s" if len(incidents) > 1 else "")
    return "MINEUR" + ("s" if len(incidents) > 1 else "")


def x__severity_label__mutmut_16(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "major" for incident in incidents):
        return "majeur" + ("s" if len(incidents) > 1 else "")
    return "mineur" + ("XXsXX" if len(incidents) > 1 else "")


def x__severity_label__mutmut_17(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "major" for incident in incidents):
        return "majeur" + ("s" if len(incidents) > 1 else "")
    return "mineur" + ("S" if len(incidents) > 1 else "")


def x__severity_label__mutmut_18(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "major" for incident in incidents):
        return "majeur" + ("s" if len(incidents) > 1 else "")
    return "mineur" + ("s" if len(incidents) >= 1 else "")


def x__severity_label__mutmut_19(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "major" for incident in incidents):
        return "majeur" + ("s" if len(incidents) > 1 else "")
    return "mineur" + ("s" if len(incidents) > 2 else "")


def x__severity_label__mutmut_20(incidents: list[IncidentSummary]) -> str:
    if any(incident.severity == "major" for incident in incidents):
        return "majeur" + ("s" if len(incidents) > 1 else "")
    return "mineur" + ("s" if len(incidents) > 1 else "XXXX")

mutants_x__severity_label__mutmut['_mutmut_orig'] = x__severity_label__mutmut_orig # type: ignore # mutmut generated
mutants_x__severity_label__mutmut['x__severity_label__mutmut_1'] = x__severity_label__mutmut_1 # type: ignore # mutmut generated
mutants_x__severity_label__mutmut['x__severity_label__mutmut_2'] = x__severity_label__mutmut_2 # type: ignore # mutmut generated
mutants_x__severity_label__mutmut['x__severity_label__mutmut_3'] = x__severity_label__mutmut_3 # type: ignore # mutmut generated
mutants_x__severity_label__mutmut['x__severity_label__mutmut_4'] = x__severity_label__mutmut_4 # type: ignore # mutmut generated
mutants_x__severity_label__mutmut['x__severity_label__mutmut_5'] = x__severity_label__mutmut_5 # type: ignore # mutmut generated
mutants_x__severity_label__mutmut['x__severity_label__mutmut_6'] = x__severity_label__mutmut_6 # type: ignore # mutmut generated
mutants_x__severity_label__mutmut['x__severity_label__mutmut_7'] = x__severity_label__mutmut_7 # type: ignore # mutmut generated
mutants_x__severity_label__mutmut['x__severity_label__mutmut_8'] = x__severity_label__mutmut_8 # type: ignore # mutmut generated
mutants_x__severity_label__mutmut['x__severity_label__mutmut_9'] = x__severity_label__mutmut_9 # type: ignore # mutmut generated
mutants_x__severity_label__mutmut['x__severity_label__mutmut_10'] = x__severity_label__mutmut_10 # type: ignore # mutmut generated
mutants_x__severity_label__mutmut['x__severity_label__mutmut_11'] = x__severity_label__mutmut_11 # type: ignore # mutmut generated
mutants_x__severity_label__mutmut['x__severity_label__mutmut_12'] = x__severity_label__mutmut_12 # type: ignore # mutmut generated
mutants_x__severity_label__mutmut['x__severity_label__mutmut_13'] = x__severity_label__mutmut_13 # type: ignore # mutmut generated
mutants_x__severity_label__mutmut['x__severity_label__mutmut_14'] = x__severity_label__mutmut_14 # type: ignore # mutmut generated
mutants_x__severity_label__mutmut['x__severity_label__mutmut_15'] = x__severity_label__mutmut_15 # type: ignore # mutmut generated
mutants_x__severity_label__mutmut['x__severity_label__mutmut_16'] = x__severity_label__mutmut_16 # type: ignore # mutmut generated
mutants_x__severity_label__mutmut['x__severity_label__mutmut_17'] = x__severity_label__mutmut_17 # type: ignore # mutmut generated
mutants_x__severity_label__mutmut['x__severity_label__mutmut_18'] = x__severity_label__mutmut_18 # type: ignore # mutmut generated
mutants_x__severity_label__mutmut['x__severity_label__mutmut_19'] = x__severity_label__mutmut_19 # type: ignore # mutmut generated
mutants_x__severity_label__mutmut['x__severity_label__mutmut_20'] = x__severity_label__mutmut_20 # type: ignore # mutmut generated
