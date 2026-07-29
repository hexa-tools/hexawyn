"""Additional tests for CertManagerAdapter uncovered methods."""

from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.cert_manager_adapter import CertManagerAdapter
from hexawyn.domain.models.certificates import IssuerType


def _mock_vanilla_with_items(*item_lists: list[dict]) -> Mock:
    """Create a VanillaAdapter mock that returns successive CRD item lists."""
    mock_vanilla = Mock()
    mock_crd = Mock()
    items_iter = iter(item_lists)

    def _list_response(*args: object, **kwargs: object) -> dict[str, list[dict]]:
        try:
            return {"items": next(items_iter)}
        except StopIteration:
            return {"items": []}

    def _get_response(*args: object, **kwargs: object) -> dict:
        try:
            return next(items_iter)[0]
        except StopIteration:
            return {}

    mock_crd.list_namespaced_custom_object.side_effect = _list_response
    mock_crd.list_cluster_custom_object.side_effect = _list_response
    mock_crd.get_namespaced_custom_object.side_effect = _get_response
    mock_crd.get_cluster_custom_object.side_effect = _get_response

    mock_vanilla._crd_api_client.return_value = mock_crd
    return mock_vanilla


_CERT_ITEM = {
    "metadata": {"name": "my-tls", "namespace": "default"},
    "spec": {
        "dnsNames": ["app.example.com"],
        "issuerRef": {"name": "letsencrypt-prod"},
        "renewBefore": "720h",
    },
    "status": {
        "conditions": [
            {"type": "Ready", "status": "True", "reason": "Ready", "message": "OK"},
        ],
        "notAfter": "2027-01-01T00:00:00Z",
    },
}

_ISSUER_ITEM = {
    "metadata": {"name": "letsencrypt-prod"},
    "spec": {
        "acme": {"server": "https://acme.example.com/directory"},
    },
    "status": {
        "conditions": [
            {"type": "Ready", "status": "True", "reason": "OK", "message": "OK"},
        ],
    },
}

_CHALLENGE_ITEM = {
    "metadata": {"name": "challenge-abc", "namespace": "default"},
    "spec": {"type": "dns-01", "dnsName": "app.example.com"},
    "status": {"state": "pending", "reason": "waiting"},
}


class TestListCertificatesMissingBranches:
    def test_list_certificates_with_namespace(self) -> None:
        mock = _mock_vanilla_with_items([_CERT_ITEM])
        adapter = CertManagerAdapter(mock)
        certs = adapter.list_certificates(namespace="default")
        assert len(certs) == 1
        assert certs[0].name == "my-tls"

    def test_list_certificates_api_exception(self) -> None:
        mock_vanilla = Mock()
        mock_crd = Mock()
        mock_crd.list_cluster_custom_object.side_effect = Exception("api error")
        mock_vanilla._crd_api_client.return_value = mock_crd
        adapter = CertManagerAdapter(mock_vanilla)
        certs = adapter.list_certificates()
        assert certs == []


class TestListIssuersMissingBranches:
    def test_list_issuers_cluster_issuers_error(self) -> None:
        mock_vanilla = Mock()
        mock_crd = Mock()

        call_count = 0

        def _cluster_side_effect(*args: object, **kwargs: object) -> dict:
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                raise Exception("cluster issuers error")
            return {"items": [_ISSUER_ITEM]}

        mock_crd.list_cluster_custom_object.side_effect = _cluster_side_effect
        mock_vanilla._crd_api_client.return_value = mock_crd
        adapter = CertManagerAdapter(mock_vanilla)
        issuers = adapter.list_issuers()
        assert len(issuers) == 1
        assert issuers[0].kind == "Issuer"

    def test_list_issuers_namespaced_error(self) -> None:
        mock_vanilla = Mock()
        mock_crd = Mock()

        call_count = 0

        def _cluster_side_effect(*args: object, **kwargs: object) -> dict:
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return {"items": [_ISSUER_ITEM]}
            raise Exception("issuers error")

        mock_crd.list_cluster_custom_object.side_effect = _cluster_side_effect
        mock_vanilla._crd_api_client.return_value = mock_crd
        adapter = CertManagerAdapter(mock_vanilla)
        issuers = adapter.list_issuers()
        assert len(issuers) == 1
        assert issuers[0].kind == "ClusterIssuer"

    def test_list_issuers_with_namespace(self) -> None:
        mock_vanilla = Mock()
        mock_crd = Mock()

        call_count = 0

        def _cluster_side_effect(*args: object, **kwargs: object) -> dict:
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return {"items": []}
            return {"items": [_ISSUER_ITEM]}

        mock_crd.list_cluster_custom_object.side_effect = _cluster_side_effect
        mock_crd.list_namespaced_custom_object.return_value = {"items": [_ISSUER_ITEM]}
        mock_vanilla._crd_api_client.return_value = mock_crd
        adapter = CertManagerAdapter(mock_vanilla)
        issuers = adapter.list_issuers(namespace="default")
        assert len(issuers) == 1


class TestGetIssuer:
    def test_get_cluster_issuer(self) -> None:
        mock = _mock_vanilla_with_items([_ISSUER_ITEM])
        adapter = CertManagerAdapter(mock)
        issuer = adapter.get_issuer("letsencrypt-prod")
        assert issuer.name == "letsencrypt-prod"
        assert issuer.kind == "ClusterIssuer"

    def test_get_namespaced_issuer_fallback(self) -> None:
        mock_vanilla = Mock()
        mock_crd = Mock()
        mock_crd.get_cluster_custom_object.side_effect = Exception("not found")
        mock_crd.get_namespaced_custom_object.return_value = _ISSUER_ITEM
        mock_vanilla._crd_api_client.return_value = mock_crd
        adapter = CertManagerAdapter(mock_vanilla)
        issuer = adapter.get_issuer("letsencrypt-prod", namespace="default")
        assert issuer.kind == "Issuer"


class TestListChallenges:
    def test_list_challenges(self) -> None:
        mock = _mock_vanilla_with_items([_CHALLENGE_ITEM])
        adapter = CertManagerAdapter(mock)
        challenges = adapter.list_challenges()
        assert len(challenges) == 1
        assert challenges[0].name == "challenge-abc"
        assert challenges[0].type == "dns-01"

    def test_list_challenges_with_namespace_filter(self) -> None:
        challenge_wrong_ns = {
            "metadata": {"name": "ch-other", "namespace": "other-ns"},
            "spec": {"type": "http-01", "dnsName": "other.example.com"},
            "status": {"state": "valid"},
        }
        mock = _mock_vanilla_with_items([_CHALLENGE_ITEM, challenge_wrong_ns])
        adapter = CertManagerAdapter(mock)
        challenges = adapter.list_challenges(namespace="default")
        assert len(challenges) == 1

    def test_list_challenges_exception(self) -> None:
        mock_vanilla = Mock()
        mock_crd = Mock()
        mock_crd.list_cluster_custom_object.side_effect = Exception("api error")
        mock_vanilla._crd_api_client.return_value = mock_crd
        adapter = CertManagerAdapter(mock_vanilla)
        assert adapter.list_challenges() == []


class TestListRequests:
    def test_list_requests(self) -> None:
        mock = _mock_vanilla_with_items([_CERT_ITEM])
        adapter = CertManagerAdapter(mock)
        certs = adapter.list_requests()
        assert len(certs) == 1

    def test_list_requests_with_namespace(self) -> None:
        mock = _mock_vanilla_with_items([_CERT_ITEM])
        adapter = CertManagerAdapter(mock)
        certs = adapter.list_requests(namespace="default")
        assert len(certs) == 1

    def test_list_requests_exception(self) -> None:
        mock_vanilla = Mock()
        mock_crd = Mock()
        mock_crd.list_cluster_custom_object.side_effect = Exception("api error")
        mock_vanilla._crd_api_client.return_value = mock_crd
        adapter = CertManagerAdapter(mock_vanilla)
        assert adapter.list_requests() == []


class TestParseIssuerType:
    def test_lets_encrypt(self) -> None:
        assert CertManagerAdapter._parse_issuer_type("letsencrypt-prod") == IssuerType.LETS_ENCRYPT

    def test_lets_encrypt_hyphen(self) -> None:
        result = CertManagerAdapter._parse_issuer_type("lets-encrypt-staging")
        assert result == IssuerType.LETS_ENCRYPT

    def test_acme(self) -> None:
        assert CertManagerAdapter._parse_issuer_type("acme-issuer") == IssuerType.LETS_ENCRYPT

    def test_vault(self) -> None:
        assert CertManagerAdapter._parse_issuer_type("vault-issuer") == IssuerType.VAULT

    def test_self_signed(self) -> None:
        assert CertManagerAdapter._parse_issuer_type("selfsigned-issuer") == IssuerType.SELF_SIGNED

    def test_ca_exact(self) -> None:
        assert CertManagerAdapter._parse_issuer_type("ca") == IssuerType.CA

    def test_ca_suffix(self) -> None:
        assert CertManagerAdapter._parse_issuer_type("my-ca") == IssuerType.CA

    def test_venafi(self) -> None:
        assert CertManagerAdapter._parse_issuer_type("venafi-tpp") == IssuerType.VENAFI

    def test_unknown(self) -> None:
        assert CertManagerAdapter._parse_issuer_type("some-random") == IssuerType.UNKNOWN


class TestCertificateStatusParsing:
    def test_issuing_status(self) -> None:
        cert = {
            "metadata": {"name": "cert-issuing", "namespace": "default"},
            "spec": {"issuerRef": {"name": "ca"}},
            "status": {
                "conditions": [
                    {"type": "Ready", "status": "False", "reason": "Issuing", "message": ""},
                ],
            },
        }
        mock = _mock_vanilla_with_items([cert])
        adapter = CertManagerAdapter(mock)
        certs = adapter.list_certificates()
        assert certs[0].status.value == "issuing"

    def test_not_ready_status(self) -> None:
        cert = {
            "metadata": {"name": "cert-failed", "namespace": "default"},
            "spec": {"issuerRef": {"name": "ca"}},
            "status": {
                "conditions": [
                    {"type": "Ready", "status": "False", "reason": "Failed", "message": "error"},
                ],
            },
        }
        mock = _mock_vanilla_with_items([cert])
        adapter = CertManagerAdapter(mock)
        certs = adapter.list_certificates()
        assert certs[0].status.value == "not_ready"

    def test_expiry_days_parse_error(self) -> None:
        cert = {
            "metadata": {"name": "cert-bad-date", "namespace": "default"},
            "spec": {"issuerRef": {"name": "ca"}},
            "status": {
                "conditions": [
                    {"type": "Ready", "status": "True", "reason": "Ready", "message": ""},
                ],
                "notAfter": "not-a-valid-date",
            },
        }
        mock = _mock_vanilla_with_items([cert])
        adapter = CertManagerAdapter(mock)
        certs = adapter.list_certificates()
        assert certs[0].days_until_expiry is None


class TestStrList:
    def test_str_list_with_values(self) -> None:
        result = CertManagerAdapter._str_list([1, "two", 3.0])
        assert result == ["1", "two", "3.0"]

    def test_str_list_non_list(self) -> None:
        result = CertManagerAdapter._str_list("not-a-list")
        assert result == []


class TestParseIssuerEdgeCases:
    def test_issuer_without_conditions(self) -> None:
        issuer = {
            "metadata": {"name": "no-cond-issuer"},
            "spec": {"acme": {}},
            "status": {},
        }
        mock_vanilla = Mock()
        mock_crd = Mock()

        call_count = 0

        def _cluster_side_effect(*args: object, **kwargs: object) -> dict:
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return {"items": [issuer]}
            return {"items": []}

        mock_crd.list_cluster_custom_object.side_effect = _cluster_side_effect
        mock_vanilla._crd_api_client.return_value = mock_crd
        adapter = CertManagerAdapter(mock_vanilla)
        issuers = adapter.list_issuers()
        assert len(issuers) == 1
        assert issuers[0].ready is False
