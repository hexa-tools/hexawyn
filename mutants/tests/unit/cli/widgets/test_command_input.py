from unittest.mock import MagicMock, patch

import pytest
from hexawyn.cli.widgets.command_input import CommandInput
from textual.app import App, ComposeResult
from textual.events import Key
from textual.widgets import Input


class _InputApp(App[None]):
    def __init__(self, widget: Input) -> None:
        super().__init__()
        self._widget = widget

    def compose(self) -> ComposeResult:
        yield self._widget


@pytest.fixture
def widget() -> Input:
    return CommandInput(placeholder="test")


class TestCommandInputInit:
    def test_inherits_from_input(self) -> None:
        w = CommandInput(placeholder="test")
        assert w.placeholder == "test"

    def test_initializes_empty_history(self) -> None:
        w = CommandInput()
        assert w.history == []

    def test_initializes_history_pos_zero(self) -> None:
        w = CommandInput()
        assert w._history_pos == 0


class TestRemember:
    def test_appends_value_to_history(self) -> None:
        w = CommandInput()
        w.remember("list pods")
        assert w.history == ["list pods"]

    def test_updates_history_position_after_remember(self) -> None:
        w = CommandInput()
        w.remember("list pods")
        assert w._history_pos == 1

    def test_does_not_append_empty_string(self) -> None:
        w = CommandInput()
        w.remember("")
        assert w.history == []

    def test_does_not_duplicate_consecutive_same_value(self) -> None:
        w = CommandInput()
        w.remember("list pods")
        w.remember("list pods")
        assert len(w.history) == 1

    def test_appends_different_value(self) -> None:
        w = CommandInput()
        w.remember("list pods")
        w.remember("get nodes")
        assert w.history == ["list pods", "get nodes"]

    def test_position_reflects_history_length(self) -> None:
        w = CommandInput()
        w.remember("cmd1")
        w.remember("cmd2")
        w.remember("cmd3")
        assert w._history_pos == 3  # noqa: PLR2004


class TestOnKey:
    @pytest.mark.asyncio
    async def test_up_navigates_to_previous_command(self) -> None:
        app = _InputApp(CommandInput())
        async with app.run_test() as _pilot:
            w = app.query_one(Input)
            w.remember("first command")
            w.remember("second command")
            w.value = ""

            await w._on_key(Key(key="up", character=""))

            assert w.value == "second command"
            assert w.cursor_position == len("second command")

    @pytest.mark.asyncio
    async def test_up_twice_goes_to_first(self) -> None:
        app = _InputApp(CommandInput())
        async with app.run_test() as _pilot:
            w = app.query_one(Input)
            w.remember("first")
            w.remember("second")
            w.value = ""

            await w._on_key(Key(key="up", character=""))
            await w._on_key(Key(key="up", character=""))

            assert w.value == "first"
            assert w._history_pos == 0

    @pytest.mark.asyncio
    async def test_up_stops_at_beginning(self) -> None:
        app = _InputApp(CommandInput())
        async with app.run_test() as _pilot:
            w = app.query_one(Input)
            w.remember("only")
            w.value = ""

            await w._on_key(Key(key="up", character="up"))
            await w._on_key(Key(key="up", character="up"))
            await w._on_key(Key(key="up", character="up"))

            assert w._history_pos == 0

    @pytest.mark.asyncio
    async def test_down_navigates_forward(self) -> None:
        app = _InputApp(CommandInput())
        async with app.run_test() as _pilot:
            w = app.query_one(Input)
            w.remember("first")
            w.remember("second")
            w.value = ""

            await w._on_key(Key(key="up", character="up"))
            await w._on_key(Key(key="up", character="up"))
            await w._on_key(Key(key="down", character="down"))

            assert w.value == "second"
            assert w._history_pos == 1

    @pytest.mark.asyncio
    async def test_down_past_end_clears_value(self) -> None:
        app = _InputApp(CommandInput())
        async with app.run_test() as _pilot:
            w = app.query_one(Input)
            w.remember("first")
            w.value = "first"

            await w._on_key(Key(key="down", character="down"))

            assert w.value == ""
            assert w._history_pos == 1

    @pytest.mark.asyncio
    async def test_down_at_end_does_not_go_beyond(self) -> None:
        app = _InputApp(CommandInput())
        async with app.run_test() as _pilot:
            w = app.query_one(Input)
            w.remember("first")
            w.remember("second")
            w._history_pos = 2

            await w._on_key(Key(key="down", character="down"))

            assert w._history_pos == 2  # noqa: PLR2004

    @pytest.mark.asyncio
    async def test_up_does_nothing_without_history(self) -> None:
        app = _InputApp(CommandInput())
        async with app.run_test() as _pilot:
            w = app.query_one(Input)
            w.value = "typed"

            event = Key(key="up", character="")
            event.stop = MagicMock()
            await w._on_key(event)

            assert w.value == "typed"
            assert w._history_pos == 0

    @pytest.mark.asyncio
    async def test_down_does_nothing_without_history(self) -> None:
        app = _InputApp(CommandInput())
        async with app.run_test() as _pilot:
            w = app.query_one(Input)
            w.value = "typed"

            event = Key(key="down", character="")
            event.stop = MagicMock()
            await w._on_key(event)

            assert w.value == "typed"
            assert w._history_pos == 0

    @pytest.mark.asyncio
    async def test_other_keys_delegate_to_super(self) -> None:
        app = _InputApp(CommandInput())
        async with app.run_test() as _pilot:
            w = app.query_one(Input)
            w.value = ""

            event = Key(key="a", character="a")
            with patch.object(w.__class__, "_on_key", wraps=w._on_key) as spy:
                await w._on_key(event)
                assert spy.called
