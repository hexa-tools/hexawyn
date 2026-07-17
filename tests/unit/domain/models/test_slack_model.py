from hexawyn.domain.models.slack import SlackBlock, SlackMessage


class TestSlackMessage:
    def test_has_text(self) -> None:
        msg = SlackMessage(text="test alert")
        assert msg.text == "test alert"

    def test_has_blocks(self) -> None:
        msg = SlackMessage(
            text="test",
            blocks=[SlackBlock(type="section", text="details")],
        )
        assert len(msg.blocks) == 1

    def test_to_payload_returns_dict(self) -> None:
        msg = SlackMessage(text="test alert")
        payload = msg.to_payload()
        assert "text" in payload
        assert payload["text"] == "test alert"

    def test_free_tier_format_no_blocks(self) -> None:
        msg = SlackMessage(text="🚨 alert", is_pro_format=False)
        payload = msg.to_payload()
        assert "blocks" not in payload

    def test_pro_tier_format_has_blocks(self) -> None:
        msg = SlackMessage(
            text="🚨 alert",
            is_pro_format=True,
            blocks=[SlackBlock(type="section", text="details")],
        )
        payload = msg.to_payload()
        assert "blocks" in payload

    def test_pro_tier_without_blocks_omits_blocks_key(self) -> None:
        msg = SlackMessage(text="alert", is_pro_format=True)
        payload = msg.to_payload()
        assert "blocks" not in payload

    def test_block_text_wrapped_in_mrkdwn(self) -> None:
        msg = SlackMessage(
            text="alert",
            is_pro_format=True,
            blocks=[SlackBlock(type="section", text="some detail")],
        )
        payload = msg.to_payload()
        blocks = payload["blocks"]
        assert isinstance(blocks, list)
        assert blocks[0]["text"]["type"] == "mrkdwn"
        assert blocks[0]["text"]["text"] == "some detail"
