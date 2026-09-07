"""Hubble Relay HTTP client — queries Cilium flow logs over HTTP."""

from __future__ import annotations

import os

import httpx

_HUBBLE_URL = os.environ.get("HUBBLE_URL", "")
_REQUEST_TIMEOUT = 10.0


def hubble_available() -> bool:
    """True when a Hubble Relay endpoint is configured."""
    return bool(_HUBBLE_URL)


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
