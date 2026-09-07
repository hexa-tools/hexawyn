from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.probe_audit import MissingProbe, ProbeAuditResult

_HTTP_PORTS = frozenset({80, 443, 3000, 8000, 8080, 8081, 8443, 9090})


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class _DeploymentInfo:
    deployment_name: str
    namespace: str
    has_service: bool
    is_exposed: bool
    workload_type: str
mutants_x__deployment_info__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__deployment_info__mutmut)
def _deployment_info(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_orig(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_1(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=None,
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_2(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=None,
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_3(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=None,
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_4(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=None,
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_5(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=None,
    )


def x__deployment_info__mutmut_6(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_7(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_8(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_9(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_10(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        )


def x__deployment_info__mutmut_11(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(None),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_12(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get(None, "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_13(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", None)),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_14(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_15(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", )),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_16(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("XXdeployment_nameXX", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_17(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("DEPLOYMENT_NAME", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_18(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "XXXX")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_19(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(None),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_20(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get(None, "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_21(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", None)),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_22(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_23(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", )),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_24(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("XXnamespaceXX", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_25(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("NAMESPACE", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_26(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "XXXX")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_27(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(None),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_28(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get(None)),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_29(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("XXhas_serviceXX")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_30(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("HAS_SERVICE")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_31(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(None),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_32(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get(None)),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_33(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("XXis_exposed_externallyXX")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_34(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("IS_EXPOSED_EXTERNALLY")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


def x__deployment_info__mutmut_35(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(None),
    )


def x__deployment_info__mutmut_36(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get(None, "Deployment")),
    )


def x__deployment_info__mutmut_37(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", None)),
    )


def x__deployment_info__mutmut_38(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("Deployment")),
    )


def x__deployment_info__mutmut_39(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", )),
    )


def x__deployment_info__mutmut_40(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("XXworkload_typeXX", "Deployment")),
    )


def x__deployment_info__mutmut_41(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("WORKLOAD_TYPE", "Deployment")),
    )


def x__deployment_info__mutmut_42(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "XXDeploymentXX")),
    )


def x__deployment_info__mutmut_43(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "deployment")),
    )


def x__deployment_info__mutmut_44(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "DEPLOYMENT")),
    )

mutants_x__deployment_info__mutmut['_mutmut_orig'] = x__deployment_info__mutmut_orig # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_1'] = x__deployment_info__mutmut_1 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_2'] = x__deployment_info__mutmut_2 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_3'] = x__deployment_info__mutmut_3 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_4'] = x__deployment_info__mutmut_4 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_5'] = x__deployment_info__mutmut_5 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_6'] = x__deployment_info__mutmut_6 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_7'] = x__deployment_info__mutmut_7 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_8'] = x__deployment_info__mutmut_8 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_9'] = x__deployment_info__mutmut_9 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_10'] = x__deployment_info__mutmut_10 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_11'] = x__deployment_info__mutmut_11 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_12'] = x__deployment_info__mutmut_12 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_13'] = x__deployment_info__mutmut_13 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_14'] = x__deployment_info__mutmut_14 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_15'] = x__deployment_info__mutmut_15 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_16'] = x__deployment_info__mutmut_16 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_17'] = x__deployment_info__mutmut_17 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_18'] = x__deployment_info__mutmut_18 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_19'] = x__deployment_info__mutmut_19 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_20'] = x__deployment_info__mutmut_20 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_21'] = x__deployment_info__mutmut_21 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_22'] = x__deployment_info__mutmut_22 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_23'] = x__deployment_info__mutmut_23 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_24'] = x__deployment_info__mutmut_24 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_25'] = x__deployment_info__mutmut_25 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_26'] = x__deployment_info__mutmut_26 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_27'] = x__deployment_info__mutmut_27 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_28'] = x__deployment_info__mutmut_28 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_29'] = x__deployment_info__mutmut_29 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_30'] = x__deployment_info__mutmut_30 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_31'] = x__deployment_info__mutmut_31 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_32'] = x__deployment_info__mutmut_32 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_33'] = x__deployment_info__mutmut_33 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_34'] = x__deployment_info__mutmut_34 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_35'] = x__deployment_info__mutmut_35 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_36'] = x__deployment_info__mutmut_36 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_37'] = x__deployment_info__mutmut_37 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_38'] = x__deployment_info__mutmut_38 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_39'] = x__deployment_info__mutmut_39 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_40'] = x__deployment_info__mutmut_40 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_41'] = x__deployment_info__mutmut_41 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_42'] = x__deployment_info__mutmut_42 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_43'] = x__deployment_info__mutmut_43 # type: ignore # mutmut generated
mutants_x__deployment_info__mutmut['x__deployment_info__mutmut_44'] = x__deployment_info__mutmut_44 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut: MutantDict = {}  # type: ignore


class ProbeAuditEngine:
    @_mutmut_mutated(mutants_xǁProbeAuditEngineǁdetect__mutmut)
    def detect(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_orig(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_1(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = None

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_2(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = None
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_3(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get(None)
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_4(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("XXcontainersXX")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_5(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("CONTAINERS")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_6(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = None

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_7(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(None) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_8(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = None
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_9(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(None)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_10(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = None
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_11(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(None)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_12(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = None

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_13(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(None)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_14(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = None
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_15(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    None, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_16(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, None, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_17(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, None, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_18(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, None
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_19(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_20(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_21(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_22(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_23(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = None
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_24(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[1] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_25(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 1
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_26(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = None
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_27(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(None),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_28(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(None),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_29(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = None
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_30(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(None, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_31(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, None, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_32(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, None, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_33(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, None, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_34(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, None)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_35(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_36(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_37(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_38(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_39(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, )
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_40(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(None)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_41(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity != "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_42(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "XXcriticalXX":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_43(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "CRITICAL":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_44(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical = 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_45(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical -= 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_46(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 2
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_47(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity != "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_48(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "XXwarningXX":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_49(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "WARNING":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_50(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning = 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_51(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning -= 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_52(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 2
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_53(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational = 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_54(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational -= 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_55(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 2

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_56(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes = 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_57(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes -= 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_58(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 2

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_59(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = None
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_60(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(None)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_61(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = None
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_62(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(None, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_63(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, None, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_64(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, None, primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_65(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", None, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_66(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, None)
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_67(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_68(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_69(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_70(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_71(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, )
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_72(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "XXwarningXX", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_73(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "WARNING", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_74(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("XXXX", ""))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_75(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", "XXXX"))
                result.misconfigured_probes.append(probe)

        return result
    def xǁProbeAuditEngineǁdetect__mutmut_76(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(None)

        return result

mutants_xǁProbeAuditEngineǁdetect__mutmut['_mutmut_orig'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_orig # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_1'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_1 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_2'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_2 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_3'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_3 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_4'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_4 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_5'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_5 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_6'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_6 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_7'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_7 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_8'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_8 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_9'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_9 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_10'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_10 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_11'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_11 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_12'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_12 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_13'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_13 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_14'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_14 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_15'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_15 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_16'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_16 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_17'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_17 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_18'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_18 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_19'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_19 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_20'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_20 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_21'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_21 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_22'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_22 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_23'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_23 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_24'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_24 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_25'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_25 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_26'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_26 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_27'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_27 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_28'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_28 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_29'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_29 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_30'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_30 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_31'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_31 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_32'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_32 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_33'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_33 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_34'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_34 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_35'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_35 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_36'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_36 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_37'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_37 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_38'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_38 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_39'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_39 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_40'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_40 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_41'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_41 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_42'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_42 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_43'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_43 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_44'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_44 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_45'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_45 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_46'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_46 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_47'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_47 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_48'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_48 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_49'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_49 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_50'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_50 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_51'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_51 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_52'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_52 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_53'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_53 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_54'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_54 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_55'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_55 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_56'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_56 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_57'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_57 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_58'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_58 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_59'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_59 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_60'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_60 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_61'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_61 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_62'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_62 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_63'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_63 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_64'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_64 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_65'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_65 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_66'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_66 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_67'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_67 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_68'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_68 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_69'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_69 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_70'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_70 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_71'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_71 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_72'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_72 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_73'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_73 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_74'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_74 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_75'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_75 # type: ignore # mutmut generated
mutants_xǁProbeAuditEngineǁdetect__mutmut['xǁProbeAuditEngineǁdetect__mutmut_76'] = ProbeAuditEngine.xǁProbeAuditEngineǁdetect__mutmut_76 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_probe__mutmut)
def _build_probe(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=info.namespace,
        missing=missing,
        severity=severity,
        exposed_port=exposed_port,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=liveness_suggestion,
        has_service=info.has_service,
        workload_type=info.workload_type,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_orig(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=info.namespace,
        missing=missing,
        severity=severity,
        exposed_port=exposed_port,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=liveness_suggestion,
        has_service=info.has_service,
        workload_type=info.workload_type,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_1(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = None
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=info.namespace,
        missing=missing,
        severity=severity,
        exposed_port=exposed_port,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=liveness_suggestion,
        has_service=info.has_service,
        workload_type=info.workload_type,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_2(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=None,
        namespace=info.namespace,
        missing=missing,
        severity=severity,
        exposed_port=exposed_port,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=liveness_suggestion,
        has_service=info.has_service,
        workload_type=info.workload_type,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_3(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=None,
        missing=missing,
        severity=severity,
        exposed_port=exposed_port,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=liveness_suggestion,
        has_service=info.has_service,
        workload_type=info.workload_type,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_4(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=info.namespace,
        missing=None,
        severity=severity,
        exposed_port=exposed_port,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=liveness_suggestion,
        has_service=info.has_service,
        workload_type=info.workload_type,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_5(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=info.namespace,
        missing=missing,
        severity=None,
        exposed_port=exposed_port,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=liveness_suggestion,
        has_service=info.has_service,
        workload_type=info.workload_type,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_6(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=info.namespace,
        missing=missing,
        severity=severity,
        exposed_port=None,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=liveness_suggestion,
        has_service=info.has_service,
        workload_type=info.workload_type,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_7(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=info.namespace,
        missing=missing,
        severity=severity,
        exposed_port=exposed_port,
        readiness_suggestion=None,
        liveness_suggestion=liveness_suggestion,
        has_service=info.has_service,
        workload_type=info.workload_type,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_8(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=info.namespace,
        missing=missing,
        severity=severity,
        exposed_port=exposed_port,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=None,
        has_service=info.has_service,
        workload_type=info.workload_type,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_9(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=info.namespace,
        missing=missing,
        severity=severity,
        exposed_port=exposed_port,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=liveness_suggestion,
        has_service=None,
        workload_type=info.workload_type,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_10(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=info.namespace,
        missing=missing,
        severity=severity,
        exposed_port=exposed_port,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=liveness_suggestion,
        has_service=info.has_service,
        workload_type=None,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_11(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=info.namespace,
        missing=missing,
        severity=severity,
        exposed_port=exposed_port,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=liveness_suggestion,
        has_service=info.has_service,
        workload_type=info.workload_type,
        is_exposed_externally=None,
    )


def x__build_probe__mutmut_12(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        namespace=info.namespace,
        missing=missing,
        severity=severity,
        exposed_port=exposed_port,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=liveness_suggestion,
        has_service=info.has_service,
        workload_type=info.workload_type,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_13(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        missing=missing,
        severity=severity,
        exposed_port=exposed_port,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=liveness_suggestion,
        has_service=info.has_service,
        workload_type=info.workload_type,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_14(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=info.namespace,
        severity=severity,
        exposed_port=exposed_port,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=liveness_suggestion,
        has_service=info.has_service,
        workload_type=info.workload_type,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_15(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=info.namespace,
        missing=missing,
        exposed_port=exposed_port,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=liveness_suggestion,
        has_service=info.has_service,
        workload_type=info.workload_type,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_16(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=info.namespace,
        missing=missing,
        severity=severity,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=liveness_suggestion,
        has_service=info.has_service,
        workload_type=info.workload_type,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_17(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=info.namespace,
        missing=missing,
        severity=severity,
        exposed_port=exposed_port,
        liveness_suggestion=liveness_suggestion,
        has_service=info.has_service,
        workload_type=info.workload_type,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_18(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=info.namespace,
        missing=missing,
        severity=severity,
        exposed_port=exposed_port,
        readiness_suggestion=readiness_suggestion,
        has_service=info.has_service,
        workload_type=info.workload_type,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_19(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=info.namespace,
        missing=missing,
        severity=severity,
        exposed_port=exposed_port,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=liveness_suggestion,
        workload_type=info.workload_type,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_20(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=info.namespace,
        missing=missing,
        severity=severity,
        exposed_port=exposed_port,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=liveness_suggestion,
        has_service=info.has_service,
        is_exposed_externally=info.is_exposed,
    )


def x__build_probe__mutmut_21(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=info.namespace,
        missing=missing,
        severity=severity,
        exposed_port=exposed_port,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=liveness_suggestion,
        has_service=info.has_service,
        workload_type=info.workload_type,
        )

mutants_x__build_probe__mutmut['_mutmut_orig'] = x__build_probe__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_1'] = x__build_probe__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_2'] = x__build_probe__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_3'] = x__build_probe__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_4'] = x__build_probe__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_5'] = x__build_probe__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_6'] = x__build_probe__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_7'] = x__build_probe__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_8'] = x__build_probe__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_9'] = x__build_probe__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_10'] = x__build_probe__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_11'] = x__build_probe__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_12'] = x__build_probe__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_13'] = x__build_probe__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_14'] = x__build_probe__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_15'] = x__build_probe__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_16'] = x__build_probe__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_17'] = x__build_probe__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_18'] = x__build_probe__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_19'] = x__build_probe__mutmut_19 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_20'] = x__build_probe__mutmut_20 # type: ignore # mutmut generated
mutants_x__build_probe__mutmut['x__build_probe__mutmut_21'] = x__build_probe__mutmut_21 # type: ignore # mutmut generated
mutants_x__exposed_port_ints__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__exposed_port_ints__mutmut)
def _exposed_port_ints(c: dict[str, object]) -> list[int]:
    """Extract the valid (>0) integer ports exposed by a container."""
    raw = c.get("exposed_ports")
    if not isinstance(raw, list):
        return []
    return [_as_int(x) for x in raw if _as_int(x) > 0]


def x__exposed_port_ints__mutmut_orig(c: dict[str, object]) -> list[int]:
    """Extract the valid (>0) integer ports exposed by a container."""
    raw = c.get("exposed_ports")
    if not isinstance(raw, list):
        return []
    return [_as_int(x) for x in raw if _as_int(x) > 0]


def x__exposed_port_ints__mutmut_1(c: dict[str, object]) -> list[int]:
    """Extract the valid (>0) integer ports exposed by a container."""
    raw = None
    if not isinstance(raw, list):
        return []
    return [_as_int(x) for x in raw if _as_int(x) > 0]


def x__exposed_port_ints__mutmut_2(c: dict[str, object]) -> list[int]:
    """Extract the valid (>0) integer ports exposed by a container."""
    raw = c.get(None)
    if not isinstance(raw, list):
        return []
    return [_as_int(x) for x in raw if _as_int(x) > 0]


def x__exposed_port_ints__mutmut_3(c: dict[str, object]) -> list[int]:
    """Extract the valid (>0) integer ports exposed by a container."""
    raw = c.get("XXexposed_portsXX")
    if not isinstance(raw, list):
        return []
    return [_as_int(x) for x in raw if _as_int(x) > 0]


def x__exposed_port_ints__mutmut_4(c: dict[str, object]) -> list[int]:
    """Extract the valid (>0) integer ports exposed by a container."""
    raw = c.get("EXPOSED_PORTS")
    if not isinstance(raw, list):
        return []
    return [_as_int(x) for x in raw if _as_int(x) > 0]


def x__exposed_port_ints__mutmut_5(c: dict[str, object]) -> list[int]:
    """Extract the valid (>0) integer ports exposed by a container."""
    raw = c.get("exposed_ports")
    if isinstance(raw, list):
        return []
    return [_as_int(x) for x in raw if _as_int(x) > 0]


def x__exposed_port_ints__mutmut_6(c: dict[str, object]) -> list[int]:
    """Extract the valid (>0) integer ports exposed by a container."""
    raw = c.get("exposed_ports")
    if not isinstance(raw, list):
        return []
    return [_as_int(None) for x in raw if _as_int(x) > 0]


def x__exposed_port_ints__mutmut_7(c: dict[str, object]) -> list[int]:
    """Extract the valid (>0) integer ports exposed by a container."""
    raw = c.get("exposed_ports")
    if not isinstance(raw, list):
        return []
    return [_as_int(x) for x in raw if _as_int(None) > 0]


def x__exposed_port_ints__mutmut_8(c: dict[str, object]) -> list[int]:
    """Extract the valid (>0) integer ports exposed by a container."""
    raw = c.get("exposed_ports")
    if not isinstance(raw, list):
        return []
    return [_as_int(x) for x in raw if _as_int(x) >= 0]


def x__exposed_port_ints__mutmut_9(c: dict[str, object]) -> list[int]:
    """Extract the valid (>0) integer ports exposed by a container."""
    raw = c.get("exposed_ports")
    if not isinstance(raw, list):
        return []
    return [_as_int(x) for x in raw if _as_int(x) > 1]

mutants_x__exposed_port_ints__mutmut['_mutmut_orig'] = x__exposed_port_ints__mutmut_orig # type: ignore # mutmut generated
mutants_x__exposed_port_ints__mutmut['x__exposed_port_ints__mutmut_1'] = x__exposed_port_ints__mutmut_1 # type: ignore # mutmut generated
mutants_x__exposed_port_ints__mutmut['x__exposed_port_ints__mutmut_2'] = x__exposed_port_ints__mutmut_2 # type: ignore # mutmut generated
mutants_x__exposed_port_ints__mutmut['x__exposed_port_ints__mutmut_3'] = x__exposed_port_ints__mutmut_3 # type: ignore # mutmut generated
mutants_x__exposed_port_ints__mutmut['x__exposed_port_ints__mutmut_4'] = x__exposed_port_ints__mutmut_4 # type: ignore # mutmut generated
mutants_x__exposed_port_ints__mutmut['x__exposed_port_ints__mutmut_5'] = x__exposed_port_ints__mutmut_5 # type: ignore # mutmut generated
mutants_x__exposed_port_ints__mutmut['x__exposed_port_ints__mutmut_6'] = x__exposed_port_ints__mutmut_6 # type: ignore # mutmut generated
mutants_x__exposed_port_ints__mutmut['x__exposed_port_ints__mutmut_7'] = x__exposed_port_ints__mutmut_7 # type: ignore # mutmut generated
mutants_x__exposed_port_ints__mutmut['x__exposed_port_ints__mutmut_8'] = x__exposed_port_ints__mutmut_8 # type: ignore # mutmut generated
mutants_x__exposed_port_ints__mutmut['x__exposed_port_ints__mutmut_9'] = x__exposed_port_ints__mutmut_9 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__find_missing_probes__mutmut)
def _find_missing_probes(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_orig(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_1(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = None
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_2(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = None

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_3(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(None):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_4(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get(None)):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_5(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("XXis_init_containerXX")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_6(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("IS_INIT_CONTAINER")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_7(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            break
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_8(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(None)

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_9(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(None))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_10(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_11(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(None):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_12(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get(None)):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_13(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("XXhas_liveness_probeXX")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_14(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("HAS_LIVENESS_PROBE")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_15(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add(None)
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_16(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("XXlivenessProbeXX")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_17(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessprobe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_18(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("LIVENESSPROBE")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_19(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_20(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(None):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_21(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get(None)):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_22(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("XXhas_readiness_probeXX")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_23(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("HAS_READINESS_PROBE")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_24(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add(None)

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_25(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("XXreadinessProbeXX")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_26(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessprobe")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_27(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("READINESSPROBE")

    return (sorted(missing), all_exposed_ports)


def x__find_missing_probes__mutmut_28(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(None), all_exposed_ports)

mutants_x__find_missing_probes__mutmut['_mutmut_orig'] = x__find_missing_probes__mutmut_orig # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_1'] = x__find_missing_probes__mutmut_1 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_2'] = x__find_missing_probes__mutmut_2 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_3'] = x__find_missing_probes__mutmut_3 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_4'] = x__find_missing_probes__mutmut_4 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_5'] = x__find_missing_probes__mutmut_5 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_6'] = x__find_missing_probes__mutmut_6 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_7'] = x__find_missing_probes__mutmut_7 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_8'] = x__find_missing_probes__mutmut_8 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_9'] = x__find_missing_probes__mutmut_9 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_10'] = x__find_missing_probes__mutmut_10 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_11'] = x__find_missing_probes__mutmut_11 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_12'] = x__find_missing_probes__mutmut_12 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_13'] = x__find_missing_probes__mutmut_13 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_14'] = x__find_missing_probes__mutmut_14 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_15'] = x__find_missing_probes__mutmut_15 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_16'] = x__find_missing_probes__mutmut_16 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_17'] = x__find_missing_probes__mutmut_17 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_18'] = x__find_missing_probes__mutmut_18 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_19'] = x__find_missing_probes__mutmut_19 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_20'] = x__find_missing_probes__mutmut_20 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_21'] = x__find_missing_probes__mutmut_21 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_22'] = x__find_missing_probes__mutmut_22 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_23'] = x__find_missing_probes__mutmut_23 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_24'] = x__find_missing_probes__mutmut_24 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_25'] = x__find_missing_probes__mutmut_25 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_26'] = x__find_missing_probes__mutmut_26 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_27'] = x__find_missing_probes__mutmut_27 # type: ignore # mutmut generated
mutants_x__find_missing_probes__mutmut['x__find_missing_probes__mutmut_28'] = x__find_missing_probes__mutmut_28 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__find_misconfigurations__mutmut)
def _find_misconfigurations(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_orig(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_1(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = None
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_2(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(None):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_3(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get(None)):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_4(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("XXis_init_containerXX")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_5(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("IS_INIT_CONTAINER")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_6(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            break
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_7(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = None

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_8(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(None)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_9(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(None):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_10(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get(None)):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_11(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("XXhas_readiness_probeXX")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_12(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("HAS_READINESS_PROBE")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_13(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = None
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_14(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(None)
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_15(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get(None))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_16(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("XXreadiness_portXX"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_17(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("READINESS_PORT"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_18(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 or rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_19(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp >= 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_20(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 1 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_21(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_22(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append(None)

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_23(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("XXreadiness_port_mismatchXX")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_24(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("READINESS_PORT_MISMATCH")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_25(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(None):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_26(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get(None)):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_27(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("XXhas_liveness_probeXX")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_28(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("HAS_LIVENESS_PROBE")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_29(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = None
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_30(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(None)
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_31(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get(None))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_32(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("XXliveness_portXX"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_33(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("LIVENESS_PORT"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_34(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 or lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_35(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp >= 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_36(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 1 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_37(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def x__find_misconfigurations__mutmut_38(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append(None)

    return issues


def x__find_misconfigurations__mutmut_39(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("XXliveness_port_mismatchXX")

    return issues


def x__find_misconfigurations__mutmut_40(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("LIVENESS_PORT_MISMATCH")

    return issues

mutants_x__find_misconfigurations__mutmut['_mutmut_orig'] = x__find_misconfigurations__mutmut_orig # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_1'] = x__find_misconfigurations__mutmut_1 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_2'] = x__find_misconfigurations__mutmut_2 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_3'] = x__find_misconfigurations__mutmut_3 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_4'] = x__find_misconfigurations__mutmut_4 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_5'] = x__find_misconfigurations__mutmut_5 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_6'] = x__find_misconfigurations__mutmut_6 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_7'] = x__find_misconfigurations__mutmut_7 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_8'] = x__find_misconfigurations__mutmut_8 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_9'] = x__find_misconfigurations__mutmut_9 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_10'] = x__find_misconfigurations__mutmut_10 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_11'] = x__find_misconfigurations__mutmut_11 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_12'] = x__find_misconfigurations__mutmut_12 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_13'] = x__find_misconfigurations__mutmut_13 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_14'] = x__find_misconfigurations__mutmut_14 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_15'] = x__find_misconfigurations__mutmut_15 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_16'] = x__find_misconfigurations__mutmut_16 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_17'] = x__find_misconfigurations__mutmut_17 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_18'] = x__find_misconfigurations__mutmut_18 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_19'] = x__find_misconfigurations__mutmut_19 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_20'] = x__find_misconfigurations__mutmut_20 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_21'] = x__find_misconfigurations__mutmut_21 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_22'] = x__find_misconfigurations__mutmut_22 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_23'] = x__find_misconfigurations__mutmut_23 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_24'] = x__find_misconfigurations__mutmut_24 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_25'] = x__find_misconfigurations__mutmut_25 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_26'] = x__find_misconfigurations__mutmut_26 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_27'] = x__find_misconfigurations__mutmut_27 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_28'] = x__find_misconfigurations__mutmut_28 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_29'] = x__find_misconfigurations__mutmut_29 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_30'] = x__find_misconfigurations__mutmut_30 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_31'] = x__find_misconfigurations__mutmut_31 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_32'] = x__find_misconfigurations__mutmut_32 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_33'] = x__find_misconfigurations__mutmut_33 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_34'] = x__find_misconfigurations__mutmut_34 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_35'] = x__find_misconfigurations__mutmut_35 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_36'] = x__find_misconfigurations__mutmut_36 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_37'] = x__find_misconfigurations__mutmut_37 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_38'] = x__find_misconfigurations__mutmut_38 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_39'] = x__find_misconfigurations__mutmut_39 # type: ignore # mutmut generated
mutants_x__find_misconfigurations__mutmut['x__find_misconfigurations__mutmut_40'] = x__find_misconfigurations__mutmut_40 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__classify_severity__mutmut)
def _classify_severity(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_orig(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_1(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = None

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_2(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace not in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_3(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("XXproductionXX", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_4(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("PRODUCTION", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_5(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "XXprodXX")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_6(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "PROD")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_7(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type not in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_8(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("XXJobXX", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_9(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_10(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("JOB", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_11(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "XXCronJobXX", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_12(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "cronjob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_13(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CRONJOB", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_14(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "XXDaemonSetXX"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_15(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "daemonset"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_16(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DAEMONSET"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_17(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "XXinformationalXX"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_18(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "INFORMATIONAL"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_19(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production or is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_20(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "XXcriticalXX"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_21(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "CRITICAL"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_22(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production or has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_23(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "XXwarningXX"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_24(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "WARNING"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_25(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" or has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_26(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type != "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_27(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "XXStatefulSetXX" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_28(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "statefulset" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_29(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "STATEFULSET" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_30(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "XXcriticalXX"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_31(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "CRITICAL"

    if has_service:
        return "warning"

    return "informational"


def x__classify_severity__mutmut_32(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "XXwarningXX"

    return "informational"


def x__classify_severity__mutmut_33(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "WARNING"

    return "informational"


def x__classify_severity__mutmut_34(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "XXinformationalXX"


def x__classify_severity__mutmut_35(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "INFORMATIONAL"

mutants_x__classify_severity__mutmut['_mutmut_orig'] = x__classify_severity__mutmut_orig # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_1'] = x__classify_severity__mutmut_1 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_2'] = x__classify_severity__mutmut_2 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_3'] = x__classify_severity__mutmut_3 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_4'] = x__classify_severity__mutmut_4 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_5'] = x__classify_severity__mutmut_5 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_6'] = x__classify_severity__mutmut_6 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_7'] = x__classify_severity__mutmut_7 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_8'] = x__classify_severity__mutmut_8 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_9'] = x__classify_severity__mutmut_9 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_10'] = x__classify_severity__mutmut_10 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_11'] = x__classify_severity__mutmut_11 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_12'] = x__classify_severity__mutmut_12 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_13'] = x__classify_severity__mutmut_13 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_14'] = x__classify_severity__mutmut_14 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_15'] = x__classify_severity__mutmut_15 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_16'] = x__classify_severity__mutmut_16 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_17'] = x__classify_severity__mutmut_17 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_18'] = x__classify_severity__mutmut_18 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_19'] = x__classify_severity__mutmut_19 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_20'] = x__classify_severity__mutmut_20 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_21'] = x__classify_severity__mutmut_21 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_22'] = x__classify_severity__mutmut_22 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_23'] = x__classify_severity__mutmut_23 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_24'] = x__classify_severity__mutmut_24 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_25'] = x__classify_severity__mutmut_25 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_26'] = x__classify_severity__mutmut_26 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_27'] = x__classify_severity__mutmut_27 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_28'] = x__classify_severity__mutmut_28 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_29'] = x__classify_severity__mutmut_29 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_30'] = x__classify_severity__mutmut_30 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_31'] = x__classify_severity__mutmut_31 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_32'] = x__classify_severity__mutmut_32 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_33'] = x__classify_severity__mutmut_33 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_34'] = x__classify_severity__mutmut_34 # type: ignore # mutmut generated
mutants_x__classify_severity__mutmut['x__classify_severity__mutmut_35'] = x__classify_severity__mutmut_35 # type: ignore # mutmut generated
mutants_x__suggest_readiness_probe__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__suggest_readiness_probe__mutmut)
def _suggest_readiness_probe(port: int) -> str:
    if port == 0:
        return "exec: not supported"
    if port in _HTTP_PORTS:
        return f"httpGet: /health path: {port}, initialDelaySeconds: 10"
    return f"tcpSocket: {port}, initialDelaySeconds: 10"


def x__suggest_readiness_probe__mutmut_orig(port: int) -> str:
    if port == 0:
        return "exec: not supported"
    if port in _HTTP_PORTS:
        return f"httpGet: /health path: {port}, initialDelaySeconds: 10"
    return f"tcpSocket: {port}, initialDelaySeconds: 10"


def x__suggest_readiness_probe__mutmut_1(port: int) -> str:
    if port != 0:
        return "exec: not supported"
    if port in _HTTP_PORTS:
        return f"httpGet: /health path: {port}, initialDelaySeconds: 10"
    return f"tcpSocket: {port}, initialDelaySeconds: 10"


def x__suggest_readiness_probe__mutmut_2(port: int) -> str:
    if port == 1:
        return "exec: not supported"
    if port in _HTTP_PORTS:
        return f"httpGet: /health path: {port}, initialDelaySeconds: 10"
    return f"tcpSocket: {port}, initialDelaySeconds: 10"


def x__suggest_readiness_probe__mutmut_3(port: int) -> str:
    if port == 0:
        return "XXexec: not supportedXX"
    if port in _HTTP_PORTS:
        return f"httpGet: /health path: {port}, initialDelaySeconds: 10"
    return f"tcpSocket: {port}, initialDelaySeconds: 10"


def x__suggest_readiness_probe__mutmut_4(port: int) -> str:
    if port == 0:
        return "EXEC: NOT SUPPORTED"
    if port in _HTTP_PORTS:
        return f"httpGet: /health path: {port}, initialDelaySeconds: 10"
    return f"tcpSocket: {port}, initialDelaySeconds: 10"


def x__suggest_readiness_probe__mutmut_5(port: int) -> str:
    if port == 0:
        return "exec: not supported"
    if port not in _HTTP_PORTS:
        return f"httpGet: /health path: {port}, initialDelaySeconds: 10"
    return f"tcpSocket: {port}, initialDelaySeconds: 10"

mutants_x__suggest_readiness_probe__mutmut['_mutmut_orig'] = x__suggest_readiness_probe__mutmut_orig # type: ignore # mutmut generated
mutants_x__suggest_readiness_probe__mutmut['x__suggest_readiness_probe__mutmut_1'] = x__suggest_readiness_probe__mutmut_1 # type: ignore # mutmut generated
mutants_x__suggest_readiness_probe__mutmut['x__suggest_readiness_probe__mutmut_2'] = x__suggest_readiness_probe__mutmut_2 # type: ignore # mutmut generated
mutants_x__suggest_readiness_probe__mutmut['x__suggest_readiness_probe__mutmut_3'] = x__suggest_readiness_probe__mutmut_3 # type: ignore # mutmut generated
mutants_x__suggest_readiness_probe__mutmut['x__suggest_readiness_probe__mutmut_4'] = x__suggest_readiness_probe__mutmut_4 # type: ignore # mutmut generated
mutants_x__suggest_readiness_probe__mutmut['x__suggest_readiness_probe__mutmut_5'] = x__suggest_readiness_probe__mutmut_5 # type: ignore # mutmut generated
mutants_x__suggest_liveness_probe__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__suggest_liveness_probe__mutmut)
def _suggest_liveness_probe(port: int) -> str:
    if port == 0:
        return "exec: not supported"
    if port in _HTTP_PORTS:
        return f"httpGet: /health path: {port}, periodSeconds: 30"
    return f"tcpSocket: {port}, periodSeconds: 30"


def x__suggest_liveness_probe__mutmut_orig(port: int) -> str:
    if port == 0:
        return "exec: not supported"
    if port in _HTTP_PORTS:
        return f"httpGet: /health path: {port}, periodSeconds: 30"
    return f"tcpSocket: {port}, periodSeconds: 30"


def x__suggest_liveness_probe__mutmut_1(port: int) -> str:
    if port != 0:
        return "exec: not supported"
    if port in _HTTP_PORTS:
        return f"httpGet: /health path: {port}, periodSeconds: 30"
    return f"tcpSocket: {port}, periodSeconds: 30"


def x__suggest_liveness_probe__mutmut_2(port: int) -> str:
    if port == 1:
        return "exec: not supported"
    if port in _HTTP_PORTS:
        return f"httpGet: /health path: {port}, periodSeconds: 30"
    return f"tcpSocket: {port}, periodSeconds: 30"


def x__suggest_liveness_probe__mutmut_3(port: int) -> str:
    if port == 0:
        return "XXexec: not supportedXX"
    if port in _HTTP_PORTS:
        return f"httpGet: /health path: {port}, periodSeconds: 30"
    return f"tcpSocket: {port}, periodSeconds: 30"


def x__suggest_liveness_probe__mutmut_4(port: int) -> str:
    if port == 0:
        return "EXEC: NOT SUPPORTED"
    if port in _HTTP_PORTS:
        return f"httpGet: /health path: {port}, periodSeconds: 30"
    return f"tcpSocket: {port}, periodSeconds: 30"


def x__suggest_liveness_probe__mutmut_5(port: int) -> str:
    if port == 0:
        return "exec: not supported"
    if port not in _HTTP_PORTS:
        return f"httpGet: /health path: {port}, periodSeconds: 30"
    return f"tcpSocket: {port}, periodSeconds: 30"

mutants_x__suggest_liveness_probe__mutmut['_mutmut_orig'] = x__suggest_liveness_probe__mutmut_orig # type: ignore # mutmut generated
mutants_x__suggest_liveness_probe__mutmut['x__suggest_liveness_probe__mutmut_1'] = x__suggest_liveness_probe__mutmut_1 # type: ignore # mutmut generated
mutants_x__suggest_liveness_probe__mutmut['x__suggest_liveness_probe__mutmut_2'] = x__suggest_liveness_probe__mutmut_2 # type: ignore # mutmut generated
mutants_x__suggest_liveness_probe__mutmut['x__suggest_liveness_probe__mutmut_3'] = x__suggest_liveness_probe__mutmut_3 # type: ignore # mutmut generated
mutants_x__suggest_liveness_probe__mutmut['x__suggest_liveness_probe__mutmut_4'] = x__suggest_liveness_probe__mutmut_4 # type: ignore # mutmut generated
mutants_x__suggest_liveness_probe__mutmut['x__suggest_liveness_probe__mutmut_5'] = x__suggest_liveness_probe__mutmut_5 # type: ignore # mutmut generated
mutants_x__first_port__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__first_port__mutmut)
def _first_port(containers: list[dict[str, object]]) -> int:
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        ports = _exposed_port_ints(c)
        if ports:
            return ports[0]
    return 0


def x__first_port__mutmut_orig(containers: list[dict[str, object]]) -> int:
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        ports = _exposed_port_ints(c)
        if ports:
            return ports[0]
    return 0


def x__first_port__mutmut_1(containers: list[dict[str, object]]) -> int:
    for c in containers:
        if _as_bool(None):
            continue
        ports = _exposed_port_ints(c)
        if ports:
            return ports[0]
    return 0


def x__first_port__mutmut_2(containers: list[dict[str, object]]) -> int:
    for c in containers:
        if _as_bool(c.get(None)):
            continue
        ports = _exposed_port_ints(c)
        if ports:
            return ports[0]
    return 0


def x__first_port__mutmut_3(containers: list[dict[str, object]]) -> int:
    for c in containers:
        if _as_bool(c.get("XXis_init_containerXX")):
            continue
        ports = _exposed_port_ints(c)
        if ports:
            return ports[0]
    return 0


def x__first_port__mutmut_4(containers: list[dict[str, object]]) -> int:
    for c in containers:
        if _as_bool(c.get("IS_INIT_CONTAINER")):
            continue
        ports = _exposed_port_ints(c)
        if ports:
            return ports[0]
    return 0


def x__first_port__mutmut_5(containers: list[dict[str, object]]) -> int:
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            break
        ports = _exposed_port_ints(c)
        if ports:
            return ports[0]
    return 0


def x__first_port__mutmut_6(containers: list[dict[str, object]]) -> int:
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        ports = None
        if ports:
            return ports[0]
    return 0


def x__first_port__mutmut_7(containers: list[dict[str, object]]) -> int:
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        ports = _exposed_port_ints(None)
        if ports:
            return ports[0]
    return 0


def x__first_port__mutmut_8(containers: list[dict[str, object]]) -> int:
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        ports = _exposed_port_ints(c)
        if ports:
            return ports[1]
    return 0


def x__first_port__mutmut_9(containers: list[dict[str, object]]) -> int:
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        ports = _exposed_port_ints(c)
        if ports:
            return ports[0]
    return 1

mutants_x__first_port__mutmut['_mutmut_orig'] = x__first_port__mutmut_orig # type: ignore # mutmut generated
mutants_x__first_port__mutmut['x__first_port__mutmut_1'] = x__first_port__mutmut_1 # type: ignore # mutmut generated
mutants_x__first_port__mutmut['x__first_port__mutmut_2'] = x__first_port__mutmut_2 # type: ignore # mutmut generated
mutants_x__first_port__mutmut['x__first_port__mutmut_3'] = x__first_port__mutmut_3 # type: ignore # mutmut generated
mutants_x__first_port__mutmut['x__first_port__mutmut_4'] = x__first_port__mutmut_4 # type: ignore # mutmut generated
mutants_x__first_port__mutmut['x__first_port__mutmut_5'] = x__first_port__mutmut_5 # type: ignore # mutmut generated
mutants_x__first_port__mutmut['x__first_port__mutmut_6'] = x__first_port__mutmut_6 # type: ignore # mutmut generated
mutants_x__first_port__mutmut['x__first_port__mutmut_7'] = x__first_port__mutmut_7 # type: ignore # mutmut generated
mutants_x__first_port__mutmut['x__first_port__mutmut_8'] = x__first_port__mutmut_8 # type: ignore # mutmut generated
mutants_x__first_port__mutmut['x__first_port__mutmut_9'] = x__first_port__mutmut_9 # type: ignore # mutmut generated
mutants_x__as_bool__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_bool__mutmut)
def _as_bool(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_orig(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_1(value: object) -> bool:
    if value is not None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_2(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_3(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(None)

mutants_x__as_bool__mutmut['_mutmut_orig'] = x__as_bool__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_bool__mutmut['x__as_bool__mutmut_1'] = x__as_bool__mutmut_1 # type: ignore # mutmut generated
mutants_x__as_bool__mutmut['x__as_bool__mutmut_2'] = x__as_bool__mutmut_2 # type: ignore # mutmut generated
mutants_x__as_bool__mutmut['x__as_bool__mutmut_3'] = x__as_bool__mutmut_3 # type: ignore # mutmut generated
mutants_x__as_int__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_int__mutmut)
def _as_int(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_orig(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_1(value: object) -> int:
    if value is not None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_2(value: object) -> int:
    if value is None:
        return 1
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_3(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(None)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_4(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(None))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_5(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 1

mutants_x__as_int__mutmut['_mutmut_orig'] = x__as_int__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_1'] = x__as_int__mutmut_1 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_2'] = x__as_int__mutmut_2 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_3'] = x__as_int__mutmut_3 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_4'] = x__as_int__mutmut_4 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_5'] = x__as_int__mutmut_5 # type: ignore # mutmut generated
