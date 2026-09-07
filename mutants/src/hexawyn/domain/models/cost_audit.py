from __future__ import annotations

from dataclasses import dataclass, field

_WASTE_HIGH_THRESHOLD = 20.0


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
mutants_x__get_str__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__get_str__mutmut)
def _get_str(data: dict[str, object], key: str, default: str) -> str:
    value = data.get(key, default)
    return str(value) if value is not None else default


def x__get_str__mutmut_orig(data: dict[str, object], key: str, default: str) -> str:
    value = data.get(key, default)
    return str(value) if value is not None else default


def x__get_str__mutmut_1(data: dict[str, object], key: str, default: str) -> str:
    value = None
    return str(value) if value is not None else default


def x__get_str__mutmut_2(data: dict[str, object], key: str, default: str) -> str:
    value = data.get(None, default)
    return str(value) if value is not None else default


def x__get_str__mutmut_3(data: dict[str, object], key: str, default: str) -> str:
    value = data.get(key, None)
    return str(value) if value is not None else default


def x__get_str__mutmut_4(data: dict[str, object], key: str, default: str) -> str:
    value = data.get(default)
    return str(value) if value is not None else default


def x__get_str__mutmut_5(data: dict[str, object], key: str, default: str) -> str:
    value = data.get(key, )
    return str(value) if value is not None else default


def x__get_str__mutmut_6(data: dict[str, object], key: str, default: str) -> str:
    value = data.get(key, default)
    return str(None) if value is not None else default


def x__get_str__mutmut_7(data: dict[str, object], key: str, default: str) -> str:
    value = data.get(key, default)
    return str(value) if value is None else default

mutants_x__get_str__mutmut['_mutmut_orig'] = x__get_str__mutmut_orig # type: ignore # mutmut generated
mutants_x__get_str__mutmut['x__get_str__mutmut_1'] = x__get_str__mutmut_1 # type: ignore # mutmut generated
mutants_x__get_str__mutmut['x__get_str__mutmut_2'] = x__get_str__mutmut_2 # type: ignore # mutmut generated
mutants_x__get_str__mutmut['x__get_str__mutmut_3'] = x__get_str__mutmut_3 # type: ignore # mutmut generated
mutants_x__get_str__mutmut['x__get_str__mutmut_4'] = x__get_str__mutmut_4 # type: ignore # mutmut generated
mutants_x__get_str__mutmut['x__get_str__mutmut_5'] = x__get_str__mutmut_5 # type: ignore # mutmut generated
mutants_x__get_str__mutmut['x__get_str__mutmut_6'] = x__get_str__mutmut_6 # type: ignore # mutmut generated
mutants_x__get_str__mutmut['x__get_str__mutmut_7'] = x__get_str__mutmut_7 # type: ignore # mutmut generated
mutants_x__get_int__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__get_int__mutmut)
def _get_int(data: dict[str, object], key: str, default: int) -> int:
    value = data.get(key, default)
    if isinstance(value, int | float):
        return int(value)
    if isinstance(value, str):
        return int(value)
    return default


def x__get_int__mutmut_orig(data: dict[str, object], key: str, default: int) -> int:
    value = data.get(key, default)
    if isinstance(value, int | float):
        return int(value)
    if isinstance(value, str):
        return int(value)
    return default


def x__get_int__mutmut_1(data: dict[str, object], key: str, default: int) -> int:
    value = None
    if isinstance(value, int | float):
        return int(value)
    if isinstance(value, str):
        return int(value)
    return default


def x__get_int__mutmut_2(data: dict[str, object], key: str, default: int) -> int:
    value = data.get(None, default)
    if isinstance(value, int | float):
        return int(value)
    if isinstance(value, str):
        return int(value)
    return default


def x__get_int__mutmut_3(data: dict[str, object], key: str, default: int) -> int:
    value = data.get(key, None)
    if isinstance(value, int | float):
        return int(value)
    if isinstance(value, str):
        return int(value)
    return default


def x__get_int__mutmut_4(data: dict[str, object], key: str, default: int) -> int:
    value = data.get(default)
    if isinstance(value, int | float):
        return int(value)
    if isinstance(value, str):
        return int(value)
    return default


def x__get_int__mutmut_5(data: dict[str, object], key: str, default: int) -> int:
    value = data.get(key, )
    if isinstance(value, int | float):
        return int(value)
    if isinstance(value, str):
        return int(value)
    return default


def x__get_int__mutmut_6(data: dict[str, object], key: str, default: int) -> int:
    value = data.get(key, default)
    if isinstance(value, int | float):
        return int(None)
    if isinstance(value, str):
        return int(value)
    return default


def x__get_int__mutmut_7(data: dict[str, object], key: str, default: int) -> int:
    value = data.get(key, default)
    if isinstance(value, int | float):
        return int(value)
    if isinstance(value, str):
        return int(None)
    return default

mutants_x__get_int__mutmut['_mutmut_orig'] = x__get_int__mutmut_orig # type: ignore # mutmut generated
mutants_x__get_int__mutmut['x__get_int__mutmut_1'] = x__get_int__mutmut_1 # type: ignore # mutmut generated
mutants_x__get_int__mutmut['x__get_int__mutmut_2'] = x__get_int__mutmut_2 # type: ignore # mutmut generated
mutants_x__get_int__mutmut['x__get_int__mutmut_3'] = x__get_int__mutmut_3 # type: ignore # mutmut generated
mutants_x__get_int__mutmut['x__get_int__mutmut_4'] = x__get_int__mutmut_4 # type: ignore # mutmut generated
mutants_x__get_int__mutmut['x__get_int__mutmut_5'] = x__get_int__mutmut_5 # type: ignore # mutmut generated
mutants_x__get_int__mutmut['x__get_int__mutmut_6'] = x__get_int__mutmut_6 # type: ignore # mutmut generated
mutants_x__get_int__mutmut['x__get_int__mutmut_7'] = x__get_int__mutmut_7 # type: ignore # mutmut generated
mutants_x__get_float__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__get_float__mutmut)
def _get_float(data: dict[str, object], key: str, default: float) -> float:
    value = data.get(key, default)
    if isinstance(value, int | float):
        return float(value)
    if isinstance(value, str):
        return float(value)
    return default


def x__get_float__mutmut_orig(data: dict[str, object], key: str, default: float) -> float:
    value = data.get(key, default)
    if isinstance(value, int | float):
        return float(value)
    if isinstance(value, str):
        return float(value)
    return default


def x__get_float__mutmut_1(data: dict[str, object], key: str, default: float) -> float:
    value = None
    if isinstance(value, int | float):
        return float(value)
    if isinstance(value, str):
        return float(value)
    return default


def x__get_float__mutmut_2(data: dict[str, object], key: str, default: float) -> float:
    value = data.get(None, default)
    if isinstance(value, int | float):
        return float(value)
    if isinstance(value, str):
        return float(value)
    return default


def x__get_float__mutmut_3(data: dict[str, object], key: str, default: float) -> float:
    value = data.get(key, None)
    if isinstance(value, int | float):
        return float(value)
    if isinstance(value, str):
        return float(value)
    return default


def x__get_float__mutmut_4(data: dict[str, object], key: str, default: float) -> float:
    value = data.get(default)
    if isinstance(value, int | float):
        return float(value)
    if isinstance(value, str):
        return float(value)
    return default


def x__get_float__mutmut_5(data: dict[str, object], key: str, default: float) -> float:
    value = data.get(key, )
    if isinstance(value, int | float):
        return float(value)
    if isinstance(value, str):
        return float(value)
    return default


def x__get_float__mutmut_6(data: dict[str, object], key: str, default: float) -> float:
    value = data.get(key, default)
    if isinstance(value, int | float):
        return float(None)
    if isinstance(value, str):
        return float(value)
    return default


def x__get_float__mutmut_7(data: dict[str, object], key: str, default: float) -> float:
    value = data.get(key, default)
    if isinstance(value, int | float):
        return float(value)
    if isinstance(value, str):
        return float(None)
    return default

mutants_x__get_float__mutmut['_mutmut_orig'] = x__get_float__mutmut_orig # type: ignore # mutmut generated
mutants_x__get_float__mutmut['x__get_float__mutmut_1'] = x__get_float__mutmut_1 # type: ignore # mutmut generated
mutants_x__get_float__mutmut['x__get_float__mutmut_2'] = x__get_float__mutmut_2 # type: ignore # mutmut generated
mutants_x__get_float__mutmut['x__get_float__mutmut_3'] = x__get_float__mutmut_3 # type: ignore # mutmut generated
mutants_x__get_float__mutmut['x__get_float__mutmut_4'] = x__get_float__mutmut_4 # type: ignore # mutmut generated
mutants_x__get_float__mutmut['x__get_float__mutmut_5'] = x__get_float__mutmut_5 # type: ignore # mutmut generated
mutants_x__get_float__mutmut['x__get_float__mutmut_6'] = x__get_float__mutmut_6 # type: ignore # mutmut generated
mutants_x__get_float__mutmut['x__get_float__mutmut_7'] = x__get_float__mutmut_7 # type: ignore # mutmut generated
mutants_x__extract_details__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__extract_details__mutmut)
def _extract_details(raw: object) -> dict[str, str | int | float]:
    if isinstance(raw, dict):
        result: dict[str, str | int | float] = {}
        for key, value in raw.items():
            if isinstance(value, str | int | float):
                result[str(key)] = value
        return result
    return {}


def x__extract_details__mutmut_orig(raw: object) -> dict[str, str | int | float]:
    if isinstance(raw, dict):
        result: dict[str, str | int | float] = {}
        for key, value in raw.items():
            if isinstance(value, str | int | float):
                result[str(key)] = value
        return result
    return {}


def x__extract_details__mutmut_1(raw: object) -> dict[str, str | int | float]:
    if isinstance(raw, dict):
        result: dict[str, str | int | float] = None
        for key, value in raw.items():
            if isinstance(value, str | int | float):
                result[str(key)] = value
        return result
    return {}


def x__extract_details__mutmut_2(raw: object) -> dict[str, str | int | float]:
    if isinstance(raw, dict):
        result: dict[str, str | int | float] = {}
        for key, value in raw.items():
            if isinstance(value, str | int | float):
                result[str(key)] = None
        return result
    return {}


def x__extract_details__mutmut_3(raw: object) -> dict[str, str | int | float]:
    if isinstance(raw, dict):
        result: dict[str, str | int | float] = {}
        for key, value in raw.items():
            if isinstance(value, str | int | float):
                result[str(None)] = value
        return result
    return {}

mutants_x__extract_details__mutmut['_mutmut_orig'] = x__extract_details__mutmut_orig # type: ignore # mutmut generated
mutants_x__extract_details__mutmut['x__extract_details__mutmut_1'] = x__extract_details__mutmut_1 # type: ignore # mutmut generated
mutants_x__extract_details__mutmut['x__extract_details__mutmut_2'] = x__extract_details__mutmut_2 # type: ignore # mutmut generated
mutants_x__extract_details__mutmut['x__extract_details__mutmut_3'] = x__extract_details__mutmut_3 # type: ignore # mutmut generated
