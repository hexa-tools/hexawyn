import json
import time
from collections.abc import Generator

import httpx

DEFAULT_TIMEOUT = 300.0
DEFAULT_POLL_INTERVAL = 1.0


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁRuntimeClientǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuntimeClientǁcheck_quota__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuntimeClientǁincrement_quota__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuntimeClientǁpost_investigation__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuntimeClientǁget_investigation__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuntimeClientǁpoll_investigation__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuntimeClientǁstream_investigation__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuntimeClientǁlist_custom_tools__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuntimeClientǁdescribe_custom_tool__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuntimeClientǁrun_custom_tool__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRuntimeClientǁstartup_scan__mutmut: MutantDict = {}  # type: ignore


class RuntimeClient:
    @_mutmut_mutated(mutants_xǁRuntimeClientǁ__init____mutmut)
    def __init__(self, endpoint: str, api_key: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._headers: dict[str, str] = {}
        if api_key:
            self._headers["X-API-Key"] = api_key
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            self._headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        self._client = httpx.Client(timeout=300.0)
    def xǁRuntimeClientǁ__init____mutmut_orig(self, endpoint: str, api_key: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._headers: dict[str, str] = {}
        if api_key:
            self._headers["X-API-Key"] = api_key
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            self._headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        self._client = httpx.Client(timeout=300.0)
    def xǁRuntimeClientǁ__init____mutmut_1(self, endpoint: str, api_key: str | None = None) -> None:
        self._endpoint = None
        self._headers: dict[str, str] = {}
        if api_key:
            self._headers["X-API-Key"] = api_key
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            self._headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        self._client = httpx.Client(timeout=300.0)
    def xǁRuntimeClientǁ__init____mutmut_2(self, endpoint: str, api_key: str | None = None) -> None:
        self._endpoint = endpoint.rstrip(None)
        self._headers: dict[str, str] = {}
        if api_key:
            self._headers["X-API-Key"] = api_key
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            self._headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        self._client = httpx.Client(timeout=300.0)
    def xǁRuntimeClientǁ__init____mutmut_3(self, endpoint: str, api_key: str | None = None) -> None:
        self._endpoint = endpoint.lstrip("/")
        self._headers: dict[str, str] = {}
        if api_key:
            self._headers["X-API-Key"] = api_key
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            self._headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        self._client = httpx.Client(timeout=300.0)
    def xǁRuntimeClientǁ__init____mutmut_4(self, endpoint: str, api_key: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("XX/XX")
        self._headers: dict[str, str] = {}
        if api_key:
            self._headers["X-API-Key"] = api_key
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            self._headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        self._client = httpx.Client(timeout=300.0)
    def xǁRuntimeClientǁ__init____mutmut_5(self, endpoint: str, api_key: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._headers: dict[str, str] = None
        if api_key:
            self._headers["X-API-Key"] = api_key
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            self._headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        self._client = httpx.Client(timeout=300.0)
    def xǁRuntimeClientǁ__init____mutmut_6(self, endpoint: str, api_key: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._headers: dict[str, str] = {}
        if api_key:
            self._headers["X-API-Key"] = None
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            self._headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        self._client = httpx.Client(timeout=300.0)
    def xǁRuntimeClientǁ__init____mutmut_7(self, endpoint: str, api_key: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._headers: dict[str, str] = {}
        if api_key:
            self._headers["XXX-API-KeyXX"] = api_key
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            self._headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        self._client = httpx.Client(timeout=300.0)
    def xǁRuntimeClientǁ__init____mutmut_8(self, endpoint: str, api_key: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._headers: dict[str, str] = {}
        if api_key:
            self._headers["x-api-key"] = api_key
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            self._headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        self._client = httpx.Client(timeout=300.0)
    def xǁRuntimeClientǁ__init____mutmut_9(self, endpoint: str, api_key: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._headers: dict[str, str] = {}
        if api_key:
            self._headers["X-API-KEY"] = api_key
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            self._headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        self._client = httpx.Client(timeout=300.0)
    def xǁRuntimeClientǁ__init____mutmut_10(self, endpoint: str, api_key: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._headers: dict[str, str] = {}
        if api_key:
            self._headers["X-API-Key"] = api_key
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            self._headers["X-Machine-ID"] = None
        except Exception:
            pass
        self._client = httpx.Client(timeout=300.0)
    def xǁRuntimeClientǁ__init____mutmut_11(self, endpoint: str, api_key: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._headers: dict[str, str] = {}
        if api_key:
            self._headers["X-API-Key"] = api_key
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            self._headers["XXX-Machine-IDXX"] = get_machine_id()
        except Exception:
            pass
        self._client = httpx.Client(timeout=300.0)
    def xǁRuntimeClientǁ__init____mutmut_12(self, endpoint: str, api_key: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._headers: dict[str, str] = {}
        if api_key:
            self._headers["X-API-Key"] = api_key
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            self._headers["x-machine-id"] = get_machine_id()
        except Exception:
            pass
        self._client = httpx.Client(timeout=300.0)
    def xǁRuntimeClientǁ__init____mutmut_13(self, endpoint: str, api_key: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._headers: dict[str, str] = {}
        if api_key:
            self._headers["X-API-Key"] = api_key
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            self._headers["X-MACHINE-ID"] = get_machine_id()
        except Exception:
            pass
        self._client = httpx.Client(timeout=300.0)
    def xǁRuntimeClientǁ__init____mutmut_14(self, endpoint: str, api_key: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._headers: dict[str, str] = {}
        if api_key:
            self._headers["X-API-Key"] = api_key
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            self._headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        self._client = None
    def xǁRuntimeClientǁ__init____mutmut_15(self, endpoint: str, api_key: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._headers: dict[str, str] = {}
        if api_key:
            self._headers["X-API-Key"] = api_key
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            self._headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        self._client = httpx.Client(timeout=None)
    def xǁRuntimeClientǁ__init____mutmut_16(self, endpoint: str, api_key: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._headers: dict[str, str] = {}
        if api_key:
            self._headers["X-API-Key"] = api_key
        try:
            from hexawyn.infrastructure.config.machine_id import get_machine_id  # hexa-lazy-import

            self._headers["X-Machine-ID"] = get_machine_id()
        except Exception:
            pass
        self._client = httpx.Client(timeout=301.0)

    def close(self) -> None:
        self._client.close()

    @_mutmut_mutated(mutants_xǁRuntimeClientǁcheck_quota__mutmut)
    def check_quota(self) -> dict[str, object]:
        response = self._client.get(f"{self._endpoint}/api/v1/quota", headers=self._headers)
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁcheck_quota__mutmut_orig(self) -> dict[str, object]:
        response = self._client.get(f"{self._endpoint}/api/v1/quota", headers=self._headers)
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁcheck_quota__mutmut_1(self) -> dict[str, object]:
        response = None
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁcheck_quota__mutmut_2(self) -> dict[str, object]:
        response = self._client.get(None, headers=self._headers)
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁcheck_quota__mutmut_3(self) -> dict[str, object]:
        response = self._client.get(f"{self._endpoint}/api/v1/quota", headers=None)
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁcheck_quota__mutmut_4(self) -> dict[str, object]:
        response = self._client.get(headers=self._headers)
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁcheck_quota__mutmut_5(self) -> dict[str, object]:
        response = self._client.get(f"{self._endpoint}/api/v1/quota", )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁcheck_quota__mutmut_6(self) -> dict[str, object]:
        response = self._client.get(f"{self._endpoint}/api/v1/quota", headers=self._headers)
        response.raise_for_status()
        data: dict[str, object] = None
        return data

    @_mutmut_mutated(mutants_xǁRuntimeClientǁincrement_quota__mutmut)
    def increment_quota(self) -> None:
        response = self._client.post(
            f"{self._endpoint}/api/v1/quota/increment", headers=self._headers
        )
        response.raise_for_status()

    def xǁRuntimeClientǁincrement_quota__mutmut_orig(self) -> None:
        response = self._client.post(
            f"{self._endpoint}/api/v1/quota/increment", headers=self._headers
        )
        response.raise_for_status()

    def xǁRuntimeClientǁincrement_quota__mutmut_1(self) -> None:
        response = None
        response.raise_for_status()

    def xǁRuntimeClientǁincrement_quota__mutmut_2(self) -> None:
        response = self._client.post(
            None, headers=self._headers
        )
        response.raise_for_status()

    def xǁRuntimeClientǁincrement_quota__mutmut_3(self) -> None:
        response = self._client.post(
            f"{self._endpoint}/api/v1/quota/increment", headers=None
        )
        response.raise_for_status()

    def xǁRuntimeClientǁincrement_quota__mutmut_4(self) -> None:
        response = self._client.post(
            headers=self._headers
        )
        response.raise_for_status()

    def xǁRuntimeClientǁincrement_quota__mutmut_5(self) -> None:
        response = self._client.post(
            f"{self._endpoint}/api/v1/quota/increment", )
        response.raise_for_status()

    @_mutmut_mutated(mutants_xǁRuntimeClientǁpost_investigation__mutmut)
    def post_investigation(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            f"{self._endpoint}/api/v1/investigations",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
            },
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["job_id"])

    def xǁRuntimeClientǁpost_investigation__mutmut_orig(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            f"{self._endpoint}/api/v1/investigations",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
            },
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["job_id"])

    def xǁRuntimeClientǁpost_investigation__mutmut_1(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = None
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["job_id"])

    def xǁRuntimeClientǁpost_investigation__mutmut_2(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            None,
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
            },
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["job_id"])

    def xǁRuntimeClientǁpost_investigation__mutmut_3(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            f"{self._endpoint}/api/v1/investigations",
            json=None,
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["job_id"])

    def xǁRuntimeClientǁpost_investigation__mutmut_4(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            f"{self._endpoint}/api/v1/investigations",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
            },
            headers=None,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["job_id"])

    def xǁRuntimeClientǁpost_investigation__mutmut_5(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
            },
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["job_id"])

    def xǁRuntimeClientǁpost_investigation__mutmut_6(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            f"{self._endpoint}/api/v1/investigations",
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["job_id"])

    def xǁRuntimeClientǁpost_investigation__mutmut_7(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            f"{self._endpoint}/api/v1/investigations",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
            },
            )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["job_id"])

    def xǁRuntimeClientǁpost_investigation__mutmut_8(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            f"{self._endpoint}/api/v1/investigations",
            json={
                "XXqueryXX": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
            },
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["job_id"])

    def xǁRuntimeClientǁpost_investigation__mutmut_9(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            f"{self._endpoint}/api/v1/investigations",
            json={
                "QUERY": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
            },
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["job_id"])

    def xǁRuntimeClientǁpost_investigation__mutmut_10(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            f"{self._endpoint}/api/v1/investigations",
            json={
                "query": query,
                "XXcluster_nameXX": cluster_name,
                "provider": provider,
                "pods": pods or [],
            },
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["job_id"])

    def xǁRuntimeClientǁpost_investigation__mutmut_11(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            f"{self._endpoint}/api/v1/investigations",
            json={
                "query": query,
                "CLUSTER_NAME": cluster_name,
                "provider": provider,
                "pods": pods or [],
            },
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["job_id"])

    def xǁRuntimeClientǁpost_investigation__mutmut_12(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            f"{self._endpoint}/api/v1/investigations",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "XXproviderXX": provider,
                "pods": pods or [],
            },
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["job_id"])

    def xǁRuntimeClientǁpost_investigation__mutmut_13(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            f"{self._endpoint}/api/v1/investigations",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "PROVIDER": provider,
                "pods": pods or [],
            },
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["job_id"])

    def xǁRuntimeClientǁpost_investigation__mutmut_14(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            f"{self._endpoint}/api/v1/investigations",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "XXpodsXX": pods or [],
            },
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["job_id"])

    def xǁRuntimeClientǁpost_investigation__mutmut_15(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            f"{self._endpoint}/api/v1/investigations",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "PODS": pods or [],
            },
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["job_id"])

    def xǁRuntimeClientǁpost_investigation__mutmut_16(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            f"{self._endpoint}/api/v1/investigations",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods and [],
            },
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["job_id"])

    def xǁRuntimeClientǁpost_investigation__mutmut_17(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            f"{self._endpoint}/api/v1/investigations",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
            },
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = None
        return str(data["job_id"])

    def xǁRuntimeClientǁpost_investigation__mutmut_18(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            f"{self._endpoint}/api/v1/investigations",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
            },
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(None)

    def xǁRuntimeClientǁpost_investigation__mutmut_19(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            f"{self._endpoint}/api/v1/investigations",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
            },
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["XXjob_idXX"])

    def xǁRuntimeClientǁpost_investigation__mutmut_20(
        self,
        query: str,
        cluster_name: str,
        provider: str,
        pods: list[dict[str, object]] | None = None,
    ) -> str:
        response = self._client.post(
            f"{self._endpoint}/api/v1/investigations",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
            },
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return str(data["JOB_ID"])

    @_mutmut_mutated(mutants_xǁRuntimeClientǁget_investigation__mutmut)
    def get_investigation(self, job_id: str) -> dict[str, object]:
        response = self._client.get(
            f"{self._endpoint}/api/v1/investigations/{job_id}",
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁget_investigation__mutmut_orig(self, job_id: str) -> dict[str, object]:
        response = self._client.get(
            f"{self._endpoint}/api/v1/investigations/{job_id}",
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁget_investigation__mutmut_1(self, job_id: str) -> dict[str, object]:
        response = None
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁget_investigation__mutmut_2(self, job_id: str) -> dict[str, object]:
        response = self._client.get(
            None,
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁget_investigation__mutmut_3(self, job_id: str) -> dict[str, object]:
        response = self._client.get(
            f"{self._endpoint}/api/v1/investigations/{job_id}",
            headers=None,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁget_investigation__mutmut_4(self, job_id: str) -> dict[str, object]:
        response = self._client.get(
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁget_investigation__mutmut_5(self, job_id: str) -> dict[str, object]:
        response = self._client.get(
            f"{self._endpoint}/api/v1/investigations/{job_id}",
            )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁget_investigation__mutmut_6(self, job_id: str) -> dict[str, object]:
        response = self._client.get(
            f"{self._endpoint}/api/v1/investigations/{job_id}",
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = None
        return data

    @_mutmut_mutated(mutants_xǁRuntimeClientǁpoll_investigation__mutmut)
    def poll_investigation(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_orig(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_1(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = None
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_2(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() - timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_3(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = None
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_4(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"XXjob_idXX": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_5(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"JOB_ID": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_6(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "XXstatusXX": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_7(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "STATUS": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_8(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "XXpendingXX", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_9(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "PENDING", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_10(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "XXresultXX": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_11(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "RESULT": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_12(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() <= deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_13(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = None
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_14(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(None)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_15(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = None
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_16(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(None)
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_17(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get(None, ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_18(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", None))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_19(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get(""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_20(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_21(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("XXstatusXX", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_22(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("STATUS", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_23(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", "XXXX"))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_24(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status not in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_25(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("XXcompletedXX", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_26(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("COMPLETED", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_27(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "XXfailedXX", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_28(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "FAILED", "complete", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_29(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "XXcompleteXX", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_30(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "COMPLETE", "degraded", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_31(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "XXdegradedXX", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_32(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "DEGRADED", "error"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_33(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "XXerrorXX"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_34(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "ERROR"):
                return status_response
            time.sleep(interval)
        return status_response

    def xǁRuntimeClientǁpoll_investigation__mutmut_35(
        self,
        job_id: str,
        timeout: float = DEFAULT_TIMEOUT,
        interval: float = DEFAULT_POLL_INTERVAL,
    ) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        status_response: dict[str, object] = {"job_id": job_id, "status": "pending", "result": None}
        while time.monotonic() < deadline:
            status_response = self.get_investigation(job_id)
            current_status = str(status_response.get("status", ""))
            if current_status in ("completed", "failed", "complete", "degraded", "error"):
                return status_response
            time.sleep(None)
        return status_response

    @_mutmut_mutated(mutants_xǁRuntimeClientǁstream_investigation__mutmut)
    def stream_investigation(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_orig(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_1(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "XXunknownXX",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_2(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "UNKNOWN",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_3(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "XXvanillaXX",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_4(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "VANILLA",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_5(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            None,
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_6(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            None,
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_7(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json=None,
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_8(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=None,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_9(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_10(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_11(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_12(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_13(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "XXPOSTXX",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_14(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "post",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_15(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "XXqueryXX": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_16(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "QUERY": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_17(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "XXcluster_nameXX": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_18(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "CLUSTER_NAME": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_19(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "XXproviderXX": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_20(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "PROVIDER": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_21(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "XXpodsXX": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_22(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "PODS": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_23(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods and [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_24(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "XXconversation_historyXX": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_25(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "CONVERSATION_HISTORY": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_26(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history and [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_27(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_28(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith(None):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_29(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("XXdata: XX"):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_30(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("DATA: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_31(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    break
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_32(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = None
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_33(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = None
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_34(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(None)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_35(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    break
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_36(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "XXdoneXX" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_37(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "DONE" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_38(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" not in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_39(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    return
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_40(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "XXerrorXX" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_41(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "ERROR" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_42(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" not in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_43(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("XXerrorXX", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_44(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("ERROR", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_45(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    return
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_46(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "XXnodeXX" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_47(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "NODE" not in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_48(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" in event:
                    continue
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_49(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    break
                yield (event["node"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_50(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["XXnodeXX"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_51(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["NODE"], event.get("output", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_52(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get(None, {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_53(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", None))

    def xǁRuntimeClientǁstream_investigation__mutmut_54(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get({}))

    def xǁRuntimeClientǁstream_investigation__mutmut_55(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("output", ))

    def xǁRuntimeClientǁstream_investigation__mutmut_56(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("XXoutputXX", {}))

    def xǁRuntimeClientǁstream_investigation__mutmut_57(  # noqa: PLR0913
        self,
        query: str,
        cluster_name: str = "unknown",
        provider: str = "vanilla",
        pods: list[dict[str, object]] | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> Generator[tuple[str, dict[str, object]], None, None]:
        """Stream investigation results via SSE. Yields (node_name, output) tuples."""
        with self._client.stream(
            "POST",
            f"{self._endpoint}/api/v1/investigations/stream",
            json={
                "query": query,
                "cluster_name": cluster_name,
                "provider": provider,
                "pods": pods or [],
                "conversation_history": conversation_history or [],
            },
            headers=self._headers,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data: "):
                    continue
                data = line[len("data: ") :]
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "done" in event:
                    break
                if "error" in event:
                    yield ("error", event)
                    break
                if "node" not in event:
                    continue
                yield (event["node"], event.get("OUTPUT", {}))

    @_mutmut_mutated(mutants_xǁRuntimeClientǁlist_custom_tools__mutmut)
    def list_custom_tools(self) -> list[dict[str, object]]:
        response = self._client.get(f"{self._endpoint}/api/v1/custom-tools", headers=self._headers)
        response.raise_for_status()
        data: list[dict[str, object]] = response.json()
        return data

    def xǁRuntimeClientǁlist_custom_tools__mutmut_orig(self) -> list[dict[str, object]]:
        response = self._client.get(f"{self._endpoint}/api/v1/custom-tools", headers=self._headers)
        response.raise_for_status()
        data: list[dict[str, object]] = response.json()
        return data

    def xǁRuntimeClientǁlist_custom_tools__mutmut_1(self) -> list[dict[str, object]]:
        response = None
        response.raise_for_status()
        data: list[dict[str, object]] = response.json()
        return data

    def xǁRuntimeClientǁlist_custom_tools__mutmut_2(self) -> list[dict[str, object]]:
        response = self._client.get(None, headers=self._headers)
        response.raise_for_status()
        data: list[dict[str, object]] = response.json()
        return data

    def xǁRuntimeClientǁlist_custom_tools__mutmut_3(self) -> list[dict[str, object]]:
        response = self._client.get(f"{self._endpoint}/api/v1/custom-tools", headers=None)
        response.raise_for_status()
        data: list[dict[str, object]] = response.json()
        return data

    def xǁRuntimeClientǁlist_custom_tools__mutmut_4(self) -> list[dict[str, object]]:
        response = self._client.get(headers=self._headers)
        response.raise_for_status()
        data: list[dict[str, object]] = response.json()
        return data

    def xǁRuntimeClientǁlist_custom_tools__mutmut_5(self) -> list[dict[str, object]]:
        response = self._client.get(f"{self._endpoint}/api/v1/custom-tools", )
        response.raise_for_status()
        data: list[dict[str, object]] = response.json()
        return data

    def xǁRuntimeClientǁlist_custom_tools__mutmut_6(self) -> list[dict[str, object]]:
        response = self._client.get(f"{self._endpoint}/api/v1/custom-tools", headers=self._headers)
        response.raise_for_status()
        data: list[dict[str, object]] = None
        return data

    @_mutmut_mutated(mutants_xǁRuntimeClientǁdescribe_custom_tool__mutmut)
    def describe_custom_tool(self, name: str) -> dict[str, object]:
        response = self._client.get(
            f"{self._endpoint}/api/v1/custom-tools/{name}", headers=self._headers
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁdescribe_custom_tool__mutmut_orig(self, name: str) -> dict[str, object]:
        response = self._client.get(
            f"{self._endpoint}/api/v1/custom-tools/{name}", headers=self._headers
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁdescribe_custom_tool__mutmut_1(self, name: str) -> dict[str, object]:
        response = None
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁdescribe_custom_tool__mutmut_2(self, name: str) -> dict[str, object]:
        response = self._client.get(
            None, headers=self._headers
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁdescribe_custom_tool__mutmut_3(self, name: str) -> dict[str, object]:
        response = self._client.get(
            f"{self._endpoint}/api/v1/custom-tools/{name}", headers=None
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁdescribe_custom_tool__mutmut_4(self, name: str) -> dict[str, object]:
        response = self._client.get(
            headers=self._headers
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁdescribe_custom_tool__mutmut_5(self, name: str) -> dict[str, object]:
        response = self._client.get(
            f"{self._endpoint}/api/v1/custom-tools/{name}", )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁdescribe_custom_tool__mutmut_6(self, name: str) -> dict[str, object]:
        response = self._client.get(
            f"{self._endpoint}/api/v1/custom-tools/{name}", headers=self._headers
        )
        response.raise_for_status()
        data: dict[str, object] = None
        return data

    @_mutmut_mutated(mutants_xǁRuntimeClientǁrun_custom_tool__mutmut)
    def run_custom_tool(self, name: str, params: dict[str, object]) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/custom-tools/{name}/run",
            json=params,
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁrun_custom_tool__mutmut_orig(self, name: str, params: dict[str, object]) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/custom-tools/{name}/run",
            json=params,
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁrun_custom_tool__mutmut_1(self, name: str, params: dict[str, object]) -> dict[str, object]:
        response = None
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁrun_custom_tool__mutmut_2(self, name: str, params: dict[str, object]) -> dict[str, object]:
        response = self._client.post(
            None,
            json=params,
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁrun_custom_tool__mutmut_3(self, name: str, params: dict[str, object]) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/custom-tools/{name}/run",
            json=None,
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁrun_custom_tool__mutmut_4(self, name: str, params: dict[str, object]) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/custom-tools/{name}/run",
            json=params,
            headers=None,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁrun_custom_tool__mutmut_5(self, name: str, params: dict[str, object]) -> dict[str, object]:
        response = self._client.post(
            json=params,
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁrun_custom_tool__mutmut_6(self, name: str, params: dict[str, object]) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/custom-tools/{name}/run",
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁrun_custom_tool__mutmut_7(self, name: str, params: dict[str, object]) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/custom-tools/{name}/run",
            json=params,
            )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁrun_custom_tool__mutmut_8(self, name: str, params: dict[str, object]) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/custom-tools/{name}/run",
            json=params,
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = None
        return data

    @_mutmut_mutated(mutants_xǁRuntimeClientǁstartup_scan__mutmut)
    def startup_scan(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/startup-scan",
            json={"cluster_name": cluster_name, "pods": pods or []},
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁstartup_scan__mutmut_orig(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/startup-scan",
            json={"cluster_name": cluster_name, "pods": pods or []},
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁstartup_scan__mutmut_1(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> dict[str, object]:
        response = None
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁstartup_scan__mutmut_2(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> dict[str, object]:
        response = self._client.post(
            None,
            json={"cluster_name": cluster_name, "pods": pods or []},
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁstartup_scan__mutmut_3(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/startup-scan",
            json=None,
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁstartup_scan__mutmut_4(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/startup-scan",
            json={"cluster_name": cluster_name, "pods": pods or []},
            headers=None,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁstartup_scan__mutmut_5(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> dict[str, object]:
        response = self._client.post(
            json={"cluster_name": cluster_name, "pods": pods or []},
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁstartup_scan__mutmut_6(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/startup-scan",
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁstartup_scan__mutmut_7(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/startup-scan",
            json={"cluster_name": cluster_name, "pods": pods or []},
            )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁstartup_scan__mutmut_8(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/startup-scan",
            json={"XXcluster_nameXX": cluster_name, "pods": pods or []},
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁstartup_scan__mutmut_9(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/startup-scan",
            json={"CLUSTER_NAME": cluster_name, "pods": pods or []},
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁstartup_scan__mutmut_10(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/startup-scan",
            json={"cluster_name": cluster_name, "XXpodsXX": pods or []},
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁstartup_scan__mutmut_11(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/startup-scan",
            json={"cluster_name": cluster_name, "PODS": pods or []},
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁstartup_scan__mutmut_12(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/startup-scan",
            json={"cluster_name": cluster_name, "pods": pods and []},
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = response.json()
        return data

    def xǁRuntimeClientǁstartup_scan__mutmut_13(
        self, cluster_name: str, pods: list[dict[str, object]] | None = None
    ) -> dict[str, object]:
        response = self._client.post(
            f"{self._endpoint}/api/v1/startup-scan",
            json={"cluster_name": cluster_name, "pods": pods or []},
            headers=self._headers,
        )
        response.raise_for_status()
        data: dict[str, object] = None
        return data

mutants_xǁRuntimeClientǁ__init____mutmut['_mutmut_orig'] = RuntimeClient.xǁRuntimeClientǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁ__init____mutmut['xǁRuntimeClientǁ__init____mutmut_1'] = RuntimeClient.xǁRuntimeClientǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁ__init____mutmut['xǁRuntimeClientǁ__init____mutmut_2'] = RuntimeClient.xǁRuntimeClientǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁ__init____mutmut['xǁRuntimeClientǁ__init____mutmut_3'] = RuntimeClient.xǁRuntimeClientǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁ__init____mutmut['xǁRuntimeClientǁ__init____mutmut_4'] = RuntimeClient.xǁRuntimeClientǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁ__init____mutmut['xǁRuntimeClientǁ__init____mutmut_5'] = RuntimeClient.xǁRuntimeClientǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁ__init____mutmut['xǁRuntimeClientǁ__init____mutmut_6'] = RuntimeClient.xǁRuntimeClientǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁ__init____mutmut['xǁRuntimeClientǁ__init____mutmut_7'] = RuntimeClient.xǁRuntimeClientǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁ__init____mutmut['xǁRuntimeClientǁ__init____mutmut_8'] = RuntimeClient.xǁRuntimeClientǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁ__init____mutmut['xǁRuntimeClientǁ__init____mutmut_9'] = RuntimeClient.xǁRuntimeClientǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁ__init____mutmut['xǁRuntimeClientǁ__init____mutmut_10'] = RuntimeClient.xǁRuntimeClientǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁ__init____mutmut['xǁRuntimeClientǁ__init____mutmut_11'] = RuntimeClient.xǁRuntimeClientǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁ__init____mutmut['xǁRuntimeClientǁ__init____mutmut_12'] = RuntimeClient.xǁRuntimeClientǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁ__init____mutmut['xǁRuntimeClientǁ__init____mutmut_13'] = RuntimeClient.xǁRuntimeClientǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁ__init____mutmut['xǁRuntimeClientǁ__init____mutmut_14'] = RuntimeClient.xǁRuntimeClientǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁ__init____mutmut['xǁRuntimeClientǁ__init____mutmut_15'] = RuntimeClient.xǁRuntimeClientǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁ__init____mutmut['xǁRuntimeClientǁ__init____mutmut_16'] = RuntimeClient.xǁRuntimeClientǁ__init____mutmut_16 # type: ignore # mutmut generated

mutants_xǁRuntimeClientǁcheck_quota__mutmut['_mutmut_orig'] = RuntimeClient.xǁRuntimeClientǁcheck_quota__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁcheck_quota__mutmut['xǁRuntimeClientǁcheck_quota__mutmut_1'] = RuntimeClient.xǁRuntimeClientǁcheck_quota__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁcheck_quota__mutmut['xǁRuntimeClientǁcheck_quota__mutmut_2'] = RuntimeClient.xǁRuntimeClientǁcheck_quota__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁcheck_quota__mutmut['xǁRuntimeClientǁcheck_quota__mutmut_3'] = RuntimeClient.xǁRuntimeClientǁcheck_quota__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁcheck_quota__mutmut['xǁRuntimeClientǁcheck_quota__mutmut_4'] = RuntimeClient.xǁRuntimeClientǁcheck_quota__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁcheck_quota__mutmut['xǁRuntimeClientǁcheck_quota__mutmut_5'] = RuntimeClient.xǁRuntimeClientǁcheck_quota__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁcheck_quota__mutmut['xǁRuntimeClientǁcheck_quota__mutmut_6'] = RuntimeClient.xǁRuntimeClientǁcheck_quota__mutmut_6 # type: ignore # mutmut generated

mutants_xǁRuntimeClientǁincrement_quota__mutmut['_mutmut_orig'] = RuntimeClient.xǁRuntimeClientǁincrement_quota__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁincrement_quota__mutmut['xǁRuntimeClientǁincrement_quota__mutmut_1'] = RuntimeClient.xǁRuntimeClientǁincrement_quota__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁincrement_quota__mutmut['xǁRuntimeClientǁincrement_quota__mutmut_2'] = RuntimeClient.xǁRuntimeClientǁincrement_quota__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁincrement_quota__mutmut['xǁRuntimeClientǁincrement_quota__mutmut_3'] = RuntimeClient.xǁRuntimeClientǁincrement_quota__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁincrement_quota__mutmut['xǁRuntimeClientǁincrement_quota__mutmut_4'] = RuntimeClient.xǁRuntimeClientǁincrement_quota__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁincrement_quota__mutmut['xǁRuntimeClientǁincrement_quota__mutmut_5'] = RuntimeClient.xǁRuntimeClientǁincrement_quota__mutmut_5 # type: ignore # mutmut generated

mutants_xǁRuntimeClientǁpost_investigation__mutmut['_mutmut_orig'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpost_investigation__mutmut['xǁRuntimeClientǁpost_investigation__mutmut_1'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpost_investigation__mutmut['xǁRuntimeClientǁpost_investigation__mutmut_2'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpost_investigation__mutmut['xǁRuntimeClientǁpost_investigation__mutmut_3'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpost_investigation__mutmut['xǁRuntimeClientǁpost_investigation__mutmut_4'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpost_investigation__mutmut['xǁRuntimeClientǁpost_investigation__mutmut_5'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpost_investigation__mutmut['xǁRuntimeClientǁpost_investigation__mutmut_6'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpost_investigation__mutmut['xǁRuntimeClientǁpost_investigation__mutmut_7'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpost_investigation__mutmut['xǁRuntimeClientǁpost_investigation__mutmut_8'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpost_investigation__mutmut['xǁRuntimeClientǁpost_investigation__mutmut_9'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpost_investigation__mutmut['xǁRuntimeClientǁpost_investigation__mutmut_10'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpost_investigation__mutmut['xǁRuntimeClientǁpost_investigation__mutmut_11'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpost_investigation__mutmut['xǁRuntimeClientǁpost_investigation__mutmut_12'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpost_investigation__mutmut['xǁRuntimeClientǁpost_investigation__mutmut_13'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpost_investigation__mutmut['xǁRuntimeClientǁpost_investigation__mutmut_14'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpost_investigation__mutmut['xǁRuntimeClientǁpost_investigation__mutmut_15'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpost_investigation__mutmut['xǁRuntimeClientǁpost_investigation__mutmut_16'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpost_investigation__mutmut['xǁRuntimeClientǁpost_investigation__mutmut_17'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpost_investigation__mutmut['xǁRuntimeClientǁpost_investigation__mutmut_18'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpost_investigation__mutmut['xǁRuntimeClientǁpost_investigation__mutmut_19'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpost_investigation__mutmut['xǁRuntimeClientǁpost_investigation__mutmut_20'] = RuntimeClient.xǁRuntimeClientǁpost_investigation__mutmut_20 # type: ignore # mutmut generated

mutants_xǁRuntimeClientǁget_investigation__mutmut['_mutmut_orig'] = RuntimeClient.xǁRuntimeClientǁget_investigation__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁget_investigation__mutmut['xǁRuntimeClientǁget_investigation__mutmut_1'] = RuntimeClient.xǁRuntimeClientǁget_investigation__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁget_investigation__mutmut['xǁRuntimeClientǁget_investigation__mutmut_2'] = RuntimeClient.xǁRuntimeClientǁget_investigation__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁget_investigation__mutmut['xǁRuntimeClientǁget_investigation__mutmut_3'] = RuntimeClient.xǁRuntimeClientǁget_investigation__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁget_investigation__mutmut['xǁRuntimeClientǁget_investigation__mutmut_4'] = RuntimeClient.xǁRuntimeClientǁget_investigation__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁget_investigation__mutmut['xǁRuntimeClientǁget_investigation__mutmut_5'] = RuntimeClient.xǁRuntimeClientǁget_investigation__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁget_investigation__mutmut['xǁRuntimeClientǁget_investigation__mutmut_6'] = RuntimeClient.xǁRuntimeClientǁget_investigation__mutmut_6 # type: ignore # mutmut generated

mutants_xǁRuntimeClientǁpoll_investigation__mutmut['_mutmut_orig'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_1'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_2'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_3'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_4'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_5'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_6'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_7'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_8'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_9'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_10'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_11'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_12'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_13'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_14'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_15'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_16'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_17'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_18'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_19'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_20'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_21'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_22'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_23'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_24'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_25'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_26'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_27'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_28'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_29'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_30'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_30 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_31'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_31 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_32'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_32 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_33'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_33 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_34'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_34 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁpoll_investigation__mutmut['xǁRuntimeClientǁpoll_investigation__mutmut_35'] = RuntimeClient.xǁRuntimeClientǁpoll_investigation__mutmut_35 # type: ignore # mutmut generated

mutants_xǁRuntimeClientǁstream_investigation__mutmut['_mutmut_orig'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_1'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_2'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_3'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_4'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_5'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_6'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_7'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_8'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_9'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_10'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_11'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_12'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_13'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_14'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_15'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_16'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_17'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_18'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_19'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_20'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_21'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_22'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_23'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_24'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_25'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_26'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_27'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_28'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_29'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_30'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_30 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_31'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_31 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_32'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_32 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_33'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_33 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_34'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_34 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_35'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_35 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_36'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_36 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_37'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_37 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_38'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_38 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_39'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_39 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_40'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_40 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_41'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_41 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_42'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_42 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_43'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_43 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_44'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_44 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_45'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_45 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_46'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_46 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_47'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_47 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_48'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_48 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_49'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_49 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_50'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_50 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_51'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_51 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_52'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_52 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_53'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_53 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_54'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_54 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_55'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_55 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_56'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_56 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstream_investigation__mutmut['xǁRuntimeClientǁstream_investigation__mutmut_57'] = RuntimeClient.xǁRuntimeClientǁstream_investigation__mutmut_57 # type: ignore # mutmut generated

mutants_xǁRuntimeClientǁlist_custom_tools__mutmut['_mutmut_orig'] = RuntimeClient.xǁRuntimeClientǁlist_custom_tools__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁlist_custom_tools__mutmut['xǁRuntimeClientǁlist_custom_tools__mutmut_1'] = RuntimeClient.xǁRuntimeClientǁlist_custom_tools__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁlist_custom_tools__mutmut['xǁRuntimeClientǁlist_custom_tools__mutmut_2'] = RuntimeClient.xǁRuntimeClientǁlist_custom_tools__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁlist_custom_tools__mutmut['xǁRuntimeClientǁlist_custom_tools__mutmut_3'] = RuntimeClient.xǁRuntimeClientǁlist_custom_tools__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁlist_custom_tools__mutmut['xǁRuntimeClientǁlist_custom_tools__mutmut_4'] = RuntimeClient.xǁRuntimeClientǁlist_custom_tools__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁlist_custom_tools__mutmut['xǁRuntimeClientǁlist_custom_tools__mutmut_5'] = RuntimeClient.xǁRuntimeClientǁlist_custom_tools__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁlist_custom_tools__mutmut['xǁRuntimeClientǁlist_custom_tools__mutmut_6'] = RuntimeClient.xǁRuntimeClientǁlist_custom_tools__mutmut_6 # type: ignore # mutmut generated

mutants_xǁRuntimeClientǁdescribe_custom_tool__mutmut['_mutmut_orig'] = RuntimeClient.xǁRuntimeClientǁdescribe_custom_tool__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁdescribe_custom_tool__mutmut['xǁRuntimeClientǁdescribe_custom_tool__mutmut_1'] = RuntimeClient.xǁRuntimeClientǁdescribe_custom_tool__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁdescribe_custom_tool__mutmut['xǁRuntimeClientǁdescribe_custom_tool__mutmut_2'] = RuntimeClient.xǁRuntimeClientǁdescribe_custom_tool__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁdescribe_custom_tool__mutmut['xǁRuntimeClientǁdescribe_custom_tool__mutmut_3'] = RuntimeClient.xǁRuntimeClientǁdescribe_custom_tool__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁdescribe_custom_tool__mutmut['xǁRuntimeClientǁdescribe_custom_tool__mutmut_4'] = RuntimeClient.xǁRuntimeClientǁdescribe_custom_tool__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁdescribe_custom_tool__mutmut['xǁRuntimeClientǁdescribe_custom_tool__mutmut_5'] = RuntimeClient.xǁRuntimeClientǁdescribe_custom_tool__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁdescribe_custom_tool__mutmut['xǁRuntimeClientǁdescribe_custom_tool__mutmut_6'] = RuntimeClient.xǁRuntimeClientǁdescribe_custom_tool__mutmut_6 # type: ignore # mutmut generated

mutants_xǁRuntimeClientǁrun_custom_tool__mutmut['_mutmut_orig'] = RuntimeClient.xǁRuntimeClientǁrun_custom_tool__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁrun_custom_tool__mutmut['xǁRuntimeClientǁrun_custom_tool__mutmut_1'] = RuntimeClient.xǁRuntimeClientǁrun_custom_tool__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁrun_custom_tool__mutmut['xǁRuntimeClientǁrun_custom_tool__mutmut_2'] = RuntimeClient.xǁRuntimeClientǁrun_custom_tool__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁrun_custom_tool__mutmut['xǁRuntimeClientǁrun_custom_tool__mutmut_3'] = RuntimeClient.xǁRuntimeClientǁrun_custom_tool__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁrun_custom_tool__mutmut['xǁRuntimeClientǁrun_custom_tool__mutmut_4'] = RuntimeClient.xǁRuntimeClientǁrun_custom_tool__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁrun_custom_tool__mutmut['xǁRuntimeClientǁrun_custom_tool__mutmut_5'] = RuntimeClient.xǁRuntimeClientǁrun_custom_tool__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁrun_custom_tool__mutmut['xǁRuntimeClientǁrun_custom_tool__mutmut_6'] = RuntimeClient.xǁRuntimeClientǁrun_custom_tool__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁrun_custom_tool__mutmut['xǁRuntimeClientǁrun_custom_tool__mutmut_7'] = RuntimeClient.xǁRuntimeClientǁrun_custom_tool__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁrun_custom_tool__mutmut['xǁRuntimeClientǁrun_custom_tool__mutmut_8'] = RuntimeClient.xǁRuntimeClientǁrun_custom_tool__mutmut_8 # type: ignore # mutmut generated

mutants_xǁRuntimeClientǁstartup_scan__mutmut['_mutmut_orig'] = RuntimeClient.xǁRuntimeClientǁstartup_scan__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstartup_scan__mutmut['xǁRuntimeClientǁstartup_scan__mutmut_1'] = RuntimeClient.xǁRuntimeClientǁstartup_scan__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstartup_scan__mutmut['xǁRuntimeClientǁstartup_scan__mutmut_2'] = RuntimeClient.xǁRuntimeClientǁstartup_scan__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstartup_scan__mutmut['xǁRuntimeClientǁstartup_scan__mutmut_3'] = RuntimeClient.xǁRuntimeClientǁstartup_scan__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstartup_scan__mutmut['xǁRuntimeClientǁstartup_scan__mutmut_4'] = RuntimeClient.xǁRuntimeClientǁstartup_scan__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstartup_scan__mutmut['xǁRuntimeClientǁstartup_scan__mutmut_5'] = RuntimeClient.xǁRuntimeClientǁstartup_scan__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstartup_scan__mutmut['xǁRuntimeClientǁstartup_scan__mutmut_6'] = RuntimeClient.xǁRuntimeClientǁstartup_scan__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstartup_scan__mutmut['xǁRuntimeClientǁstartup_scan__mutmut_7'] = RuntimeClient.xǁRuntimeClientǁstartup_scan__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstartup_scan__mutmut['xǁRuntimeClientǁstartup_scan__mutmut_8'] = RuntimeClient.xǁRuntimeClientǁstartup_scan__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstartup_scan__mutmut['xǁRuntimeClientǁstartup_scan__mutmut_9'] = RuntimeClient.xǁRuntimeClientǁstartup_scan__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstartup_scan__mutmut['xǁRuntimeClientǁstartup_scan__mutmut_10'] = RuntimeClient.xǁRuntimeClientǁstartup_scan__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstartup_scan__mutmut['xǁRuntimeClientǁstartup_scan__mutmut_11'] = RuntimeClient.xǁRuntimeClientǁstartup_scan__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstartup_scan__mutmut['xǁRuntimeClientǁstartup_scan__mutmut_12'] = RuntimeClient.xǁRuntimeClientǁstartup_scan__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRuntimeClientǁstartup_scan__mutmut['xǁRuntimeClientǁstartup_scan__mutmut_13'] = RuntimeClient.xǁRuntimeClientǁstartup_scan__mutmut_13 # type: ignore # mutmut generated
