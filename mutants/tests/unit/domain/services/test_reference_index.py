from __future__ import annotations

from hexawyn.application.ports.driven.secret_rotation_audit_port import SecretRaw


def _make_secret(
    namespace: str = "default",
    annotations: dict[str, str] | None = None,
    secret_type: str = "Opaque",
) -> SecretRaw:
    return {
        "name": "test-secret",
        "namespace": namespace,
        "secret_type": secret_type,
        "data_keys": ["key1"],
        "managed_fields": [],
        "creation_timestamp": "2026-01-01T00:00:00Z",
        "annotations": annotations or {},
    }


class TestExclusionReason:
    def test_namespace_exempt_from_policy(self) -> None:
        from hexawyn.domain.services.secret_rotation.reference_index import exclusion_reason

        secret = _make_secret(namespace="kube-system")
        exempt = {"kube-system", "kube-public"}

        result = exclusion_reason(secret, exempt)

        assert result == "namespace exempt from rotation policy"

    def test_externally_managed_by_external_secrets(self) -> None:
        from hexawyn.domain.services.secret_rotation.reference_index import exclusion_reason

        secret = _make_secret(
            namespace="production",
            annotations={"externalsecrets.io/secret-store": "aws-secrets-manager"},
        )

        result = exclusion_reason(secret, set())

        assert result == "externally managed (External Secrets Operator)"

    def test_auto_rotated_by_cert_manager(self) -> None:
        from hexawyn.domain.services.secret_rotation.reference_index import exclusion_reason

        secret = _make_secret(
            namespace="default",
            secret_type="kubernetes.io/tls",
            annotations={"cert-manager.io/certificate-name": "my-cert"},
        )

        result = exclusion_reason(secret, set())

        assert result == "auto-rotated (cert-manager)"

    def test_no_exclusion_reason_for_normal_secret(self) -> None:
        from hexawyn.domain.services.secret_rotation.reference_index import exclusion_reason

        secret = _make_secret()

        result = exclusion_reason(secret, set())

        assert result is None

    def test_non_tls_secret_with_cert_manager_annotation_not_excluded(self) -> None:
        from hexawyn.domain.services.secret_rotation.reference_index import exclusion_reason

        secret = _make_secret(
            namespace="default",
            secret_type="Opaque",
            annotations={"cert-manager.io/certificate-name": "my-cert"},
        )

        result = exclusion_reason(secret, set())

        assert result is None

    def test_exempt_namespace_checked_first(self) -> None:
        from hexawyn.domain.services.secret_rotation.reference_index import exclusion_reason

        secret = _make_secret(
            namespace="kube-system",
            annotations={"externalsecrets.io/secret-store": "vault"},
        )
        exempt = {"kube-system"}

        result = exclusion_reason(secret, exempt)

        assert result == "namespace exempt from rotation policy"

    def test_empty_exempt_namespaces_does_not_exclude(self) -> None:
        from hexawyn.domain.services.secret_rotation.reference_index import exclusion_reason

        secret = _make_secret(namespace="default")

        result = exclusion_reason(secret, set())

        assert result is None

    def test_cert_manager_requires_tls_type(self) -> None:
        from hexawyn.domain.services.secret_rotation.reference_index import exclusion_reason

        secret = _make_secret(
            namespace="default",
            secret_type="Opaque",
            annotations={"cert-manager.io/certificate-name": "my-cert"},
        )

        result = exclusion_reason(secret, set())

        assert result is None


class TestIndexReferences:
    def test_happy_path_indexes_workloads_by_secret(self) -> None:
        from hexawyn.domain.services.secret_rotation.reference_index import index_references

        refs: list[dict[str, str]] = [
            {"namespace": "default", "secret_name": "db-creds", "workload_name": "api-server"},
            {"namespace": "default", "secret_name": "db-creds", "workload_name": "worker"},
            {"namespace": "production", "secret_name": "api-token", "workload_name": "gateway"},
        ]

        result = index_references(refs)

        assert result[("default", "db-creds")] == ["api-server", "worker"]
        assert result[("production", "api-token")] == ["gateway"]

    def test_empty_references_returns_empty_dict(self) -> None:
        from hexawyn.domain.services.secret_rotation.reference_index import index_references

        result = index_references([])

        assert result == {}

    def test_single_reference_returns_single_entry(self) -> None:
        from hexawyn.domain.services.secret_rotation.reference_index import index_references

        refs: list[dict[str, str]] = [
            {"namespace": "ns", "secret_name": "secret-1", "workload_name": "deploy-1"},
        ]

        result = index_references(refs)

        assert len(result) == 1
        assert result[("ns", "secret-1")] == ["deploy-1"]

    def test_return_type_is_dict_of_list(self) -> None:
        from hexawyn.domain.services.secret_rotation.reference_index import index_references

        result = index_references([])

        assert isinstance(result, dict)
