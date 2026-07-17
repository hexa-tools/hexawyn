from unittest.mock import MagicMock, patch

import pytest

pytest.importorskip("datadog_api_client")
from datadog_api_client.exceptions import ApiException  # noqa: E402
from hexawyn.application.ports.driven.log_search_port import LogSearchPort  # noqa: E402
from hexawyn.domain.errors import (  # noqa: E402
    AdapterTimeoutError,
    ClusterUnreachableError,
    InsufficientPermissionsError,
)


def _log(message: str, timestamp: str = "2026-01-01T00:00:00Z", service: str = "web") -> MagicMock:
    attrs = type("Attrs", (), {})()
    attrs.message = message
    attrs.timestamp = timestamp
    attrs.service = service
    log = MagicMock()
    log.attributes = attrs
    return log


def _response(logs: list[MagicMock]) -> MagicMock:
    resp = MagicMock()
    resp.data = logs
    return resp


def _adapter(api: MagicMock):
    from hexawyn.adapters.secondary.datadog.datadog_logs_adapter import (
        DatadogLogsAdapter,
    )

    return DatadogLogsAdapter(logs_api=api)


class TestContract:
    def test_is_a_log_search_port(self) -> None:
        assert isinstance(_adapter(MagicMock()), LogSearchPort)


class TestFetchPodContainerLogs:
    def test_groups_lines_by_container(self) -> None:
        api = MagicMock()
        api.list_logs.return_value = _response(
            [
                _log("boot ok\nserving", service="app"),
                _log("proxy up", service="sidecar"),
            ]
        )
        adapter = _adapter(api)

        result = adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        by_name = {c["container"]: c for c in result}
        assert by_name["app"]["lines"] == ["boot ok", "serving"]
        assert by_name["sidecar"]["lines"] == ["proxy up"]
        assert by_name["app"]["truncated"] is False

    def test_fallback_to_unknown_container(self) -> None:
        api = MagicMock()
        log = _log("bare line")
        log.attributes.service = None
        api.list_logs.return_value = _response([log])
        adapter = _adapter(api)

        result = adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        assert result[0]["container"] == "unknown"

    def test_blank_lines_skipped(self) -> None:
        api = MagicMock()
        payload = "line-a\n\nline-b"
        api.list_logs.return_value = _response([_log(payload, service="app")])
        adapter = _adapter(api)

        result = adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        assert result[0]["lines"] == ["line-a", "line-b"]

    def test_empty_returns_empty(self) -> None:
        api = MagicMock()
        api.list_logs.return_value = _response([])
        adapter = _adapter(api)

        assert adapter.fetch_pod_container_logs("payments-api", "prod", 15) == []

    def test_truncates_at_max_lines(self) -> None:
        from hexawyn.adapters.secondary.datadog import datadog_logs_adapter as module

        max_lines = module._MAX_LINES_PER_CONTAINER
        api = MagicMock()
        lines = "\n".join(f"line-{i}" for i in range(max_lines + 10))
        api.list_logs.return_value = _response([_log(lines, service="app")])
        adapter = _adapter(api)

        result = adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        assert len(result[0]["lines"]) == max_lines
        assert result[0]["truncated"] is True

    def test_subsequent_logs_skipped_after_truncation(self) -> None:
        from hexawyn.adapters.secondary.datadog import datadog_logs_adapter as module

        max_lines = module._MAX_LINES_PER_CONTAINER
        api = MagicMock()
        lines1 = "\n".join(f"line-{i}" for i in range(max_lines + 2))
        lines2 = "\n".join(f"extra-{i}" for i in range(5))
        api.list_logs.return_value = _response(
            [
                _log(lines1, service="app"),
                _log(lines2, service="app"),
            ]
        )
        adapter = _adapter(api)

        result = adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        assert len(result[0]["lines"]) == max_lines
        assert result[0]["truncated"] is True

    def test_break_on_limit_mid_loop(self) -> None:
        from hexawyn.adapters.secondary.datadog import datadog_logs_adapter as module

        max_lines = module._MAX_LINES_PER_CONTAINER
        exactly_max = "\n".join(f"line-{i}" for i in range(max_lines))
        trailing = "\n".join(f"skipped-{i}" for i in range(3))
        api = MagicMock()
        api.list_logs.return_value = _response(
            [
                _log(f"{exactly_max}\n{trailing}", service="app"),
            ]
        )
        adapter = _adapter(api)

        result = adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        assert len(result[0]["lines"]) == max_lines
        assert result[0]["truncated"] is True
        assert "skipped-0" not in result[0]["lines"]


class TestErrorTranslation:
    def test_rate_limit_raises_adapter_timeout(self) -> None:
        api = MagicMock()
        api.list_logs.side_effect = ApiException(status=429)
        adapter = _adapter(api)

        with pytest.raises(AdapterTimeoutError):
            adapter.fetch_pod_container_logs("payments-api", "prod", 15)

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        api = MagicMock()
        api.list_logs.side_effect = ApiException(status=403)
        adapter = _adapter(api)

        with pytest.raises(InsufficientPermissionsError):
            adapter.fetch_pod_container_logs("payments-api", "prod", 15)

    def test_other_error_raises_cluster_unreachable(self) -> None:
        api = MagicMock()
        api.list_logs.side_effect = ApiException(status=500)
        adapter = _adapter(api)

        with pytest.raises(ClusterUnreachableError):
            adapter.fetch_pod_container_logs("payments-api", "prod", 15)


class TestHelpers:
    def test_container_name_returns_service(self) -> None:
        from hexawyn.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )

        attrs = type("Attrs", (), {})()
        attrs.service = "my-app"
        adapter = DatadogLogsAdapter(logs_api=MagicMock())

        assert adapter._container_name(attrs) == "my-app"

    def test_container_name_falls_back_to_unknown(self) -> None:
        from unittest.mock import MagicMock

        from hexawyn.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )

        attrs = type("Attrs", (), {})()
        adapter = DatadogLogsAdapter(logs_api=MagicMock())

        assert adapter._container_name(attrs) == "unknown"

    def test_build_logs_api_constructs_config(self) -> None:
        from hexawyn.adapters.secondary.datadog.datadog_logs_adapter import _build_logs_api

        cfg_data: dict[str, str] = {}
        cfg_mock = MagicMock()
        cfg_mock.api_key = cfg_data
        cfg_mock.server_variables = {}

        with (
            patch("datadog_api_client.Configuration", return_value=cfg_mock),
            patch("datadog_api_client.ApiClient"),
            patch("datadog_api_client.v2.api.logs_api.LogsApi"),
        ):
            _build_logs_api("k", "a", "datadoghq.eu")

        assert cfg_data["apiKeyAuth"] == "k"
        assert cfg_data["appKeyAuth"] == "a"
        assert cfg_mock.server_variables["site"] == "datadoghq.eu"


class TestLazyApiCreation:
    def test_lazily_builds_logs_api(self) -> None:
        from hexawyn.adapters.secondary.datadog import datadog_logs_adapter as module
        from hexawyn.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )

        created_api = MagicMock()
        created_api.list_logs.return_value = _response([])
        adapter = DatadogLogsAdapter(key="k", app_key="a", site="datadoghq.com")

        with patch.object(module, "_build_logs_api", return_value=created_api) as build:
            adapter.fetch_pod_container_logs("payments-api", "prod", 15)

        build.assert_called_once_with("k", "a", "datadoghq.com")
