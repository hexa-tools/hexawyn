from __future__ import annotations

import pytest
from hexawyn.adapters.secondary.cilium import hubble_client as hc


class _FakeResponse:
    def __init__(self, payload: object) -> None:
        self._payload = payload

    def raise_for_status(self) -> None:
        return None

    def json(self) -> object:
        return self._payload


class TestHubbleClient:
    def test_hubble_available_when_url_set(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(hc, "_HUBBLE_URL", "http://hubble:4245")
        assert hc.hubble_available() is True

    def test_hubble_available_false_when_no_url(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(hc, "_HUBBLE_URL", "")
        assert hc.hubble_available() is False

    def test_fetch_returns_flows(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(hc, "_HUBBLE_URL", "http://hubble:4245")
        monkeypatch.setattr(
            hc.httpx,
            "get",
            lambda *args, **kwargs: _FakeResponse({"flows": [{"verdict": "FORWARDED"}]}),
        )

        flows = hc.fetch_hubble_flows()

        assert len(flows) == 1  # noqa: PLR2004
        assert flows[0]["verdict"] == "FORWARDED"

    def test_fetch_returns_empty_on_non_dict(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(hc, "_HUBBLE_URL", "http://hubble:4245")
        monkeypatch.setattr(hc.httpx, "get", lambda *a, **k: _FakeResponse(["not-a-dict"]))

        assert hc.fetch_hubble_flows() == []

    def test_fetch_returns_empty_when_flows_not_list(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(hc, "_HUBBLE_URL", "http://hubble:4245")
        monkeypatch.setattr(hc.httpx, "get", lambda *a, **k: _FakeResponse({"flows": "nope"}))

        assert hc.fetch_hubble_flows() == []

    def test_fetch_passes_all_params(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(hc, "_HUBBLE_URL", "http://hubble:4245")
        captured: dict[str, object] = {}

        def fake_get(
            url: str, params: dict[str, str] | None = None, timeout: float | None = None
        ) -> _FakeResponse:
            captured["params"] = params
            return _FakeResponse({"flows": []})

        monkeypatch.setattr(hc.httpx, "get", fake_get)

        hc.fetch_hubble_flows(
            namespace="payments",
            pod="web-0",
            direction="ingress",
            verdict="FORWARDED",
            window_minutes=30,
            limit=5,
        )

        params = captured["params"]
        assert params is not None
        assert params["namespace"] == "payments"
        assert params["pod"] == "web-0"
        assert params["direction"] == "ingress"
        assert params["verdict"] == "FORWARDED"
        assert params["window_minutes"] == "30"
        assert params["limit"] == "5"

    def test_fetch_raises_on_transport_error(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(hc, "_HUBBLE_URL", "http://hubble:4245")

        def raise_error(*args: object, **kwargs: object) -> object:
            raise hc.httpx.ConnectError("boom")

        monkeypatch.setattr(hc.httpx, "get", raise_error)

        with pytest.raises(hc.httpx.ConnectError):
            hc.fetch_hubble_flows()
