from __future__ import annotations

from collections.abc import Mapping


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_container_images__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_container_images__mutmut)
def get_container_images(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_orig(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_1(data: Mapping[str, object]) -> dict[str, str]:
    spec = None
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_2(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get(None)
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_3(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("XXspecXX")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_4(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("SPEC")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_5(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_6(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = None
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_7(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get(None)
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_8(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("XXtemplateXX")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_9(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("TEMPLATE")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_10(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_11(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = None
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_12(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get(None)
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_13(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("XXspecXX")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_14(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("SPEC")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_15(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_16(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = None
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_17(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get(None)
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_18(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("XXcontainersXX")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_19(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("CONTAINERS")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_20(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_21(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = None
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_22(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_23(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            break
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_24(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = None
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_25(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get(None)
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_26(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("XXnameXX")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_27(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("NAME")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_28(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = None
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_29(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get(None)
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_30(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("XXimageXX")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_31(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("IMAGE")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_32(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) or isinstance(image, str):
            result[name] = image
    return result


def x_get_container_images__mutmut_33(data: Mapping[str, object]) -> dict[str, str]:
    spec = data.get("spec")
    if not isinstance(spec, Mapping):
        return {}
    template = spec.get("template")
    if not isinstance(template, Mapping):
        return {}
    pod_spec = template.get("spec")
    if not isinstance(pod_spec, Mapping):
        return {}
    containers = pod_spec.get("containers")
    if not isinstance(containers, list):
        return {}

    result: dict[str, str] = {}
    for container in containers:
        if not isinstance(container, Mapping):
            continue
        name = container.get("name")
        image = container.get("image")
        if isinstance(name, str) and isinstance(image, str):
            result[name] = None
    return result

mutants_x_get_container_images__mutmut['_mutmut_orig'] = x_get_container_images__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_1'] = x_get_container_images__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_2'] = x_get_container_images__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_3'] = x_get_container_images__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_4'] = x_get_container_images__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_5'] = x_get_container_images__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_6'] = x_get_container_images__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_7'] = x_get_container_images__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_8'] = x_get_container_images__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_9'] = x_get_container_images__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_10'] = x_get_container_images__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_11'] = x_get_container_images__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_12'] = x_get_container_images__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_13'] = x_get_container_images__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_14'] = x_get_container_images__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_15'] = x_get_container_images__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_16'] = x_get_container_images__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_17'] = x_get_container_images__mutmut_17 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_18'] = x_get_container_images__mutmut_18 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_19'] = x_get_container_images__mutmut_19 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_20'] = x_get_container_images__mutmut_20 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_21'] = x_get_container_images__mutmut_21 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_22'] = x_get_container_images__mutmut_22 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_23'] = x_get_container_images__mutmut_23 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_24'] = x_get_container_images__mutmut_24 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_25'] = x_get_container_images__mutmut_25 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_26'] = x_get_container_images__mutmut_26 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_27'] = x_get_container_images__mutmut_27 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_28'] = x_get_container_images__mutmut_28 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_29'] = x_get_container_images__mutmut_29 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_30'] = x_get_container_images__mutmut_30 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_31'] = x_get_container_images__mutmut_31 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_32'] = x_get_container_images__mutmut_32 # type: ignore # mutmut generated
mutants_x_get_container_images__mutmut['x_get_container_images__mutmut_33'] = x_get_container_images__mutmut_33 # type: ignore # mutmut generated
