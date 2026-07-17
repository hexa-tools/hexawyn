from __future__ import annotations

from abc import ABC
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.ports.driving.gitops_detect.gitops_detect_command import (
    GitOpsDetectCommand,
)
from hexawyn.application.ports.driving.gitops_detect.gitops_detect_response import (
    GitOpsDetectResponse,
)
from hexawyn.application.ports.driving.gitops_detect.gitops_detect_service_port import (
    GitOpsDetectServicePort,
)
from hexawyn.application.service.gitops_detect_service import GitOpsDetectService
from hexawyn.application.use_case.gitops_detect.gitops_detect_use_case import (
    GitOpsDetectUseCase,
)
from hexawyn.domain.models.gitops import GitOpsDetectionResult, GitOpsEngine
from hexawyn.mcp.tools.gitops_detect import gitops_detect


class TestGitOpsDetectCommand:
    def test_is_frozen(self) -> None:
        cmd = GitOpsDetectCommand()
        with pytest.raises(AttributeError):
            cmd.namespace = "other"  # type: ignore[misc]


class TestGitOpsDetectResponse:
    def test_defaults(self) -> None:
        resp = GitOpsDetectResponse()
        assert resp.engine == "unknown"
        assert resp.version is None
        assert resp.error is None

    def test_with_detection(self) -> None:
        resp = GitOpsDetectResponse(
            engine="flux",
            version="v2.4.0",
            namespace="flux-system",
            apps_count=12,
            out_of_sync_count=2,
            failed_count=1,
        )
        assert resp.engine == "flux"
        assert resp.apps_count == 12
        assert resp.out_of_sync_count == 2


class TestGitOpsDetectServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(GitOpsDetectServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            GitOpsDetectServicePort()  # type: ignore[abstract]


class TestGitOpsDetectUseCase:
    def test_delegates_to_service(self) -> None:
        fake = MagicMock(spec=GitOpsDetectServicePort)
        expected = GitOpsDetectResponse(engine="flux", apps_count=5)
        fake.detect.return_value = expected
        uc = GitOpsDetectUseCase(service=fake)
        result = uc.execute(GitOpsDetectCommand())
        assert result.engine == "flux"
        fake.detect.assert_called_once()


class TestGitOpsDetectService:
    def test_implements_port(self) -> None:
        svc = GitOpsDetectService(gitops_port=MagicMock(spec=GitOpsPort))
        assert isinstance(svc, GitOpsDetectServicePort)

    def test_flux_detected(self) -> None:
        gitops = MagicMock(spec=GitOpsPort)
        gitops.detect_engine.return_value = GitOpsDetectionResult(
            engine=GitOpsEngine.FLUX,
            version="v2.4.0",
            namespace="flux-system",
            apps_count=12,
            out_of_sync_count=2,
            failed_count=1,
        )
        svc = GitOpsDetectService(gitops_port=gitops)
        result = svc.detect(GitOpsDetectCommand())
        assert result.engine == "flux"
        assert result.apps_count == 12
        assert result.out_of_sync_count == 2
        assert result.error is None

    def test_none_detected(self) -> None:
        gitops = MagicMock(spec=GitOpsPort)
        gitops.detect_engine.return_value = GitOpsDetectionResult(
            engine=GitOpsEngine.NONE,
            version=None,
            namespace=None,
            apps_count=0,
            out_of_sync_count=0,
            failed_count=0,
        )
        svc = GitOpsDetectService(gitops_port=gitops)
        result = svc.detect(GitOpsDetectCommand())
        assert result.engine == "none"
        assert result.apps_count == 0


class TestGitOpsDetectTool:
    def test_returns_detection(self) -> None:
        with patch("hexawyn.mcp.server.build_gitops_adapter") as mock_build:
            mock_adapter = MagicMock(spec=GitOpsPort)
            mock_adapter.detect_engine.return_value = GitOpsDetectionResult(
                engine=GitOpsEngine.FLUX,
                version="v2.3.0",
                namespace="flux-system",
                apps_count=8,
                out_of_sync_count=1,
                failed_count=0,
            )
            mock_build.return_value = mock_adapter

            result = gitops_detect()

        assert result["error"] is None
        assert result["engine"] == "flux"
        assert result["apps_count"] == 8

    def test_handles_error(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_gitops_adapter",
            side_effect=RuntimeError("k8s unreachable"),
        ):
            result = gitops_detect()

        assert result["error"] is not None
        assert "k8s unreachable" in str(result["error"])
