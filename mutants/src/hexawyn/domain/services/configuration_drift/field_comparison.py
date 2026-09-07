from __future__ import annotations

from collections.abc import Mapping

from hexawyn.domain.models.configuration_drift import DriftedField
from hexawyn.domain.services.configuration_drift.drift_severity import classify_severity

_ABSENT = "<absent>"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_image__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_image__mutmut)
def get_image(data: Mapping[str, object]) -> str | None:
    """First container's image — mirrors resource_yaml.py's ResourceYAMLResult
    convention of first-container-only for pod-template fields."""
    containers = _get_containers(data)
    if not containers:
        return None
    image = containers[0].get("image")
    return str(image) if image is not None else None


def x_get_image__mutmut_orig(data: Mapping[str, object]) -> str | None:
    """First container's image — mirrors resource_yaml.py's ResourceYAMLResult
    convention of first-container-only for pod-template fields."""
    containers = _get_containers(data)
    if not containers:
        return None
    image = containers[0].get("image")
    return str(image) if image is not None else None


def x_get_image__mutmut_1(data: Mapping[str, object]) -> str | None:
    """First container's image — mirrors resource_yaml.py's ResourceYAMLResult
    convention of first-container-only for pod-template fields."""
    containers = None
    if not containers:
        return None
    image = containers[0].get("image")
    return str(image) if image is not None else None


def x_get_image__mutmut_2(data: Mapping[str, object]) -> str | None:
    """First container's image — mirrors resource_yaml.py's ResourceYAMLResult
    convention of first-container-only for pod-template fields."""
    containers = _get_containers(None)
    if not containers:
        return None
    image = containers[0].get("image")
    return str(image) if image is not None else None


def x_get_image__mutmut_3(data: Mapping[str, object]) -> str | None:
    """First container's image — mirrors resource_yaml.py's ResourceYAMLResult
    convention of first-container-only for pod-template fields."""
    containers = _get_containers(data)
    if containers:
        return None
    image = containers[0].get("image")
    return str(image) if image is not None else None


def x_get_image__mutmut_4(data: Mapping[str, object]) -> str | None:
    """First container's image — mirrors resource_yaml.py's ResourceYAMLResult
    convention of first-container-only for pod-template fields."""
    containers = _get_containers(data)
    if not containers:
        return None
    image = None
    return str(image) if image is not None else None


def x_get_image__mutmut_5(data: Mapping[str, object]) -> str | None:
    """First container's image — mirrors resource_yaml.py's ResourceYAMLResult
    convention of first-container-only for pod-template fields."""
    containers = _get_containers(data)
    if not containers:
        return None
    image = containers[0].get(None)
    return str(image) if image is not None else None


def x_get_image__mutmut_6(data: Mapping[str, object]) -> str | None:
    """First container's image — mirrors resource_yaml.py's ResourceYAMLResult
    convention of first-container-only for pod-template fields."""
    containers = _get_containers(data)
    if not containers:
        return None
    image = containers[1].get("image")
    return str(image) if image is not None else None


def x_get_image__mutmut_7(data: Mapping[str, object]) -> str | None:
    """First container's image — mirrors resource_yaml.py's ResourceYAMLResult
    convention of first-container-only for pod-template fields."""
    containers = _get_containers(data)
    if not containers:
        return None
    image = containers[0].get("XXimageXX")
    return str(image) if image is not None else None


def x_get_image__mutmut_8(data: Mapping[str, object]) -> str | None:
    """First container's image — mirrors resource_yaml.py's ResourceYAMLResult
    convention of first-container-only for pod-template fields."""
    containers = _get_containers(data)
    if not containers:
        return None
    image = containers[0].get("IMAGE")
    return str(image) if image is not None else None


def x_get_image__mutmut_9(data: Mapping[str, object]) -> str | None:
    """First container's image — mirrors resource_yaml.py's ResourceYAMLResult
    convention of first-container-only for pod-template fields."""
    containers = _get_containers(data)
    if not containers:
        return None
    image = containers[0].get("image")
    return str(None) if image is not None else None


def x_get_image__mutmut_10(data: Mapping[str, object]) -> str | None:
    """First container's image — mirrors resource_yaml.py's ResourceYAMLResult
    convention of first-container-only for pod-template fields."""
    containers = _get_containers(data)
    if not containers:
        return None
    image = containers[0].get("image")
    return str(image) if image is None else None

mutants_x_get_image__mutmut['_mutmut_orig'] = x_get_image__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_image__mutmut['x_get_image__mutmut_1'] = x_get_image__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_image__mutmut['x_get_image__mutmut_2'] = x_get_image__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_image__mutmut['x_get_image__mutmut_3'] = x_get_image__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_image__mutmut['x_get_image__mutmut_4'] = x_get_image__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_image__mutmut['x_get_image__mutmut_5'] = x_get_image__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_image__mutmut['x_get_image__mutmut_6'] = x_get_image__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_image__mutmut['x_get_image__mutmut_7'] = x_get_image__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_image__mutmut['x_get_image__mutmut_8'] = x_get_image__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_image__mutmut['x_get_image__mutmut_9'] = x_get_image__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_image__mutmut['x_get_image__mutmut_10'] = x_get_image__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_replicas__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_replicas__mutmut)
def get_replicas(data: Mapping[str, object]) -> int | None:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return None
    replicas = spec.get("replicas")
    return replicas if isinstance(replicas, int) else None


def x_get_replicas__mutmut_orig(data: Mapping[str, object]) -> int | None:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return None
    replicas = spec.get("replicas")
    return replicas if isinstance(replicas, int) else None


def x_get_replicas__mutmut_1(data: Mapping[str, object]) -> int | None:
    spec = None
    if not isinstance(spec, dict):
        return None
    replicas = spec.get("replicas")
    return replicas if isinstance(replicas, int) else None


def x_get_replicas__mutmut_2(data: Mapping[str, object]) -> int | None:
    spec = data.get(None)
    if not isinstance(spec, dict):
        return None
    replicas = spec.get("replicas")
    return replicas if isinstance(replicas, int) else None


def x_get_replicas__mutmut_3(data: Mapping[str, object]) -> int | None:
    spec = data.get("XXspecXX")
    if not isinstance(spec, dict):
        return None
    replicas = spec.get("replicas")
    return replicas if isinstance(replicas, int) else None


def x_get_replicas__mutmut_4(data: Mapping[str, object]) -> int | None:
    spec = data.get("SPEC")
    if not isinstance(spec, dict):
        return None
    replicas = spec.get("replicas")
    return replicas if isinstance(replicas, int) else None


def x_get_replicas__mutmut_5(data: Mapping[str, object]) -> int | None:
    spec = data.get("spec")
    if isinstance(spec, dict):
        return None
    replicas = spec.get("replicas")
    return replicas if isinstance(replicas, int) else None


def x_get_replicas__mutmut_6(data: Mapping[str, object]) -> int | None:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return None
    replicas = None
    return replicas if isinstance(replicas, int) else None


def x_get_replicas__mutmut_7(data: Mapping[str, object]) -> int | None:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return None
    replicas = spec.get(None)
    return replicas if isinstance(replicas, int) else None


def x_get_replicas__mutmut_8(data: Mapping[str, object]) -> int | None:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return None
    replicas = spec.get("XXreplicasXX")
    return replicas if isinstance(replicas, int) else None


def x_get_replicas__mutmut_9(data: Mapping[str, object]) -> int | None:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return None
    replicas = spec.get("REPLICAS")
    return replicas if isinstance(replicas, int) else None

mutants_x_get_replicas__mutmut['_mutmut_orig'] = x_get_replicas__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_replicas__mutmut['x_get_replicas__mutmut_1'] = x_get_replicas__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_replicas__mutmut['x_get_replicas__mutmut_2'] = x_get_replicas__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_replicas__mutmut['x_get_replicas__mutmut_3'] = x_get_replicas__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_replicas__mutmut['x_get_replicas__mutmut_4'] = x_get_replicas__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_replicas__mutmut['x_get_replicas__mutmut_5'] = x_get_replicas__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_replicas__mutmut['x_get_replicas__mutmut_6'] = x_get_replicas__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_replicas__mutmut['x_get_replicas__mutmut_7'] = x_get_replicas__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_replicas__mutmut['x_get_replicas__mutmut_8'] = x_get_replicas__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_replicas__mutmut['x_get_replicas__mutmut_9'] = x_get_replicas__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_env_vars__mutmut)
def get_env_vars(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = str(item.get("value", ""))
    return result


def x_get_env_vars__mutmut_orig(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = str(item.get("value", ""))
    return result


def x_get_env_vars__mutmut_1(data: Mapping[str, object]) -> dict[str, str]:
    containers = None
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = str(item.get("value", ""))
    return result


def x_get_env_vars__mutmut_2(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(None)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = str(item.get("value", ""))
    return result


def x_get_env_vars__mutmut_3(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = str(item.get("value", ""))
    return result


def x_get_env_vars__mutmut_4(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = None
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = str(item.get("value", ""))
    return result


def x_get_env_vars__mutmut_5(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get(None)
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = str(item.get("value", ""))
    return result


def x_get_env_vars__mutmut_6(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[1].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = str(item.get("value", ""))
    return result


def x_get_env_vars__mutmut_7(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("XXenvXX")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = str(item.get("value", ""))
    return result


def x_get_env_vars__mutmut_8(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("ENV")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = str(item.get("value", ""))
    return result


def x_get_env_vars__mutmut_9(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = str(item.get("value", ""))
    return result


def x_get_env_vars__mutmut_10(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = None
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = str(item.get("value", ""))
    return result


def x_get_env_vars__mutmut_11(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) or "name" in item:
            result[str(item["name"])] = str(item.get("value", ""))
    return result


def x_get_env_vars__mutmut_12(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "XXnameXX" in item:
            result[str(item["name"])] = str(item.get("value", ""))
    return result


def x_get_env_vars__mutmut_13(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "NAME" in item:
            result[str(item["name"])] = str(item.get("value", ""))
    return result


def x_get_env_vars__mutmut_14(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" not in item:
            result[str(item["name"])] = str(item.get("value", ""))
    return result


def x_get_env_vars__mutmut_15(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = None
    return result


def x_get_env_vars__mutmut_16(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(None)] = str(item.get("value", ""))
    return result


def x_get_env_vars__mutmut_17(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["XXnameXX"])] = str(item.get("value", ""))
    return result


def x_get_env_vars__mutmut_18(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["NAME"])] = str(item.get("value", ""))
    return result


def x_get_env_vars__mutmut_19(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = str(None)
    return result


def x_get_env_vars__mutmut_20(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = str(item.get(None, ""))
    return result


def x_get_env_vars__mutmut_21(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = str(item.get("value", None))
    return result


def x_get_env_vars__mutmut_22(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = str(item.get(""))
    return result


def x_get_env_vars__mutmut_23(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = str(item.get("value", ))
    return result


def x_get_env_vars__mutmut_24(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = str(item.get("XXvalueXX", ""))
    return result


def x_get_env_vars__mutmut_25(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = str(item.get("VALUE", ""))
    return result


def x_get_env_vars__mutmut_26(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    env_list = containers[0].get("env")
    if not isinstance(env_list, list):
        return {}
    result: dict[str, str] = {}
    for item in env_list:
        if isinstance(item, dict) and "name" in item:
            result[str(item["name"])] = str(item.get("value", "XXXX"))
    return result

mutants_x_get_env_vars__mutmut['_mutmut_orig'] = x_get_env_vars__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_1'] = x_get_env_vars__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_2'] = x_get_env_vars__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_3'] = x_get_env_vars__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_4'] = x_get_env_vars__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_5'] = x_get_env_vars__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_6'] = x_get_env_vars__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_7'] = x_get_env_vars__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_8'] = x_get_env_vars__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_9'] = x_get_env_vars__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_10'] = x_get_env_vars__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_11'] = x_get_env_vars__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_12'] = x_get_env_vars__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_13'] = x_get_env_vars__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_14'] = x_get_env_vars__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_15'] = x_get_env_vars__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_16'] = x_get_env_vars__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_17'] = x_get_env_vars__mutmut_17 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_18'] = x_get_env_vars__mutmut_18 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_19'] = x_get_env_vars__mutmut_19 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_20'] = x_get_env_vars__mutmut_20 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_21'] = x_get_env_vars__mutmut_21 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_22'] = x_get_env_vars__mutmut_22 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_23'] = x_get_env_vars__mutmut_23 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_24'] = x_get_env_vars__mutmut_24 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_25'] = x_get_env_vars__mutmut_25 # type: ignore # mutmut generated
mutants_x_get_env_vars__mutmut['x_get_env_vars__mutmut_26'] = x_get_env_vars__mutmut_26 # type: ignore # mutmut generated
mutants_x_get_resource_limits__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_resource_limits__mutmut)
def get_resource_limits(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    resources = containers[0].get("resources")
    if not isinstance(resources, dict):
        return {}
    limits = resources.get("limits")
    if not isinstance(limits, dict):
        return {}
    return {str(key): str(value) for key, value in limits.items()}


def x_get_resource_limits__mutmut_orig(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    resources = containers[0].get("resources")
    if not isinstance(resources, dict):
        return {}
    limits = resources.get("limits")
    if not isinstance(limits, dict):
        return {}
    return {str(key): str(value) for key, value in limits.items()}


def x_get_resource_limits__mutmut_1(data: Mapping[str, object]) -> dict[str, str]:
    containers = None
    if not containers:
        return {}
    resources = containers[0].get("resources")
    if not isinstance(resources, dict):
        return {}
    limits = resources.get("limits")
    if not isinstance(limits, dict):
        return {}
    return {str(key): str(value) for key, value in limits.items()}


def x_get_resource_limits__mutmut_2(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(None)
    if not containers:
        return {}
    resources = containers[0].get("resources")
    if not isinstance(resources, dict):
        return {}
    limits = resources.get("limits")
    if not isinstance(limits, dict):
        return {}
    return {str(key): str(value) for key, value in limits.items()}


def x_get_resource_limits__mutmut_3(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if containers:
        return {}
    resources = containers[0].get("resources")
    if not isinstance(resources, dict):
        return {}
    limits = resources.get("limits")
    if not isinstance(limits, dict):
        return {}
    return {str(key): str(value) for key, value in limits.items()}


def x_get_resource_limits__mutmut_4(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    resources = None
    if not isinstance(resources, dict):
        return {}
    limits = resources.get("limits")
    if not isinstance(limits, dict):
        return {}
    return {str(key): str(value) for key, value in limits.items()}


def x_get_resource_limits__mutmut_5(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    resources = containers[0].get(None)
    if not isinstance(resources, dict):
        return {}
    limits = resources.get("limits")
    if not isinstance(limits, dict):
        return {}
    return {str(key): str(value) for key, value in limits.items()}


def x_get_resource_limits__mutmut_6(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    resources = containers[1].get("resources")
    if not isinstance(resources, dict):
        return {}
    limits = resources.get("limits")
    if not isinstance(limits, dict):
        return {}
    return {str(key): str(value) for key, value in limits.items()}


def x_get_resource_limits__mutmut_7(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    resources = containers[0].get("XXresourcesXX")
    if not isinstance(resources, dict):
        return {}
    limits = resources.get("limits")
    if not isinstance(limits, dict):
        return {}
    return {str(key): str(value) for key, value in limits.items()}


def x_get_resource_limits__mutmut_8(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    resources = containers[0].get("RESOURCES")
    if not isinstance(resources, dict):
        return {}
    limits = resources.get("limits")
    if not isinstance(limits, dict):
        return {}
    return {str(key): str(value) for key, value in limits.items()}


def x_get_resource_limits__mutmut_9(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    resources = containers[0].get("resources")
    if isinstance(resources, dict):
        return {}
    limits = resources.get("limits")
    if not isinstance(limits, dict):
        return {}
    return {str(key): str(value) for key, value in limits.items()}


def x_get_resource_limits__mutmut_10(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    resources = containers[0].get("resources")
    if not isinstance(resources, dict):
        return {}
    limits = None
    if not isinstance(limits, dict):
        return {}
    return {str(key): str(value) for key, value in limits.items()}


def x_get_resource_limits__mutmut_11(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    resources = containers[0].get("resources")
    if not isinstance(resources, dict):
        return {}
    limits = resources.get(None)
    if not isinstance(limits, dict):
        return {}
    return {str(key): str(value) for key, value in limits.items()}


def x_get_resource_limits__mutmut_12(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    resources = containers[0].get("resources")
    if not isinstance(resources, dict):
        return {}
    limits = resources.get("XXlimitsXX")
    if not isinstance(limits, dict):
        return {}
    return {str(key): str(value) for key, value in limits.items()}


def x_get_resource_limits__mutmut_13(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    resources = containers[0].get("resources")
    if not isinstance(resources, dict):
        return {}
    limits = resources.get("LIMITS")
    if not isinstance(limits, dict):
        return {}
    return {str(key): str(value) for key, value in limits.items()}


def x_get_resource_limits__mutmut_14(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    resources = containers[0].get("resources")
    if not isinstance(resources, dict):
        return {}
    limits = resources.get("limits")
    if isinstance(limits, dict):
        return {}
    return {str(key): str(value) for key, value in limits.items()}


def x_get_resource_limits__mutmut_15(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    resources = containers[0].get("resources")
    if not isinstance(resources, dict):
        return {}
    limits = resources.get("limits")
    if not isinstance(limits, dict):
        return {}
    return {str(None): str(value) for key, value in limits.items()}


def x_get_resource_limits__mutmut_16(data: Mapping[str, object]) -> dict[str, str]:
    containers = _get_containers(data)
    if not containers:
        return {}
    resources = containers[0].get("resources")
    if not isinstance(resources, dict):
        return {}
    limits = resources.get("limits")
    if not isinstance(limits, dict):
        return {}
    return {str(key): str(None) for key, value in limits.items()}

mutants_x_get_resource_limits__mutmut['_mutmut_orig'] = x_get_resource_limits__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_resource_limits__mutmut['x_get_resource_limits__mutmut_1'] = x_get_resource_limits__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_resource_limits__mutmut['x_get_resource_limits__mutmut_2'] = x_get_resource_limits__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_resource_limits__mutmut['x_get_resource_limits__mutmut_3'] = x_get_resource_limits__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_resource_limits__mutmut['x_get_resource_limits__mutmut_4'] = x_get_resource_limits__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_resource_limits__mutmut['x_get_resource_limits__mutmut_5'] = x_get_resource_limits__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_resource_limits__mutmut['x_get_resource_limits__mutmut_6'] = x_get_resource_limits__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_resource_limits__mutmut['x_get_resource_limits__mutmut_7'] = x_get_resource_limits__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_resource_limits__mutmut['x_get_resource_limits__mutmut_8'] = x_get_resource_limits__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_resource_limits__mutmut['x_get_resource_limits__mutmut_9'] = x_get_resource_limits__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_resource_limits__mutmut['x_get_resource_limits__mutmut_10'] = x_get_resource_limits__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_resource_limits__mutmut['x_get_resource_limits__mutmut_11'] = x_get_resource_limits__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_resource_limits__mutmut['x_get_resource_limits__mutmut_12'] = x_get_resource_limits__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_resource_limits__mutmut['x_get_resource_limits__mutmut_13'] = x_get_resource_limits__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_resource_limits__mutmut['x_get_resource_limits__mutmut_14'] = x_get_resource_limits__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_resource_limits__mutmut['x_get_resource_limits__mutmut_15'] = x_get_resource_limits__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_resource_limits__mutmut['x_get_resource_limits__mutmut_16'] = x_get_resource_limits__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_labels__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_labels__mutmut)
def get_labels(data: Mapping[str, object]) -> dict[str, str]:
    metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        return {}
    labels = metadata.get("labels")
    if not isinstance(labels, dict):
        return {}
    return {str(key): str(value) for key, value in labels.items()}


def x_get_labels__mutmut_orig(data: Mapping[str, object]) -> dict[str, str]:
    metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        return {}
    labels = metadata.get("labels")
    if not isinstance(labels, dict):
        return {}
    return {str(key): str(value) for key, value in labels.items()}


def x_get_labels__mutmut_1(data: Mapping[str, object]) -> dict[str, str]:
    metadata = None
    if not isinstance(metadata, dict):
        return {}
    labels = metadata.get("labels")
    if not isinstance(labels, dict):
        return {}
    return {str(key): str(value) for key, value in labels.items()}


def x_get_labels__mutmut_2(data: Mapping[str, object]) -> dict[str, str]:
    metadata = data.get(None)
    if not isinstance(metadata, dict):
        return {}
    labels = metadata.get("labels")
    if not isinstance(labels, dict):
        return {}
    return {str(key): str(value) for key, value in labels.items()}


def x_get_labels__mutmut_3(data: Mapping[str, object]) -> dict[str, str]:
    metadata = data.get("XXmetadataXX")
    if not isinstance(metadata, dict):
        return {}
    labels = metadata.get("labels")
    if not isinstance(labels, dict):
        return {}
    return {str(key): str(value) for key, value in labels.items()}


def x_get_labels__mutmut_4(data: Mapping[str, object]) -> dict[str, str]:
    metadata = data.get("METADATA")
    if not isinstance(metadata, dict):
        return {}
    labels = metadata.get("labels")
    if not isinstance(labels, dict):
        return {}
    return {str(key): str(value) for key, value in labels.items()}


def x_get_labels__mutmut_5(data: Mapping[str, object]) -> dict[str, str]:
    metadata = data.get("metadata")
    if isinstance(metadata, dict):
        return {}
    labels = metadata.get("labels")
    if not isinstance(labels, dict):
        return {}
    return {str(key): str(value) for key, value in labels.items()}


def x_get_labels__mutmut_6(data: Mapping[str, object]) -> dict[str, str]:
    metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        return {}
    labels = None
    if not isinstance(labels, dict):
        return {}
    return {str(key): str(value) for key, value in labels.items()}


def x_get_labels__mutmut_7(data: Mapping[str, object]) -> dict[str, str]:
    metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        return {}
    labels = metadata.get(None)
    if not isinstance(labels, dict):
        return {}
    return {str(key): str(value) for key, value in labels.items()}


def x_get_labels__mutmut_8(data: Mapping[str, object]) -> dict[str, str]:
    metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        return {}
    labels = metadata.get("XXlabelsXX")
    if not isinstance(labels, dict):
        return {}
    return {str(key): str(value) for key, value in labels.items()}


def x_get_labels__mutmut_9(data: Mapping[str, object]) -> dict[str, str]:
    metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        return {}
    labels = metadata.get("LABELS")
    if not isinstance(labels, dict):
        return {}
    return {str(key): str(value) for key, value in labels.items()}


def x_get_labels__mutmut_10(data: Mapping[str, object]) -> dict[str, str]:
    metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        return {}
    labels = metadata.get("labels")
    if isinstance(labels, dict):
        return {}
    return {str(key): str(value) for key, value in labels.items()}


def x_get_labels__mutmut_11(data: Mapping[str, object]) -> dict[str, str]:
    metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        return {}
    labels = metadata.get("labels")
    if not isinstance(labels, dict):
        return {}
    return {str(None): str(value) for key, value in labels.items()}


def x_get_labels__mutmut_12(data: Mapping[str, object]) -> dict[str, str]:
    metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        return {}
    labels = metadata.get("labels")
    if not isinstance(labels, dict):
        return {}
    return {str(key): str(None) for key, value in labels.items()}

mutants_x_get_labels__mutmut['_mutmut_orig'] = x_get_labels__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_labels__mutmut['x_get_labels__mutmut_1'] = x_get_labels__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_labels__mutmut['x_get_labels__mutmut_2'] = x_get_labels__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_labels__mutmut['x_get_labels__mutmut_3'] = x_get_labels__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_labels__mutmut['x_get_labels__mutmut_4'] = x_get_labels__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_labels__mutmut['x_get_labels__mutmut_5'] = x_get_labels__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_labels__mutmut['x_get_labels__mutmut_6'] = x_get_labels__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_labels__mutmut['x_get_labels__mutmut_7'] = x_get_labels__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_labels__mutmut['x_get_labels__mutmut_8'] = x_get_labels__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_labels__mutmut['x_get_labels__mutmut_9'] = x_get_labels__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_labels__mutmut['x_get_labels__mutmut_10'] = x_get_labels__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_labels__mutmut['x_get_labels__mutmut_11'] = x_get_labels__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_labels__mutmut['x_get_labels__mutmut_12'] = x_get_labels__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_configmap_data__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_configmap_data__mutmut)
def get_configmap_data(data: Mapping[str, object]) -> dict[str, str]:
    cm_data = data.get("data")
    if not isinstance(cm_data, dict):
        return {}
    return {str(key): str(value) for key, value in cm_data.items()}


def x_get_configmap_data__mutmut_orig(data: Mapping[str, object]) -> dict[str, str]:
    cm_data = data.get("data")
    if not isinstance(cm_data, dict):
        return {}
    return {str(key): str(value) for key, value in cm_data.items()}


def x_get_configmap_data__mutmut_1(data: Mapping[str, object]) -> dict[str, str]:
    cm_data = None
    if not isinstance(cm_data, dict):
        return {}
    return {str(key): str(value) for key, value in cm_data.items()}


def x_get_configmap_data__mutmut_2(data: Mapping[str, object]) -> dict[str, str]:
    cm_data = data.get(None)
    if not isinstance(cm_data, dict):
        return {}
    return {str(key): str(value) for key, value in cm_data.items()}


def x_get_configmap_data__mutmut_3(data: Mapping[str, object]) -> dict[str, str]:
    cm_data = data.get("XXdataXX")
    if not isinstance(cm_data, dict):
        return {}
    return {str(key): str(value) for key, value in cm_data.items()}


def x_get_configmap_data__mutmut_4(data: Mapping[str, object]) -> dict[str, str]:
    cm_data = data.get("DATA")
    if not isinstance(cm_data, dict):
        return {}
    return {str(key): str(value) for key, value in cm_data.items()}


def x_get_configmap_data__mutmut_5(data: Mapping[str, object]) -> dict[str, str]:
    cm_data = data.get("data")
    if isinstance(cm_data, dict):
        return {}
    return {str(key): str(value) for key, value in cm_data.items()}


def x_get_configmap_data__mutmut_6(data: Mapping[str, object]) -> dict[str, str]:
    cm_data = data.get("data")
    if not isinstance(cm_data, dict):
        return {}
    return {str(None): str(value) for key, value in cm_data.items()}


def x_get_configmap_data__mutmut_7(data: Mapping[str, object]) -> dict[str, str]:
    cm_data = data.get("data")
    if not isinstance(cm_data, dict):
        return {}
    return {str(key): str(None) for key, value in cm_data.items()}

mutants_x_get_configmap_data__mutmut['_mutmut_orig'] = x_get_configmap_data__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_configmap_data__mutmut['x_get_configmap_data__mutmut_1'] = x_get_configmap_data__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_configmap_data__mutmut['x_get_configmap_data__mutmut_2'] = x_get_configmap_data__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_configmap_data__mutmut['x_get_configmap_data__mutmut_3'] = x_get_configmap_data__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_configmap_data__mutmut['x_get_configmap_data__mutmut_4'] = x_get_configmap_data__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_configmap_data__mutmut['x_get_configmap_data__mutmut_5'] = x_get_configmap_data__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_configmap_data__mutmut['x_get_configmap_data__mutmut_6'] = x_get_configmap_data__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_configmap_data__mutmut['x_get_configmap_data__mutmut_7'] = x_get_configmap_data__mutmut_7 # type: ignore # mutmut generated
mutants_x_compare_scalar_field__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compare_scalar_field__mutmut)
def compare_scalar_field(
    field_name: str, desired: object, live: object, resource_kind: str
) -> list[DriftedField]:
    if desired == live:
        return []
    return [
        DriftedField(
            field_path=field_name,
            desired_value=str(desired),
            live_value=str(live),
            severity=classify_severity(field_name, resource_kind),
        )
    ]


def x_compare_scalar_field__mutmut_orig(
    field_name: str, desired: object, live: object, resource_kind: str
) -> list[DriftedField]:
    if desired == live:
        return []
    return [
        DriftedField(
            field_path=field_name,
            desired_value=str(desired),
            live_value=str(live),
            severity=classify_severity(field_name, resource_kind),
        )
    ]


def x_compare_scalar_field__mutmut_1(
    field_name: str, desired: object, live: object, resource_kind: str
) -> list[DriftedField]:
    if desired != live:
        return []
    return [
        DriftedField(
            field_path=field_name,
            desired_value=str(desired),
            live_value=str(live),
            severity=classify_severity(field_name, resource_kind),
        )
    ]


def x_compare_scalar_field__mutmut_2(
    field_name: str, desired: object, live: object, resource_kind: str
) -> list[DriftedField]:
    if desired == live:
        return []
    return [
        DriftedField(
            field_path=None,
            desired_value=str(desired),
            live_value=str(live),
            severity=classify_severity(field_name, resource_kind),
        )
    ]


def x_compare_scalar_field__mutmut_3(
    field_name: str, desired: object, live: object, resource_kind: str
) -> list[DriftedField]:
    if desired == live:
        return []
    return [
        DriftedField(
            field_path=field_name,
            desired_value=None,
            live_value=str(live),
            severity=classify_severity(field_name, resource_kind),
        )
    ]


def x_compare_scalar_field__mutmut_4(
    field_name: str, desired: object, live: object, resource_kind: str
) -> list[DriftedField]:
    if desired == live:
        return []
    return [
        DriftedField(
            field_path=field_name,
            desired_value=str(desired),
            live_value=None,
            severity=classify_severity(field_name, resource_kind),
        )
    ]


def x_compare_scalar_field__mutmut_5(
    field_name: str, desired: object, live: object, resource_kind: str
) -> list[DriftedField]:
    if desired == live:
        return []
    return [
        DriftedField(
            field_path=field_name,
            desired_value=str(desired),
            live_value=str(live),
            severity=None,
        )
    ]


def x_compare_scalar_field__mutmut_6(
    field_name: str, desired: object, live: object, resource_kind: str
) -> list[DriftedField]:
    if desired == live:
        return []
    return [
        DriftedField(
            desired_value=str(desired),
            live_value=str(live),
            severity=classify_severity(field_name, resource_kind),
        )
    ]


def x_compare_scalar_field__mutmut_7(
    field_name: str, desired: object, live: object, resource_kind: str
) -> list[DriftedField]:
    if desired == live:
        return []
    return [
        DriftedField(
            field_path=field_name,
            live_value=str(live),
            severity=classify_severity(field_name, resource_kind),
        )
    ]


def x_compare_scalar_field__mutmut_8(
    field_name: str, desired: object, live: object, resource_kind: str
) -> list[DriftedField]:
    if desired == live:
        return []
    return [
        DriftedField(
            field_path=field_name,
            desired_value=str(desired),
            severity=classify_severity(field_name, resource_kind),
        )
    ]


def x_compare_scalar_field__mutmut_9(
    field_name: str, desired: object, live: object, resource_kind: str
) -> list[DriftedField]:
    if desired == live:
        return []
    return [
        DriftedField(
            field_path=field_name,
            desired_value=str(desired),
            live_value=str(live),
            )
    ]


def x_compare_scalar_field__mutmut_10(
    field_name: str, desired: object, live: object, resource_kind: str
) -> list[DriftedField]:
    if desired == live:
        return []
    return [
        DriftedField(
            field_path=field_name,
            desired_value=str(None),
            live_value=str(live),
            severity=classify_severity(field_name, resource_kind),
        )
    ]


def x_compare_scalar_field__mutmut_11(
    field_name: str, desired: object, live: object, resource_kind: str
) -> list[DriftedField]:
    if desired == live:
        return []
    return [
        DriftedField(
            field_path=field_name,
            desired_value=str(desired),
            live_value=str(None),
            severity=classify_severity(field_name, resource_kind),
        )
    ]


def x_compare_scalar_field__mutmut_12(
    field_name: str, desired: object, live: object, resource_kind: str
) -> list[DriftedField]:
    if desired == live:
        return []
    return [
        DriftedField(
            field_path=field_name,
            desired_value=str(desired),
            live_value=str(live),
            severity=classify_severity(None, resource_kind),
        )
    ]


def x_compare_scalar_field__mutmut_13(
    field_name: str, desired: object, live: object, resource_kind: str
) -> list[DriftedField]:
    if desired == live:
        return []
    return [
        DriftedField(
            field_path=field_name,
            desired_value=str(desired),
            live_value=str(live),
            severity=classify_severity(field_name, None),
        )
    ]


def x_compare_scalar_field__mutmut_14(
    field_name: str, desired: object, live: object, resource_kind: str
) -> list[DriftedField]:
    if desired == live:
        return []
    return [
        DriftedField(
            field_path=field_name,
            desired_value=str(desired),
            live_value=str(live),
            severity=classify_severity(resource_kind),
        )
    ]


def x_compare_scalar_field__mutmut_15(
    field_name: str, desired: object, live: object, resource_kind: str
) -> list[DriftedField]:
    if desired == live:
        return []
    return [
        DriftedField(
            field_path=field_name,
            desired_value=str(desired),
            live_value=str(live),
            severity=classify_severity(field_name, ),
        )
    ]

mutants_x_compare_scalar_field__mutmut['_mutmut_orig'] = x_compare_scalar_field__mutmut_orig # type: ignore # mutmut generated
mutants_x_compare_scalar_field__mutmut['x_compare_scalar_field__mutmut_1'] = x_compare_scalar_field__mutmut_1 # type: ignore # mutmut generated
mutants_x_compare_scalar_field__mutmut['x_compare_scalar_field__mutmut_2'] = x_compare_scalar_field__mutmut_2 # type: ignore # mutmut generated
mutants_x_compare_scalar_field__mutmut['x_compare_scalar_field__mutmut_3'] = x_compare_scalar_field__mutmut_3 # type: ignore # mutmut generated
mutants_x_compare_scalar_field__mutmut['x_compare_scalar_field__mutmut_4'] = x_compare_scalar_field__mutmut_4 # type: ignore # mutmut generated
mutants_x_compare_scalar_field__mutmut['x_compare_scalar_field__mutmut_5'] = x_compare_scalar_field__mutmut_5 # type: ignore # mutmut generated
mutants_x_compare_scalar_field__mutmut['x_compare_scalar_field__mutmut_6'] = x_compare_scalar_field__mutmut_6 # type: ignore # mutmut generated
mutants_x_compare_scalar_field__mutmut['x_compare_scalar_field__mutmut_7'] = x_compare_scalar_field__mutmut_7 # type: ignore # mutmut generated
mutants_x_compare_scalar_field__mutmut['x_compare_scalar_field__mutmut_8'] = x_compare_scalar_field__mutmut_8 # type: ignore # mutmut generated
mutants_x_compare_scalar_field__mutmut['x_compare_scalar_field__mutmut_9'] = x_compare_scalar_field__mutmut_9 # type: ignore # mutmut generated
mutants_x_compare_scalar_field__mutmut['x_compare_scalar_field__mutmut_10'] = x_compare_scalar_field__mutmut_10 # type: ignore # mutmut generated
mutants_x_compare_scalar_field__mutmut['x_compare_scalar_field__mutmut_11'] = x_compare_scalar_field__mutmut_11 # type: ignore # mutmut generated
mutants_x_compare_scalar_field__mutmut['x_compare_scalar_field__mutmut_12'] = x_compare_scalar_field__mutmut_12 # type: ignore # mutmut generated
mutants_x_compare_scalar_field__mutmut['x_compare_scalar_field__mutmut_13'] = x_compare_scalar_field__mutmut_13 # type: ignore # mutmut generated
mutants_x_compare_scalar_field__mutmut['x_compare_scalar_field__mutmut_14'] = x_compare_scalar_field__mutmut_14 # type: ignore # mutmut generated
mutants_x_compare_scalar_field__mutmut['x_compare_scalar_field__mutmut_15'] = x_compare_scalar_field__mutmut_15 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compare_dict_field__mutmut)
def compare_dict_field(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(field_name, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_orig(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(field_name, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_1(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = None
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(field_name, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_2(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(None):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(field_name, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_3(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) & set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(field_name, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_4(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(None) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(field_name, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_5(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(None)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(field_name, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_6(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = None
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(field_name, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_7(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(None)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(field_name, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_8(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = None
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(field_name, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_9(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(None)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(field_name, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_10(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value == live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(field_name, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_11(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                None
            )
    return fields


def x_compare_dict_field__mutmut_12(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=None,
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(field_name, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_13(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=None,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(field_name, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_14(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=None,
                    severity=classify_severity(field_name, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_15(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=None,
                )
            )
    return fields


def x_compare_dict_field__mutmut_16(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(field_name, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_17(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(field_name, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_18(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    severity=classify_severity(field_name, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_19(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    )
            )
    return fields


def x_compare_dict_field__mutmut_20(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(field_name, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_21(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is None else _ABSENT,
                    severity=classify_severity(field_name, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_22(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(None, resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_23(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(field_name, None),
                )
            )
    return fields


def x_compare_dict_field__mutmut_24(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(resource_kind),
                )
            )
    return fields


def x_compare_dict_field__mutmut_25(
    field_name: str, desired: dict[str, str], live: dict[str, str], resource_kind: str
) -> list[DriftedField]:
    fields: list[DriftedField] = []
    for key in sorted(set(desired) | set(live)):
        desired_value = desired.get(key)
        live_value = live.get(key)
        if desired_value != live_value:
            fields.append(
                DriftedField(
                    field_path=f"{field_name}.{key}",
                    desired_value=desired_value if desired_value is not None else _ABSENT,
                    live_value=live_value if live_value is not None else _ABSENT,
                    severity=classify_severity(field_name, ),
                )
            )
    return fields

mutants_x_compare_dict_field__mutmut['_mutmut_orig'] = x_compare_dict_field__mutmut_orig # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_1'] = x_compare_dict_field__mutmut_1 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_2'] = x_compare_dict_field__mutmut_2 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_3'] = x_compare_dict_field__mutmut_3 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_4'] = x_compare_dict_field__mutmut_4 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_5'] = x_compare_dict_field__mutmut_5 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_6'] = x_compare_dict_field__mutmut_6 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_7'] = x_compare_dict_field__mutmut_7 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_8'] = x_compare_dict_field__mutmut_8 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_9'] = x_compare_dict_field__mutmut_9 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_10'] = x_compare_dict_field__mutmut_10 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_11'] = x_compare_dict_field__mutmut_11 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_12'] = x_compare_dict_field__mutmut_12 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_13'] = x_compare_dict_field__mutmut_13 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_14'] = x_compare_dict_field__mutmut_14 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_15'] = x_compare_dict_field__mutmut_15 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_16'] = x_compare_dict_field__mutmut_16 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_17'] = x_compare_dict_field__mutmut_17 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_18'] = x_compare_dict_field__mutmut_18 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_19'] = x_compare_dict_field__mutmut_19 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_20'] = x_compare_dict_field__mutmut_20 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_21'] = x_compare_dict_field__mutmut_21 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_22'] = x_compare_dict_field__mutmut_22 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_23'] = x_compare_dict_field__mutmut_23 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_24'] = x_compare_dict_field__mutmut_24 # type: ignore # mutmut generated
mutants_x_compare_dict_field__mutmut['x_compare_dict_field__mutmut_25'] = x_compare_dict_field__mutmut_25 # type: ignore # mutmut generated
mutants_x__get_containers__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__get_containers__mutmut)
def _get_containers(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return []
    template = spec.get("template")
    if not isinstance(template, dict):
        return []
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_orig(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return []
    template = spec.get("template")
    if not isinstance(template, dict):
        return []
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_1(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = None
    if not isinstance(spec, dict):
        return []
    template = spec.get("template")
    if not isinstance(template, dict):
        return []
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_2(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get(None)
    if not isinstance(spec, dict):
        return []
    template = spec.get("template")
    if not isinstance(template, dict):
        return []
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_3(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get("XXspecXX")
    if not isinstance(spec, dict):
        return []
    template = spec.get("template")
    if not isinstance(template, dict):
        return []
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_4(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get("SPEC")
    if not isinstance(spec, dict):
        return []
    template = spec.get("template")
    if not isinstance(template, dict):
        return []
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_5(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get("spec")
    if isinstance(spec, dict):
        return []
    template = spec.get("template")
    if not isinstance(template, dict):
        return []
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_6(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return []
    template = None
    if not isinstance(template, dict):
        return []
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_7(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return []
    template = spec.get(None)
    if not isinstance(template, dict):
        return []
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_8(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return []
    template = spec.get("XXtemplateXX")
    if not isinstance(template, dict):
        return []
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_9(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return []
    template = spec.get("TEMPLATE")
    if not isinstance(template, dict):
        return []
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_10(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return []
    template = spec.get("template")
    if isinstance(template, dict):
        return []
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_11(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return []
    template = spec.get("template")
    if not isinstance(template, dict):
        return []
    pod_spec = None
    if not isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_12(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return []
    template = spec.get("template")
    if not isinstance(template, dict):
        return []
    pod_spec = template.get(None)
    if not isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_13(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return []
    template = spec.get("template")
    if not isinstance(template, dict):
        return []
    pod_spec = template.get("XXspecXX")
    if not isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_14(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return []
    template = spec.get("template")
    if not isinstance(template, dict):
        return []
    pod_spec = template.get("SPEC")
    if not isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_15(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return []
    template = spec.get("template")
    if not isinstance(template, dict):
        return []
    pod_spec = template.get("spec")
    if isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_16(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return []
    template = spec.get("template")
    if not isinstance(template, dict):
        return []
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, dict):
        return []
    containers = None
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_17(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return []
    template = spec.get("template")
    if not isinstance(template, dict):
        return []
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get(None)
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_18(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return []
    template = spec.get("template")
    if not isinstance(template, dict):
        return []
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get("XXcontainersXX")
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_19(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return []
    template = spec.get("template")
    if not isinstance(template, dict):
        return []
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get("CONTAINERS")
    if not isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]


def x__get_containers__mutmut_20(data: Mapping[str, object]) -> list[Mapping[str, object]]:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return []
    template = spec.get("template")
    if not isinstance(template, dict):
        return []
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, dict):
        return []
    containers = pod_spec.get("containers")
    if isinstance(containers, list):
        return []
    return [container for container in containers if isinstance(container, dict)]

mutants_x__get_containers__mutmut['_mutmut_orig'] = x__get_containers__mutmut_orig # type: ignore # mutmut generated
mutants_x__get_containers__mutmut['x__get_containers__mutmut_1'] = x__get_containers__mutmut_1 # type: ignore # mutmut generated
mutants_x__get_containers__mutmut['x__get_containers__mutmut_2'] = x__get_containers__mutmut_2 # type: ignore # mutmut generated
mutants_x__get_containers__mutmut['x__get_containers__mutmut_3'] = x__get_containers__mutmut_3 # type: ignore # mutmut generated
mutants_x__get_containers__mutmut['x__get_containers__mutmut_4'] = x__get_containers__mutmut_4 # type: ignore # mutmut generated
mutants_x__get_containers__mutmut['x__get_containers__mutmut_5'] = x__get_containers__mutmut_5 # type: ignore # mutmut generated
mutants_x__get_containers__mutmut['x__get_containers__mutmut_6'] = x__get_containers__mutmut_6 # type: ignore # mutmut generated
mutants_x__get_containers__mutmut['x__get_containers__mutmut_7'] = x__get_containers__mutmut_7 # type: ignore # mutmut generated
mutants_x__get_containers__mutmut['x__get_containers__mutmut_8'] = x__get_containers__mutmut_8 # type: ignore # mutmut generated
mutants_x__get_containers__mutmut['x__get_containers__mutmut_9'] = x__get_containers__mutmut_9 # type: ignore # mutmut generated
mutants_x__get_containers__mutmut['x__get_containers__mutmut_10'] = x__get_containers__mutmut_10 # type: ignore # mutmut generated
mutants_x__get_containers__mutmut['x__get_containers__mutmut_11'] = x__get_containers__mutmut_11 # type: ignore # mutmut generated
mutants_x__get_containers__mutmut['x__get_containers__mutmut_12'] = x__get_containers__mutmut_12 # type: ignore # mutmut generated
mutants_x__get_containers__mutmut['x__get_containers__mutmut_13'] = x__get_containers__mutmut_13 # type: ignore # mutmut generated
mutants_x__get_containers__mutmut['x__get_containers__mutmut_14'] = x__get_containers__mutmut_14 # type: ignore # mutmut generated
mutants_x__get_containers__mutmut['x__get_containers__mutmut_15'] = x__get_containers__mutmut_15 # type: ignore # mutmut generated
mutants_x__get_containers__mutmut['x__get_containers__mutmut_16'] = x__get_containers__mutmut_16 # type: ignore # mutmut generated
mutants_x__get_containers__mutmut['x__get_containers__mutmut_17'] = x__get_containers__mutmut_17 # type: ignore # mutmut generated
mutants_x__get_containers__mutmut['x__get_containers__mutmut_18'] = x__get_containers__mutmut_18 # type: ignore # mutmut generated
mutants_x__get_containers__mutmut['x__get_containers__mutmut_19'] = x__get_containers__mutmut_19 # type: ignore # mutmut generated
mutants_x__get_containers__mutmut['x__get_containers__mutmut_20'] = x__get_containers__mutmut_20 # type: ignore # mutmut generated
