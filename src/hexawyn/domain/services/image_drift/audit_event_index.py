from __future__ import annotations

from hexawyn.application.ports.driven.drift_detection_port import ResourceManifestRaw
from hexawyn.application.ports.driven.image_drift_port import ResolvedContainerImageRaw


def index_resolved_images(
    resolved: list[ResolvedContainerImageRaw],
) -> dict[tuple[str, str], str]:
    return {(item["deployment"], item["container"]): item["image_id"] for item in resolved}


def find_matching(
    manifests: list[ResourceManifestRaw], kind: str, name: str
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind and raw["name"] == name:
            return raw
    return None
