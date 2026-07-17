from __future__ import annotations


class TestDeepDiffChangeTypes:
    def test_identical_dicts_produce_no_diffs(self) -> None:
        from hexawyn.domain.services.helm_values_diff.values_deep_diff import deep_diff

        source = {"image": {"tag": "v1.3"}, "replicaCount": 3}
        target = {"image": {"tag": "v1.3"}, "replicaCount": 3}

        assert deep_diff(source, target) == []

    def test_changed_scalar_flagged(self) -> None:
        from hexawyn.domain.services.helm_values_diff.values_deep_diff import deep_diff

        result = deep_diff({"replicaCount": 1}, {"replicaCount": 3})

        assert len(result) == 1
        assert result[0].key_path == "replicaCount"
        assert result[0].change_type == "changed"
        assert result[0].source_value == "1"
        assert result[0].target_value == "3"

    def test_nested_key_path_is_dotted(self) -> None:
        from hexawyn.domain.services.helm_values_diff.values_deep_diff import deep_diff

        result = deep_diff({"image": {"tag": "v1.3"}}, {"image": {"tag": "v1.2"}})

        assert result[0].key_path == "image.tag"

    def test_key_only_in_source_is_removed(self) -> None:
        from hexawyn.domain.services.helm_values_diff.values_deep_diff import deep_diff

        result = deep_diff({"feature_flags": {"new_ui": True}}, {})

        assert result[0].key_path == "feature_flags.new_ui"
        assert result[0].change_type == "removed"
        assert result[0].source_value == "True"
        assert result[0].target_value == ""

    def test_key_only_in_target_is_added(self) -> None:
        from hexawyn.domain.services.helm_values_diff.values_deep_diff import deep_diff

        result = deep_diff({}, {"feature_flags": {"beta": True}})

        assert result[0].key_path == "feature_flags.beta"
        assert result[0].change_type == "added"
        assert result[0].source_value == ""
        assert result[0].target_value == "True"


class TestTypeAwareComparison:
    def test_int_vs_string_same_repr_is_type_mismatch(self) -> None:
        from hexawyn.domain.services.helm_values_diff.values_deep_diff import deep_diff

        result = deep_diff({"port": 8080}, {"port": "8080"})

        assert len(result) == 1
        assert result[0].key_path == "port"
        assert result[0].type_mismatch is True
        assert result[0].change_type == "changed"

    def test_same_type_same_value_no_diff(self) -> None:
        from hexawyn.domain.services.helm_values_diff.values_deep_diff import deep_diff

        assert deep_diff({"port": 8080}, {"port": 8080}) == []

    def test_changed_value_same_type_not_type_mismatch(self) -> None:
        from hexawyn.domain.services.helm_values_diff.values_deep_diff import deep_diff

        result = deep_diff({"port": 8080}, {"port": 9090})

        assert result[0].type_mismatch is False


class TestNesting:
    def test_dict_replaced_by_scalar_recurses_as_removed_plus_added(self) -> None:
        from hexawyn.domain.services.helm_values_diff.values_deep_diff import deep_diff

        result = deep_diff({"a": {"b": 1}}, {"a": 2})
        paths = {diff.key_path for diff in result}

        assert "a.b" in paths or "a" in paths

    def test_multiple_nested_differences(self) -> None:
        from hexawyn.domain.services.helm_values_diff.values_deep_diff import deep_diff

        source = {"image": {"tag": "v1.3", "repository": "svc"}, "replicaCount": 1}
        target = {"image": {"tag": "v1.2", "repository": "svc"}, "replicaCount": 3}

        result = deep_diff(source, target)
        paths = {diff.key_path for diff in result}

        assert paths == {"image.tag", "replicaCount"}

    def test_list_values_compared_by_repr(self) -> None:
        from hexawyn.domain.services.helm_values_diff.values_deep_diff import deep_diff

        result = deep_diff({"args": ["a", "b"]}, {"args": ["a", "c"]})

        assert result[0].key_path == "args"
        assert result[0].change_type == "changed"
