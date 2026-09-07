from __future__ import annotations

from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class TopologySnapshot:
    cluster_name: str
    snapshot: dict[str, object] = field(default_factory=dict)

    @property
    def node_count(self) -> int:
        return _get_int(self.snapshot, "nodes")

    @property
    def pod_count(self) -> int:
        return _get_int(self.snapshot, "pods")

    @property
    def service_count(self) -> int:
        return _get_int(self.snapshot, "services")

    @property
    def namespace_count(self) -> int:
        namespaces = self.snapshot.get("namespaces")
        if isinstance(namespaces, list):
            return len(namespaces)
        return _get_int(self.snapshot, "namespaces")

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> TopologySnapshot:
        raw_snapshot = data.get("snapshot", {})
        if isinstance(raw_snapshot, dict):
            snapshot: dict[str, object] = raw_snapshot
        else:
            snapshot = {}
        return cls(
            cluster_name=str(data.get("cluster_name", "")),
            snapshot=snapshot,
        )
mutants_x__get_int__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__get_int__mutmut)
def _get_int(source: dict[str, object], key: str) -> int:
    value = source.get(key, 0)
    if isinstance(value, int | float):
        return int(value)
    if isinstance(value, str):
        return int(value)
    return 0


def x__get_int__mutmut_orig(source: dict[str, object], key: str) -> int:
    value = source.get(key, 0)
    if isinstance(value, int | float):
        return int(value)
    if isinstance(value, str):
        return int(value)
    return 0


def x__get_int__mutmut_1(source: dict[str, object], key: str) -> int:
    value = None
    if isinstance(value, int | float):
        return int(value)
    if isinstance(value, str):
        return int(value)
    return 0


def x__get_int__mutmut_2(source: dict[str, object], key: str) -> int:
    value = source.get(None, 0)
    if isinstance(value, int | float):
        return int(value)
    if isinstance(value, str):
        return int(value)
    return 0


def x__get_int__mutmut_3(source: dict[str, object], key: str) -> int:
    value = source.get(key, None)
    if isinstance(value, int | float):
        return int(value)
    if isinstance(value, str):
        return int(value)
    return 0


def x__get_int__mutmut_4(source: dict[str, object], key: str) -> int:
    value = source.get(0)
    if isinstance(value, int | float):
        return int(value)
    if isinstance(value, str):
        return int(value)
    return 0


def x__get_int__mutmut_5(source: dict[str, object], key: str) -> int:
    value = source.get(key, )
    if isinstance(value, int | float):
        return int(value)
    if isinstance(value, str):
        return int(value)
    return 0


def x__get_int__mutmut_6(source: dict[str, object], key: str) -> int:
    value = source.get(key, 1)
    if isinstance(value, int | float):
        return int(value)
    if isinstance(value, str):
        return int(value)
    return 0


def x__get_int__mutmut_7(source: dict[str, object], key: str) -> int:
    value = source.get(key, 0)
    if isinstance(value, int | float):
        return int(None)
    if isinstance(value, str):
        return int(value)
    return 0


def x__get_int__mutmut_8(source: dict[str, object], key: str) -> int:
    value = source.get(key, 0)
    if isinstance(value, int | float):
        return int(value)
    if isinstance(value, str):
        return int(None)
    return 0


def x__get_int__mutmut_9(source: dict[str, object], key: str) -> int:
    value = source.get(key, 0)
    if isinstance(value, int | float):
        return int(value)
    if isinstance(value, str):
        return int(value)
    return 1

mutants_x__get_int__mutmut['_mutmut_orig'] = x__get_int__mutmut_orig # type: ignore # mutmut generated
mutants_x__get_int__mutmut['x__get_int__mutmut_1'] = x__get_int__mutmut_1 # type: ignore # mutmut generated
mutants_x__get_int__mutmut['x__get_int__mutmut_2'] = x__get_int__mutmut_2 # type: ignore # mutmut generated
mutants_x__get_int__mutmut['x__get_int__mutmut_3'] = x__get_int__mutmut_3 # type: ignore # mutmut generated
mutants_x__get_int__mutmut['x__get_int__mutmut_4'] = x__get_int__mutmut_4 # type: ignore # mutmut generated
mutants_x__get_int__mutmut['x__get_int__mutmut_5'] = x__get_int__mutmut_5 # type: ignore # mutmut generated
mutants_x__get_int__mutmut['x__get_int__mutmut_6'] = x__get_int__mutmut_6 # type: ignore # mutmut generated
mutants_x__get_int__mutmut['x__get_int__mutmut_7'] = x__get_int__mutmut_7 # type: ignore # mutmut generated
mutants_x__get_int__mutmut['x__get_int__mutmut_8'] = x__get_int__mutmut_8 # type: ignore # mutmut generated
mutants_x__get_int__mutmut['x__get_int__mutmut_9'] = x__get_int__mutmut_9 # type: ignore # mutmut generated
