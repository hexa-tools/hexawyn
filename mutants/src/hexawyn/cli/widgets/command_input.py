from typing import Any

from textual.events import Key
from textual.widgets import Input


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCommandInputǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCommandInputǁremember__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCommandInputǁ_on_key__mutmut: MutantDict = {}  # type: ignore


class CommandInput(Input):
    @_mutmut_mutated(mutants_xǁCommandInputǁ__init____mutmut)
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.history: list[str] = []
        self._history_pos = 0
    def xǁCommandInputǁ__init____mutmut_orig(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.history: list[str] = []
        self._history_pos = 0
    def xǁCommandInputǁ__init____mutmut_1(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.history: list[str] = None
        self._history_pos = 0
    def xǁCommandInputǁ__init____mutmut_2(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.history: list[str] = []
        self._history_pos = None
    def xǁCommandInputǁ__init____mutmut_3(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.history: list[str] = []
        self._history_pos = 1

    @_mutmut_mutated(mutants_xǁCommandInputǁremember__mutmut)
    def remember(self, value: str) -> None:
        if value and (not self.history or self.history[-1] != value):
            self.history.append(value)
        self._history_pos = len(self.history)

    def xǁCommandInputǁremember__mutmut_orig(self, value: str) -> None:
        if value and (not self.history or self.history[-1] != value):
            self.history.append(value)
        self._history_pos = len(self.history)

    def xǁCommandInputǁremember__mutmut_1(self, value: str) -> None:
        if value or (not self.history or self.history[-1] != value):
            self.history.append(value)
        self._history_pos = len(self.history)

    def xǁCommandInputǁremember__mutmut_2(self, value: str) -> None:
        if value and (not self.history and self.history[-1] != value):
            self.history.append(value)
        self._history_pos = len(self.history)

    def xǁCommandInputǁremember__mutmut_3(self, value: str) -> None:
        if value and (self.history or self.history[-1] != value):
            self.history.append(value)
        self._history_pos = len(self.history)

    def xǁCommandInputǁremember__mutmut_4(self, value: str) -> None:
        if value and (not self.history or self.history[+1] != value):
            self.history.append(value)
        self._history_pos = len(self.history)

    def xǁCommandInputǁremember__mutmut_5(self, value: str) -> None:
        if value and (not self.history or self.history[-2] != value):
            self.history.append(value)
        self._history_pos = len(self.history)

    def xǁCommandInputǁremember__mutmut_6(self, value: str) -> None:
        if value and (not self.history or self.history[-1] == value):
            self.history.append(value)
        self._history_pos = len(self.history)

    def xǁCommandInputǁremember__mutmut_7(self, value: str) -> None:
        if value and (not self.history or self.history[-1] != value):
            self.history.append(None)
        self._history_pos = len(self.history)

    def xǁCommandInputǁremember__mutmut_8(self, value: str) -> None:
        if value and (not self.history or self.history[-1] != value):
            self.history.append(value)
        self._history_pos = None

    @_mutmut_mutated(mutants_xǁCommandInputǁ_on_key__mutmut)
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

    async def xǁCommandInputǁ_on_key__mutmut_orig(self, event: Key) -> None:
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

    async def xǁCommandInputǁ_on_key__mutmut_1(self, event: Key) -> None:
        if event.key == "up" and self.history or self._history_pos > 0:
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

    async def xǁCommandInputǁ_on_key__mutmut_2(self, event: Key) -> None:
        if event.key == "up" or self.history and self._history_pos > 0:
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

    async def xǁCommandInputǁ_on_key__mutmut_3(self, event: Key) -> None:
        if event.key != "up" and self.history and self._history_pos > 0:
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

    async def xǁCommandInputǁ_on_key__mutmut_4(self, event: Key) -> None:
        if event.key == "XXupXX" and self.history and self._history_pos > 0:
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

    async def xǁCommandInputǁ_on_key__mutmut_5(self, event: Key) -> None:
        if event.key == "UP" and self.history and self._history_pos > 0:
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

    async def xǁCommandInputǁ_on_key__mutmut_6(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos >= 0:
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

    async def xǁCommandInputǁ_on_key__mutmut_7(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 1:
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

    async def xǁCommandInputǁ_on_key__mutmut_8(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos = 1
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

    async def xǁCommandInputǁ_on_key__mutmut_9(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos += 1
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

    async def xǁCommandInputǁ_on_key__mutmut_10(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos -= 2
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

    async def xǁCommandInputǁ_on_key__mutmut_11(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos -= 1
            self.value = None
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

    async def xǁCommandInputǁ_on_key__mutmut_12(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos -= 1
            self.value = self.history[self._history_pos]
            self.cursor_position = None
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

    async def xǁCommandInputǁ_on_key__mutmut_13(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos -= 1
            self.value = self.history[self._history_pos]
            self.cursor_position = len(self.value)
            event.stop()
        elif event.key == "down" or self.history:
            self._history_pos = min(self._history_pos + 1, len(self.history))
            self.value = (
                self.history[self._history_pos] if self._history_pos < len(self.history) else ""
            )
            self.cursor_position = len(self.value)
            event.stop()
        else:
            await super()._on_key(event)

    async def xǁCommandInputǁ_on_key__mutmut_14(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos -= 1
            self.value = self.history[self._history_pos]
            self.cursor_position = len(self.value)
            event.stop()
        elif event.key != "down" and self.history:
            self._history_pos = min(self._history_pos + 1, len(self.history))
            self.value = (
                self.history[self._history_pos] if self._history_pos < len(self.history) else ""
            )
            self.cursor_position = len(self.value)
            event.stop()
        else:
            await super()._on_key(event)

    async def xǁCommandInputǁ_on_key__mutmut_15(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos -= 1
            self.value = self.history[self._history_pos]
            self.cursor_position = len(self.value)
            event.stop()
        elif event.key == "XXdownXX" and self.history:
            self._history_pos = min(self._history_pos + 1, len(self.history))
            self.value = (
                self.history[self._history_pos] if self._history_pos < len(self.history) else ""
            )
            self.cursor_position = len(self.value)
            event.stop()
        else:
            await super()._on_key(event)

    async def xǁCommandInputǁ_on_key__mutmut_16(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos -= 1
            self.value = self.history[self._history_pos]
            self.cursor_position = len(self.value)
            event.stop()
        elif event.key == "DOWN" and self.history:
            self._history_pos = min(self._history_pos + 1, len(self.history))
            self.value = (
                self.history[self._history_pos] if self._history_pos < len(self.history) else ""
            )
            self.cursor_position = len(self.value)
            event.stop()
        else:
            await super()._on_key(event)

    async def xǁCommandInputǁ_on_key__mutmut_17(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos -= 1
            self.value = self.history[self._history_pos]
            self.cursor_position = len(self.value)
            event.stop()
        elif event.key == "down" and self.history:
            self._history_pos = None
            self.value = (
                self.history[self._history_pos] if self._history_pos < len(self.history) else ""
            )
            self.cursor_position = len(self.value)
            event.stop()
        else:
            await super()._on_key(event)

    async def xǁCommandInputǁ_on_key__mutmut_18(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos -= 1
            self.value = self.history[self._history_pos]
            self.cursor_position = len(self.value)
            event.stop()
        elif event.key == "down" and self.history:
            self._history_pos = min(None, len(self.history))
            self.value = (
                self.history[self._history_pos] if self._history_pos < len(self.history) else ""
            )
            self.cursor_position = len(self.value)
            event.stop()
        else:
            await super()._on_key(event)

    async def xǁCommandInputǁ_on_key__mutmut_19(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos -= 1
            self.value = self.history[self._history_pos]
            self.cursor_position = len(self.value)
            event.stop()
        elif event.key == "down" and self.history:
            self._history_pos = min(self._history_pos + 1, None)
            self.value = (
                self.history[self._history_pos] if self._history_pos < len(self.history) else ""
            )
            self.cursor_position = len(self.value)
            event.stop()
        else:
            await super()._on_key(event)

    async def xǁCommandInputǁ_on_key__mutmut_20(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos -= 1
            self.value = self.history[self._history_pos]
            self.cursor_position = len(self.value)
            event.stop()
        elif event.key == "down" and self.history:
            self._history_pos = min(len(self.history))
            self.value = (
                self.history[self._history_pos] if self._history_pos < len(self.history) else ""
            )
            self.cursor_position = len(self.value)
            event.stop()
        else:
            await super()._on_key(event)

    async def xǁCommandInputǁ_on_key__mutmut_21(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos -= 1
            self.value = self.history[self._history_pos]
            self.cursor_position = len(self.value)
            event.stop()
        elif event.key == "down" and self.history:
            self._history_pos = min(self._history_pos + 1, )
            self.value = (
                self.history[self._history_pos] if self._history_pos < len(self.history) else ""
            )
            self.cursor_position = len(self.value)
            event.stop()
        else:
            await super()._on_key(event)

    async def xǁCommandInputǁ_on_key__mutmut_22(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos -= 1
            self.value = self.history[self._history_pos]
            self.cursor_position = len(self.value)
            event.stop()
        elif event.key == "down" and self.history:
            self._history_pos = min(self._history_pos - 1, len(self.history))
            self.value = (
                self.history[self._history_pos] if self._history_pos < len(self.history) else ""
            )
            self.cursor_position = len(self.value)
            event.stop()
        else:
            await super()._on_key(event)

    async def xǁCommandInputǁ_on_key__mutmut_23(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos -= 1
            self.value = self.history[self._history_pos]
            self.cursor_position = len(self.value)
            event.stop()
        elif event.key == "down" and self.history:
            self._history_pos = min(self._history_pos + 2, len(self.history))
            self.value = (
                self.history[self._history_pos] if self._history_pos < len(self.history) else ""
            )
            self.cursor_position = len(self.value)
            event.stop()
        else:
            await super()._on_key(event)

    async def xǁCommandInputǁ_on_key__mutmut_24(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos -= 1
            self.value = self.history[self._history_pos]
            self.cursor_position = len(self.value)
            event.stop()
        elif event.key == "down" and self.history:
            self._history_pos = min(self._history_pos + 1, len(self.history))
            self.value = None
            self.cursor_position = len(self.value)
            event.stop()
        else:
            await super()._on_key(event)

    async def xǁCommandInputǁ_on_key__mutmut_25(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos -= 1
            self.value = self.history[self._history_pos]
            self.cursor_position = len(self.value)
            event.stop()
        elif event.key == "down" and self.history:
            self._history_pos = min(self._history_pos + 1, len(self.history))
            self.value = (
                self.history[self._history_pos] if self._history_pos <= len(self.history) else ""
            )
            self.cursor_position = len(self.value)
            event.stop()
        else:
            await super()._on_key(event)

    async def xǁCommandInputǁ_on_key__mutmut_26(self, event: Key) -> None:
        if event.key == "up" and self.history and self._history_pos > 0:
            self._history_pos -= 1
            self.value = self.history[self._history_pos]
            self.cursor_position = len(self.value)
            event.stop()
        elif event.key == "down" and self.history:
            self._history_pos = min(self._history_pos + 1, len(self.history))
            self.value = (
                self.history[self._history_pos] if self._history_pos < len(self.history) else "XXXX"
            )
            self.cursor_position = len(self.value)
            event.stop()
        else:
            await super()._on_key(event)

    async def xǁCommandInputǁ_on_key__mutmut_27(self, event: Key) -> None:
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
            self.cursor_position = None
            event.stop()
        else:
            await super()._on_key(event)

    async def xǁCommandInputǁ_on_key__mutmut_28(self, event: Key) -> None:
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
            await super()._on_key(None)

mutants_xǁCommandInputǁ__init____mutmut['_mutmut_orig'] = CommandInput.xǁCommandInputǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCommandInputǁ__init____mutmut['xǁCommandInputǁ__init____mutmut_1'] = CommandInput.xǁCommandInputǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ__init____mutmut['xǁCommandInputǁ__init____mutmut_2'] = CommandInput.xǁCommandInputǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ__init____mutmut['xǁCommandInputǁ__init____mutmut_3'] = CommandInput.xǁCommandInputǁ__init____mutmut_3 # type: ignore # mutmut generated

mutants_xǁCommandInputǁremember__mutmut['_mutmut_orig'] = CommandInput.xǁCommandInputǁremember__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCommandInputǁremember__mutmut['xǁCommandInputǁremember__mutmut_1'] = CommandInput.xǁCommandInputǁremember__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCommandInputǁremember__mutmut['xǁCommandInputǁremember__mutmut_2'] = CommandInput.xǁCommandInputǁremember__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCommandInputǁremember__mutmut['xǁCommandInputǁremember__mutmut_3'] = CommandInput.xǁCommandInputǁremember__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCommandInputǁremember__mutmut['xǁCommandInputǁremember__mutmut_4'] = CommandInput.xǁCommandInputǁremember__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCommandInputǁremember__mutmut['xǁCommandInputǁremember__mutmut_5'] = CommandInput.xǁCommandInputǁremember__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCommandInputǁremember__mutmut['xǁCommandInputǁremember__mutmut_6'] = CommandInput.xǁCommandInputǁremember__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCommandInputǁremember__mutmut['xǁCommandInputǁremember__mutmut_7'] = CommandInput.xǁCommandInputǁremember__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCommandInputǁremember__mutmut['xǁCommandInputǁremember__mutmut_8'] = CommandInput.xǁCommandInputǁremember__mutmut_8 # type: ignore # mutmut generated

mutants_xǁCommandInputǁ_on_key__mutmut['_mutmut_orig'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_1'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_2'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_3'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_4'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_5'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_6'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_7'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_8'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_9'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_10'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_11'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_12'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_13'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_14'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_15'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_16'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_17'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_18'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_19'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_20'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_21'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_22'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_23'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_24'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_25'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_26'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_26 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_27'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_27 # type: ignore # mutmut generated
mutants_xǁCommandInputǁ_on_key__mutmut['xǁCommandInputǁ_on_key__mutmut_28'] = CommandInput.xǁCommandInputǁ_on_key__mutmut_28 # type: ignore # mutmut generated
