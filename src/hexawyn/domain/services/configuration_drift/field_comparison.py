from __future__ import annotations

from collections.abc import Mapping

from hexawyn.domain.models.configuration_drift import DriftedField
from hexawyn.domain.services.configuration_drift.drift_severity import classify_severity

_ABSENT = "<absent>"


def get_image(data: Mapping[str, object]) -> str | None:
    """First container's image — mirrors resource_yaml.py's ResourceYAMLResult
    convention of first-container-only for pod-template fields."""
    containers = _get_containers(data)
    if not containers:
        return None
    image = containers[0].get("image")
    return str(image) if image is not None else None


def get_replicas(data: Mapping[str, object]) -> int | None:
    spec = data.get("spec")
    if not isinstance(spec, dict):
        return None
    replicas = spec.get("replicas")
    return replicas if isinstance(replicas, int) else None


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


def get_labels(data: Mapping[str, object]) -> dict[str, str]:
    metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        return {}
    labels = metadata.get("labels")
    if not isinstance(labels, dict):
        return {}
    return {str(key): str(value) for key, value in labels.items()}


def get_configmap_data(data: Mapping[str, object]) -> dict[str, str]:
    cm_data = data.get("data")
    if not isinstance(cm_data, dict):
        return {}
    return {str(key): str(value) for key, value in cm_data.items()}


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
