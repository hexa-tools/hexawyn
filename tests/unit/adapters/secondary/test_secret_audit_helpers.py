from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
    _extract_secret_names,
    _to_managed_fields_entry,
    _to_secret_raw,
    _translate_error,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _mk(**attrs: object) -> Mock:
    m = Mock()
    for k, v in attrs.items():
        setattr(m, k, v)
    return m


class TestToSecretRaw:
    def test_converts_secret(self) -> None:
        item = _mk(
            metadata=_mk(
                name="my-secret",
                namespace="default",
                managed_fields=[],
                creation_timestamp=_mk(isoformat=lambda: "2024-01-01T00:00:00Z"),
                annotations={},
            ),
            type="Opaque",
            data={"username": "dXNlcg==", "password": "cGFzcw=="},
        )
        result = _to_secret_raw(item)
        assert result["name"] == "my-secret"
        assert result["namespace"] == "default"
        assert result["secret_type"] == "Opaque"
        assert result["data_keys"] == ["password", "username"]

    def test_none_data_handled(self) -> None:
        item = _mk(
            metadata=_mk(
                name="s",
                namespace="n",
                managed_fields=[],
                creation_timestamp=_mk(isoformat=lambda: "2024-01-01T00:00:00Z"),
                annotations={},
            ),
            type="Opaque",
            data=None,
        )
        result = _to_secret_raw(item)
        assert result["data_keys"] == []


class TestToManagedFieldsEntrySecret:
    def test_converts_entry(self) -> None:
        entry = _mk(
            manager="kubectl",
            operation="Update",
            time=_mk(isoformat=lambda: "2024-01-01T00:00:00Z"),
            fields_v1={"key": "value"},
        )
        result = _to_managed_fields_entry(entry)
        assert result["manager"] == "kubectl"
        assert result["operation"] == "Update"
        assert result["fields_v1_raw"] == {"key": "value"}

    def test_fields_v1_not_dict(self) -> None:
        entry = _mk(
            manager="kubectl",
            operation="Update",
            time=_mk(isoformat=lambda: "2024-01-01T00:00:00Z"),
            fields_v1="bad",
        )
        result = _to_managed_fields_entry(entry)
        assert result["fields_v1_raw"] == {}


class TestExtractSecretNames:
    def test_env_from_secret_ref(self) -> None:
        pod_spec = _mk(
            containers=[
                _mk(
                    env_from=[_mk(secret_ref=_mk(name="secret-a"))],
                    env=[],
                )
            ],
            init_containers=[],
            volumes=[],
        )
        result = _extract_secret_names(pod_spec)
        assert result == {"secret-a"}

    def test_env_secret_key_ref(self) -> None:
        pod_spec = _mk(
            containers=[
                _mk(
                    env_from=[],
                    env=[
                        _mk(
                            value_from=_mk(secret_key_ref=_mk(name="secret-b")),
                        )
                    ],
                )
            ],
            init_containers=[],
            volumes=[],
        )
        result = _extract_secret_names(pod_spec)
        assert result == {"secret-b"}

    def test_volume_secret(self) -> None:
        pod_spec = _mk(
            containers=[],
            init_containers=[],
            volumes=[_mk(secret=_mk(secret_name="vol-secret"), projected=None)],
        )
        result = _extract_secret_names(pod_spec)
        assert result == {"vol-secret"}

    def test_projected_volume_secret(self) -> None:
        pod_spec = _mk(
            containers=[],
            init_containers=[],
            volumes=[
                _mk(
                    secret=None,
                    projected=_mk(sources=[_mk(secret=_mk(name="proj-secret"))]),
                )
            ],
        )
        result = _extract_secret_names(pod_spec)
        assert result == {"proj-secret"}

    def test_empty_pod_spec(self) -> None:
        pod_spec = _mk(containers=[], init_containers=[], volumes=[])
        result = _extract_secret_names(pod_spec)
        assert result == set()

    def test_none_containers(self) -> None:
        pod_spec = _mk(containers=None, init_containers=None, volumes=[])
        result = _extract_secret_names(pod_spec)
        assert result == set()

    def test_env_from_without_secret_ref(self) -> None:
        pod_spec = _mk(
            containers=[_mk(env_from=[_mk(secret_ref=None)], env=[])],
            init_containers=[],
            volumes=[],
        )
        result = _extract_secret_names(pod_spec)
        assert result == set()

    def test_env_without_value_from(self) -> None:
        pod_spec = _mk(
            containers=[_mk(env=[_mk(value_from=None)], env_from=[])],
            init_containers=[],
            volumes=[],
        )
        result = _extract_secret_names(pod_spec)
        assert result == set()


class TestSecretTranslateError:
    def test_forbidden(self) -> None:
        assert isinstance(_translate_error(_mk(status=403)), InsufficientPermissionsError)

    def test_other(self) -> None:
        assert isinstance(_translate_error(Exception("err")), ClusterUnreachableError)
