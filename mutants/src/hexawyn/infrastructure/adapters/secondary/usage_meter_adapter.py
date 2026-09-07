from hexawyn.application.ports.driven.usage_meter_port import UsageMeterPort


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁUsageMeterAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁUsageMeterAdapterǁset_usage__mutmut: MutantDict = {}  # type: ignore
mutants_xǁUsageMeterAdapterǁget_usage__mutmut: MutantDict = {}  # type: ignore


class UsageMeterAdapter(UsageMeterPort):
    @_mutmut_mutated(mutants_xǁUsageMeterAdapterǁ__init____mutmut)
    def __init__(self) -> None:
        self._counts: dict[str, int] = {}
    def xǁUsageMeterAdapterǁ__init____mutmut_orig(self) -> None:
        self._counts: dict[str, int] = {}
    def xǁUsageMeterAdapterǁ__init____mutmut_1(self) -> None:
        self._counts: dict[str, int] = None

    @_mutmut_mutated(mutants_xǁUsageMeterAdapterǁset_usage__mutmut)
    def set_usage(self, resource: str, count: int) -> None:
        self._counts[resource] = count

    def xǁUsageMeterAdapterǁset_usage__mutmut_orig(self, resource: str, count: int) -> None:
        self._counts[resource] = count

    def xǁUsageMeterAdapterǁset_usage__mutmut_1(self, resource: str, count: int) -> None:
        self._counts[resource] = None

    @_mutmut_mutated(mutants_xǁUsageMeterAdapterǁget_usage__mutmut)
    def get_usage(self, resource: str) -> int:
        return self._counts.get(resource, 0)

    def xǁUsageMeterAdapterǁget_usage__mutmut_orig(self, resource: str) -> int:
        return self._counts.get(resource, 0)

    def xǁUsageMeterAdapterǁget_usage__mutmut_1(self, resource: str) -> int:
        return self._counts.get(None, 0)

    def xǁUsageMeterAdapterǁget_usage__mutmut_2(self, resource: str) -> int:
        return self._counts.get(resource, None)

    def xǁUsageMeterAdapterǁget_usage__mutmut_3(self, resource: str) -> int:
        return self._counts.get(0)

    def xǁUsageMeterAdapterǁget_usage__mutmut_4(self, resource: str) -> int:
        return self._counts.get(resource, )

    def xǁUsageMeterAdapterǁget_usage__mutmut_5(self, resource: str) -> int:
        return self._counts.get(resource, 1)

mutants_xǁUsageMeterAdapterǁ__init____mutmut['_mutmut_orig'] = UsageMeterAdapter.xǁUsageMeterAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁUsageMeterAdapterǁ__init____mutmut['xǁUsageMeterAdapterǁ__init____mutmut_1'] = UsageMeterAdapter.xǁUsageMeterAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁUsageMeterAdapterǁset_usage__mutmut['_mutmut_orig'] = UsageMeterAdapter.xǁUsageMeterAdapterǁset_usage__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUsageMeterAdapterǁset_usage__mutmut['xǁUsageMeterAdapterǁset_usage__mutmut_1'] = UsageMeterAdapter.xǁUsageMeterAdapterǁset_usage__mutmut_1 # type: ignore # mutmut generated

mutants_xǁUsageMeterAdapterǁget_usage__mutmut['_mutmut_orig'] = UsageMeterAdapter.xǁUsageMeterAdapterǁget_usage__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUsageMeterAdapterǁget_usage__mutmut['xǁUsageMeterAdapterǁget_usage__mutmut_1'] = UsageMeterAdapter.xǁUsageMeterAdapterǁget_usage__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUsageMeterAdapterǁget_usage__mutmut['xǁUsageMeterAdapterǁget_usage__mutmut_2'] = UsageMeterAdapter.xǁUsageMeterAdapterǁget_usage__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUsageMeterAdapterǁget_usage__mutmut['xǁUsageMeterAdapterǁget_usage__mutmut_3'] = UsageMeterAdapter.xǁUsageMeterAdapterǁget_usage__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUsageMeterAdapterǁget_usage__mutmut['xǁUsageMeterAdapterǁget_usage__mutmut_4'] = UsageMeterAdapter.xǁUsageMeterAdapterǁget_usage__mutmut_4 # type: ignore # mutmut generated
mutants_xǁUsageMeterAdapterǁget_usage__mutmut['xǁUsageMeterAdapterǁget_usage__mutmut_5'] = UsageMeterAdapter.xǁUsageMeterAdapterǁget_usage__mutmut_5 # type: ignore # mutmut generated
