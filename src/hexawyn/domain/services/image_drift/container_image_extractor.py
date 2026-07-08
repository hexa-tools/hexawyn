from __future__ import annotations

from collections.abc import Mapping


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
