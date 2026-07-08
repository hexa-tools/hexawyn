from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.gitops_port import GitOpsPort


class TestGitOpsPort:
    def test_is_abstract(self) -> None:
        assert issubclass(GitOpsPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            GitOpsPort()  # type: ignore[abstract]

    def test_has_detect_engine(self) -> None:
        method = GitOpsPort.detect_engine
        assert getattr(method, "__isabstractmethod__", False)

    def test_has_list_apps(self) -> None:
        method = GitOpsPort.list_apps
        assert getattr(method, "__isabstractmethod__", False)

    def test_has_get_app(self) -> None:
        method = GitOpsPort.get_app
        assert getattr(method, "__isabstractmethod__", False)

    def test_has_list_sources(self) -> None:
        method = GitOpsPort.list_sources
        assert getattr(method, "__isabstractmethod__", False)

    def test_has_get_source(self) -> None:
        method = GitOpsPort.get_source
        assert getattr(method, "__isabstractmethod__", False)
