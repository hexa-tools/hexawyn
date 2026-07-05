from __future__ import annotations

import subprocess
from pathlib import Path

import yaml
from hexawyn.application.ports.driven.drift_detection_port import (
    DriftDetectionPort,
    ResourceManifestRaw,
)
from hexawyn.domain.errors import KustomizeNotFoundError, ManifestRenderError

_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS = 15.0


class KustomizeDriftAdapter(DriftDetectionPort):
    """Secondary adapter — shells out to the `kustomize` CLI. `source` is a
    local overlay directory path (e.g. `overlays/production`) — the overlay
    is inherently "applied" by rendering that exact path."""

    def render_desired_manifests(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        stdout = self._run(["build", source])
        return _parse_multi_doc_yaml(stdout)

    def source_exists(self, source: str, namespace: str) -> bool:
        """Kustomize has no release-registry concept, unlike Helm — a plain
        path existence check is the closest equivalent, kept symmetric with
        the shared port for orphan-detection generality."""
        return Path(source).exists()

    def _run(self, args: list[str]) -> str:
        command = ["kustomize", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_KUSTOMIZE_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise KustomizeNotFoundError() from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="kustomize command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout


def _parse_multi_doc_yaml(stdout: str) -> list[ResourceManifestRaw]:
    manifests: list[ResourceManifestRaw] = []
    for doc in yaml.safe_load_all(stdout):
        if not isinstance(doc, dict):
            continue
        kind = doc.get("kind")
        metadata = doc.get("metadata")
        if not isinstance(kind, str) or not isinstance(metadata, dict):
            continue
        name = metadata.get("name")
        if not isinstance(name, str):
            continue
        namespace = metadata.get("namespace")
        manifests.append(
            ResourceManifestRaw(
                kind=kind,
                name=name,
                namespace=namespace if isinstance(namespace, str) else "",
                data=doc,
            )
        )
    return manifests
