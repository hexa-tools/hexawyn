from __future__ import annotations

import pytest
from hexawyn.application.ports.driven.ingress_port import IngressInfo, IngressPort


class TestIngressPortContract:
    def test_port_is_abstract(self) -> None:
        with pytest.raises(TypeError):
            IngressPort()  # type: ignore[abstract]

    def test_ingress_info_requires_expected_keys(self) -> None:
        info: IngressInfo = {
            "name": "payments-api",
            "namespace": "production",
            "host": "api.payments.example.com",
            "target_service": "payment-api",
            "tls_enabled": True,
        }
        assert info["name"] == "payments-api"
        assert info["namespace"] == "production"
        assert info["host"] == "api.payments.example.com"
        assert info["target_service"] == "payment-api"
        assert info["tls_enabled"] is True

    def test_concrete_port_returns_ingress_info(self) -> None:
        class FakeIngressPort(IngressPort):
            def list_ingresses(self, namespace: str) -> list[IngressInfo]:
                return [
                    {
                        "name": "frontend",
                        "namespace": namespace,
                        "host": "staging.example.com",
                        "target_service": "frontend",
                        "tls_enabled": False,
                    }
                ]

        port = FakeIngressPort()
        result = port.list_ingresses(namespace="staging")
        assert len(result) == 1  # noqa: PLR2004
        assert result[0]["name"] == "frontend"
        assert result[0]["tls_enabled"] is False
