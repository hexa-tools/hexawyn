from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.cli.screens.context_picker import ContextPickerScreen
from hexawyn.infrastructure.config.kubernetes_context import ClusterContext


class TestContextPickerScreen:
    @staticmethod
    def _make_context(name: str, is_current: bool = False) -> ClusterContext:
        return ClusterContext(
            name=name,
            cluster="my-cluster",
            namespace="default",
            user="admin",
            is_current=is_current,
        )

    @staticmethod
    def _create_screen(contexts: list[ClusterContext]) -> ContextPickerScreen:
        with patch("hexawyn.cli.screens.context_picker.ModalScreen.__init__", return_value=None):
            return ContextPickerScreen(contexts)

    def test_init(self) -> None:
        ctx = self._make_context("prod")
        screen = self._create_screen([ctx])
        assert screen._contexts == [ctx]
        assert screen._focused_context_index == 0  # noqa: PLR2004

    def test_init_current_context_focused(self) -> None:
        ctx_a = self._make_context("staging")
        ctx_b = self._make_context("prod", is_current=True)
        screen = self._create_screen([ctx_a, ctx_b])
        assert screen._focused_context_index == 1  # noqa: PLR2004

    def test_current_context_index_returns_current(self) -> None:
        ctx_a = self._make_context("staging")
        ctx_b = self._make_context("prod", is_current=True)
        screen = self._create_screen([ctx_a, ctx_b])
        assert screen._current_context_index() == 1  # noqa: PLR2004

    def test_current_context_index_fallback_to_zero(self) -> None:
        ctx_a = self._make_context("staging")
        ctx_b = self._make_context("prod")
        screen = self._create_screen([ctx_a, ctx_b])
        assert screen._current_context_index() == 0  # noqa: PLR2004

    def test_current_context_index_empty(self) -> None:
        screen = self._create_screen([])
        assert screen._current_context_index() == 0  # noqa: PLR2004

    def test_focus_next_context_wraps(self) -> None:
        screen = self._create_screen(
            [self._make_context("a"), self._make_context("b"), self._make_context("c")]
        )
        screen._focused_context_index = 2
        screen._focus_context_button = MagicMock()  # type: ignore[method-assign]
        screen.action_focus_next_context()
        assert screen._focused_context_index == 0  # noqa: PLR2004

    def test_focus_next_context_increments(self) -> None:
        screen = self._create_screen([self._make_context("a"), self._make_context("b")])
        screen._focus_context_button = MagicMock()  # type: ignore[method-assign]
        screen.action_focus_next_context()
        assert screen._focused_context_index == 1  # noqa: PLR2004

    def test_focus_previous_context_wraps(self) -> None:
        screen = self._create_screen([self._make_context("a"), self._make_context("b")])
        screen._focused_context_index = 0
        screen._focus_context_button = MagicMock()  # type: ignore[method-assign]
        screen.action_focus_previous_context()
        assert screen._focused_context_index == 1  # noqa: PLR2004

    def test_focus_previous_context_decrements(self) -> None:
        screen = self._create_screen([self._make_context("a"), self._make_context("b")])
        screen._focused_context_index = 1
        screen._focus_context_button = MagicMock()  # type: ignore[method-assign]
        screen.action_focus_previous_context()
        assert screen._focused_context_index == 0  # noqa: PLR2004

    def test_focus_next_context_empty_list(self) -> None:
        screen = self._create_screen([])
        screen._focused_context_index = 5
        screen.action_focus_next_context()
        assert screen._focused_context_index == 5  # noqa: PLR2004

    def test_focus_previous_context_empty_list(self) -> None:
        screen = self._create_screen([])
        screen._focused_context_index = 5
        screen.action_focus_previous_context()
        assert screen._focused_context_index == 5  # noqa: PLR2004

    def test_on_button_pressed_cancel(self) -> None:
        screen = self._create_screen([self._make_context("prod")])
        mock_event = MagicMock()
        mock_event.button.id = "context-cancel"
        screen.dismiss = MagicMock()
        screen.on_button_pressed(mock_event)
        screen.dismiss.assert_called_once_with(None)

    def test_on_button_pressed_context(self) -> None:
        screen = self._create_screen([self._make_context("prod")])
        mock_event = MagicMock()
        mock_event.button.id = "context-prod"
        screen.dismiss = MagicMock()
        screen.on_button_pressed(mock_event)
        screen.dismiss.assert_called_once_with("prod")

    def test_action_cancel_dismisses_none(self) -> None:
        screen = self._create_screen([self._make_context("prod")])
        screen.dismiss = MagicMock()
        screen.action_cancel()
        screen.dismiss.assert_called_once_with(None)
