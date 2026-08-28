from __future__ import annotations

from hexawyn.domain.services.cilium.identity_builder import (
    build_identities_result,
    not_installed_identities_result,
)


def _identity(
    raw_id: str,
    spec_labels: list[str] | None = None,
    meta_labels: dict[str, str] | None = None,
) -> dict:
    metadata = {"name": raw_id}
    if meta_labels:
        metadata["labels"] = meta_labels
    spec: dict[str, object] = {}
    if spec_labels:
        spec["labels"] = spec_labels
    return {"metadata": metadata, "spec": spec}


def _endpoint(raw_id: str) -> dict:
    return {"status": {"identity": {"id": raw_id}}}


class TestBuildIdentitiesResult:
    def test_lists_identities_with_endpoint_counts(self) -> None:
        identities = [
            _identity("100", spec_labels=["a", "b"]),
            _identity("200", spec_labels=["c"]),
        ]
        endpoints = [_endpoint("100"), _endpoint("100"), _endpoint("200")]

        result = build_identities_result(identities, endpoints)

        assert result.installed is True
        assert result.status == "present"
        assert result.total_identities == 2  # noqa: PLR2004
        assert result.identities[0].id == "100"
        assert result.identities[0].labels == ("a", "b")
        assert result.identities[0].endpoint_count == 2  # noqa: PLR2004
        assert result.identities[1].endpoint_count == 1  # noqa: PLR2004

    def test_falls_back_to_metadata_labels(self) -> None:
        identities = [_identity("100", meta_labels={"app": "db", "tier": "db"})]

        result = build_identities_result(identities, [])

        assert result.identities[0].labels == ("app=db", "tier=db")

    def test_identity_without_labels_reported_empty(self) -> None:
        identities = [_identity("100", spec_labels=[])]

        result = build_identities_result(identities, [])

        assert result.identities[0].labels == ()

    def test_empty_identities(self) -> None:
        result = build_identities_result([], [])

        assert result.installed is True
        assert result.status == "empty"
        assert result.total_identities == 0
        assert result.note is not None

    def test_malformed_id_preserved_raw(self) -> None:
        identities = [{"metadata": {"name": "not-a-numeric-id"}, "spec": {}}]

        result = build_identities_result(identities, [])

        assert result.identities[0].id == "not-a-numeric-id"

    def test_endpoints_without_identity_id_ignored(self) -> None:
        identities = [_identity("100")]
        endpoints = [
            _endpoint("100"),
            {"status": {}},
            {"status": {"identity": "not-a-dict"}},
            {"status": {"identity": {"id": None}}},
        ]

        result = build_identities_result(identities, endpoints)

        assert result.identities[0].endpoint_count == 1  # noqa: PLR2004


class TestNotInstalledIdentitiesResult:
    def test_returns_marker(self) -> None:
        result = not_installed_identities_result()
        assert result.installed is False
        assert result.status == "not_installed"
        assert result.identities == []
        assert result.note is not None
