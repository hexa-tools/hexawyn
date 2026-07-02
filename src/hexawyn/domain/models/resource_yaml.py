from __future__ import annotations

from dataclasses import dataclass
from typing import cast


@dataclass(frozen=True)
class ResourceYAMLRequest:
    resource_name: str
    namespace: str
    kind: str


@dataclass(frozen=True)
class ResourceYAMLResult:
    resource_name: str
    namespace: str
    kind: str
    resource_found: bool
    yaml_data: dict[str, object]
    image_tags: list[str]
    resource_limits: dict[str, str]
    resource_requests: dict[str, str]

    @staticmethod
    def _extract_image_tags(data: dict[str, object]) -> list[str]:
        tags: list[str] = []
        try:
            spec = cast(dict[str, object], data.get("spec", {}))
            template = cast(dict[str, object], spec.get("template", {}))
            pod_spec = cast(dict[str, object], template.get("spec", {}))
            containers = cast(list[dict[str, object]], pod_spec.get("containers", []))
            for c in containers:
                img = str(c.get("image", ""))
                if img:
                    tags.append(img)
            init_containers = cast(list[dict[str, object]], pod_spec.get("initContainers", []))
            for c in init_containers:
                img = str(c.get("image", ""))
                if img:
                    tags.append(img)
        except Exception:
            pass
        return tags

    @staticmethod
    def _extract_limits(data: dict[str, object]) -> dict[str, str]:
        result: dict[str, str] = {}
        try:
            spec = cast(dict[str, object], data.get("spec", {}))
            template = cast(dict[str, object], spec.get("template", {}))
            pod_spec = cast(dict[str, object], template.get("spec", {}))
            containers = cast(list[dict[str, object]], pod_spec.get("containers", []))
            if containers:
                resources = cast(dict[str, object], containers[0].get("resources", {}))
                limits = cast(dict[str, object], resources.get("limits", {}))
                result = {str(k): str(v) for k, v in limits.items()}
        except Exception:
            pass
        return result

    @staticmethod
    def _extract_requests(data: dict[str, object]) -> dict[str, str]:
        result: dict[str, str] = {}
        try:
            spec = cast(dict[str, object], data.get("spec", {}))
            template = cast(dict[str, object], spec.get("template", {}))
            pod_spec = cast(dict[str, object], template.get("spec", {}))
            containers = cast(list[dict[str, object]], pod_spec.get("containers", []))
            if containers:
                resources = cast(dict[str, object], containers[0].get("resources", {}))
                requests = cast(dict[str, object], resources.get("requests", {}))
                result = {str(k): str(v) for k, v in requests.items()}
        except Exception:
            pass
        return result

    @staticmethod
    def _redact_secret(data: dict[str, object]) -> dict[str, object]:
        if data.get("kind") == "Secret" and "data" in data:
            data_val = cast(dict[str, object], data.get("data", {}))
            redacted = {k: "***REDACTED***" for k in data_val}
            result = dict(data)
            result["data"] = redacted
            return result
        return data

    @staticmethod
    def compute(
        request: ResourceYAMLRequest,
        yaml_data: dict[str, object],
        resource_found: bool,
    ) -> ResourceYAMLResult:
        if not resource_found:
            return ResourceYAMLResult(
                resource_name=request.resource_name,
                namespace=request.namespace,
                kind=request.kind,
                resource_found=False,
                yaml_data={},
                image_tags=[],
                resource_limits={},
                resource_requests={},
            )

        redacted = ResourceYAMLResult._redact_secret(yaml_data)
        return ResourceYAMLResult(
            resource_name=request.resource_name,
            namespace=request.namespace,
            kind=request.kind,
            resource_found=True,
            yaml_data=redacted,
            image_tags=ResourceYAMLResult._extract_image_tags(yaml_data),
            resource_limits=ResourceYAMLResult._extract_limits(yaml_data),
            resource_requests=ResourceYAMLResult._extract_requests(yaml_data),
        )
