from __future__ import annotations

from dataclasses import dataclass, field

_WASTE_HIGH_THRESHOLD = 20.0


@dataclass
class CostAudit:
    namespace: str
    pod_count: int = 0
    total_cost: float = 0.0
    total_waste: float = 0.0
    waste_percent: float = 0.0
    savings_right_sizing: float = 0.0
    savings_spot: float = 0.0
    savings_total: float = 0.0
    details: dict[str, str | int | float] = field(default_factory=dict)

    @property
    def effective_cost(self) -> float:
        return self.total_cost - self.total_waste

    @property
    def savings_percent(self) -> float:
        if self.total_cost == 0.0:
            return 0.0
        return round((self.savings_total / self.total_cost) * 100, 2)

    @property
    def is_waste_high(self) -> bool:
        return self.waste_percent > _WASTE_HIGH_THRESHOLD

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> CostAudit:
        return cls(
            namespace=_get_str(data, "namespace", ""),
            pod_count=_get_int(data, "pod_count", 0),
            total_cost=_get_float(data, "total_cost", 0.0),
            total_waste=_get_float(data, "total_waste", 0.0),
            waste_percent=_get_float(data, "waste_percent", 0.0),
            savings_right_sizing=_get_float(data, "savings_right_sizing", 0.0),
            savings_spot=_get_float(data, "savings_spot", 0.0),
            savings_total=_get_float(data, "savings_total", 0.0),
            details=_extract_details(data.get("details", {})),
        )


def _get_str(data: dict[str, object], key: str, default: str) -> str:
    value = data.get(key, default)
    return str(value) if value is not None else default


def _get_int(data: dict[str, object], key: str, default: int) -> int:
    value = data.get(key, default)
    if isinstance(value, int | float):
        return int(value)
    if isinstance(value, str):
        return int(value)
    return default


def _get_float(data: dict[str, object], key: str, default: float) -> float:
    value = data.get(key, default)
    if isinstance(value, int | float):
        return float(value)
    if isinstance(value, str):
        return float(value)
    return default


def _extract_details(raw: object) -> dict[str, str | int | float]:
    if isinstance(raw, dict):
        result: dict[str, str | int | float] = {}
        for key, value in raw.items():
            if isinstance(value, str | int | float):
                result[str(key)] = value
        return result
    return {}
