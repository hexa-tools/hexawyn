"""Hubble Relay HTTP client — queries Cilium flow logs over HTTP."""

from __future__ import annotations

import os

import httpx

_HUBBLE_URL = os.environ.get("HUBBLE_URL", "")
_REQUEST_TIMEOUT = 10.0


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_hubble_available__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_hubble_available__mutmut)
def hubble_available() -> bool:
    """True when a Hubble Relay endpoint is configured."""
    return bool(_HUBBLE_URL)


def x_hubble_available__mutmut_orig() -> bool:
    """True when a Hubble Relay endpoint is configured."""
    return bool(_HUBBLE_URL)


def x_hubble_available__mutmut_1() -> bool:
    """True when a Hubble Relay endpoint is configured."""
    return bool(None)

mutants_x_hubble_available__mutmut['_mutmut_orig'] = x_hubble_available__mutmut_orig # type: ignore # mutmut generated
mutants_x_hubble_available__mutmut['x_hubble_available__mutmut_1'] = x_hubble_available__mutmut_1 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_fetch_hubble_flows__mutmut)
def fetch_hubble_flows(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_orig(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_1(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 16,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_2(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 101,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_3(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = None
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_4(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"XXwindow_minutesXX": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_5(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"WINDOW_MINUTES": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_6(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(None), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_7(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "XXlimitXX": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_8(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "LIMIT": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_9(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(None)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_10(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = None
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_11(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["XXnamespaceXX"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_12(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["NAMESPACE"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_13(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = None
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_14(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["XXpodXX"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_15(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["POD"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_16(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = None
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_17(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["XXdirectionXX"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_18(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["DIRECTION"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_19(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = None
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_20(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["XXverdictXX"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_21(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["VERDICT"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_22(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = None
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_23(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(None, params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_24(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=None, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_25(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=None)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_26(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_27(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_28(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, )
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_29(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = None
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_30(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if isinstance(data, dict):
        return []
    flows = data.get("flows")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_31(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = None
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_32(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get(None)
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_33(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("XXflowsXX")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_34(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("FLOWS")
    if not isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]


def x_fetch_hubble_flows__mutmut_35(  # noqa: PLR0913
    namespace: str | None = None,
    pod: str | None = None,
    direction: str | None = None,
    verdict: str | None = None,
    window_minutes: int = 15,
    limit: int = 100,
) -> list[dict[str, object]]:
    """Fetch flow objects from Hubble Relay. Raises on transport errors."""
    params: dict[str, str] = {"window_minutes": str(window_minutes), "limit": str(limit)}
    if namespace:
        params["namespace"] = namespace
    if pod:
        params["pod"] = pod
    if direction:
        params["direction"] = direction
    if verdict:
        params["verdict"] = verdict
    response = httpx.get(f"{_HUBBLE_URL}/flows", params=params, timeout=_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        return []
    flows = data.get("flows")
    if isinstance(flows, list):
        return []
    return [flow for flow in flows if isinstance(flow, dict)]

mutants_x_fetch_hubble_flows__mutmut['_mutmut_orig'] = x_fetch_hubble_flows__mutmut_orig # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_1'] = x_fetch_hubble_flows__mutmut_1 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_2'] = x_fetch_hubble_flows__mutmut_2 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_3'] = x_fetch_hubble_flows__mutmut_3 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_4'] = x_fetch_hubble_flows__mutmut_4 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_5'] = x_fetch_hubble_flows__mutmut_5 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_6'] = x_fetch_hubble_flows__mutmut_6 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_7'] = x_fetch_hubble_flows__mutmut_7 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_8'] = x_fetch_hubble_flows__mutmut_8 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_9'] = x_fetch_hubble_flows__mutmut_9 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_10'] = x_fetch_hubble_flows__mutmut_10 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_11'] = x_fetch_hubble_flows__mutmut_11 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_12'] = x_fetch_hubble_flows__mutmut_12 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_13'] = x_fetch_hubble_flows__mutmut_13 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_14'] = x_fetch_hubble_flows__mutmut_14 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_15'] = x_fetch_hubble_flows__mutmut_15 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_16'] = x_fetch_hubble_flows__mutmut_16 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_17'] = x_fetch_hubble_flows__mutmut_17 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_18'] = x_fetch_hubble_flows__mutmut_18 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_19'] = x_fetch_hubble_flows__mutmut_19 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_20'] = x_fetch_hubble_flows__mutmut_20 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_21'] = x_fetch_hubble_flows__mutmut_21 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_22'] = x_fetch_hubble_flows__mutmut_22 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_23'] = x_fetch_hubble_flows__mutmut_23 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_24'] = x_fetch_hubble_flows__mutmut_24 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_25'] = x_fetch_hubble_flows__mutmut_25 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_26'] = x_fetch_hubble_flows__mutmut_26 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_27'] = x_fetch_hubble_flows__mutmut_27 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_28'] = x_fetch_hubble_flows__mutmut_28 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_29'] = x_fetch_hubble_flows__mutmut_29 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_30'] = x_fetch_hubble_flows__mutmut_30 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_31'] = x_fetch_hubble_flows__mutmut_31 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_32'] = x_fetch_hubble_flows__mutmut_32 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_33'] = x_fetch_hubble_flows__mutmut_33 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_34'] = x_fetch_hubble_flows__mutmut_34 # type: ignore # mutmut generated
mutants_x_fetch_hubble_flows__mutmut['x_fetch_hubble_flows__mutmut_35'] = x_fetch_hubble_flows__mutmut_35 # type: ignore # mutmut generated
