"""RED → GREEN — Layer 1: Kustomize Patch Conflict domain models."""

from hexawyn.domain.models.kustomize_patch_conflict import (
    KustomizePatchConflictReport,
    PatchConflict,
    PatchRedundancy,
    PatchValue,
)


class TestPatchValue:
    def test_is_frozen(self) -> None:
        import pytest

        v = PatchValue(source_file="a.yaml", value="2", patch_type="strategic_merge")
        with pytest.raises(Exception):
            v.value = "3"  # type: ignore[misc]


class TestPatchConflict:
    def test_is_frozen(self) -> None:
        import pytest

        c = PatchConflict(
            field_path="spec.replicas",
            resource="Deployment/svc",
            conflicting_values=[],
            effective_value="5",
            severity="warning",
        )
        with pytest.raises(Exception):
            c.effective_value = "2"  # type: ignore[misc]


class TestPatchRedundancy:
    def test_is_frozen(self) -> None:
        import pytest

        r = PatchRedundancy(
            field_path="spec.replicas",
            resource="Deployment/svc",
            base_value="1",
            patch_value="1",
            source_file="patches/a.yaml",
            severity="informational",
        )
        with pytest.raises(Exception):
            r.patch_value = "2"  # type: ignore[misc]


class TestKustomizePatchConflictReport:
    def test_default_values(self) -> None:
        report = KustomizePatchConflictReport()
        assert report.patch_conflicts == []
        assert report.total_conflicts == 0

    def test_can_populate(self) -> None:
        report = KustomizePatchConflictReport(
            overlay_path="overlays/prod",
            total_conflicts=3,
            total_redundancies=2,
        )
        assert report.overlay_path == "overlays/prod"
        assert report.total_conflicts == 3  # noqa: PLR2004
