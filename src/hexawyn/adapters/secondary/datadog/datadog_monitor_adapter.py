from __future__ import annotations

from typing import Protocol, cast

from hexawyn.application.ports.driven.monitoring_port import MonitoringPort
from hexawyn.domain.errors import MetricsUnavailableError

_TRIGGERED_STATES = {"Alert", "Warn", "No Data"}


class _Monitor(Protocol):
    name: str
    overall_state: str
    message: str
    tags: list[str]


class MonitorsApi(Protocol):
    """Minimal contract for the Datadog v1 MonitorsApi used here."""

    def list_monitors(self) -> list[_Monitor]: ...


class DatadogMonitorAdapter(MonitoringPort):
    """MonitoringPort backed by Datadog Monitors API.

    Reads active Datadog monitors — an active monitor == a potential incident
    to feed into the hexawyn investigation pipeline. All calls are read-only
    (monitors_read scope).
    """

    def __init__(
        self,
        monitors_api: MonitorsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._monitors_api = monitors_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def get_triggered_monitors(self) -> list[dict[str, str | int | float]]:
        from datadog_api_client.exceptions import ApiException

        try:
            monitors = self._api().list_monitors()
        except ApiException as exc:
            raise MetricsUnavailableError(
                "Datadog Monitors API request failed.",
                context={"status": str(getattr(exc, "status", None))},
            ) from exc
        return [
            {
                "name": str(m.name),
                "status": str(m.overall_state),
                "message": str(m.message),
                "tags": ", ".join(m.tags),
            }
            for m in monitors
            if m.overall_state in _TRIGGERED_STATES
        ]

    def get_apm_services(self) -> list[dict[str, str | int | float]]:
        raise NotImplementedError("get_apm_services is not yet implemented for Datadog")

    def _api(self) -> MonitorsApi:
        if self._monitors_api is None:
            self._monitors_api = _build_monitors_api(self._key, self._app_key, self._site)
        return self._monitors_api


def _build_monitors_api(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MonitorsApi, DatadogMonitorsApi(ApiClient(configuration)))
