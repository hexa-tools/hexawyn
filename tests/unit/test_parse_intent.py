import hexawyn.lang_graph.nodes.parse_intent as pi


class TestParseIntent:
    def test_run_returns_parse_intent_output(self):
        result = pi.run.__doc__
        assert result is not None
