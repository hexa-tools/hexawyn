from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import Protocol, cast

from hexawyn.application.ports.driven.log_search_port import LogSearchPort, RawContainerLog
from hexawyn.domain.errors import (
    AdapterTimeoutError,
    ClusterUnreachableError,
    InsufficientPermissionsError,
)

_MAX_LINES_PER_CONTAINER = 5000
_UNKNOWN_CONTAINER = "unknown"
_RATE_LIMIT_STATUS = 429
_UNAUTHORIZED_STATUSES = (401, 403)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class _LogAttribute(Protocol):
    message: str
    timestamp: str
    service: str


class _Log(Protocol):
    attributes: _LogAttribute


class _LogsResponse(Protocol):
    data: list[_Log] | None


class LogsApi(Protocol):
    """Minimal contract for the Datadog v2 LogsApi used here."""

    def list_logs(self, *, body: object) -> _LogsResponse: ...
mutants_xǁDatadogLogsAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDatadogLogsAdapterǁ_container_name__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDatadogLogsAdapterǁ_api__mutmut: MutantDict = {}  # type: ignore


class DatadogLogsAdapter(LogSearchPort):
    """LogSearchPort backed by Datadog Logs API.

    Reads pod/container logs natively — no `kubectl logs` on Datadog-
    instrumented clusters.
    """

    @_mutmut_mutated(mutants_xǁDatadogLogsAdapterǁ__init____mutmut)
    def __init__(
        self,
        logs_api: LogsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._logs_api = logs_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogLogsAdapterǁ__init____mutmut_orig(
        self,
        logs_api: LogsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._logs_api = logs_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogLogsAdapterǁ__init____mutmut_1(
        self,
        logs_api: LogsApi | None = None,
        key: str = "XXXX",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._logs_api = logs_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogLogsAdapterǁ__init____mutmut_2(
        self,
        logs_api: LogsApi | None = None,
        key: str = "",
        app_key: str = "XXXX",
        site: str = "datadoghq.com",
    ) -> None:
        self._logs_api = logs_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogLogsAdapterǁ__init____mutmut_3(
        self,
        logs_api: LogsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "XXdatadoghq.comXX",
    ) -> None:
        self._logs_api = logs_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogLogsAdapterǁ__init____mutmut_4(
        self,
        logs_api: LogsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "DATADOGHQ.COM",
    ) -> None:
        self._logs_api = logs_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogLogsAdapterǁ__init____mutmut_5(
        self,
        logs_api: LogsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._logs_api = None
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogLogsAdapterǁ__init____mutmut_6(
        self,
        logs_api: LogsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._logs_api = logs_api
        self._key = None
        self._app_key = app_key
        self._site = site

    def xǁDatadogLogsAdapterǁ__init____mutmut_7(
        self,
        logs_api: LogsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._logs_api = logs_api
        self._key = key
        self._app_key = None
        self._site = site

    def xǁDatadogLogsAdapterǁ__init____mutmut_8(
        self,
        logs_api: LogsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._logs_api = logs_api
        self._key = key
        self._app_key = app_key
        self._site = None

    @_mutmut_mutated(mutants_xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut)
    def fetch_pod_container_logs(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        data = self._list_logs(pod_name, namespace, time_window_minutes)
        return self._group_by_container(data)

    def xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_orig(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        data = self._list_logs(pod_name, namespace, time_window_minutes)
        return self._group_by_container(data)

    def xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_1(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        data = None
        return self._group_by_container(data)

    def xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_2(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        data = self._list_logs(None, namespace, time_window_minutes)
        return self._group_by_container(data)

    def xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_3(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        data = self._list_logs(pod_name, None, time_window_minutes)
        return self._group_by_container(data)

    def xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_4(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        data = self._list_logs(pod_name, namespace, None)
        return self._group_by_container(data)

    def xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_5(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        data = self._list_logs(namespace, time_window_minutes)
        return self._group_by_container(data)

    def xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_6(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        data = self._list_logs(pod_name, time_window_minutes)
        return self._group_by_container(data)

    def xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_7(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        data = self._list_logs(pod_name, namespace, )
        return self._group_by_container(data)

    def xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_8(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        data = self._list_logs(pod_name, namespace, time_window_minutes)
        return self._group_by_container(None)

    @_mutmut_mutated(mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut)
    def _list_logs(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                to=now.isoformat(),
            ),
            page=LogsListRequestPage(limit=100),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_orig(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                to=now.isoformat(),
            ),
            page=LogsListRequestPage(limit=100),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_1(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = None
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                to=now.isoformat(),
            ),
            page=LogsListRequestPage(limit=100),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_2(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(None)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                to=now.isoformat(),
            ),
            page=LogsListRequestPage(limit=100),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_3(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = None
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_4(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=None,
            page=LogsListRequestPage(limit=100),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_5(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                to=now.isoformat(),
            ),
            page=None,
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_6(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                to=now.isoformat(),
            ),
            page=LogsListRequestPage(limit=100),
            sort=None,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_7(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            page=LogsListRequestPage(limit=100),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_8(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                to=now.isoformat(),
            ),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_9(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                to=now.isoformat(),
            ),
            page=LogsListRequestPage(limit=100),
            )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_10(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=None,
                _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                to=now.isoformat(),
            ),
            page=LogsListRequestPage(limit=100),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_11(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=None,
                to=now.isoformat(),
            ),
            page=LogsListRequestPage(limit=100),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_12(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                to=None,
            ),
            page=LogsListRequestPage(limit=100),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_13(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                to=now.isoformat(),
            ),
            page=LogsListRequestPage(limit=100),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_14(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                to=now.isoformat(),
            ),
            page=LogsListRequestPage(limit=100),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_15(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                ),
            page=LogsListRequestPage(limit=100),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_16(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=(now + timedelta(minutes=window_minutes)).isoformat(),
                to=now.isoformat(),
            ),
            page=LogsListRequestPage(limit=100),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_17(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=(now - timedelta(minutes=None)).isoformat(),
                to=now.isoformat(),
            ),
            page=LogsListRequestPage(limit=100),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_18(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                to=now.isoformat(),
            ),
            page=LogsListRequestPage(limit=None),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_19(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                to=now.isoformat(),
            ),
            page=LogsListRequestPage(limit=101),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_20(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                to=now.isoformat(),
            ),
            page=LogsListRequestPage(limit=100),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = None
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_21(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                to=now.isoformat(),
            ),
            page=LogsListRequestPage(limit=100),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=None)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_22(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                to=now.isoformat(),
            ),
            page=LogsListRequestPage(limit=100),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(None) from exc
        return list(response.data or [])

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_23(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                to=now.isoformat(),
            ),
            page=LogsListRequestPage(limit=100),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(None)

    def xǁDatadogLogsAdapterǁ_list_logs__mutmut_24(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                to=now.isoformat(),
            ),
            page=LogsListRequestPage(limit=100),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data and [])

    @_mutmut_mutated(mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut)
    def _group_by_container(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_orig(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_1(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = None
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_2(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = None
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_3(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = None
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_4(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = None
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_5(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(None)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_6(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = None
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_7(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(None, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_8(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, None)
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_9(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault([])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_10(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, )
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_11(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container not in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_12(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                break
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_13(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(None).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_14(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = None
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_15(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_16(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    break
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_17(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) > _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_18(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(None)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_19(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    return
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_20(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(None)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_21(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=None,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_22(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=None,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_23(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=None,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_24(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_25(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_26(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                )
            for container, lines in lines_by_container.items()
        ]

    def xǁDatadogLogsAdapterǁ_group_by_container__mutmut_27(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container not in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    @_mutmut_mutated(mutants_xǁDatadogLogsAdapterǁ_container_name__mutmut)
    def _container_name(self, attrs: _LogAttribute) -> str:
        service = getattr(attrs, "service", None)
        return str(service) if service else _UNKNOWN_CONTAINER

    def xǁDatadogLogsAdapterǁ_container_name__mutmut_orig(self, attrs: _LogAttribute) -> str:
        service = getattr(attrs, "service", None)
        return str(service) if service else _UNKNOWN_CONTAINER

    def xǁDatadogLogsAdapterǁ_container_name__mutmut_1(self, attrs: _LogAttribute) -> str:
        service = None
        return str(service) if service else _UNKNOWN_CONTAINER

    def xǁDatadogLogsAdapterǁ_container_name__mutmut_2(self, attrs: _LogAttribute) -> str:
        service = getattr(None, "service", None)
        return str(service) if service else _UNKNOWN_CONTAINER

    def xǁDatadogLogsAdapterǁ_container_name__mutmut_3(self, attrs: _LogAttribute) -> str:
        service = getattr(attrs, None, None)
        return str(service) if service else _UNKNOWN_CONTAINER

    def xǁDatadogLogsAdapterǁ_container_name__mutmut_4(self, attrs: _LogAttribute) -> str:
        service = getattr("service", None)
        return str(service) if service else _UNKNOWN_CONTAINER

    def xǁDatadogLogsAdapterǁ_container_name__mutmut_5(self, attrs: _LogAttribute) -> str:
        service = getattr(attrs, None)
        return str(service) if service else _UNKNOWN_CONTAINER

    def xǁDatadogLogsAdapterǁ_container_name__mutmut_6(self, attrs: _LogAttribute) -> str:
        service = getattr(attrs, "service", )
        return str(service) if service else _UNKNOWN_CONTAINER

    def xǁDatadogLogsAdapterǁ_container_name__mutmut_7(self, attrs: _LogAttribute) -> str:
        service = getattr(attrs, "XXserviceXX", None)
        return str(service) if service else _UNKNOWN_CONTAINER

    def xǁDatadogLogsAdapterǁ_container_name__mutmut_8(self, attrs: _LogAttribute) -> str:
        service = getattr(attrs, "SERVICE", None)
        return str(service) if service else _UNKNOWN_CONTAINER

    def xǁDatadogLogsAdapterǁ_container_name__mutmut_9(self, attrs: _LogAttribute) -> str:
        service = getattr(attrs, "service", None)
        return str(None) if service else _UNKNOWN_CONTAINER

    @_mutmut_mutated(mutants_xǁDatadogLogsAdapterǁ_api__mutmut)
    def _api(self) -> LogsApi:
        if self._logs_api is None:
            self._logs_api = _build_logs_api(self._key, self._app_key, self._site)
        return self._logs_api

    def xǁDatadogLogsAdapterǁ_api__mutmut_orig(self) -> LogsApi:
        if self._logs_api is None:
            self._logs_api = _build_logs_api(self._key, self._app_key, self._site)
        return self._logs_api

    def xǁDatadogLogsAdapterǁ_api__mutmut_1(self) -> LogsApi:
        if self._logs_api is not None:
            self._logs_api = _build_logs_api(self._key, self._app_key, self._site)
        return self._logs_api

    def xǁDatadogLogsAdapterǁ_api__mutmut_2(self) -> LogsApi:
        if self._logs_api is None:
            self._logs_api = None
        return self._logs_api

    def xǁDatadogLogsAdapterǁ_api__mutmut_3(self) -> LogsApi:
        if self._logs_api is None:
            self._logs_api = _build_logs_api(None, self._app_key, self._site)
        return self._logs_api

    def xǁDatadogLogsAdapterǁ_api__mutmut_4(self) -> LogsApi:
        if self._logs_api is None:
            self._logs_api = _build_logs_api(self._key, None, self._site)
        return self._logs_api

    def xǁDatadogLogsAdapterǁ_api__mutmut_5(self) -> LogsApi:
        if self._logs_api is None:
            self._logs_api = _build_logs_api(self._key, self._app_key, None)
        return self._logs_api

    def xǁDatadogLogsAdapterǁ_api__mutmut_6(self) -> LogsApi:
        if self._logs_api is None:
            self._logs_api = _build_logs_api(self._app_key, self._site)
        return self._logs_api

    def xǁDatadogLogsAdapterǁ_api__mutmut_7(self) -> LogsApi:
        if self._logs_api is None:
            self._logs_api = _build_logs_api(self._key, self._site)
        return self._logs_api

    def xǁDatadogLogsAdapterǁ_api__mutmut_8(self) -> LogsApi:
        if self._logs_api is None:
            self._logs_api = _build_logs_api(self._key, self._app_key, )
        return self._logs_api

mutants_xǁDatadogLogsAdapterǁ__init____mutmut['_mutmut_orig'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ__init____mutmut['xǁDatadogLogsAdapterǁ__init____mutmut_1'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ__init____mutmut['xǁDatadogLogsAdapterǁ__init____mutmut_2'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ__init____mutmut['xǁDatadogLogsAdapterǁ__init____mutmut_3'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ__init____mutmut['xǁDatadogLogsAdapterǁ__init____mutmut_4'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ__init____mutmut['xǁDatadogLogsAdapterǁ__init____mutmut_5'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ__init____mutmut['xǁDatadogLogsAdapterǁ__init____mutmut_6'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ__init____mutmut['xǁDatadogLogsAdapterǁ__init____mutmut_7'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ__init____mutmut['xǁDatadogLogsAdapterǁ__init____mutmut_8'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ__init____mutmut_8 # type: ignore # mutmut generated

mutants_xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut['_mutmut_orig'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut['xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_1'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut['xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_2'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut['xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_3'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut['xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_4'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut['xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_5'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut['xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_6'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut['xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_7'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut['xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_8'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁfetch_pod_container_logs__mutmut_8 # type: ignore # mutmut generated

mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['_mutmut_orig'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_1'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_2'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_3'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_4'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_5'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_6'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_7'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_8'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_9'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_10'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_11'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_12'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_13'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_14'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_15'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_16'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_17'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_18'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_19'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_20'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_21'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_22'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_23'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_list_logs__mutmut['xǁDatadogLogsAdapterǁ_list_logs__mutmut_24'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_list_logs__mutmut_24 # type: ignore # mutmut generated

mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['_mutmut_orig'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_1'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_2'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_3'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_4'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_5'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_6'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_7'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_8'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_9'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_10'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_11'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_12'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_13'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_14'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_15'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_16'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_17'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_18'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_19'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_20'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_21'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_22'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_23'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_24'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_25'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_26'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_group_by_container__mutmut['xǁDatadogLogsAdapterǁ_group_by_container__mutmut_27'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_group_by_container__mutmut_27 # type: ignore # mutmut generated

mutants_xǁDatadogLogsAdapterǁ_container_name__mutmut['_mutmut_orig'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_container_name__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_container_name__mutmut['xǁDatadogLogsAdapterǁ_container_name__mutmut_1'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_container_name__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_container_name__mutmut['xǁDatadogLogsAdapterǁ_container_name__mutmut_2'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_container_name__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_container_name__mutmut['xǁDatadogLogsAdapterǁ_container_name__mutmut_3'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_container_name__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_container_name__mutmut['xǁDatadogLogsAdapterǁ_container_name__mutmut_4'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_container_name__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_container_name__mutmut['xǁDatadogLogsAdapterǁ_container_name__mutmut_5'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_container_name__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_container_name__mutmut['xǁDatadogLogsAdapterǁ_container_name__mutmut_6'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_container_name__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_container_name__mutmut['xǁDatadogLogsAdapterǁ_container_name__mutmut_7'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_container_name__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_container_name__mutmut['xǁDatadogLogsAdapterǁ_container_name__mutmut_8'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_container_name__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_container_name__mutmut['xǁDatadogLogsAdapterǁ_container_name__mutmut_9'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_container_name__mutmut_9 # type: ignore # mutmut generated

mutants_xǁDatadogLogsAdapterǁ_api__mutmut['_mutmut_orig'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_api__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_api__mutmut['xǁDatadogLogsAdapterǁ_api__mutmut_1'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_api__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_api__mutmut['xǁDatadogLogsAdapterǁ_api__mutmut_2'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_api__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_api__mutmut['xǁDatadogLogsAdapterǁ_api__mutmut_3'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_api__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_api__mutmut['xǁDatadogLogsAdapterǁ_api__mutmut_4'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_api__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_api__mutmut['xǁDatadogLogsAdapterǁ_api__mutmut_5'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_api__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_api__mutmut['xǁDatadogLogsAdapterǁ_api__mutmut_6'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_api__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_api__mutmut['xǁDatadogLogsAdapterǁ_api__mutmut_7'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_api__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDatadogLogsAdapterǁ_api__mutmut['xǁDatadogLogsAdapterǁ_api__mutmut_8'] = DatadogLogsAdapter.xǁDatadogLogsAdapterǁ_api__mutmut_8 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_orig(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_1(exc: Exception) -> Exception:
    status = None
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_2(exc: Exception) -> Exception:
    status = getattr(None, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_3(exc: Exception) -> Exception:
    status = getattr(exc, None, None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_4(exc: Exception) -> Exception:
    status = getattr("status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_5(exc: Exception) -> Exception:
    status = getattr(exc, None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_6(exc: Exception) -> Exception:
    status = getattr(exc, "status", )
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_7(exc: Exception) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_8(exc: Exception) -> Exception:
    status = getattr(exc, "STATUS", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_9(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status != _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_10(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError(None, context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_11(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context=None)
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_12(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError(context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_13(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", )
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_14(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("XXDatadog rate limit reached.XX", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_15(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_16(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("DATADOG RATE LIMIT REACHED.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_17(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"XXstatusXX": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_18(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"STATUS": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_19(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(None)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_20(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status not in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_21(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            None, context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_22(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context=None
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_23(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_24(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_25(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "XXDatadog API rejected the credentials.XX", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_26(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "datadog api rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_27(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "DATADOG API REJECTED THE CREDENTIALS.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_28(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"XXstatusXX": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_29(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"STATUS": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_30(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(None)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_31(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        None, context={"status": str(status)}
    )


def x__translate_error__mutmut_32(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context=None
    )


def x__translate_error__mutmut_33(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        context={"status": str(status)}
    )


def x__translate_error__mutmut_34(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", )


def x__translate_error__mutmut_35(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "XXDatadog Logs API request failed.XX", context={"status": str(status)}
    )


def x__translate_error__mutmut_36(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "datadog logs api request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_37(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "DATADOG LOGS API REQUEST FAILED.", context={"status": str(status)}
    )


def x__translate_error__mutmut_38(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"XXstatusXX": str(status)}
    )


def x__translate_error__mutmut_39(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"STATUS": str(status)}
    )


def x__translate_error__mutmut_40(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(None)}
    )

mutants_x__translate_error__mutmut['_mutmut_orig'] = x__translate_error__mutmut_orig # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_1'] = x__translate_error__mutmut_1 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_2'] = x__translate_error__mutmut_2 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_3'] = x__translate_error__mutmut_3 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_4'] = x__translate_error__mutmut_4 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_5'] = x__translate_error__mutmut_5 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_6'] = x__translate_error__mutmut_6 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_7'] = x__translate_error__mutmut_7 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_8'] = x__translate_error__mutmut_8 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_9'] = x__translate_error__mutmut_9 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_10'] = x__translate_error__mutmut_10 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_11'] = x__translate_error__mutmut_11 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_12'] = x__translate_error__mutmut_12 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_13'] = x__translate_error__mutmut_13 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_14'] = x__translate_error__mutmut_14 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_15'] = x__translate_error__mutmut_15 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_16'] = x__translate_error__mutmut_16 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_17'] = x__translate_error__mutmut_17 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_18'] = x__translate_error__mutmut_18 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_19'] = x__translate_error__mutmut_19 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_20'] = x__translate_error__mutmut_20 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_21'] = x__translate_error__mutmut_21 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_22'] = x__translate_error__mutmut_22 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_23'] = x__translate_error__mutmut_23 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_24'] = x__translate_error__mutmut_24 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_25'] = x__translate_error__mutmut_25 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_26'] = x__translate_error__mutmut_26 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_27'] = x__translate_error__mutmut_27 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_28'] = x__translate_error__mutmut_28 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_29'] = x__translate_error__mutmut_29 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_30'] = x__translate_error__mutmut_30 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_31'] = x__translate_error__mutmut_31 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_32'] = x__translate_error__mutmut_32 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_33'] = x__translate_error__mutmut_33 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_34'] = x__translate_error__mutmut_34 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_35'] = x__translate_error__mutmut_35 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_36'] = x__translate_error__mutmut_36 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_37'] = x__translate_error__mutmut_37 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_38'] = x__translate_error__mutmut_38 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_39'] = x__translate_error__mutmut_39 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_40'] = x__translate_error__mutmut_40 # type: ignore # mutmut generated
mutants_x__build_logs_api__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_logs_api__mutmut)
def _build_logs_api(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(LogsApi, DatadogLogsApi(ApiClient(configuration)))


def x__build_logs_api__mutmut_orig(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(LogsApi, DatadogLogsApi(ApiClient(configuration)))


def x__build_logs_api__mutmut_1(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = None
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(LogsApi, DatadogLogsApi(ApiClient(configuration)))


def x__build_logs_api__mutmut_2(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = None
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(LogsApi, DatadogLogsApi(ApiClient(configuration)))


def x__build_logs_api__mutmut_3(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = Configuration()
    configuration.api_key["XXapiKeyAuthXX"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(LogsApi, DatadogLogsApi(ApiClient(configuration)))


def x__build_logs_api__mutmut_4(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = Configuration()
    configuration.api_key["apikeyauth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(LogsApi, DatadogLogsApi(ApiClient(configuration)))


def x__build_logs_api__mutmut_5(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = Configuration()
    configuration.api_key["APIKEYAUTH"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(LogsApi, DatadogLogsApi(ApiClient(configuration)))


def x__build_logs_api__mutmut_6(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = None
    configuration.server_variables["site"] = site
    return cast(LogsApi, DatadogLogsApi(ApiClient(configuration)))


def x__build_logs_api__mutmut_7(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["XXappKeyAuthXX"] = app_key
    configuration.server_variables["site"] = site
    return cast(LogsApi, DatadogLogsApi(ApiClient(configuration)))


def x__build_logs_api__mutmut_8(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appkeyauth"] = app_key
    configuration.server_variables["site"] = site
    return cast(LogsApi, DatadogLogsApi(ApiClient(configuration)))


def x__build_logs_api__mutmut_9(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["APPKEYAUTH"] = app_key
    configuration.server_variables["site"] = site
    return cast(LogsApi, DatadogLogsApi(ApiClient(configuration)))


def x__build_logs_api__mutmut_10(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = None
    return cast(LogsApi, DatadogLogsApi(ApiClient(configuration)))


def x__build_logs_api__mutmut_11(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["XXsiteXX"] = site
    return cast(LogsApi, DatadogLogsApi(ApiClient(configuration)))


def x__build_logs_api__mutmut_12(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["SITE"] = site
    return cast(LogsApi, DatadogLogsApi(ApiClient(configuration)))


def x__build_logs_api__mutmut_13(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(None, DatadogLogsApi(ApiClient(configuration)))


def x__build_logs_api__mutmut_14(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(LogsApi, None)


def x__build_logs_api__mutmut_15(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(DatadogLogsApi(ApiClient(configuration)))


def x__build_logs_api__mutmut_16(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(LogsApi, )


def x__build_logs_api__mutmut_17(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(LogsApi, DatadogLogsApi(None))


def x__build_logs_api__mutmut_18(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(LogsApi, DatadogLogsApi(ApiClient(None)))

mutants_x__build_logs_api__mutmut['_mutmut_orig'] = x__build_logs_api__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_logs_api__mutmut['x__build_logs_api__mutmut_1'] = x__build_logs_api__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_logs_api__mutmut['x__build_logs_api__mutmut_2'] = x__build_logs_api__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_logs_api__mutmut['x__build_logs_api__mutmut_3'] = x__build_logs_api__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_logs_api__mutmut['x__build_logs_api__mutmut_4'] = x__build_logs_api__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_logs_api__mutmut['x__build_logs_api__mutmut_5'] = x__build_logs_api__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_logs_api__mutmut['x__build_logs_api__mutmut_6'] = x__build_logs_api__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_logs_api__mutmut['x__build_logs_api__mutmut_7'] = x__build_logs_api__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_logs_api__mutmut['x__build_logs_api__mutmut_8'] = x__build_logs_api__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_logs_api__mutmut['x__build_logs_api__mutmut_9'] = x__build_logs_api__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_logs_api__mutmut['x__build_logs_api__mutmut_10'] = x__build_logs_api__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_logs_api__mutmut['x__build_logs_api__mutmut_11'] = x__build_logs_api__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_logs_api__mutmut['x__build_logs_api__mutmut_12'] = x__build_logs_api__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_logs_api__mutmut['x__build_logs_api__mutmut_13'] = x__build_logs_api__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_logs_api__mutmut['x__build_logs_api__mutmut_14'] = x__build_logs_api__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_logs_api__mutmut['x__build_logs_api__mutmut_15'] = x__build_logs_api__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_logs_api__mutmut['x__build_logs_api__mutmut_16'] = x__build_logs_api__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_logs_api__mutmut['x__build_logs_api__mutmut_17'] = x__build_logs_api__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_logs_api__mutmut['x__build_logs_api__mutmut_18'] = x__build_logs_api__mutmut_18 # type: ignore # mutmut generated
