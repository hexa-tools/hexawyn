from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.use_case.troubleshooting.chat_cli.chat_cli_use_case import (
    ChatCliUseCase,
)


def _cluster_context_mock() -> MagicMock:
    k8s = MagicMock()
    k8s.get_cluster_context.return_value = {
        "name": "test",
        "cluster": "test-cluster",
        "provider": "vanilla",
        "namespace": "default",
    }
    return k8s


def _investigation_output() -> dict[str, object]:
    return {
        "status": "ok",
        "answer": "test",
        "suggestions": [],
        "usage": {},
        "embedding": [0.1],
        "cause": "test",
        "solution": "fix",
        "error": None,
        "predicted_intents": [],
    }


class TestIncrementQuota:
    def test_remote_mode_increments_cp_only(self) -> None:
        k8s = _cluster_context_mock()
        runtime = MagicMock()
        runtime.run_investigation.return_value = _investigation_output()
        use_case = ChatCliUseCase(k8s_port=k8s, runtime=runtime)

        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.get_runtime_mode",
                return_value="remote",
            ),
            patch(
                "hexawyn.infrastructure.config.quota_manager.increment_quota"
            ) as mock_local_increment,
        ):
            use_case._increment_quota()

        runtime.increment_quota.assert_called_once()
        mock_local_increment.assert_not_called()

    def test_remote_mode_swallows_cp_error(self) -> None:
        k8s = _cluster_context_mock()
        runtime = MagicMock()
        runtime.increment_quota.side_effect = RuntimeError("cp down")
        use_case = ChatCliUseCase(k8s_port=k8s, runtime=runtime)

        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.get_runtime_mode",
                return_value="remote",
            ),
            patch(
                "hexawyn.infrastructure.config.quota_manager.increment_quota"
            ) as mock_local_increment,
        ):
            use_case._increment_quota()

        runtime.increment_quota.assert_called_once()
        mock_local_increment.assert_not_called()

    def test_embedded_mode_increments_local_only(self) -> None:
        k8s = _cluster_context_mock()
        runtime = MagicMock()
        use_case = ChatCliUseCase(k8s_port=k8s, runtime=runtime)

        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.get_runtime_mode",
                return_value="embedded",
            ),
            patch(
                "hexawyn.infrastructure.config.quota_manager.increment_quota"
            ) as mock_local_increment,
        ):
            use_case._increment_quota()

        runtime.increment_quota.assert_not_called()
        mock_local_increment.assert_called_once()

    def test_embedded_mode_swallows_local_error(self) -> None:
        k8s = _cluster_context_mock()
        runtime = MagicMock()
        use_case = ChatCliUseCase(k8s_port=k8s, runtime=runtime)

        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.get_runtime_mode",
                return_value="embedded",
            ),
            patch(
                "hexawyn.infrastructure.config.quota_manager.increment_quota",
                side_effect=RuntimeError("db down"),
            ),
        ):
            use_case._increment_quota()

        runtime.increment_quota.assert_not_called()
