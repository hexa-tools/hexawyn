from typing import Any

from textual.events import Key
from textual.widgets import Input


class CommandInput(Input):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.history: list[str] = []
        self._history_pos = 0

    def remember(self, value: str) -> None:
        if value and (not self.history or self.history[-1] != value):
            self.history.append(value)
        self._history_pos = len(self.history)

    async def _on_key(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos -= 1
            self.value = self.history[self._history_pos]
            self.cursor_position = len(self.value)
            event.stop()
        elif event.key == "down" and self.history:
            self._history_pos = min(self._history_pos + 1, len(self.history))
            self.value = (
                self.history[self._history_pos] if self._history_pos < len(self.history) else ""
            )
            self.cursor_position = len(self.value)
            event.stop()
        else:
            await super()._on_key(event)
