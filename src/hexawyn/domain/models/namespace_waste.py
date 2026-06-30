from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NamespaceWaste:
    """Waste analysis result for one namespace — CPU and memory treated independently."""

    namespace: str
    cpu_requested_cores: float
    cpu_actual_avg_cores: float
    cpu_waste_pct: float
    cpu_wasted_cores: float
    memory_requested_gb: float
    memory_actual_avg_gb: float
    memory_waste_pct: float
    memory_wasted_gb: float
    is_over_provisioned: bool

    @property
    def max_waste_pct(self) -> float:
        """Ranking key — worst of CPU or memory waste."""
        return max(self.cpu_waste_pct, self.memory_waste_pct)


@dataclass(frozen=True)
class ExcludedNamespace:
    """Namespace excluded from waste analysis with an explanatory reason."""

    namespace: str
    reason: str


@dataclass
class OverProvisioningReport:
    """Full result: ranked namespaces, exclusions, and aggregated totals."""

    namespaces: list[NamespaceWaste]
    excluded: list[ExcludedNamespace]
    total_wasted_cpu_cores: float
    total_wasted_memory_gb: float
    analysis_window_days: int
