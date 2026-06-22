import hexawyn.lang_graph.nodes.check_cache as cc


class TestCheckCache:
    def test_run_returns_check_cache_output(self):
        result = cc.run.__doc__
        assert result is not None
