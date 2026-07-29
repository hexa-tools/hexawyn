from __future__ import annotations

import datetime

from hexawyn.application.ports.driven.cluster_certificate_health_port import IngressRef
from hexawyn.domain.services.certificate.cert_parser import (
    build_ingress_map,
    is_wildcard,
    parse_pem_to_cert_info,
)

_RSA_2048_CERT_PEM = """-----BEGIN CERTIFICATE-----
MIICzTCCAbWgAwIBAgIUUxkHU6zz43tUK6BEp5fKMsbUUqEwDQYJKoZIhvcNAQEL
BQAwFjEUMBIGA1UEAwwLZXhhbXBsZS5jb20wHhcNMjYwNzI0MDAwMDAwWhcNMjcw
NzI0MDAwMDAwWjAWMRQwEgYDVQQDDAtleGFtcGxlLmNvbTCCASIwDQYJKoZIhvcN
AQEBBQADggEPADCCAQoCggEBAIwmzHR1925TZsMkigcAQYygQA8RkLUzIbgld8IH
MG0C01wVfjRImENV+EphhmXHO8fRKV2URG+M9i09dHzs2/76a8wRMwpcUbICKZFR
sZApJJROd+EXRNQ4c+AD0pc+enBftHUOzmqESv4PlgmQlZFhx5Cbx8Ypz8xjwqnP
2TQLlvb7ptjHzoJG9rd79z8YgPj4bSgQPYUyOyCcvvhD5MLbDhMfhkTdsoIJHYz+
SAGAl9LLoYPlk1DyQWS9dFCXp+9ibEhm7Gs1EMPs68VdpGW/YgFYE2Wnx6mfyoux
xomtpqKaIeazz+yFY9kmndDBS3XrO5/TkO5iJmDoqTMR5IcCAwEAAaMTMBEwDwYD
VR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEAcfyHCfjVh3p/tb5HbNEA
gbaYf6vBmyDlpSZqfq0GdlOZbsqOQ1GGD2L+WfwCx5H6P0j7bxjTXCicNAKQANRv
0GpxMY417YexwuQaliO8IpiZteL8z9RgCFlDx5xX48rrPCG8ztMI7tQIaIrsFJLS
5bwelwYZjoTcHw8cJ4YjaFcWKZla5wQMk0UBAUvfBKqNLU2+TOnkl6MQpcwk8JN5
ngBUnyTrIz4jmbDOkG0usOmRY3lGmcQL7OJRe+M2fwBu/PGBjdl1mfSnKWVUdqlG
Dg+dSqtqRUcXMpKEXZMmlL0cDaVrFPL5WYPITgM9CLFc3eMNdg9A15/cEaIU5r6B
jA==
-----END CERTIFICATE-----"""

_EXPIRED_CERT_PEM = """-----BEGIN CERTIFICATE-----
MIICzTCCAbWgAwIBAgIUYgF4CSJfRfrwZNNngSy0WAX0ZqgwDQYJKoZIhvcNAQEL
BQAwFjEUMBIGA1UEAwwLZXhhbXBsZS5jb20wHhcNMjAwNzI0MDAwMDAwWhcNMjEw
NzI0MDAwMDAwWjAWMRQwEgYDVQQDDAtleGFtcGxlLmNvbTCCASIwDQYJKoZIhvcN
AQEBBQADggEPADCCAQoCggEBAIwmzHR1925TZsMkigcAQYygQA8RkLUzIbgld8IH
MG0C01wVfjRImENV+EphhmXHO8fRKV2URG+M9i09dHzs2/76a8wRMwpcUbICKZFR
sZApJJROd+EXRNQ4c+AD0pc+enBftHUOzmqESv4PlgmQlZFhx5Cbx8Ypz8xjwqnP
2TQLlvb7ptjHzoJG9rd79z8YgPj4bSgQPYUyOyCcvvhD5MLbDhMfhkTdsoIJHYz+
SAGAl9LLoYPlk1DyQWS9dFCXp+9ibEhm7Gs1EMPs68VdpGW/YgFYE2Wnx6mfyoux
xomtpqKaIeazz+yFY9kmndDBS3XrO5/TkO5iJmDoqTMR5IcCAwEAAaMTMBEwDwYD
VR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEAcfyHCfjVh3p/tb5HbNEA
gbaYf6vBmyDlpSZqfq0GdlOZbsqOQ1GGD2L+WfwCx5H6P0j7bxjTXCicNAKQANRv
0GpxMY417YexwuQaliO8IpiZteL8z9RgCFlDx5xX48rrPCG8ztMI7tQIaIrsFJLS
5bwelwYZjoTcHw8cJ4YjaFcWKZla5wQMk0UBAUvfBKqNLU2+TOnkl6MQpcwk8JN5
ngBUnyTrIz4jmbDOkG0usOmRY3lGmcQL7OJRe+M2fwBu/PGBjdl1mfSnKWVUdqlG
Dg+dSqtqRUcXMpKEXZMmlL0cDaVrFPL5WYPITgM9CLFc3eMNdg9A15/cEaIU5r6B
jA==
-----END CERTIFICATE-----"""


class TestBuildIngressMap:
    def test_single_ingress_per_secret(self) -> None:
        ingresses: list[IngressRef] = [
            IngressRef(
                ingress_name="app-ingress",
                namespace="default",
                secret_name="app-tls",
                host="app.example.com",
            ),
        ]
        result = build_ingress_map(ingresses)
        assert result == {"app-tls": ["app-ingress"]}

    def test_multiple_ingresses_same_secret(self) -> None:
        ingresses: list[IngressRef] = [
            IngressRef(
                ingress_name="app-ingress",
                namespace="default",
                secret_name="app-tls",
                host="app.example.com",
            ),
            IngressRef(
                ingress_name="api-ingress",
                namespace="default",
                secret_name="app-tls",
                host="api.example.com",
            ),
        ]
        result = build_ingress_map(ingresses)
        assert result == {"app-tls": ["app-ingress", "api-ingress"]}

    def test_multiple_secrets(self) -> None:
        ingresses: list[IngressRef] = [
            IngressRef(
                ingress_name="app-ingress",
                namespace="default",
                secret_name="app-tls",
                host="app.example.com",
            ),
            IngressRef(
                ingress_name="db-ingress",
                namespace="default",
                secret_name="db-tls",
                host="db.example.com",
            ),
        ]
        result = build_ingress_map(ingresses)
        assert result == {"app-tls": ["app-ingress"], "db-tls": ["db-ingress"]}

    def test_empty_ingresses(self) -> None:
        result = build_ingress_map([])
        assert result == {}

    def test_three_ingresses_same_secret(self) -> None:
        ingresses: list[IngressRef] = [
            IngressRef(ingress_name="a", namespace="ns", secret_name="sec", host="a.example.com"),
            IngressRef(ingress_name="b", namespace="ns", secret_name="sec", host="b.example.com"),
            IngressRef(ingress_name="c", namespace="ns", secret_name="sec", host="c.example.com"),
        ]
        result = build_ingress_map(ingresses)
        assert len(result["sec"]) == 3  # noqa: PLR2004

    def test_return_type_is_dict_of_lists(self) -> None:
        result = build_ingress_map([])
        assert isinstance(result, dict)


class TestIsWildcard:
    def test_subject_cn_starts_with_wildcard(self) -> None:
        assert is_wildcard("*.example.com", []) is True

    def test_san_contains_wildcard(self) -> None:
        assert is_wildcard("example.com", ["*.example.com", "example.com"]) is True

    def test_no_wildcard_at_all(self) -> None:
        assert is_wildcard("example.com", ["www.example.com", "api.example.com"]) is False

    def test_empty_san_list(self) -> None:
        assert is_wildcard("*.example.com", []) is True
        assert is_wildcard("example.com", []) is False

    def test_subject_cn_has_wildcard_asterisk_in_middle_but_not_prefix(self) -> None:
        assert is_wildcard("test*.example.com", []) is False

    def test_wildcard_only_in_san_not_in_cn(self) -> None:
        assert is_wildcard("example.com", ["*.example.com"]) is True

    def test_asterisk_in_san_not_prefix(self) -> None:
        assert is_wildcard("example.com", ["test.*.example.com"]) is False

    def test_both_cn_and_san_have_wildcards(self) -> None:
        assert is_wildcard("*.example.com", ["*.other.com"]) is True

    def test_empty_string_subject_cn(self) -> None:
        assert is_wildcard("", []) is False
        assert is_wildcard("", ["*.example.com"]) is True


class TestParsePemToCertInfo:
    def test_parses_valid_pem_certificate(self) -> None:
        info = parse_pem_to_cert_info(_RSA_2048_CERT_PEM)
        assert info.subject_cn != ""
        assert info.issuer_cn != ""
        assert info.days_remaining > 0
        assert info.key_size == 2048  # noqa: PLR2004
        assert info.is_ca is True
        assert info.serial_number != ""

    def test_days_remaining_positive_for_future_cert(self) -> None:
        info = parse_pem_to_cert_info(_RSA_2048_CERT_PEM)
        assert info.days_remaining > 0

    def test_not_after_is_datetime(self) -> None:
        info = parse_pem_to_cert_info(_RSA_2048_CERT_PEM)
        assert isinstance(info.not_after, datetime.datetime)

    def test_not_before_is_datetime(self) -> None:
        info = parse_pem_to_cert_info(_RSA_2048_CERT_PEM)
        assert isinstance(info.not_before, datetime.datetime)

    def test_signature_algorithm_is_string(self) -> None:
        info = parse_pem_to_cert_info(_RSA_2048_CERT_PEM)
        assert isinstance(info.signature_algorithm, str)
        assert len(info.signature_algorithm) > 0

    def test_subject_full_contains_cn(self) -> None:
        info = parse_pem_to_cert_info(_RSA_2048_CERT_PEM)
        assert info.subject_cn in info.subject_full

    def test_return_type_has_all_fields(self) -> None:
        info = parse_pem_to_cert_info(_RSA_2048_CERT_PEM)
        assert hasattr(info, "subject_cn")
        assert hasattr(info, "issuer_cn")
        assert hasattr(info, "not_before")
        assert hasattr(info, "not_after")
        assert hasattr(info, "days_remaining")
        assert hasattr(info, "san_list")
        assert hasattr(info, "is_ca")
        assert hasattr(info, "key_size")
        assert hasattr(info, "serial_number")
        assert hasattr(info, "signature_algorithm")
        assert hasattr(info, "subject_full")
        assert hasattr(info, "issuer_full")

    def test_san_list_is_empty_for_cert_without_san(self) -> None:
        info = parse_pem_to_cert_info(_RSA_2048_CERT_PEM)
        assert isinstance(info.san_list, list)

    def test_returns_certificate_info_with_non_empty_strings(self) -> None:
        info = parse_pem_to_cert_info(_RSA_2048_CERT_PEM)
        assert isinstance(info.subject_cn, str)
        assert isinstance(info.issuer_cn, str)
        assert isinstance(info.serial_number, str)

    def test_key_size_is_positive_int(self) -> None:
        info = parse_pem_to_cert_info(_RSA_2048_CERT_PEM)
        assert isinstance(info.key_size, int)
        assert info.key_size > 0

    def test_expired_cert_has_negative_days(self) -> None:
        info = parse_pem_to_cert_info(_EXPIRED_CERT_PEM)
        assert info.days_remaining < 0

    def test_bytes_pem_also_works(self) -> None:
        pem_bytes = _RSA_2048_CERT_PEM.encode("utf-8")
        info = parse_pem_to_cert_info(pem_bytes)  # type: ignore[arg-type]
        assert info.key_size == 2048  # noqa: PLR2004
