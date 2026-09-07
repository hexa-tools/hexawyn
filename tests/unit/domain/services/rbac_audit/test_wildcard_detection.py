"""Unit tests for wildcard/secrets detection on a single PolicyRule."""

from __future__ import annotations


class TestHasWildcardVerb:
    def test_wildcard_verb_is_detected(self) -> None:
        from hexawyn.domain.models.rbac_audit import PolicyRule
        from hexawyn.domain.services.rbac_audit.wildcard_detection import (
            has_wildcard_verb,
        )

        rule = PolicyRule(verbs=["*"], resources=["secrets"], api_groups=[""])

        assert has_wildcard_verb(rule) is True

    def test_explicit_verbs_are_not_wildcard(self) -> None:
        from hexawyn.domain.models.rbac_audit import PolicyRule
        from hexawyn.domain.services.rbac_audit.wildcard_detection import (
            has_wildcard_verb,
        )

        rule = PolicyRule(verbs=["get", "list"], resources=["pods"], api_groups=[""])

        assert has_wildcard_verb(rule) is False


class TestHasWildcardResource:
    def test_wildcard_resource_is_detected(self) -> None:
        from hexawyn.domain.models.rbac_audit import PolicyRule
        from hexawyn.domain.services.rbac_audit.wildcard_detection import (
            has_wildcard_resource,
        )

        rule = PolicyRule(verbs=["get"], resources=["*"], api_groups=["*"])

        assert has_wildcard_resource(rule) is True

    def test_explicit_resources_are_not_wildcard(self) -> None:
        from hexawyn.domain.models.rbac_audit import PolicyRule
        from hexawyn.domain.services.rbac_audit.wildcard_detection import (
            has_wildcard_resource,
        )

        rule = PolicyRule(verbs=["get"], resources=["pods"], api_groups=[""])

        assert has_wildcard_resource(rule) is False


class TestTargetsSecrets:
    def test_secrets_resource_is_detected(self) -> None:
        from hexawyn.domain.models.rbac_audit import PolicyRule
        from hexawyn.domain.services.rbac_audit.wildcard_detection import (
            targets_secrets,
        )

        rule = PolicyRule(verbs=["*"], resources=["secrets"], api_groups=[""])

        assert targets_secrets(rule) is True

    def test_non_secrets_resource_is_not_flagged(self) -> None:
        from hexawyn.domain.models.rbac_audit import PolicyRule
        from hexawyn.domain.services.rbac_audit.wildcard_detection import (
            targets_secrets,
        )

        rule = PolicyRule(verbs=["*"], resources=["pods"], api_groups=[""])

        assert targets_secrets(rule) is False
