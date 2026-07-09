"""TDD: Anonymizer — RED phase."""


class TestRedactionPolicy:
    def test_default_policy_masks_secrets(self) -> None:
        from hexawyn.domain.models.anonymization import RedactionPolicy

        p = RedactionPolicy()
        assert p.mask_secrets is True
        assert p.mask_tokens is True
        assert p.mask_ips is True
        assert p.mask_resource_names is False

    def test_custom_policy(self) -> None:
        from hexawyn.domain.models.anonymization import RedactionPolicy

        p = RedactionPolicy(mask_resource_names=True)
        assert p.mask_resource_names is True


class TestDestinationEnum:
    def test_values(self) -> None:
        from hexawyn.domain.models.anonymization import Destination

        assert Destination.LOCAL.value == "local"
        assert Destination.SLACK.value == "slack"
        assert Destination.EXPORT.value == "export"
        assert Destination.LOG.value == "log"


class TestSensitiveKindEnum:
    def test_values(self) -> None:
        from hexawyn.domain.models.anonymization import SensitiveKind

        assert SensitiveKind.SECRET_REF.value == "secret_ref"
        assert SensitiveKind.TOKEN.value == "token"
        assert SensitiveKind.IP.value == "ip"
        assert SensitiveKind.EMAIL.value == "email"
        assert SensitiveKind.INTERNAL_HOST.value == "internal_host"


class TestSensitiveMatch:
    def test_creation(self) -> None:
        from hexawyn.domain.models.anonymization import SensitiveKind, SensitiveMatch

        match = SensitiveMatch(kind=SensitiveKind.IP, original="10.0.0.1", placeholder="<IP_1>")
        assert match.kind == SensitiveKind.IP
        assert match.original == "10.0.0.1"
        assert match.placeholder == "<IP_1>"


class TestAnonymizationMap:
    def test_empty_map(self) -> None:
        from hexawyn.domain.models.anonymization import AnonymizationMap

        m = AnonymizationMap()
        assert m.matches == []


class TestRegexAnonymizerMask:
    def test_masks_secret_ref(self) -> None:
        from hexawyn.domain.models.anonymization import RedactionPolicy
        from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

        adapter = RegexAnonymizerAdapter()
        text = "Use secret: my-app-secret"
        masked, _map = adapter.mask(text, RedactionPolicy())
        assert "my-app-secret" not in masked
        assert "<SECRET_REF" in masked

    def test_masks_ip(self) -> None:
        from hexawyn.domain.models.anonymization import RedactionPolicy
        from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

        adapter = RegexAnonymizerAdapter()
        text = "Node IP is 10.42.0.15, pod on 192.168.1.100"
        masked, _map = adapter.mask(text, RedactionPolicy())
        assert "10.42.0.15" not in masked
        assert "192.168.1.100" not in masked

    def test_masks_token(self) -> None:
        from hexawyn.domain.models.anonymization import RedactionPolicy
        from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

        adapter = RegexAnonymizerAdapter()
        text = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xxxxx.yyyyy"
        masked, _map = adapter.mask(text, RedactionPolicy())
        assert "eyJ" not in masked

    def test_preserves_resource_names_by_default(self) -> None:
        from hexawyn.domain.models.anonymization import RedactionPolicy
        from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

        adapter = RegexAnonymizerAdapter()
        text = "Deployment nginx-deployment has issue"
        masked, _map = adapter.mask(text, RedactionPolicy())
        assert "nginx-deployment" in masked

    def test_masks_resource_names_when_enabled(self) -> None:
        from hexawyn.domain.models.anonymization import RedactionPolicy
        from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

        adapter = RegexAnonymizerAdapter()
        text = "Deployment nginx-deployment has issue"
        masked, _map = adapter.mask(text, RedactionPolicy(mask_resource_names=True))
        assert "nginx-deployment" not in masked


class TestRegexAnonymizerUnmask:
    def test_roundtrip_local(self) -> None:
        from hexawyn.domain.models.anonymization import Destination, RedactionPolicy
        from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

        adapter = RegexAnonymizerAdapter()
        original = "Secret name: my-app-secret, IP: 10.0.0.1"
        masked, amap = adapter.mask(original, RedactionPolicy())
        restored = adapter.unmask(masked, amap, Destination.LOCAL)
        assert restored == original

    def test_unmask_refused_for_slack(self) -> None:
        from hexawyn.domain.models.anonymization import Destination, RedactionPolicy
        from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

        adapter = RegexAnonymizerAdapter()
        original = "Secret: my-secret"
        masked, amap = adapter.mask(original, RedactionPolicy())
        result = adapter.unmask(masked, amap, Destination.SLACK)
        assert "my-secret" not in result


class TestAnonymizationMapNeverSerialized:
    def test_map_has_no_persist_method(self) -> None:
        from hexawyn.domain.models.anonymization import AnonymizationMap

        m = AnonymizationMap()
        assert not hasattr(m, "save")
        assert not hasattr(m, "to_dict")
