from __future__ import annotations

from hexawyn.domain.models.anonymization import (
    AnonymizationMap,
    Destination,
    RedactionPolicy,
    SensitiveKind,
    SensitiveMatch,
)
from hexawyn.domain.models.slack import SlackBlock, SlackMessage
from hexawyn.domain.models.topology_snapshot import TopologySnapshot


class TestAnonymizationModels:
    def test_sensitive_kind_values(self) -> None:
        assert SensitiveKind.SECRET_REF.value == "secret_ref"

    def test_destination_values(self) -> None:
        assert Destination.SLACK.value == "slack"

    def test_sensitive_match(self) -> None:
        m = SensitiveMatch(kind=SensitiveKind.TOKEN, original="abc123", placeholder="***")
        assert m.kind == SensitiveKind.TOKEN

    def test_anonymization_map(self) -> None:
        am = AnonymizationMap()
        assert am.matches == []

    def test_redaction_policy_defaults(self) -> None:
        rp = RedactionPolicy()
        assert rp.mask_secrets is True
        assert rp.mask_ips is True


class TestSlackModels:
    def test_slack_block(self) -> None:
        b = SlackBlock(type="section", text="hello")
        assert b.type == "section"

    def test_slack_message_basic(self) -> None:
        m = SlackMessage(text="hi")
        assert m.text == "hi"
        assert m.is_pro_format is False
        payload = m.to_payload()
        assert payload == {"text": "hi"}

    def test_slack_message_pro_format(self) -> None:
        m = SlackMessage(
            text="title", is_pro_format=True, blocks=[SlackBlock(type="section", text="body")]
        )
        payload = m.to_payload()
        assert payload["text"] == "title"
        assert "blocks" in payload

    def test_slack_message_pro_without_blocks(self) -> None:
        m = SlackMessage(text="x", is_pro_format=True)
        payload = m.to_payload()
        assert "blocks" not in payload


class TestTopologySnapshot:
    def test_defaults(self) -> None:
        ts = TopologySnapshot(cluster_name="test")
        assert ts.node_count == 0
        assert ts.pod_count == 0

    def test_from_dict(self) -> None:
        ts = TopologySnapshot.from_dict(
            {
                "cluster_name": "prod",
                "snapshot": {
                    "nodes": 10,
                    "pods": 100,
                    "services": 20,
                    "namespaces": ["ns1", "ns2"],
                },
            }
        )
        assert ts.cluster_name == "prod"
        assert ts.node_count == 10  # noqa: PLR2004
        assert ts.pod_count == 100  # noqa: PLR2004
        assert ts.service_count == 20  # noqa: PLR2004
        assert ts.namespace_count == 2  # noqa: PLR2004

    def test_from_dict_non_dict_snapshot(self) -> None:
        ts = TopologySnapshot.from_dict({"cluster_name": "x", "snapshot": "bad"})
        assert ts.snapshot == {}
