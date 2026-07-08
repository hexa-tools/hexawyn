from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.alert_notification_port import AlertNotificationPort
from hexawyn.application.ports.driven.pod_log_watch_port import PodLogWatchPort
from hexawyn.domain.models.analyze_pod_logs import PodLogLine


class TestWatchPodLogsTool:
    def test_returns_watch_result(self) -> None:
        from hexawyn.mcp.tools.watch_pod_logs import watch_pod_logs

        with (
            patch("hexawyn.mcp.server.build_pod_log_watch_adapter") as build_watch,
            patch("hexawyn.mcp.server.build_alert_notification_adapter") as build_alert,
        ):
            watch_adapter = MagicMock(spec=PodLogWatchPort)
            watch_adapter.watch.return_value = iter(
                [
                    PodLogLine(
                        timestamp="T1",
                        level="ERROR",
                        message="OOMKilled memory limit exceeded",
                        run_index=0,
                        is_json=False,
                    )
                ]
            )
            watch_adapter.pod_exists.return_value = True
            build_watch.return_value = watch_adapter
            build_alert.return_value = MagicMock(spec=AlertNotificationPort)

            result = watch_pod_logs(pod_name="payment-service-7f9b", namespace="prod")

        assert result["error"] is None
        assert result["pod_name"] == "payment-service-7f9b"
        assert len(result["alerts"]) == 1
        assert result["alerts"][0]["category"] == "oom"

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.watch_pod_logs import watch_pod_logs

        with patch(
            "hexawyn.mcp.server.build_pod_log_watch_adapter",
            side_effect=RuntimeError("Pod 'ghost' not found in namespace 'prod'"),
        ):
            result = watch_pod_logs(pod_name="ghost", namespace="prod")

        assert result["error"] == "Pod 'ghost' not found in namespace 'prod'"


class TestBuildPodLogWatchAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.mcp.server import build_pod_log_watch_adapter

        assert isinstance(build_pod_log_watch_adapter(), PodLogWatchPort)


class TestBuildAlertNotificationAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.mcp.server import build_alert_notification_adapter

        assert isinstance(build_alert_notification_adapter(), AlertNotificationPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.watch_pod_logs")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
