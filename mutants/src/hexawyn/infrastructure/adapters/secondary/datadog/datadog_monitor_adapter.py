from __future__ import annotations

from typing import Protocol, cast

from hexawyn.application.ports.driven.monitoring_port import MonitoringPort
from hexawyn.domain.errors import MetricsUnavailableError

_TRIGGERED_STATES = {"Alert", "Warn", "No Data"}


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class _Monitor(Protocol):
    name: str
    overall_state: str
    message: str
    tags: list[str]


class MonitorsApi(Protocol):
    """Minimal contract for the Datadog v1 MonitorsApi used here."""

    def list_monitors(self) -> list[_Monitor]: ...
mutants_xǁDatadogMonitorAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDatadogMonitorAdapterǁ_api__mutmut: MutantDict = {}  # type: ignore


class DatadogMonitorAdapter(MonitoringPort):
    """MonitoringPort backed by Datadog Monitors API.

    Reads active Datadog monitors — an active monitor == a potential incident
    to feed into the hexawyn investigation pipeline. All calls are read-only
    (monitors_read scope).
    """

    @_mutmut_mutated(mutants_xǁDatadogMonitorAdapterǁ__init____mutmut)
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

    def xǁDatadogMonitorAdapterǁ__init____mutmut_orig(
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

    def xǁDatadogMonitorAdapterǁ__init____mutmut_1(
        self,
        monitors_api: MonitorsApi | None = None,
        key: str = "XXXX",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._monitors_api = monitors_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogMonitorAdapterǁ__init____mutmut_2(
        self,
        monitors_api: MonitorsApi | None = None,
        key: str = "",
        app_key: str = "XXXX",
        site: str = "datadoghq.com",
    ) -> None:
        self._monitors_api = monitors_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogMonitorAdapterǁ__init____mutmut_3(
        self,
        monitors_api: MonitorsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "XXdatadoghq.comXX",
    ) -> None:
        self._monitors_api = monitors_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogMonitorAdapterǁ__init____mutmut_4(
        self,
        monitors_api: MonitorsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "DATADOGHQ.COM",
    ) -> None:
        self._monitors_api = monitors_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogMonitorAdapterǁ__init____mutmut_5(
        self,
        monitors_api: MonitorsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._monitors_api = None
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogMonitorAdapterǁ__init____mutmut_6(
        self,
        monitors_api: MonitorsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._monitors_api = monitors_api
        self._key = None
        self._app_key = app_key
        self._site = site

    def xǁDatadogMonitorAdapterǁ__init____mutmut_7(
        self,
        monitors_api: MonitorsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._monitors_api = monitors_api
        self._key = key
        self._app_key = None
        self._site = site

    def xǁDatadogMonitorAdapterǁ__init____mutmut_8(
        self,
        monitors_api: MonitorsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._monitors_api = monitors_api
        self._key = key
        self._app_key = app_key
        self._site = None

    @_mutmut_mutated(mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut)
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

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_orig(self) -> list[dict[str, str | int | float]]:
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

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_1(self) -> list[dict[str, str | int | float]]:
        from datadog_api_client.exceptions import ApiException

        try:
            monitors = None
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

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_2(self) -> list[dict[str, str | int | float]]:
        from datadog_api_client.exceptions import ApiException

        try:
            monitors = self._api().list_monitors()
        except ApiException as exc:
            raise MetricsUnavailableError(
                None,
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

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_3(self) -> list[dict[str, str | int | float]]:
        from datadog_api_client.exceptions import ApiException

        try:
            monitors = self._api().list_monitors()
        except ApiException as exc:
            raise MetricsUnavailableError(
                "Datadog Monitors API request failed.",
                context=None,
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

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_4(self) -> list[dict[str, str | int | float]]:
        from datadog_api_client.exceptions import ApiException

        try:
            monitors = self._api().list_monitors()
        except ApiException as exc:
            raise MetricsUnavailableError(
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

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_5(self) -> list[dict[str, str | int | float]]:
        from datadog_api_client.exceptions import ApiException

        try:
            monitors = self._api().list_monitors()
        except ApiException as exc:
            raise MetricsUnavailableError(
                "Datadog Monitors API request failed.",
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

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_6(self) -> list[dict[str, str | int | float]]:
        from datadog_api_client.exceptions import ApiException

        try:
            monitors = self._api().list_monitors()
        except ApiException as exc:
            raise MetricsUnavailableError(
                "XXDatadog Monitors API request failed.XX",
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

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_7(self) -> list[dict[str, str | int | float]]:
        from datadog_api_client.exceptions import ApiException

        try:
            monitors = self._api().list_monitors()
        except ApiException as exc:
            raise MetricsUnavailableError(
                "datadog monitors api request failed.",
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

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_8(self) -> list[dict[str, str | int | float]]:
        from datadog_api_client.exceptions import ApiException

        try:
            monitors = self._api().list_monitors()
        except ApiException as exc:
            raise MetricsUnavailableError(
                "DATADOG MONITORS API REQUEST FAILED.",
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

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_9(self) -> list[dict[str, str | int | float]]:
        from datadog_api_client.exceptions import ApiException

        try:
            monitors = self._api().list_monitors()
        except ApiException as exc:
            raise MetricsUnavailableError(
                "Datadog Monitors API request failed.",
                context={"XXstatusXX": str(getattr(exc, "status", None))},
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

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_10(self) -> list[dict[str, str | int | float]]:
        from datadog_api_client.exceptions import ApiException

        try:
            monitors = self._api().list_monitors()
        except ApiException as exc:
            raise MetricsUnavailableError(
                "Datadog Monitors API request failed.",
                context={"STATUS": str(getattr(exc, "status", None))},
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

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_11(self) -> list[dict[str, str | int | float]]:
        from datadog_api_client.exceptions import ApiException

        try:
            monitors = self._api().list_monitors()
        except ApiException as exc:
            raise MetricsUnavailableError(
                "Datadog Monitors API request failed.",
                context={"status": str(None)},
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

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_12(self) -> list[dict[str, str | int | float]]:
        from datadog_api_client.exceptions import ApiException

        try:
            monitors = self._api().list_monitors()
        except ApiException as exc:
            raise MetricsUnavailableError(
                "Datadog Monitors API request failed.",
                context={"status": str(getattr(None, "status", None))},
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

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_13(self) -> list[dict[str, str | int | float]]:
        from datadog_api_client.exceptions import ApiException

        try:
            monitors = self._api().list_monitors()
        except ApiException as exc:
            raise MetricsUnavailableError(
                "Datadog Monitors API request failed.",
                context={"status": str(getattr(exc, None, None))},
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

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_14(self) -> list[dict[str, str | int | float]]:
        from datadog_api_client.exceptions import ApiException

        try:
            monitors = self._api().list_monitors()
        except ApiException as exc:
            raise MetricsUnavailableError(
                "Datadog Monitors API request failed.",
                context={"status": str(getattr("status", None))},
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

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_15(self) -> list[dict[str, str | int | float]]:
        from datadog_api_client.exceptions import ApiException

        try:
            monitors = self._api().list_monitors()
        except ApiException as exc:
            raise MetricsUnavailableError(
                "Datadog Monitors API request failed.",
                context={"status": str(getattr(exc, None))},
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

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_16(self) -> list[dict[str, str | int | float]]:
        from datadog_api_client.exceptions import ApiException

        try:
            monitors = self._api().list_monitors()
        except ApiException as exc:
            raise MetricsUnavailableError(
                "Datadog Monitors API request failed.",
                context={"status": str(getattr(exc, "status", ))},
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

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_17(self) -> list[dict[str, str | int | float]]:
        from datadog_api_client.exceptions import ApiException

        try:
            monitors = self._api().list_monitors()
        except ApiException as exc:
            raise MetricsUnavailableError(
                "Datadog Monitors API request failed.",
                context={"status": str(getattr(exc, "XXstatusXX", None))},
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

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_18(self) -> list[dict[str, str | int | float]]:
        from datadog_api_client.exceptions import ApiException

        try:
            monitors = self._api().list_monitors()
        except ApiException as exc:
            raise MetricsUnavailableError(
                "Datadog Monitors API request failed.",
                context={"status": str(getattr(exc, "STATUS", None))},
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

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_19(self) -> list[dict[str, str | int | float]]:
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
                "XXnameXX": str(m.name),
                "status": str(m.overall_state),
                "message": str(m.message),
                "tags": ", ".join(m.tags),
            }
            for m in monitors
            if m.overall_state in _TRIGGERED_STATES
        ]

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_20(self) -> list[dict[str, str | int | float]]:
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
                "NAME": str(m.name),
                "status": str(m.overall_state),
                "message": str(m.message),
                "tags": ", ".join(m.tags),
            }
            for m in monitors
            if m.overall_state in _TRIGGERED_STATES
        ]

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_21(self) -> list[dict[str, str | int | float]]:
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
                "name": str(None),
                "status": str(m.overall_state),
                "message": str(m.message),
                "tags": ", ".join(m.tags),
            }
            for m in monitors
            if m.overall_state in _TRIGGERED_STATES
        ]

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_22(self) -> list[dict[str, str | int | float]]:
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
                "XXstatusXX": str(m.overall_state),
                "message": str(m.message),
                "tags": ", ".join(m.tags),
            }
            for m in monitors
            if m.overall_state in _TRIGGERED_STATES
        ]

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_23(self) -> list[dict[str, str | int | float]]:
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
                "STATUS": str(m.overall_state),
                "message": str(m.message),
                "tags": ", ".join(m.tags),
            }
            for m in monitors
            if m.overall_state in _TRIGGERED_STATES
        ]

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_24(self) -> list[dict[str, str | int | float]]:
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
                "status": str(None),
                "message": str(m.message),
                "tags": ", ".join(m.tags),
            }
            for m in monitors
            if m.overall_state in _TRIGGERED_STATES
        ]

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_25(self) -> list[dict[str, str | int | float]]:
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
                "XXmessageXX": str(m.message),
                "tags": ", ".join(m.tags),
            }
            for m in monitors
            if m.overall_state in _TRIGGERED_STATES
        ]

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_26(self) -> list[dict[str, str | int | float]]:
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
                "MESSAGE": str(m.message),
                "tags": ", ".join(m.tags),
            }
            for m in monitors
            if m.overall_state in _TRIGGERED_STATES
        ]

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_27(self) -> list[dict[str, str | int | float]]:
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
                "message": str(None),
                "tags": ", ".join(m.tags),
            }
            for m in monitors
            if m.overall_state in _TRIGGERED_STATES
        ]

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_28(self) -> list[dict[str, str | int | float]]:
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
                "XXtagsXX": ", ".join(m.tags),
            }
            for m in monitors
            if m.overall_state in _TRIGGERED_STATES
        ]

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_29(self) -> list[dict[str, str | int | float]]:
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
                "TAGS": ", ".join(m.tags),
            }
            for m in monitors
            if m.overall_state in _TRIGGERED_STATES
        ]

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_30(self) -> list[dict[str, str | int | float]]:
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
                "tags": ", ".join(None),
            }
            for m in monitors
            if m.overall_state in _TRIGGERED_STATES
        ]

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_31(self) -> list[dict[str, str | int | float]]:
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
                "tags": "XX, XX".join(m.tags),
            }
            for m in monitors
            if m.overall_state in _TRIGGERED_STATES
        ]

    def xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_32(self) -> list[dict[str, str | int | float]]:
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
            if m.overall_state not in _TRIGGERED_STATES
        ]

    def get_apm_services(self) -> list[dict[str, str | int | float]]:
        return []

    @_mutmut_mutated(mutants_xǁDatadogMonitorAdapterǁ_api__mutmut)
    def _api(self) -> MonitorsApi:
        if self._monitors_api is None:
            self._monitors_api = _build_monitors_api(self._key, self._app_key, self._site)
        return self._monitors_api

    def xǁDatadogMonitorAdapterǁ_api__mutmut_orig(self) -> MonitorsApi:
        if self._monitors_api is None:
            self._monitors_api = _build_monitors_api(self._key, self._app_key, self._site)
        return self._monitors_api

    def xǁDatadogMonitorAdapterǁ_api__mutmut_1(self) -> MonitorsApi:
        if self._monitors_api is not None:
            self._monitors_api = _build_monitors_api(self._key, self._app_key, self._site)
        return self._monitors_api

    def xǁDatadogMonitorAdapterǁ_api__mutmut_2(self) -> MonitorsApi:
        if self._monitors_api is None:
            self._monitors_api = None
        return self._monitors_api

    def xǁDatadogMonitorAdapterǁ_api__mutmut_3(self) -> MonitorsApi:
        if self._monitors_api is None:
            self._monitors_api = _build_monitors_api(None, self._app_key, self._site)
        return self._monitors_api

    def xǁDatadogMonitorAdapterǁ_api__mutmut_4(self) -> MonitorsApi:
        if self._monitors_api is None:
            self._monitors_api = _build_monitors_api(self._key, None, self._site)
        return self._monitors_api

    def xǁDatadogMonitorAdapterǁ_api__mutmut_5(self) -> MonitorsApi:
        if self._monitors_api is None:
            self._monitors_api = _build_monitors_api(self._key, self._app_key, None)
        return self._monitors_api

    def xǁDatadogMonitorAdapterǁ_api__mutmut_6(self) -> MonitorsApi:
        if self._monitors_api is None:
            self._monitors_api = _build_monitors_api(self._app_key, self._site)
        return self._monitors_api

    def xǁDatadogMonitorAdapterǁ_api__mutmut_7(self) -> MonitorsApi:
        if self._monitors_api is None:
            self._monitors_api = _build_monitors_api(self._key, self._site)
        return self._monitors_api

    def xǁDatadogMonitorAdapterǁ_api__mutmut_8(self) -> MonitorsApi:
        if self._monitors_api is None:
            self._monitors_api = _build_monitors_api(self._key, self._app_key, )
        return self._monitors_api

mutants_xǁDatadogMonitorAdapterǁ__init____mutmut['_mutmut_orig'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁ__init____mutmut['xǁDatadogMonitorAdapterǁ__init____mutmut_1'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁ__init____mutmut['xǁDatadogMonitorAdapterǁ__init____mutmut_2'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁ__init____mutmut['xǁDatadogMonitorAdapterǁ__init____mutmut_3'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁ__init____mutmut['xǁDatadogMonitorAdapterǁ__init____mutmut_4'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁ__init____mutmut['xǁDatadogMonitorAdapterǁ__init____mutmut_5'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁ__init____mutmut['xǁDatadogMonitorAdapterǁ__init____mutmut_6'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁ__init____mutmut['xǁDatadogMonitorAdapterǁ__init____mutmut_7'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁ__init____mutmut['xǁDatadogMonitorAdapterǁ__init____mutmut_8'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁ__init____mutmut_8 # type: ignore # mutmut generated

mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['_mutmut_orig'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_1'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_2'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_3'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_4'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_5'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_6'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_7'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_8'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_9'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_10'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_11'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_12'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_13'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_14'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_15'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_16'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_17'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_18'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_19'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_20'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_21'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_22'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_23'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_24'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_25'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_26'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_27'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_28'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_29'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_30'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_31'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut['xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_32'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁget_triggered_monitors__mutmut_32 # type: ignore # mutmut generated

mutants_xǁDatadogMonitorAdapterǁ_api__mutmut['_mutmut_orig'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁ_api__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁ_api__mutmut['xǁDatadogMonitorAdapterǁ_api__mutmut_1'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁ_api__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁ_api__mutmut['xǁDatadogMonitorAdapterǁ_api__mutmut_2'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁ_api__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁ_api__mutmut['xǁDatadogMonitorAdapterǁ_api__mutmut_3'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁ_api__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁ_api__mutmut['xǁDatadogMonitorAdapterǁ_api__mutmut_4'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁ_api__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁ_api__mutmut['xǁDatadogMonitorAdapterǁ_api__mutmut_5'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁ_api__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁ_api__mutmut['xǁDatadogMonitorAdapterǁ_api__mutmut_6'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁ_api__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁ_api__mutmut['xǁDatadogMonitorAdapterǁ_api__mutmut_7'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁ_api__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDatadogMonitorAdapterǁ_api__mutmut['xǁDatadogMonitorAdapterǁ_api__mutmut_8'] = DatadogMonitorAdapter.xǁDatadogMonitorAdapterǁ_api__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_monitors_api__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_monitors_api__mutmut)
def _build_monitors_api(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MonitorsApi, DatadogMonitorsApi(ApiClient(configuration)))


def x__build_monitors_api__mutmut_orig(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MonitorsApi, DatadogMonitorsApi(ApiClient(configuration)))


def x__build_monitors_api__mutmut_1(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = None
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MonitorsApi, DatadogMonitorsApi(ApiClient(configuration)))


def x__build_monitors_api__mutmut_2(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = None
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MonitorsApi, DatadogMonitorsApi(ApiClient(configuration)))


def x__build_monitors_api__mutmut_3(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = Configuration()
    configuration.api_key["XXapiKeyAuthXX"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MonitorsApi, DatadogMonitorsApi(ApiClient(configuration)))


def x__build_monitors_api__mutmut_4(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = Configuration()
    configuration.api_key["apikeyauth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MonitorsApi, DatadogMonitorsApi(ApiClient(configuration)))


def x__build_monitors_api__mutmut_5(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = Configuration()
    configuration.api_key["APIKEYAUTH"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MonitorsApi, DatadogMonitorsApi(ApiClient(configuration)))


def x__build_monitors_api__mutmut_6(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = None
    configuration.server_variables["site"] = site
    return cast(MonitorsApi, DatadogMonitorsApi(ApiClient(configuration)))


def x__build_monitors_api__mutmut_7(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["XXappKeyAuthXX"] = app_key
    configuration.server_variables["site"] = site
    return cast(MonitorsApi, DatadogMonitorsApi(ApiClient(configuration)))


def x__build_monitors_api__mutmut_8(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appkeyauth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MonitorsApi, DatadogMonitorsApi(ApiClient(configuration)))


def x__build_monitors_api__mutmut_9(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["APPKEYAUTH"] = app_key
    configuration.server_variables["site"] = site
    return cast(MonitorsApi, DatadogMonitorsApi(ApiClient(configuration)))


def x__build_monitors_api__mutmut_10(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = None
    return cast(MonitorsApi, DatadogMonitorsApi(ApiClient(configuration)))


def x__build_monitors_api__mutmut_11(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["XXsiteXX"] = site
    return cast(MonitorsApi, DatadogMonitorsApi(ApiClient(configuration)))


def x__build_monitors_api__mutmut_12(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["SITE"] = site
    return cast(MonitorsApi, DatadogMonitorsApi(ApiClient(configuration)))


def x__build_monitors_api__mutmut_13(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(None, DatadogMonitorsApi(ApiClient(configuration)))


def x__build_monitors_api__mutmut_14(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MonitorsApi, None)


def x__build_monitors_api__mutmut_15(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(DatadogMonitorsApi(ApiClient(configuration)))


def x__build_monitors_api__mutmut_16(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MonitorsApi, )


def x__build_monitors_api__mutmut_17(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MonitorsApi, DatadogMonitorsApi(None))


def x__build_monitors_api__mutmut_18(key: str, app_key: str, site: str) -> MonitorsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v1.api.monitors_api import MonitorsApi as DatadogMonitorsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(MonitorsApi, DatadogMonitorsApi(ApiClient(None)))

mutants_x__build_monitors_api__mutmut['_mutmut_orig'] = x__build_monitors_api__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_monitors_api__mutmut['x__build_monitors_api__mutmut_1'] = x__build_monitors_api__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_monitors_api__mutmut['x__build_monitors_api__mutmut_2'] = x__build_monitors_api__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_monitors_api__mutmut['x__build_monitors_api__mutmut_3'] = x__build_monitors_api__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_monitors_api__mutmut['x__build_monitors_api__mutmut_4'] = x__build_monitors_api__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_monitors_api__mutmut['x__build_monitors_api__mutmut_5'] = x__build_monitors_api__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_monitors_api__mutmut['x__build_monitors_api__mutmut_6'] = x__build_monitors_api__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_monitors_api__mutmut['x__build_monitors_api__mutmut_7'] = x__build_monitors_api__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_monitors_api__mutmut['x__build_monitors_api__mutmut_8'] = x__build_monitors_api__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_monitors_api__mutmut['x__build_monitors_api__mutmut_9'] = x__build_monitors_api__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_monitors_api__mutmut['x__build_monitors_api__mutmut_10'] = x__build_monitors_api__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_monitors_api__mutmut['x__build_monitors_api__mutmut_11'] = x__build_monitors_api__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_monitors_api__mutmut['x__build_monitors_api__mutmut_12'] = x__build_monitors_api__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_monitors_api__mutmut['x__build_monitors_api__mutmut_13'] = x__build_monitors_api__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_monitors_api__mutmut['x__build_monitors_api__mutmut_14'] = x__build_monitors_api__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_monitors_api__mutmut['x__build_monitors_api__mutmut_15'] = x__build_monitors_api__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_monitors_api__mutmut['x__build_monitors_api__mutmut_16'] = x__build_monitors_api__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_monitors_api__mutmut['x__build_monitors_api__mutmut_17'] = x__build_monitors_api__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_monitors_api__mutmut['x__build_monitors_api__mutmut_18'] = x__build_monitors_api__mutmut_18 # type: ignore # mutmut generated
