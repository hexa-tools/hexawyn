from hexawyn.domain.models.security_audit import SecurityAudit


class TestSecurityAudit:
    def test_minimal_construction(self) -> None:
        entry = SecurityAudit(cluster_name="prod-eu", severity="low")
        assert entry.cluster_name == "prod-eu"
        assert entry.severity == "low"
        assert entry.findings == {}

    def test_full_construction(self) -> None:
        findings = {
            "rbac": {"overly_permissive_roles": 3, "unused_service_accounts": 7},
            "secrets": {"expired_tokens": 2, "unencrypted": 1},
            "certificates": {"expiring_soon": 1, "days_left": 12},
        }
        entry = SecurityAudit(
            cluster_name="prod-eu",
            findings=findings,
            severity="high",
        )
        assert entry.cluster_name == "prod-eu"
        assert entry.severity == "high"
        assert entry.findings == findings

    def test_is_dataclass(self) -> None:
        entry = SecurityAudit(cluster_name="test", severity="low")
        assert hasattr(entry, "__dataclass_fields__")

    def test_is_critical_true_for_critical_severity(self) -> None:
        entry = SecurityAudit(cluster_name="prod", severity="critical")
        assert entry.is_critical is True

    def test_is_critical_false_for_high(self) -> None:
        entry = SecurityAudit(cluster_name="prod", severity="high")
        assert entry.is_critical is False

    def test_is_critical_false_for_low(self) -> None:
        entry = SecurityAudit(cluster_name="prod", severity="low")
        assert entry.is_critical is False

    def test_total_issues_counts_rbac_secrets_and_certs(self) -> None:
        entry = SecurityAudit(
            cluster_name="prod",
            severity="medium",
            findings={
                "rbac": {"overly_permissive_roles": 3},
                "secrets": {"expired_tokens": 2, "unencrypted": 1},
                "certificates": {"expiring_soon": 4},
            },
        )
        assert entry.total_issues == 10

    def test_total_issues_returns_zero_for_empty_findings(self) -> None:
        entry = SecurityAudit(cluster_name="empty", severity="low")
        assert entry.total_issues == 0

    def test_total_issues_handles_non_numeric_values(self) -> None:
        entry = SecurityAudit(
            cluster_name="prod",
            severity="low",
            findings={
                "rbac": {"description": "no issues"},
                "secrets": {"token_list": ["token-a", "token-b"]},
            },
        )
        assert entry.total_issues == 0

    def test_category_summary_returns_keys(self) -> None:
        entry = SecurityAudit(
            cluster_name="prod",
            severity="medium",
            findings={
                "rbac": {"issues": 3},
                "secrets": {"issues": 1},
                "certificates": {"issues": 4},
            },
        )
        categories = entry.category_summary
        assert "rbac" in categories
        assert "secrets" in categories
        assert "certificates" in categories

    def test_from_dict_constructs_full_object(self) -> None:
        data: dict[str, object] = {
            "cluster_name": "staging",
            "severity": "high",
            "findings": {"rbac": {"overly_permissive": 5}},
        }
        entry = SecurityAudit.from_dict(data)
        assert entry.cluster_name == "staging"
        assert entry.severity == "high"
        assert entry.findings == {"rbac": {"overly_permissive": 5}}
        assert entry.is_critical is False

    def test_from_dict_uses_defaults(self) -> None:
        entry = SecurityAudit.from_dict({"cluster_name": "bare", "severity": "low"})
        assert entry.cluster_name == "bare"
        assert entry.severity == "low"
        assert entry.findings == {}
