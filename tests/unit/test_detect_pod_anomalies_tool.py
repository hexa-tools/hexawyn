from __future__ import annotations

from unittest.mock import MagicMock, patch


def _pod(name: str, current: float = 200.0) -> dict:
    baseline = [200.0 + ((i % 3) - 1) * 2.0 for i in range(167)]
    return {
        "pod_name": name,
        "namespace": "production",
        "pod_age_hours": 720.0,
        "hours_since_last_restart": None,
        "baseline_window_hours": 168.0,
        "cpu_baseline_millicores": baseline,
        "cpu_current_millicores": current,
        "memory_baseline_bytes": [500.0] * 167,
        "memory_current_bytes": 500.0,
        "error_rate_baseline_pct": [0.1] * 167,
        "error_rate_current_pct": 0.1,
        "is_scheduled_batch_job": False,
    }


class TestDetectPodAnomaliesTool:
    def test_returns_report(self) -> None:
        from hexawyn.mcp.tools.detect_pod_anomalies import detect_pod_anomalies

        with (
            patch("hexawyn.mcp.server.build_pod_metrics_baseline_adapter") as build_metrics,
            patch("hexawyn.mcp.server.build_k8s_adapter") as build_k8s,
        ):
            metrics_adapter = MagicMock()
            metrics_adapter.get_all_pod_metrics_data.return_value = [
                _pod("payment-api", current=850.0)
            ]
            build_metrics.return_value = metrics_adapter

            k8s_adapter = MagicMock()
            k8s_adapter.list_namespaces.return_value = [
                {"name": "production", "status": "Active", "age": "100d"}
            ]
            build_k8s.return_value = k8s_adapter

            result = detect_pod_anomalies(namespace="production")

        assert result["error"] is None
        assert result["total_pods"] == 1
        assert len(result["anomalies"]) == 1
        assert result["anomalies"][0]["severity"] == "critical"

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_pod_anomalies import detect_pod_anomalies

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            side_effect=RuntimeError("Namespace 'ghost' not found"),
        ):
            result = detect_pod_anomalies(namespace="ghost")

        assert result["error"] == "Namespace 'ghost' not found"


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_pod_anomalies")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
