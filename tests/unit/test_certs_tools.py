from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.domain.models.certificates import (
    AcmeChallenge,
    Certificate,
    CertificateIssuer,
    CertificateStatus,
    CertManagerDetectionResult,
    IssuerType,
)


class TestCertsDetect:
    def test_tool_returns_detection(self) -> None:
        from hexawyn.mcp.tools.certs_detect import certs_detect

        with patch("hexawyn.mcp.server.build_cert_manager_adapter") as mock_build:
            adapter = MagicMock(spec=CertManagerPort)
            adapter.detect.return_value = CertManagerDetectionResult(
                installed=True,
                version="v1.16.2",
                namespace="cert-manager",
                total_certs=15,
                ready_certs=12,
                expiring_soon=3,
                failed_certs=1,
                active_challenges=2,
            )
            mock_build.return_value = adapter
            result = certs_detect()
        assert result["error"] is None
        assert result["installed"] is True
        assert result["expiring_soon"] == 3

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.certs_detect import certs_detect

        with patch(
            "hexawyn.mcp.server.build_cert_manager_adapter", side_effect=RuntimeError("boom")
        ):
            result = certs_detect()
        assert result["error"] == "boom"


class TestCertsList:
    def test_tool_returns_certs(self) -> None:
        from hexawyn.mcp.tools.certs_list import certs_list

        with patch("hexawyn.mcp.server.build_cert_manager_adapter") as mock_build:
            adapter = MagicMock(spec=CertManagerPort)
            adapter.list_certificates.return_value = [
                Certificate(
                    name="payments-tls",
                    namespace="production",
                    status=CertificateStatus.READY,
                    issuer_name="letsencrypt-prod",
                    issuer_type=IssuerType.LETS_ENCRYPT,
                    dns_names=["payments.example.com"],
                    not_before="2026-06-01T00:00:00Z",
                    not_after="2026-09-01T00:00:00Z",
                    days_until_expiry=60,
                    renewal_time=None,
                    auto_renew=True,
                    message=None,
                ),
            ]
            mock_build.return_value = adapter
            result = certs_list()
        assert result["error"] is None
        assert len(result["certificates"]) == 1

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.certs_list import certs_list

        with patch(
            "hexawyn.mcp.server.build_cert_manager_adapter", side_effect=RuntimeError("boom")
        ):
            result = certs_list()
        assert result["error"] == "boom"


class TestCertsGet:
    def test_tool_returns_detail(self) -> None:
        from hexawyn.mcp.tools.certs_get import certs_get

        with patch("hexawyn.mcp.server.build_cert_manager_adapter") as mock_build:
            adapter = MagicMock(spec=CertManagerPort)
            adapter.get_certificate.return_value = Certificate(
                name="payments-tls",
                namespace="production",
                status=CertificateStatus.NOT_READY,
                issuer_name="letsencrypt-prod",
                issuer_type=IssuerType.LETS_ENCRYPT,
                dns_names=["payments.example.com"],
                not_before=None,
                not_after=None,
                days_until_expiry=None,
                renewal_time=None,
                auto_renew=False,
                message="Certificate expired: ACME challenge failed — DNS propagation timeout",
            )
            mock_build.return_value = adapter
            result = certs_get(name="payments-tls", namespace="production")
        assert result["error"] is None
        assert result["status"] == "not_ready"

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.certs_get import certs_get

        with patch(
            "hexawyn.mcp.server.build_cert_manager_adapter", side_effect=RuntimeError("boom")
        ):
            result = certs_get(name="x", namespace="ns")
        assert result["error"] == "boom"


class TestCertsStatusExplain:
    def test_tool_returns_explanation(self) -> None:
        from hexawyn.mcp.tools.certs_status_explain import certs_status_explain

        with patch("hexawyn.mcp.server.build_cert_manager_adapter") as mock_build:
            adapter = MagicMock(spec=CertManagerPort)
            adapter.get_certificate.return_value = Certificate(
                name="payments-tls",
                namespace="production",
                status=CertificateStatus.NOT_READY,
                issuer_name="le",
                issuer_type=IssuerType.LETS_ENCRYPT,
                dns_names=["payments.example.com"],
                not_before=None,
                not_after=None,
                days_until_expiry=None,
                renewal_time=None,
                auto_renew=False,
                message="ACME challenge failed: DNS propagation timeout",
            )
            mock_build.return_value = adapter
            result = certs_status_explain(name="payments-tls", namespace="production")
        assert result["error"] is None
        assert result["status"] == "not_ready"

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.certs_status_explain import certs_status_explain

        with patch(
            "hexawyn.mcp.server.build_cert_manager_adapter", side_effect=RuntimeError("boom")
        ):
            result = certs_status_explain(name="x", namespace="ns")
        assert result["error"] == "boom"


class TestCertsIssuersList:
    def test_tool_returns_issuers(self) -> None:
        from hexawyn.mcp.tools.certs_issuers_list import certs_issuers_list

        with patch("hexawyn.mcp.server.build_cert_manager_adapter") as mock_build:
            adapter = MagicMock(spec=CertManagerPort)
            adapter.list_issuers.return_value = [
                CertificateIssuer(
                    name="letsencrypt-prod",
                    namespace=None,
                    kind="ClusterIssuer",
                    issuer_type=IssuerType.LETS_ENCRYPT,
                    ready=True,
                    server="https://acme-v02.api.letsencrypt.org/directory",
                    message=None,
                ),
            ]
            mock_build.return_value = adapter
            result = certs_issuers_list()
        assert result["error"] is None
        assert len(result["issuers"]) == 1

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.certs_issuers_list import certs_issuers_list

        with patch(
            "hexawyn.mcp.server.build_cert_manager_adapter", side_effect=RuntimeError("boom")
        ):
            result = certs_issuers_list()
        assert result["error"] == "boom"


class TestCertsIssuerGet:
    def test_tool_returns_detail(self) -> None:
        from hexawyn.mcp.tools.certs_issuer_get import certs_issuer_get

        with patch("hexawyn.mcp.server.build_cert_manager_adapter") as mock_build:
            adapter = MagicMock(spec=CertManagerPort)
            adapter.get_issuer.return_value = CertificateIssuer(
                name="letsencrypt-staging",
                namespace=None,
                kind="ClusterIssuer",
                issuer_type=IssuerType.LETS_ENCRYPT,
                ready=True,
                server="https://acme-staging.api.letsencrypt.org/directory",
                message=None,
            )
            mock_build.return_value = adapter
            result = certs_issuer_get(name="letsencrypt-staging")
        assert result["error"] is None
        assert result["issuer_type"] == "lets_encrypt"

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.certs_issuer_get import certs_issuer_get

        with patch(
            "hexawyn.mcp.server.build_cert_manager_adapter", side_effect=RuntimeError("boom")
        ):
            result = certs_issuer_get(name="x")
        assert result["error"] == "boom"


class TestCertsChallengesList:
    def test_tool_returns_challenges(self) -> None:
        from hexawyn.mcp.tools.certs_challenges_list import certs_challenges_list

        with patch("hexawyn.mcp.server.build_cert_manager_adapter") as mock_build:
            adapter = MagicMock(spec=CertManagerPort)
            adapter.list_challenges.return_value = [
                AcmeChallenge(
                    name="payments-abc-123",
                    namespace="production",
                    type="dns-01",
                    domain="payments.example.com",
                    state="pending",
                    reason=None,
                    age_seconds=45,
                ),
            ]
            mock_build.return_value = adapter
            result = certs_challenges_list()
        assert result["error"] is None
        assert len(result["challenges"]) == 1

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.certs_challenges_list import certs_challenges_list

        with patch(
            "hexawyn.mcp.server.build_cert_manager_adapter", side_effect=RuntimeError("boom")
        ):
            result = certs_challenges_list()
        assert result["error"] == "boom"


class TestCertsRequestsList:
    def test_tool_returns_requests(self) -> None:
        from hexawyn.mcp.tools.certs_requests_list import certs_requests_list

        with patch("hexawyn.mcp.server.build_cert_manager_adapter") as mock_build:
            adapter = MagicMock(spec=CertManagerPort)
            adapter.list_requests.return_value = [
                Certificate(
                    name="payments-tls-req",
                    namespace="production",
                    status=CertificateStatus.ISSUING,
                    issuer_name="le",
                    issuer_type=IssuerType.LETS_ENCRYPT,
                    dns_names=["payments.example.com"],
                    not_before=None,
                    not_after=None,
                    days_until_expiry=None,
                    renewal_time=None,
                    auto_renew=True,
                    message=None,
                ),
            ]
            mock_build.return_value = adapter
            result = certs_requests_list()
        assert result["error"] is None
        assert len(result["requests"]) == 1

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.certs_requests_list import certs_requests_list

        with patch(
            "hexawyn.mcp.server.build_cert_manager_adapter", side_effect=RuntimeError("boom")
        ):
            result = certs_requests_list()
        assert result["error"] == "boom"


class TestBuildCertManagerAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
        from hexawyn.mcp.server import build_cert_manager_adapter

        adapter = build_cert_manager_adapter()
        assert isinstance(adapter, CertManagerPort)


class TestRegisterFunctions:
    def test_all_certs_tools_have_register(self) -> None:
        import importlib

        tools = [
            "certs_detect",
            "certs_list",
            "certs_get",
            "certs_status_explain",
            "certs_issuers_list",
            "certs_issuer_get",
            "certs_challenges_list",
            "certs_requests_list",
        ]
        from fastmcp import FastMCP

        test_mcp = FastMCP("test-certs")
        for tool_name in tools:
            mod = importlib.import_module(f"hexawyn.mcp.tools.{tool_name}")
            register_fn = getattr(mod, "register", None)
            assert callable(register_fn)
            register_fn(test_mcp)
