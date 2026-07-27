from unittest.mock import MagicMock, patch

import pytest
from hexawyn.cli.widgets.command_input import CommandInput
from textual.events import Key


class TestCommandInputInit:
    def test_inherits_from_input(self) -> None:
        widget = CommandInput(placeholder="test")
        assert widget.placeholder == "test"

    def test_initializes_empty_history(self) -> None:
        widget = CommandInput()
        assert widget.history == []

    def test_initializes_history_pos_zero(self) -> None:
        widget = CommandInput()
        assert widget._history_pos == 0


class TestRemember:
    def test_appends_value_to_history(self) -> None:
        widget = CommandInput()
        widget.remember("list pods")
        assert widget.history == ["list pods"]

    def test_updates_history_position_after_remember(self) -> None:
        widget = CommandInput()
        widget.remember("list pods")
        assert widget._history_pos == 1

    def test_does_not_append_empty_string(self) -> None:
        widget = CommandInput()
        widget.remember("")
        assert widget.history == []

    def test_does_not_duplicate_consecutive_same_value(self) -> None:
        widget = CommandInput()
        widget.remember("list pods")
        widget.remember("list pods")
        assert len(widget.history) == 1

    def test_appends_different_value(self) -> None:
        widget = CommandInput()
        widget.remember("list pods")
        widget.remember("get nodes")
        assert widget.history == ["list pods", "get nodes"]

    def test_position_reflects_history_length(self) -> None:
        widget = CommandInput()
        widget.remember("cmd1")
        widget.remember("cmd2")
        widget.remember("cmd3")
        assert widget._history_pos == 3  # noqa: PLR2004


class TestOnKey:
    @pytest.mark.asyncio
    async def test_up_navigates_to_previous_command(self) -> None:
        widget = CommandInput()
        widget.remember("first command")
        widget.remember("second command")
        widget.value = ""

        event = Key(key="up", character="")
        await widget._on_key(event)

        assert widget.value == "second command"
        assert widget.cursor_position == len("second command")

    @pytest.mark.asyncio
    async def test_up_twice_goes_to_first(self) -> None:
        widget = CommandInput()
        widget.remember("first")
        widget.remember("second")
        widget.value = ""

        await widget._on_key(Key(key="up", character=""))
        await widget._on_key(Key(key="up", character=""))

        assert widget.value == "first"
        assert widget._history_pos == 0

    @pytest.mark.asyncio
    async def test_up_stops_at_beginning(self) -> None:
        widget = CommandInput()
        widget.remember("only")
        widget.value = ""

        await widget._on_key(Key(key="up", character="up"))
        await widget._on_key(Key(key="up", character="up"))
        await widget._on_key(Key(key="up", character="up"))

        assert widget._history_pos == 0

    @pytest.mark.asyncio
    async def test_down_navigates_forward(self) -> None:
        widget = CommandInput()
        widget.remember("first")
        widget.remember("second")
        widget.value = ""

        await widget._on_key(Key(key="up", character="up"))
        await widget._on_key(Key(key="up", character="up"))
        await widget._on_key(Key(key="down", character="down"))

        assert widget.value == "second"
        assert widget._history_pos == 1

    @pytest.mark.asyncio
    async def test_down_past_end_clears_value(self) -> None:
        widget = CommandInput()
        widget.remember("first")
        widget.value = "first"

        await widget._on_key(Key(key="down", character="down"))

        assert widget.value == ""
        assert widget._history_pos == 1

    @pytest.mark.asyncio
    async def test_down_at_end_does_not_go_beyond(self) -> None:
        widget = CommandInput()
        widget.remember("first")
        widget.remember("second")
        widget._history_pos = 2

        await widget._on_key(Key(key="down", character="down"))

        assert widget._history_pos == 2  # noqa: PLR2004

    @pytest.mark.asyncio
    async def test_up_does_nothing_without_history(self) -> None:
        widget = CommandInput()
        widget.value = "typed"

        event = Key(key="up", character="")
        event.stop = MagicMock()
        await widget._on_key(event)

        assert widget.value == "typed"
        assert widget._history_pos == 0

    @pytest.mark.asyncio
    async def test_down_does_nothing_without_history(self) -> None:
        widget = CommandInput()
        widget.value = "typed"

        event = Key(key="down", character="")
        event.stop = MagicMock()
        await widget._on_key(event)

        assert widget.value == "typed"
        assert widget._history_pos == 0

    @pytest.mark.asyncio
    async def test_other_keys_delegate_to_super(self) -> None:
        widget = CommandInput()
        widget.value = ""

        event = Key(key="a", character="a")
        with patch.object(widget.__class__, "_on_key", wraps=widget._on_key) as spy:
            await widget._on_key(event)
            assert spy.called
