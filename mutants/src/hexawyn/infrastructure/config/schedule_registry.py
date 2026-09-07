from hexawyn.domain.services.schedule.check_runner import UseCaseRegistry


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


def _certs_list(params: dict[str, str]) -> dict[str, object]:
    from hexawyn.mcp.tools.check_cluster_certificate_health import check_cluster_certificate_health

    return check_cluster_certificate_health()


def _global_health(params: dict[str, str]) -> dict[str, object]:
    from hexawyn.mcp.tools.global_health_check import global_health_check

    return global_health_check()
mutants_x_build_registry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_registry__mutmut)
def build_registry() -> UseCaseRegistry:
    registry: UseCaseRegistry = {}
    registry["certs_list"] = _certs_list
    registry["global_health_check"] = _global_health
    return registry


def x_build_registry__mutmut_orig() -> UseCaseRegistry:
    registry: UseCaseRegistry = {}
    registry["certs_list"] = _certs_list
    registry["global_health_check"] = _global_health
    return registry


def x_build_registry__mutmut_1() -> UseCaseRegistry:
    registry: UseCaseRegistry = None
    registry["certs_list"] = _certs_list
    registry["global_health_check"] = _global_health
    return registry


def x_build_registry__mutmut_2() -> UseCaseRegistry:
    registry: UseCaseRegistry = {}
    registry["certs_list"] = None
    registry["global_health_check"] = _global_health
    return registry


def x_build_registry__mutmut_3() -> UseCaseRegistry:
    registry: UseCaseRegistry = {}
    registry["XXcerts_listXX"] = _certs_list
    registry["global_health_check"] = _global_health
    return registry


def x_build_registry__mutmut_4() -> UseCaseRegistry:
    registry: UseCaseRegistry = {}
    registry["CERTS_LIST"] = _certs_list
    registry["global_health_check"] = _global_health
    return registry


def x_build_registry__mutmut_5() -> UseCaseRegistry:
    registry: UseCaseRegistry = {}
    registry["certs_list"] = _certs_list
    registry["global_health_check"] = None
    return registry


def x_build_registry__mutmut_6() -> UseCaseRegistry:
    registry: UseCaseRegistry = {}
    registry["certs_list"] = _certs_list
    registry["XXglobal_health_checkXX"] = _global_health
    return registry


def x_build_registry__mutmut_7() -> UseCaseRegistry:
    registry: UseCaseRegistry = {}
    registry["certs_list"] = _certs_list
    registry["GLOBAL_HEALTH_CHECK"] = _global_health
    return registry

mutants_x_build_registry__mutmut['_mutmut_orig'] = x_build_registry__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_registry__mutmut['x_build_registry__mutmut_1'] = x_build_registry__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_registry__mutmut['x_build_registry__mutmut_2'] = x_build_registry__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_registry__mutmut['x_build_registry__mutmut_3'] = x_build_registry__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_registry__mutmut['x_build_registry__mutmut_4'] = x_build_registry__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_registry__mutmut['x_build_registry__mutmut_5'] = x_build_registry__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_registry__mutmut['x_build_registry__mutmut_6'] = x_build_registry__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_registry__mutmut['x_build_registry__mutmut_7'] = x_build_registry__mutmut_7 # type: ignore # mutmut generated
