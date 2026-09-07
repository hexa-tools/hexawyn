from __future__ import annotations

from hexawyn.domain.models.cilium import CiliumIdentitiesResult, CiliumIdentityInfo
from hexawyn.domain.services.cilium.identity_builder import (
    _count_endpoint_ids,
    _endpoint_identity_id,
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

    def test_exact_present_result(self) -> None:
        identities = [
            _identity("100", spec_labels=["a", "b"]),
            _identity("200", spec_labels=["c"]),
        ]
        endpoints = [_endpoint("100"), _endpoint("100"), _endpoint("200")]

        result = build_identities_result(identities, endpoints)

        assert isinstance(result, CiliumIdentitiesResult)
        assert result == CiliumIdentitiesResult(
            installed=True,
            status="present",
            total_identities=2,  # noqa: PLR2004
            identities=[
                CiliumIdentityInfo(
                    id="100",
                    labels=("a", "b"),
                    endpoint_count=2,  # noqa: PLR2004
                ),
                CiliumIdentityInfo(
                    id="200",
                    labels=("c",),
                    endpoint_count=1,  # noqa: PLR2004
                ),
            ],
            note=None,
        )

    def test_missing_metadata_name_empty_id(self) -> None:
        result = build_identities_result([{"spec": {}}], [])

        assert result.identities[0].id == ""
        assert result.identities[0].endpoint_count == 0

    def test_identity_id_absent_from_endpoints_zero_count(self) -> None:
        result = build_identities_result([_identity("900")], [_endpoint("100")])

        assert result.identities[0].endpoint_count == 0

    def test_empty_exact_result(self) -> None:
        result = build_identities_result([], [])

        assert result == CiliumIdentitiesResult(
            installed=True,
            status="empty",
            total_identities=0,
            identities=[],
            note="No Cilium identities found",
        )


class TestNotInstalledIdentitiesResult:
    def test_returns_marker(self) -> None:
        result = not_installed_identities_result()
        assert result.installed is False
        assert result.status == "not_installed"
        assert result.identities == []
        assert result.note is not None

    def test_exact_dataclass(self) -> None:
        result = not_installed_identities_result()

        assert result == CiliumIdentitiesResult(
            installed=False,
            status="not_installed",
            total_identities=0,
            identities=[],
            note="Cilium is not installed in this cluster",
        )


class TestCountEndpointIds:
    def test_counts_valid_ids_and_skips_invalid(self) -> None:
        endpoints = [
            _endpoint("100"),
            _endpoint("100"),
            {"status": {}},
            {"status": {"identity": "not-a-dict"}},
            {"status": {"identity": {"id": None}}},
            _endpoint("200"),
        ]

        counts = _count_endpoint_ids(endpoints)

        assert counts == {"100": 2, "200": 1}  # noqa: PLR2004


class TestEndpointIdentityId:
    def test_returns_id_when_present(self) -> None:
        assert _endpoint_identity_id(_endpoint("100")) == "100"

    def test_none_when_no_status(self) -> None:
        assert _endpoint_identity_id({}) is None

    def test_none_when_identity_not_dict(self) -> None:
        assert _endpoint_identity_id({"status": {"identity": "raw"}}) is None

    def test_none_when_id_missing(self) -> None:
        assert _endpoint_identity_id({"status": {"identity": {}}}) is None

    def test_none_when_id_none(self) -> None:
        assert _endpoint_identity_id({"status": {"identity": {"id": None}}}) is None
