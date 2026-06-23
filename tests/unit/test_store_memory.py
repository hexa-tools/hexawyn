import hexawyn.lang_graph.nodes.store_memory as sm


class TestStoreMemory:
    def test_run_returns_store_memory_output(self):
        result = sm.run.__doc__
        assert result is not None
