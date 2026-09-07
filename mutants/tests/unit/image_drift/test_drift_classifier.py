"""Unit tests for classify_drift — digest comparison (when both sides resolve
one) takes priority over tag comparison; otherwise falls back to tag-only."""

from __future__ import annotations

from hexawyn.domain.models.image_drift import ImageReference
from hexawyn.domain.services.image_drift.drift_classifier import classify_drift


def _ref(
    repository: str = "app", tag: str | None = None, digest: str | None = None
) -> ImageReference:
    return ImageReference(repository=repository, tag=tag, digest=digest)


class TestTagMismatch:
    def test_tc1_tags_differ_no_digest_anywhere_is_tag_mismatch(self) -> None:
        running = _ref(tag="v1.3-hotfix")
        declared = _ref(tag="v1.2")

        assert classify_drift(running, declared, running_image_id=None) == "tag_mismatch"


class TestInSync:
    def test_tc2_same_tag_no_digest_is_in_sync(self) -> None:
        running = _ref(tag="v1.2")
        declared = _ref(tag="v1.2")

        assert classify_drift(running, declared, running_image_id=None) is None


class TestDigestMismatch:
    def test_tc3_declared_digest_vs_resolved_running_image_id_differ(self) -> None:
        running = _ref(repository="analytics", tag="v2.0")
        declared = _ref(repository="analytics", digest="sha256:def456")

        result = classify_drift(running, declared, running_image_id="analytics@sha256:abc123")

        assert result == "digest_mismatch"

    def test_image_id_with_scheme_prefix_is_parsed(self) -> None:
        running = _ref(repository="analytics", tag="v2.0")
        declared = _ref(repository="analytics", digest="sha256:def456")

        result = classify_drift(
            running, declared, running_image_id="docker-pullable://analytics@sha256:abc123"
        )

        assert result == "digest_mismatch"

    def test_image_id_using_colon_sha256_shorthand_is_parsed(self) -> None:
        running = _ref(repository="analytics", tag="v2.0")
        declared = _ref(repository="analytics", digest="sha256:def456")

        result = classify_drift(running, declared, running_image_id="analytics:sha256:abc123")

        assert result == "digest_mismatch"

    def test_running_ref_itself_digest_pinned_and_differs(self) -> None:
        running = _ref(repository="analytics", digest="sha256:abc123")
        declared = _ref(repository="analytics", digest="sha256:def456")

        assert classify_drift(running, declared, running_image_id=None) == "digest_mismatch"

    def test_matching_digests_are_in_sync_even_if_tags_differ(self) -> None:
        running = _ref(repository="analytics", tag="v2.0")
        declared = _ref(repository="analytics", digest="sha256:abc123")

        result = classify_drift(running, declared, running_image_id="analytics@sha256:abc123")

        assert result is None


class TestFallsBackToTagWhenDigestUnavailable:
    def test_declared_has_digest_but_running_image_id_missing_falls_back_to_tag(self) -> None:
        running = _ref(repository="analytics", tag="v2.0")
        declared = _ref(repository="analytics", digest="sha256:def456")

        result = classify_drift(running, declared, running_image_id=None)

        assert result == "tag_mismatch"

    def test_running_has_digest_but_declared_does_not_falls_back_to_tag(self) -> None:
        running = _ref(repository="analytics", digest="sha256:abc123")
        declared = _ref(repository="analytics", tag="v2.0")

        result = classify_drift(running, declared, running_image_id=None)

        assert result == "tag_mismatch"

    def test_unparseable_image_id_falls_back_to_tag(self) -> None:
        running = _ref(repository="analytics", tag="v2.0")
        declared = _ref(repository="analytics", digest="sha256:def456")

        result = classify_drift(running, declared, running_image_id="not-a-digest-shape")

        assert result == "tag_mismatch"
