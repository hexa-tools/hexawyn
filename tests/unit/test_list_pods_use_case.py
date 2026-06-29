from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.k8s_port import PodInfo
from hexawyn.application.ports.driving.list_pods.list_pods_command import ListPodsCommand
from hexawyn.application.ports.driving.list_pods.list_pods_response import ListPodsResponse
from hexawyn.application.ports.driving.list_pods.list_pods_service_port import (
    ListPodsServicePort,
)
from hexawyn.application.service.list_pods_service import ListPodsService, _sort_key
from hexawyn.application.use_case.list_pods.list_pods_use_case import ListPodsUseCase


class TestListPodsCommand:
    def test_is_frozen(self) -> None:
        cmd = ListPodsCommand(namespace="default")
        with pytest.raises(AttributeError):
            cmd.namespace = "other"  # type: ignore[misc]

    def test_namespace_field(self) -> None:
        cmd = ListPodsCommand(namespace="production")
        assert cmd.namespace == "production"


class TestListPodsResponse:
    def test_default_pods_is_empty(self) -> None:
        resp = ListPodsResponse()
        assert resp.pods == []

    def test_accepts_pods_list(self) -> None:
        pod = PodInfo(name="api", namespace="ns", status="Running", restarts=0, age="1d", node="n1")
        resp = ListPodsResponse(pods=[pod])
        assert len(resp.pods) == 1
        assert resp.pods[0]["name"] == "api"


class TestListPodsServicePort:
    def test_is_abstract(self) -> None:
        from abc import ABC

        assert issubclass(ListPodsServicePort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            ListPodsServicePort()  # type: ignore[abstract]


class TestListPodsUseCase:
    def test_delegates_to_service_port(self) -> None:
        fake_service = MagicMock(spec=ListPodsServicePort)
        pod = PodInfo(name="api", namespace="ns", status="Running", restarts=0, age="1d", node="n1")
        expected = ListPodsResponse(pods=[pod])
        fake_service.list_pods.return_value = expected

        use_case = ListPodsUseCase(service=fake_service)
        result = use_case.execute(ListPodsCommand(namespace="ns"))

        assert result.pods == [pod]
        fake_service.list_pods.assert_called_once()

    def test_passes_command_to_service(self) -> None:
        fake_service = MagicMock(spec=ListPodsServicePort)
        fake_service.list_pods.return_value = ListPodsResponse()

        cmd = ListPodsCommand(namespace="production")
        use_case = ListPodsUseCase(service=fake_service)
        use_case.execute(cmd)

        fake_service.list_pods.assert_called_once_with(cmd)


class TestListPodsService:
    def test_implements_service_port(self) -> None:
        service = ListPodsService(k8s_port=MagicMock())
        assert isinstance(service, ListPodsServicePort)

    def test_sorts_unhealthy_first(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = [
            PodInfo(name="b", namespace="ns", status="Running", restarts=0, age="1d", node="n1"),
            PodInfo(name="a", namespace="ns", status="CrashLoop", restarts=5, age="2d", node="n2"),
        ]
        service = ListPodsService(k8s_port=k8s)
        result = service.list_pods(ListPodsCommand(namespace="ns"))
        assert result.pods[0]["status"] == "CrashLoop"
        assert result.pods[1]["status"] == "Running"

    def test_empty_namespace(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = []
        service = ListPodsService(k8s_port=k8s)
        result = service.list_pods(ListPodsCommand(namespace="empty"))
        assert result.pods == []


class TestSortKey:
    def test_crashloop_before_running(self) -> None:
        crash = PodInfo(
            name="a", namespace="ns", status="CrashLoop", restarts=5, age="1d", node="n1"
        )
        running = PodInfo(
            name="b", namespace="ns", status="Running", restarts=0, age="1d", node="n1"
        )
        assert _sort_key(crash) < _sort_key(running)

    def test_pending_before_running(self) -> None:
        pending = PodInfo(
            name="a", namespace="ns", status="Pending", restarts=0, age="1d", node="n1"
        )
        running = PodInfo(
            name="b", namespace="ns", status="Running", restarts=0, age="1d", node="n1"
        )
        assert _sort_key(pending) < _sort_key(running)
