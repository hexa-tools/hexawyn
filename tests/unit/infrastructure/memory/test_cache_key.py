from hexawyn.infrastructure.memory.duckdb_cache_adapter import compute_cache_key


class TestComputeCacheKey:
    def test_same_inputs_produce_same_hash(self):
        a = compute_cache_key("prod", "investigate", "ns", "pod-1", "why crash?")
        b = compute_cache_key("prod", "investigate", "ns", "pod-1", "why crash?")
        assert a == b

    def test_different_cluster_produces_different_hash(self):
        a = compute_cache_key("prod", "t", "ns", "r", "q")
        b = compute_cache_key("staging", "t", "ns", "r", "q")
        assert a != b

    def test_different_query_produces_different_hash(self):
        a = compute_cache_key("prod", "t", "ns", "r", "q1")
        b = compute_cache_key("prod", "t", "ns", "r", "q2")
        assert a != b

    def test_case_insensitive(self):
        a = compute_cache_key("PROD", "T", "NS", "R", "Q")
        b = compute_cache_key("prod", "t", "ns", "r", "q")
        assert a == b

    def test_returns_64_char_hex_string(self):
        key = compute_cache_key("c", "t", "n", "r", "q")
        assert len(key) == 64
        assert all(c in "0123456789abcdef" for c in key)

    def test_empty_inputs_produce_valid_hash(self) -> None:
        key = compute_cache_key("", "", "", "", "")
        assert len(key) == 64
        assert all(c in "0123456789abcdef" for c in key)

    def test_whitespace_only_inputs_produce_valid_hash(self) -> None:
        key = compute_cache_key("  ", "\t", "\n", " ", "   ")
        assert len(key) == 64

    def test_long_inputs_produce_valid_hash(self) -> None:
        long_text = "x" * 10_000
        key = compute_cache_key(long_text, long_text, long_text, long_text, long_text)
        assert len(key) == 64

    def test_special_characters_inputs_produce_valid_hash(self) -> None:
        key = compute_cache_key("prod!", "tool@", "ns#", "res$", "query%")
        assert len(key) == 64

    def test_unicode_inputs_produce_valid_hash(self) -> None:
        key = compute_cache_key("pröd", "tööl", "nämespace", "resöurce", "quéry")
        assert len(key) == 64

    def test_same_normalized_inputs_produce_same_hash(self) -> None:
        a = compute_cache_key("PROD", "TOOL", "NS", "RES", "Q")
        b = compute_cache_key("prod", "tool", "ns", "res", "q")
        assert a == b
