from __future__ import annotations

import subprocess
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.helm_values_diff_port import HelmValuesDiffPort
from hexawyn.domain.errors import HelmNotFoundError, ManifestRenderError

_VALUES_YAML = """
image:
  tag: v1.3
  repository: payment-service
replicaCount: 1
logging:
  level: DEBUG
"""

_ANCHOR_YAML = """
defaults: &defaults
  timeout: 30
staging:
  <<: *defaults
  replicas: 1
"""


def _completed(stdout: str, returncode: int = 0, stderr: str = "") -> MagicMock:
    result = MagicMock()
    result.stdout = stdout
    result.stderr = stderr
    result.returncode = returncode
    return result


class TestPortImplementation:
    def test_is_a_helm_values_diff_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.helm_values_adapter import HelmValuesAdapter

        assert isinstance(HelmValuesAdapter(), HelmValuesDiffPort)


class TestGetEffectiveValues:
    def test_parses_values_yaml(self) -> None:
        from hexawyn.adapters.secondary.gitops.helm_values_adapter import HelmValuesAdapter

        with patch("subprocess.run", return_value=_completed(_VALUES_YAML)) as run:
            result = HelmValuesAdapter().get_effective_values("payment-service", "staging")

        assert result["release"] == "payment-service"
        assert result["namespace"] == "staging"
        assert result["values"]["image"]["tag"] == "v1.3"
        assert result["values"]["replicaCount"] == 1
        args = run.call_args[0][0]
        assert args[0] == "helm"
        assert "get" in args and "values" in args
        assert "-a" in args
        assert "payment-service" in args
        assert "staging" in args

    def test_resolves_yaml_anchors(self) -> None:
        from hexawyn.adapters.secondary.gitops.helm_values_adapter import HelmValuesAdapter

        with patch("subprocess.run", return_value=_completed(_ANCHOR_YAML)):
            result = HelmValuesAdapter().get_effective_values("app", "staging")

        assert result["values"]["staging"]["timeout"] == 30
        assert result["values"]["staging"]["replicas"] == 1

    def test_empty_values_returns_empty_dict(self) -> None:
        from hexawyn.adapters.secondary.gitops.helm_values_adapter import HelmValuesAdapter

        with patch("subprocess.run", return_value=_completed("null\n")):
            result = HelmValuesAdapter().get_effective_values("app", "prod")

        assert result["values"] == {}

    def test_missing_helm_binary_raises_helm_not_found(self) -> None:
        from hexawyn.adapters.secondary.gitops.helm_values_adapter import HelmValuesAdapter

        with patch("subprocess.run", side_effect=FileNotFoundError()):
            with pytest.raises(HelmNotFoundError):
                HelmValuesAdapter().get_effective_values("app", "prod")

    def test_helm_error_raises_manifest_render_error(self) -> None:
        from hexawyn.adapters.secondary.gitops.helm_values_adapter import HelmValuesAdapter

        failed = _completed("", returncode=1, stderr="release: not found")
        with patch("subprocess.run", return_value=failed):
            with pytest.raises(ManifestRenderError):
                HelmValuesAdapter().get_effective_values("missing", "prod")

    def test_timeout_raises_manifest_render_error(self) -> None:
        from hexawyn.adapters.secondary.gitops.helm_values_adapter import HelmValuesAdapter

        with patch(
            "subprocess.run",
            side_effect=subprocess.TimeoutExpired(cmd="helm", timeout=30.0),
        ):
            with pytest.raises(ManifestRenderError):
                HelmValuesAdapter().get_effective_values("app", "prod")

    def test_non_mapping_yaml_returns_empty_dict(self) -> None:
        from hexawyn.adapters.secondary.gitops.helm_values_adapter import HelmValuesAdapter

        with patch("subprocess.run", return_value=_completed("- a\n- b\n")):
            result = HelmValuesAdapter().get_effective_values("app", "prod")

        assert result["values"] == {}
