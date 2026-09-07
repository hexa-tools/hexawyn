from __future__ import annotations

from typing import cast

import httpx

from hexawyn.application.ports.driven.kubearchive_port import (
    HistoricalPodInfo,
    KubeArchivePort,
    KubeArchiveQuery,
    KubeArchiveResponse,
)
from hexawyn.domain.errors import ComponentNotInstalledError


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubeArchiveHTTPAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut: MutantDict = {}  # type: ignore


class KubeArchiveHTTPAdapter(KubeArchivePort):
    @_mutmut_mutated(mutants_xǁKubeArchiveHTTPAdapterǁ__init____mutmut)
    def __init__(self, endpoint: str) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._client = httpx.Client(timeout=10.0)
    def xǁKubeArchiveHTTPAdapterǁ__init____mutmut_orig(self, endpoint: str) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._client = httpx.Client(timeout=10.0)
    def xǁKubeArchiveHTTPAdapterǁ__init____mutmut_1(self, endpoint: str) -> None:
        self._endpoint = None
        self._client = httpx.Client(timeout=10.0)
    def xǁKubeArchiveHTTPAdapterǁ__init____mutmut_2(self, endpoint: str) -> None:
        self._endpoint = endpoint.rstrip(None)
        self._client = httpx.Client(timeout=10.0)
    def xǁKubeArchiveHTTPAdapterǁ__init____mutmut_3(self, endpoint: str) -> None:
        self._endpoint = endpoint.lstrip("/")
        self._client = httpx.Client(timeout=10.0)
    def xǁKubeArchiveHTTPAdapterǁ__init____mutmut_4(self, endpoint: str) -> None:
        self._endpoint = endpoint.rstrip("XX/XX")
        self._client = httpx.Client(timeout=10.0)
    def xǁKubeArchiveHTTPAdapterǁ__init____mutmut_5(self, endpoint: str) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._client = None
    def xǁKubeArchiveHTTPAdapterǁ__init____mutmut_6(self, endpoint: str) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._client = httpx.Client(timeout=None)
    def xǁKubeArchiveHTTPAdapterǁ__init____mutmut_7(self, endpoint: str) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._client = httpx.Client(timeout=11.0)

    def close(self) -> None:
        self._client.close()

    @_mutmut_mutated(mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut)
    def query_historical_state(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_orig(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_1(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = None
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_2(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                None,
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_3(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params=None,
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_4(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_5(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_6(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "XXnamespaceXX": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_7(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "NAMESPACE": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_8(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["XXnamespaceXX"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_9(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["NAMESPACE"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_10(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "XXkindXX": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_11(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "KIND": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_12(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["XXresource_typeXX"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_13(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["RESOURCE_TYPE"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_14(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "XXtimestampXX": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_15(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "TIMESTAMP": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_16(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["XXtimestampXX"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_17(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["TIMESTAMP"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_18(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = None
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_19(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                None,
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_20(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                None,
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_21(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context=None,
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_22(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_23(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_24(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_25(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "XXKubeArchiveXX",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_26(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "kubearchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_27(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KUBEARCHIVE",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_28(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "XXhttps://kubearchive.org/docs/installationXX",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_29(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "HTTPS://KUBEARCHIVE.ORG/DOCS/INSTALLATION",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_30(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"XXendpointXX": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_31(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"ENDPOINT": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_32(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "XXdetailXX": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_33(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "DETAIL": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_34(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(None)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_35(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = None
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_36(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get(None)
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_37(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("XXitemsXX")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_38(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("ITEMS")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_39(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = None
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_40(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None or isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_41(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_42(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_43(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    break
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_44(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = None
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_45(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(None, item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_46(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], None)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_47(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_48(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], )
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_49(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    None
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_50(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=None,
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_51(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=None,
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_52(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=None,
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_53(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=None,
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_54(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=None,
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_55(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=None,
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_56(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=None,
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_57(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_58(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_59(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_60(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_61(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_62(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_63(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_64(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(None),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_65(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get(None, "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_66(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", None)),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_67(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_68(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", )),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_69(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("XXnameXX", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_70(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("NAME", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_71(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "XXXX")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_72(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(None),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_73(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get(None, query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_74(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", None)),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_75(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get(query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_76(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", )),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_77(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("XXnamespaceXX", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_78(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("NAMESPACE", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_79(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["XXnamespaceXX"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_80(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["NAMESPACE"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_81(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(None),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_82(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get(None, "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_83(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", None)),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_84(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_85(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", )),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_86(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("XXphaseXX", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_87(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("PHASE", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_88(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "XXUnknownXX")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_89(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_90(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "UNKNOWN")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_91(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(None),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_92(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(None)),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_93(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get(None, 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_94(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", None))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_95(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get(0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_96(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", ))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_97(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("XXrestart_countXX", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_98(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("RESTART_COUNT", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_99(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 1))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_100(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            None
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_101(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get(None, query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_102(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", None)
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_103(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get(query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_104(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", )
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_105(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("XXqueried_timestampXX", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_106(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("QUERIED_TIMESTAMP", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_107(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["XXtimestampXX"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_108(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["TIMESTAMP"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_109(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(None),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_110(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get(None, True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_111(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", None)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_112(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get(True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_113(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", )),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_114(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("XXcurrently_existsXX", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_115(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("CURRENTLY_EXISTS", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_116(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", False)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_117(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(None),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_118(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get(None, False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_119(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", None)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_120(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get(False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_121(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", )),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_122(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("XXstatus_changed_sinceXX", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_123(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("STATUS_CHANGED_SINCE", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_124(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", True)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_125(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = None
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_126(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get(None, len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_127(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", None)
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_128(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get(len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_129(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", )
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_130(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("XXtotal_resourcesXX", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_131(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("TOTAL_RESOURCES", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_132(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = None

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_133(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(None) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_134(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(None)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_135(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_136(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=None,
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_137(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=None,
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_138(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=None,
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_139(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=None,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_140(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=None,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_141(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=None,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_142(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_143(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_144(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_145(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_146(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_147(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_148(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_149(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(None),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_150(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get(None, query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_151(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", None)),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_152(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get(query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_153(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", )),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_154(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("XXnamespaceXX", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_155(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("NAMESPACE", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_156(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["XXnamespaceXX"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_157(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["NAMESPACE"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_158(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(None),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_159(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get(None, query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_160(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", None)),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_161(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get(query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_162(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", )),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_163(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("XXresource_typeXX", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_164(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("RESOURCE_TYPE", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_165(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["XXresource_typeXX"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_166(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["RESOURCE_TYPE"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_167(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(None),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_168(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get(None, query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_169(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", None)),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_170(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get(query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_171(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", )),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_172(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("XXqueried_timestampXX", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_173(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("QUERIED_TIMESTAMP", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_174(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["XXtimestampXX"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_175(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["TIMESTAMP"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=True,
            error=None,
        )

    def xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_176(self, query: KubeArchiveQuery) -> KubeArchiveResponse:
        try:
            response = self._client.get(
                f"{self._endpoint}/api/v1/resources",
                params={
                    "namespace": query["namespace"],
                    "kind": query["resource_type"],
                    "timestamp": query["timestamp"],
                },
            )
            response.raise_for_status()
            data: dict[str, object] = response.json()
        except (httpx.ConnectError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            raise ComponentNotInstalledError(
                "KubeArchive",
                "https://kubearchive.org/docs/installation",
                context={"endpoint": self._endpoint, "detail": str(exc)},
            ) from exc

        raw_items = data.get("items")
        pods: list[HistoricalPodInfo] = []
        if raw_items is not None and isinstance(raw_items, list):
            for item in raw_items:
                if not isinstance(item, dict):
                    continue
                item_dict: dict[str, object] = cast(dict[str, object], item)
                pods.append(
                    HistoricalPodInfo(
                        name=str(item_dict.get("name", "")),
                        namespace=str(item_dict.get("namespace", query["namespace"])),
                        phase=str(item_dict.get("phase", "Unknown")),
                        restart_count=int(str(item_dict.get("restart_count", 0))),
                        queried_timestamp=str(
                            item_dict.get("queried_timestamp", query["timestamp"])
                        ),
                        currently_exists=bool(item_dict.get("currently_exists", True)),
                        status_changed_since=bool(item_dict.get("status_changed_since", False)),
                    )
                )

        total_resources_raw = data.get("total_resources", len(pods))
        total_resources = (
            int(str(total_resources_raw)) if total_resources_raw is not None else len(pods)
        )

        return KubeArchiveResponse(
            namespace=str(data.get("namespace", query["namespace"])),
            resource_type=str(data.get("resource_type", query["resource_type"])),
            queried_timestamp=str(data.get("queried_timestamp", query["timestamp"])),
            total_resources=total_resources,
            pods=pods,
            kubearchive_available=False,
            error=None,
        )

mutants_xǁKubeArchiveHTTPAdapterǁ__init____mutmut['_mutmut_orig'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁ__init____mutmut['xǁKubeArchiveHTTPAdapterǁ__init____mutmut_1'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁ__init____mutmut['xǁKubeArchiveHTTPAdapterǁ__init____mutmut_2'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁ__init____mutmut['xǁKubeArchiveHTTPAdapterǁ__init____mutmut_3'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁ__init____mutmut['xǁKubeArchiveHTTPAdapterǁ__init____mutmut_4'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁ__init____mutmut['xǁKubeArchiveHTTPAdapterǁ__init____mutmut_5'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁ__init____mutmut['xǁKubeArchiveHTTPAdapterǁ__init____mutmut_6'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁ__init____mutmut['xǁKubeArchiveHTTPAdapterǁ__init____mutmut_7'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁ__init____mutmut_7 # type: ignore # mutmut generated

mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['_mutmut_orig'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_1'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_2'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_3'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_4'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_5'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_6'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_7'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_8'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_9'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_10'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_11'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_12'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_13'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_14'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_15'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_16'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_17'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_18'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_19'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_20'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_21'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_22'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_23'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_24'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_25'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_26'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_27'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_28'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_29'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_30'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_31'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_32'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_32 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_33'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_33 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_34'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_34 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_35'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_35 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_36'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_36 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_37'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_37 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_38'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_38 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_39'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_39 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_40'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_40 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_41'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_41 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_42'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_42 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_43'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_43 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_44'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_44 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_45'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_45 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_46'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_46 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_47'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_47 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_48'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_48 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_49'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_49 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_50'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_50 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_51'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_51 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_52'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_52 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_53'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_53 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_54'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_54 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_55'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_55 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_56'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_56 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_57'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_57 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_58'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_58 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_59'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_59 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_60'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_60 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_61'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_61 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_62'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_62 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_63'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_63 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_64'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_64 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_65'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_65 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_66'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_66 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_67'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_67 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_68'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_68 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_69'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_69 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_70'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_70 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_71'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_71 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_72'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_72 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_73'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_73 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_74'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_74 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_75'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_75 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_76'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_76 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_77'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_77 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_78'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_78 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_79'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_79 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_80'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_80 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_81'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_81 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_82'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_82 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_83'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_83 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_84'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_84 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_85'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_85 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_86'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_86 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_87'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_87 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_88'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_88 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_89'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_89 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_90'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_90 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_91'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_91 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_92'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_92 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_93'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_93 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_94'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_94 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_95'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_95 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_96'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_96 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_97'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_97 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_98'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_98 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_99'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_99 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_100'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_100 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_101'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_101 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_102'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_102 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_103'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_103 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_104'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_104 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_105'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_105 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_106'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_106 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_107'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_107 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_108'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_108 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_109'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_109 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_110'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_110 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_111'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_111 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_112'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_112 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_113'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_113 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_114'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_114 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_115'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_115 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_116'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_116 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_117'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_117 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_118'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_118 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_119'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_119 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_120'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_120 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_121'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_121 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_122'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_122 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_123'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_123 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_124'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_124 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_125'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_125 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_126'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_126 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_127'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_127 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_128'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_128 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_129'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_129 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_130'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_130 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_131'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_131 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_132'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_132 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_133'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_133 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_134'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_134 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_135'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_135 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_136'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_136 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_137'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_137 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_138'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_138 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_139'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_139 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_140'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_140 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_141'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_141 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_142'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_142 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_143'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_143 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_144'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_144 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_145'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_145 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_146'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_146 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_147'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_147 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_148'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_148 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_149'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_149 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_150'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_150 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_151'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_151 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_152'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_152 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_153'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_153 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_154'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_154 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_155'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_155 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_156'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_156 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_157'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_157 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_158'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_158 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_159'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_159 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_160'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_160 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_161'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_161 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_162'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_162 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_163'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_163 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_164'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_164 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_165'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_165 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_166'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_166 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_167'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_167 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_168'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_168 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_169'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_169 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_170'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_170 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_171'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_171 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_172'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_172 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_173'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_173 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_174'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_174 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_175'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_175 # type: ignore # mutmut generated
mutants_xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut['xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_176'] = KubeArchiveHTTPAdapter.xǁKubeArchiveHTTPAdapterǁquery_historical_state__mutmut_176 # type: ignore # mutmut generated
