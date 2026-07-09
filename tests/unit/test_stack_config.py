from unittest.mock import patch

import pytest


class TestGetStackOverride:
    def test_returns_none_when_no_override(self) -> None:
        from hexawyn.infrastructure.config import stack_config

        with patch.object(stack_config, "load_config", return_value={}):
            assert stack_config.get_stack_override("prod-eks") is None

    def test_returns_stored_override(self) -> None:
        from hexawyn.infrastructure.config import stack_config

        config = {"stack_overrides": {"prod-eks": "aws"}}
        with patch.object(stack_config, "load_config", return_value=config):
            assert stack_config.get_stack_override("prod-eks") == "aws"

    def test_ignores_invalid_override_value(self) -> None:
        from hexawyn.infrastructure.config import stack_config

        config = {"stack_overrides": {"prod-eks": "nonsense"}}
        with patch.object(stack_config, "load_config", return_value=config):
            assert stack_config.get_stack_override("prod-eks") is None

    def test_ignores_non_dict_overrides(self) -> None:
        from hexawyn.infrastructure.config import stack_config

        with patch.object(stack_config, "load_config", return_value={"stack_overrides": "oops"}):
            assert stack_config.get_stack_override("prod-eks") is None


class TestSetStackOverride:
    def test_persists_override(self) -> None:
        from hexawyn.infrastructure.config import stack_config

        saved: dict[str, object] = {}
        with (
            patch.object(stack_config, "load_config", return_value={}),
            patch.object(stack_config, "save_config", side_effect=saved.update),
        ):
            stack_config.set_stack_override("prod-eks", "aws")

        assert saved["stack_overrides"] == {"prod-eks": "aws"}

    def test_preserves_existing_config_keys(self) -> None:
        from hexawyn.infrastructure.config import stack_config

        saved: dict[str, object] = {}
        existing = {"llm": {"provider": "x"}, "stack_overrides": {"other": "vanilla"}}
        with (
            patch.object(stack_config, "load_config", return_value=existing),
            patch.object(stack_config, "save_config", side_effect=saved.update),
        ):
            stack_config.set_stack_override("prod-eks", "aws")

        assert saved["llm"] == {"provider": "x"}
        assert saved["stack_overrides"] == {"other": "vanilla", "prod-eks": "aws"}

    def test_rejects_invalid_provider(self) -> None:
        from hexawyn.infrastructure.config import stack_config

        with pytest.raises(ValueError):
            stack_config.set_stack_override("prod-eks", "azure")

    def test_accepts_gcp_provider(self) -> None:
        from hexawyn.infrastructure.config import stack_config

        saved: dict[str, object] = {}
        with (
            patch.object(stack_config, "load_config", return_value={}),
            patch.object(stack_config, "save_config", side_effect=saved.update),
        ):
            stack_config.set_stack_override("gke_p_r_c", "gcp")

        assert saved["stack_overrides"] == {"gke_p_r_c": "gcp"}


class TestClearStackOverride:
    def test_removes_override(self) -> None:
        from hexawyn.infrastructure.config import stack_config

        saved: dict[str, object] = {}
        existing = {"stack_overrides": {"prod-eks": "aws", "other": "vanilla"}}
        with (
            patch.object(stack_config, "load_config", return_value=existing),
            patch.object(stack_config, "save_config", side_effect=saved.update),
        ):
            stack_config.clear_stack_override("prod-eks")

        assert saved["stack_overrides"] == {"other": "vanilla"}

    def test_noop_when_absent(self) -> None:
        from hexawyn.infrastructure.config import stack_config

        with (
            patch.object(stack_config, "load_config", return_value={}),
            patch.object(stack_config, "save_config") as save,
        ):
            stack_config.clear_stack_override("prod-eks")

        save.assert_not_called()
