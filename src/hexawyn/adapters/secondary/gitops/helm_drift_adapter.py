from __future__ import annotations

import subprocess

import yaml
from hexawyn.application.ports.driven.drift_detection_port import (
    DriftDetectionPort,
    ResourceManifestRaw,
)
from hexawyn.domain.errors import ComponentNotInstalledError, ManifestRenderError

_HELM_COMMAND_TIMEOUT_SECONDS = 30.0
_NOT_FOUND_HINT = "not found"


class HelmDriftAdapter(DriftDetectionPort):
    """Secondary adapter — shells out to the `helm` CLI. Renders desired
    state via `helm get manifest` (the frozen, stored release manifest),
    never `helm template` (which would re-render fresh and bake in a new
    Helm `date`-function timestamp on every call — see plan Context)."""

    def render_desired_manifests(self, source: str, namespace: str) -> list[ResourceManifestRaw]:
        stdout = self._run(["get", "manifest", source, "-n", namespace])
        return _parse_multi_doc_yaml(stdout)

    def source_exists(self, source: str, namespace: str) -> bool:
        try:
            self._run(["status", source, "-n", namespace, "-o", "json"])
        except ManifestRenderError as exc:
            if _NOT_FOUND_HINT in exc.detail.lower():
                return False
            raise
        return True

    def _run(self, args: list[str]) -> str:
        command = ["helm", *args]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=_HELM_COMMAND_TIMEOUT_SECONDS,
            )
        except FileNotFoundError as exc:
            raise ComponentNotInstalledError("helm", "https://helm.sh/docs/intro/install/") from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
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
