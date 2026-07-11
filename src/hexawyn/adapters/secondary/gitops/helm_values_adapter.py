from __future__ import annotations

import subprocess

import yaml
from hexawyn.application.ports.driven.helm_values_diff_port import (
    HelmReleaseValues,
    HelmValuesDiffPort,
)
from hexawyn.domain.errors import HelmNotFoundError, ManifestRenderError

_HELM_COMMAND_TIMEOUT_SECONDS = 30.0


class HelmValuesAdapter(HelmValuesDiffPort):
    """Secondary adapter — reads effective Helm values via the `helm` CLI.

    Uses ``helm get values <release> -n <namespace> -a -o yaml`` so the merged
    user-supplied values (including CI ``--set`` overrides) are returned, not
    the raw values.yaml. YAML anchors/aliases are resolved by the safe loader.
    """

    def get_effective_values(self, release: str, namespace: str) -> HelmReleaseValues:
        stdout = self._run(["get", "values", release, "-n", namespace, "-a", "-o", "yaml"])
        parsed = yaml.safe_load(stdout)
        values = parsed if isinstance(parsed, dict) else {}
        return HelmReleaseValues(release=release, namespace=namespace, values=values)

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
            raise HelmNotFoundError() from exc
        except subprocess.TimeoutExpired as exc:
            raise ManifestRenderError(
                source=" ".join(args), detail="helm command timed out"
            ) from exc

        if result.returncode != 0:
            raise ManifestRenderError(source=" ".join(args), detail=result.stderr.strip())
        return result.stdout
