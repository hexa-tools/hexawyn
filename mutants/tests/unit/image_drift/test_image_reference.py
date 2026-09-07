"""Unit tests for parse_image_reference / is_mutable_tag."""

from __future__ import annotations


class TestParseImageReferenceTag:
    def test_repo_and_tag(self) -> None:
        from hexawyn.domain.services.image_drift.image_reference import parse_image_reference

        ref = parse_image_reference("payment:v1.2")

        assert ref.repository == "payment"
        assert ref.tag == "v1.2"
        assert ref.digest is None

    def test_no_tag_no_digest(self) -> None:
        from hexawyn.domain.services.image_drift.image_reference import parse_image_reference

        ref = parse_image_reference("payment")

        assert ref.repository == "payment"
        assert ref.tag is None
        assert ref.digest is None

    def test_registry_with_port_is_not_mistaken_for_tag(self) -> None:
        from hexawyn.domain.services.image_drift.image_reference import parse_image_reference

        ref = parse_image_reference("myregistry:5000/payment:v1.2")

        assert ref.repository == "myregistry:5000/payment"
        assert ref.tag == "v1.2"
        assert ref.digest is None

    def test_registry_with_port_and_no_tag(self) -> None:
        from hexawyn.domain.services.image_drift.image_reference import parse_image_reference

        ref = parse_image_reference("myregistry:5000/payment")

        assert ref.repository == "myregistry:5000/payment"
        assert ref.tag is None
        assert ref.digest is None


class TestParseImageReferenceDigest:
    def test_at_sign_digest_format(self) -> None:
        from hexawyn.domain.services.image_drift.image_reference import parse_image_reference

        ref = parse_image_reference("analytics@sha256:def456")

        assert ref.repository == "analytics"
        assert ref.tag is None
        assert ref.digest == "sha256:def456"

    def test_colon_sha256_shorthand_format(self) -> None:
        from hexawyn.domain.services.image_drift.image_reference import parse_image_reference

        ref = parse_image_reference("analytics:sha256:def456")

        assert ref.repository == "analytics"
        assert ref.tag is None
        assert ref.digest == "sha256:def456"

    def test_at_sign_takes_priority_over_colon_parsing(self) -> None:
        from hexawyn.domain.services.image_drift.image_reference import parse_image_reference

        ref = parse_image_reference("myregistry:5000/analytics@sha256:abc123")

        assert ref.repository == "myregistry:5000/analytics"
        assert ref.digest == "sha256:abc123"


class TestIsMutableTag:
    def test_none_is_mutable(self) -> None:
        from hexawyn.domain.services.image_drift.image_reference import is_mutable_tag

        assert is_mutable_tag(None) is True

    def test_latest_is_mutable(self) -> None:
        from hexawyn.domain.services.image_drift.image_reference import is_mutable_tag

        assert is_mutable_tag("latest") is True

    def test_explicit_version_is_not_mutable(self) -> None:
        from hexawyn.domain.services.image_drift.image_reference import is_mutable_tag

        assert is_mutable_tag("v1.2") is False
