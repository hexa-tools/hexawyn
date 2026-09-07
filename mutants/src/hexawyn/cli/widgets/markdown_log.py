"""MarkdownLog — Markdown widget that accepts RichLog-style write() calls.

RichLog renders Rich markup; MarkdownLog renders Markdown (colors, headers,
code) like opencode/claudecode. With Textual 8+, the content supports native
mouse text selection (click-drag) and Ctrl+C copies the selection.
"""

from __future__ import annotations

from rich.text import Text
from textual import events
from textual.selection import Selection
from textual.widgets import Markdown


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁMarkdownLogǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁMarkdownLogǁ_on_mouse_up__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMarkdownLogǁwrite__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMarkdownLogǁwrite_lines__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMarkdownLogǁwrite_code_block__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMarkdownLogǁ_strip_rich_markup__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMarkdownLogǁ_append_lines__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMarkdownLogǁ_append_text__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMarkdownLogǁ_refresh_markdown__mutmut: MutantDict = {}  # type: ignore


class MarkdownLog(Markdown):
    """Markdown widget that accumulates content via write() calls.

    Supports native mouse text selection (Textual 8+): when the mouse button
    is released after a drag selection, the selected text is copied to the
    clipboard and a notification is shown.
    """

    @_mutmut_mutated(mutants_xǁMarkdownLogǁ__init____mutmut)
    def __init__(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = True,
    ) -> None:
        super().__init__(
            markdown or "",
            name=name,
            id=id,
            classes=classes,
            open_links=open_links,
        )
        self._markdown = markdown or ""
        self._plain_parts: list[str] = []
        self._last_copied: str = ""

    def xǁMarkdownLogǁ__init____mutmut_orig(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = True,
    ) -> None:
        super().__init__(
            markdown or "",
            name=name,
            id=id,
            classes=classes,
            open_links=open_links,
        )
        self._markdown = markdown or ""
        self._plain_parts: list[str] = []
        self._last_copied: str = ""

    def xǁMarkdownLogǁ__init____mutmut_1(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = False,
    ) -> None:
        super().__init__(
            markdown or "",
            name=name,
            id=id,
            classes=classes,
            open_links=open_links,
        )
        self._markdown = markdown or ""
        self._plain_parts: list[str] = []
        self._last_copied: str = ""

    def xǁMarkdownLogǁ__init____mutmut_2(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = True,
    ) -> None:
        super().__init__(
            None,
            name=name,
            id=id,
            classes=classes,
            open_links=open_links,
        )
        self._markdown = markdown or ""
        self._plain_parts: list[str] = []
        self._last_copied: str = ""

    def xǁMarkdownLogǁ__init____mutmut_3(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = True,
    ) -> None:
        super().__init__(
            markdown or "",
            name=None,
            id=id,
            classes=classes,
            open_links=open_links,
        )
        self._markdown = markdown or ""
        self._plain_parts: list[str] = []
        self._last_copied: str = ""

    def xǁMarkdownLogǁ__init____mutmut_4(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = True,
    ) -> None:
        super().__init__(
            markdown or "",
            name=name,
            id=None,
            classes=classes,
            open_links=open_links,
        )
        self._markdown = markdown or ""
        self._plain_parts: list[str] = []
        self._last_copied: str = ""

    def xǁMarkdownLogǁ__init____mutmut_5(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = True,
    ) -> None:
        super().__init__(
            markdown or "",
            name=name,
            id=id,
            classes=None,
            open_links=open_links,
        )
        self._markdown = markdown or ""
        self._plain_parts: list[str] = []
        self._last_copied: str = ""

    def xǁMarkdownLogǁ__init____mutmut_6(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = True,
    ) -> None:
        super().__init__(
            markdown or "",
            name=name,
            id=id,
            classes=classes,
            open_links=None,
        )
        self._markdown = markdown or ""
        self._plain_parts: list[str] = []
        self._last_copied: str = ""

    def xǁMarkdownLogǁ__init____mutmut_7(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = True,
    ) -> None:
        super().__init__(
            name=name,
            id=id,
            classes=classes,
            open_links=open_links,
        )
        self._markdown = markdown or ""
        self._plain_parts: list[str] = []
        self._last_copied: str = ""

    def xǁMarkdownLogǁ__init____mutmut_8(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = True,
    ) -> None:
        super().__init__(
            markdown or "",
            id=id,
            classes=classes,
            open_links=open_links,
        )
        self._markdown = markdown or ""
        self._plain_parts: list[str] = []
        self._last_copied: str = ""

    def xǁMarkdownLogǁ__init____mutmut_9(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = True,
    ) -> None:
        super().__init__(
            markdown or "",
            name=name,
            classes=classes,
            open_links=open_links,
        )
        self._markdown = markdown or ""
        self._plain_parts: list[str] = []
        self._last_copied: str = ""

    def xǁMarkdownLogǁ__init____mutmut_10(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = True,
    ) -> None:
        super().__init__(
            markdown or "",
            name=name,
            id=id,
            open_links=open_links,
        )
        self._markdown = markdown or ""
        self._plain_parts: list[str] = []
        self._last_copied: str = ""

    def xǁMarkdownLogǁ__init____mutmut_11(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = True,
    ) -> None:
        super().__init__(
            markdown or "",
            name=name,
            id=id,
            classes=classes,
            )
        self._markdown = markdown or ""
        self._plain_parts: list[str] = []
        self._last_copied: str = ""

    def xǁMarkdownLogǁ__init____mutmut_12(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = True,
    ) -> None:
        super().__init__(
            markdown and "",
            name=name,
            id=id,
            classes=classes,
            open_links=open_links,
        )
        self._markdown = markdown or ""
        self._plain_parts: list[str] = []
        self._last_copied: str = ""

    def xǁMarkdownLogǁ__init____mutmut_13(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = True,
    ) -> None:
        super().__init__(
            markdown or "XXXX",
            name=name,
            id=id,
            classes=classes,
            open_links=open_links,
        )
        self._markdown = markdown or ""
        self._plain_parts: list[str] = []
        self._last_copied: str = ""

    def xǁMarkdownLogǁ__init____mutmut_14(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = True,
    ) -> None:
        super().__init__(
            markdown or "",
            name=name,
            id=id,
            classes=classes,
            open_links=open_links,
        )
        self._markdown = None
        self._plain_parts: list[str] = []
        self._last_copied: str = ""

    def xǁMarkdownLogǁ__init____mutmut_15(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = True,
    ) -> None:
        super().__init__(
            markdown or "",
            name=name,
            id=id,
            classes=classes,
            open_links=open_links,
        )
        self._markdown = markdown and ""
        self._plain_parts: list[str] = []
        self._last_copied: str = ""

    def xǁMarkdownLogǁ__init____mutmut_16(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = True,
    ) -> None:
        super().__init__(
            markdown or "",
            name=name,
            id=id,
            classes=classes,
            open_links=open_links,
        )
        self._markdown = markdown or "XXXX"
        self._plain_parts: list[str] = []
        self._last_copied: str = ""

    def xǁMarkdownLogǁ__init____mutmut_17(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = True,
    ) -> None:
        super().__init__(
            markdown or "",
            name=name,
            id=id,
            classes=classes,
            open_links=open_links,
        )
        self._markdown = markdown or ""
        self._plain_parts: list[str] = None
        self._last_copied: str = ""

    def xǁMarkdownLogǁ__init____mutmut_18(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = True,
    ) -> None:
        super().__init__(
            markdown or "",
            name=name,
            id=id,
            classes=classes,
            open_links=open_links,
        )
        self._markdown = markdown or ""
        self._plain_parts: list[str] = []
        self._last_copied: str = None

    def xǁMarkdownLogǁ__init____mutmut_19(  # noqa: PLR0913
        self,
        markdown: str | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        open_links: bool = True,
    ) -> None:
        super().__init__(
            markdown or "",
            name=name,
            id=id,
            classes=classes,
            open_links=open_links,
        )
        self._markdown = markdown or ""
        self._plain_parts: list[str] = []
        self._last_copied: str = "XXXX"

    @property
    def plain_text(self) -> str:
        """Plain-text buffer used for mouse selection."""
        return "\n".join(self._plain_parts)

    @_mutmut_mutated(mutants_xǁMarkdownLogǁ_on_mouse_up__mutmut)
    async def _on_mouse_up(self, event: events.MouseUp) -> None:
        await super()._on_mouse_up(event)
        self._copy_current_selection()

    async def xǁMarkdownLogǁ_on_mouse_up__mutmut_orig(self, event: events.MouseUp) -> None:
        await super()._on_mouse_up(event)
        self._copy_current_selection()

    async def xǁMarkdownLogǁ_on_mouse_up__mutmut_1(self, event: events.MouseUp) -> None:
        await super()._on_mouse_up(None)
        self._copy_current_selection()

    def selection_updated(self, selection: Selection | None) -> None:
        """Copy the selected text to the clipboard on mouse release."""
        self._copy_current_selection()

    @_mutmut_mutated(mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut)
    def _copy_current_selection(self) -> None:
        try:
            selected = self.screen.get_selected_text()
        except Exception:
            return
        if not selected:
            return
        if selected == self._last_copied:
            return
        self._last_copied = selected
        self._copy_to_clipboard(selected)
        self.notify("Copied to clipboard", title="Selection", timeout=2.0)

    def xǁMarkdownLogǁ_copy_current_selection__mutmut_orig(self) -> None:
        try:
            selected = self.screen.get_selected_text()
        except Exception:
            return
        if not selected:
            return
        if selected == self._last_copied:
            return
        self._last_copied = selected
        self._copy_to_clipboard(selected)
        self.notify("Copied to clipboard", title="Selection", timeout=2.0)

    def xǁMarkdownLogǁ_copy_current_selection__mutmut_1(self) -> None:
        try:
            selected = None
        except Exception:
            return
        if not selected:
            return
        if selected == self._last_copied:
            return
        self._last_copied = selected
        self._copy_to_clipboard(selected)
        self.notify("Copied to clipboard", title="Selection", timeout=2.0)

    def xǁMarkdownLogǁ_copy_current_selection__mutmut_2(self) -> None:
        try:
            selected = self.screen.get_selected_text()
        except Exception:
            return
        if selected:
            return
        if selected == self._last_copied:
            return
        self._last_copied = selected
        self._copy_to_clipboard(selected)
        self.notify("Copied to clipboard", title="Selection", timeout=2.0)

    def xǁMarkdownLogǁ_copy_current_selection__mutmut_3(self) -> None:
        try:
            selected = self.screen.get_selected_text()
        except Exception:
            return
        if not selected:
            return
        if selected != self._last_copied:
            return
        self._last_copied = selected
        self._copy_to_clipboard(selected)
        self.notify("Copied to clipboard", title="Selection", timeout=2.0)

    def xǁMarkdownLogǁ_copy_current_selection__mutmut_4(self) -> None:
        try:
            selected = self.screen.get_selected_text()
        except Exception:
            return
        if not selected:
            return
        if selected == self._last_copied:
            return
        self._last_copied = None
        self._copy_to_clipboard(selected)
        self.notify("Copied to clipboard", title="Selection", timeout=2.0)

    def xǁMarkdownLogǁ_copy_current_selection__mutmut_5(self) -> None:
        try:
            selected = self.screen.get_selected_text()
        except Exception:
            return
        if not selected:
            return
        if selected == self._last_copied:
            return
        self._last_copied = selected
        self._copy_to_clipboard(None)
        self.notify("Copied to clipboard", title="Selection", timeout=2.0)

    def xǁMarkdownLogǁ_copy_current_selection__mutmut_6(self) -> None:
        try:
            selected = self.screen.get_selected_text()
        except Exception:
            return
        if not selected:
            return
        if selected == self._last_copied:
            return
        self._last_copied = selected
        self._copy_to_clipboard(selected)
        self.notify(None, title="Selection", timeout=2.0)

    def xǁMarkdownLogǁ_copy_current_selection__mutmut_7(self) -> None:
        try:
            selected = self.screen.get_selected_text()
        except Exception:
            return
        if not selected:
            return
        if selected == self._last_copied:
            return
        self._last_copied = selected
        self._copy_to_clipboard(selected)
        self.notify("Copied to clipboard", title=None, timeout=2.0)

    def xǁMarkdownLogǁ_copy_current_selection__mutmut_8(self) -> None:
        try:
            selected = self.screen.get_selected_text()
        except Exception:
            return
        if not selected:
            return
        if selected == self._last_copied:
            return
        self._last_copied = selected
        self._copy_to_clipboard(selected)
        self.notify("Copied to clipboard", title="Selection", timeout=None)

    def xǁMarkdownLogǁ_copy_current_selection__mutmut_9(self) -> None:
        try:
            selected = self.screen.get_selected_text()
        except Exception:
            return
        if not selected:
            return
        if selected == self._last_copied:
            return
        self._last_copied = selected
        self._copy_to_clipboard(selected)
        self.notify(title="Selection", timeout=2.0)

    def xǁMarkdownLogǁ_copy_current_selection__mutmut_10(self) -> None:
        try:
            selected = self.screen.get_selected_text()
        except Exception:
            return
        if not selected:
            return
        if selected == self._last_copied:
            return
        self._last_copied = selected
        self._copy_to_clipboard(selected)
        self.notify("Copied to clipboard", timeout=2.0)

    def xǁMarkdownLogǁ_copy_current_selection__mutmut_11(self) -> None:
        try:
            selected = self.screen.get_selected_text()
        except Exception:
            return
        if not selected:
            return
        if selected == self._last_copied:
            return
        self._last_copied = selected
        self._copy_to_clipboard(selected)
        self.notify("Copied to clipboard", title="Selection", )

    def xǁMarkdownLogǁ_copy_current_selection__mutmut_12(self) -> None:
        try:
            selected = self.screen.get_selected_text()
        except Exception:
            return
        if not selected:
            return
        if selected == self._last_copied:
            return
        self._last_copied = selected
        self._copy_to_clipboard(selected)
        self.notify("XXCopied to clipboardXX", title="Selection", timeout=2.0)

    def xǁMarkdownLogǁ_copy_current_selection__mutmut_13(self) -> None:
        try:
            selected = self.screen.get_selected_text()
        except Exception:
            return
        if not selected:
            return
        if selected == self._last_copied:
            return
        self._last_copied = selected
        self._copy_to_clipboard(selected)
        self.notify("copied to clipboard", title="Selection", timeout=2.0)

    def xǁMarkdownLogǁ_copy_current_selection__mutmut_14(self) -> None:
        try:
            selected = self.screen.get_selected_text()
        except Exception:
            return
        if not selected:
            return
        if selected == self._last_copied:
            return
        self._last_copied = selected
        self._copy_to_clipboard(selected)
        self.notify("COPIED TO CLIPBOARD", title="Selection", timeout=2.0)

    def xǁMarkdownLogǁ_copy_current_selection__mutmut_15(self) -> None:
        try:
            selected = self.screen.get_selected_text()
        except Exception:
            return
        if not selected:
            return
        if selected == self._last_copied:
            return
        self._last_copied = selected
        self._copy_to_clipboard(selected)
        self.notify("Copied to clipboard", title="XXSelectionXX", timeout=2.0)

    def xǁMarkdownLogǁ_copy_current_selection__mutmut_16(self) -> None:
        try:
            selected = self.screen.get_selected_text()
        except Exception:
            return
        if not selected:
            return
        if selected == self._last_copied:
            return
        self._last_copied = selected
        self._copy_to_clipboard(selected)
        self.notify("Copied to clipboard", title="selection", timeout=2.0)

    def xǁMarkdownLogǁ_copy_current_selection__mutmut_17(self) -> None:
        try:
            selected = self.screen.get_selected_text()
        except Exception:
            return
        if not selected:
            return
        if selected == self._last_copied:
            return
        self._last_copied = selected
        self._copy_to_clipboard(selected)
        self.notify("Copied to clipboard", title="SELECTION", timeout=2.0)

    def xǁMarkdownLogǁ_copy_current_selection__mutmut_18(self) -> None:
        try:
            selected = self.screen.get_selected_text()
        except Exception:
            return
        if not selected:
            return
        if selected == self._last_copied:
            return
        self._last_copied = selected
        self._copy_to_clipboard(selected)
        self.notify("Copied to clipboard", title="Selection", timeout=3.0)

    @_mutmut_mutated(mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut)
    def _copy_to_clipboard(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_orig(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_1(self, text: str) -> None:
        import platform
        import subprocess

        system = None
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_2(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system != "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_3(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "XXDarwinXX":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_4(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_5(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "DARWIN":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_6(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(None, input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_7(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=None, check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_8(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=None)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_9(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_10(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_11(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), )
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_12(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["XXpbcopyXX"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_13(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["PBCOPY"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_14(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=False)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_15(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system != "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_16(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "XXLinuxXX":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_17(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_18(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "LINUX":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_19(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["XXwl-copyXX"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_20(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["WL-COPY"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_21(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["XXxclipXX", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_22(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["XCLIP", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_23(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "XX-selectionXX", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_24(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-SELECTION", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_25(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "XXcXX"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_26(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "C"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_27(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(None, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_28(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=None, check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_29(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=None)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_30(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_31(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_32(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), )
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_33(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=False)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        continue
        except Exception:
            pass

    def xǁMarkdownLogǁ_copy_to_clipboard__mutmut_34(self, text: str) -> None:
        import platform
        import subprocess

        system = platform.system()
        try:
            if system == "Darwin":
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif system == "Linux":
                for cmd in (["wl-copy"], ["xclip", "-selection", "c"]):
                    try:
                        subprocess.run(cmd, input=text.encode(), check=True)
                        return
                    except (FileNotFoundError, subprocess.CalledProcessError):
                        break
        except Exception:
            pass

    @_mutmut_mutated(mutants_xǁMarkdownLogǁwrite__mutmut)
    def write(self, renderable: object = "", expand: bool = False) -> None:  # noqa: ARG002
        """Append plain text, markdown, or a list of (text, style) tuples."""
        if isinstance(renderable, list):
            self._append_lines(renderable)
        elif isinstance(renderable, str):
            self._append_text(self._strip_rich_markup(renderable))
        elif renderable is not None:
            self._append_text(str(renderable))

    def xǁMarkdownLogǁwrite__mutmut_orig(self, renderable: object = "", expand: bool = False) -> None:  # noqa: ARG002
        """Append plain text, markdown, or a list of (text, style) tuples."""
        if isinstance(renderable, list):
            self._append_lines(renderable)
        elif isinstance(renderable, str):
            self._append_text(self._strip_rich_markup(renderable))
        elif renderable is not None:
            self._append_text(str(renderable))

    def xǁMarkdownLogǁwrite__mutmut_1(self, renderable: object = "XXXX", expand: bool = False) -> None:  # noqa: ARG002
        """Append plain text, markdown, or a list of (text, style) tuples."""
        if isinstance(renderable, list):
            self._append_lines(renderable)
        elif isinstance(renderable, str):
            self._append_text(self._strip_rich_markup(renderable))
        elif renderable is not None:
            self._append_text(str(renderable))

    def xǁMarkdownLogǁwrite__mutmut_2(self, renderable: object = "", expand: bool = True) -> None:  # noqa: ARG002
        """Append plain text, markdown, or a list of (text, style) tuples."""
        if isinstance(renderable, list):
            self._append_lines(renderable)
        elif isinstance(renderable, str):
            self._append_text(self._strip_rich_markup(renderable))
        elif renderable is not None:
            self._append_text(str(renderable))

    def xǁMarkdownLogǁwrite__mutmut_3(self, renderable: object = "", expand: bool = False) -> None:  # noqa: ARG002
        """Append plain text, markdown, or a list of (text, style) tuples."""
        if isinstance(renderable, list):
            self._append_lines(None)
        elif isinstance(renderable, str):
            self._append_text(self._strip_rich_markup(renderable))
        elif renderable is not None:
            self._append_text(str(renderable))

    def xǁMarkdownLogǁwrite__mutmut_4(self, renderable: object = "", expand: bool = False) -> None:  # noqa: ARG002
        """Append plain text, markdown, or a list of (text, style) tuples."""
        if isinstance(renderable, list):
            self._append_lines(renderable)
        elif isinstance(renderable, str):
            self._append_text(None)
        elif renderable is not None:
            self._append_text(str(renderable))

    def xǁMarkdownLogǁwrite__mutmut_5(self, renderable: object = "", expand: bool = False) -> None:  # noqa: ARG002
        """Append plain text, markdown, or a list of (text, style) tuples."""
        if isinstance(renderable, list):
            self._append_lines(renderable)
        elif isinstance(renderable, str):
            self._append_text(self._strip_rich_markup(None))
        elif renderable is not None:
            self._append_text(str(renderable))

    def xǁMarkdownLogǁwrite__mutmut_6(self, renderable: object = "", expand: bool = False) -> None:  # noqa: ARG002
        """Append plain text, markdown, or a list of (text, style) tuples."""
        if isinstance(renderable, list):
            self._append_lines(renderable)
        elif isinstance(renderable, str):
            self._append_text(self._strip_rich_markup(renderable))
        elif renderable is None:
            self._append_text(str(renderable))

    def xǁMarkdownLogǁwrite__mutmut_7(self, renderable: object = "", expand: bool = False) -> None:  # noqa: ARG002
        """Append plain text, markdown, or a list of (text, style) tuples."""
        if isinstance(renderable, list):
            self._append_lines(renderable)
        elif isinstance(renderable, str):
            self._append_text(self._strip_rich_markup(renderable))
        elif renderable is not None:
            self._append_text(None)

    def xǁMarkdownLogǁwrite__mutmut_8(self, renderable: object = "", expand: bool = False) -> None:  # noqa: ARG002
        """Append plain text, markdown, or a list of (text, style) tuples."""
        if isinstance(renderable, list):
            self._append_lines(renderable)
        elif isinstance(renderable, str):
            self._append_text(self._strip_rich_markup(renderable))
        elif renderable is not None:
            self._append_text(str(None))

    @_mutmut_mutated(mutants_xǁMarkdownLogǁwrite_lines__mutmut)
    def write_lines(self, lines: list[tuple[str, str]]) -> None:
        """Append a list of (text, style) tuples as plain text."""
        self._append_lines(lines)

    def xǁMarkdownLogǁwrite_lines__mutmut_orig(self, lines: list[tuple[str, str]]) -> None:
        """Append a list of (text, style) tuples as plain text."""
        self._append_lines(lines)

    def xǁMarkdownLogǁwrite_lines__mutmut_1(self, lines: list[tuple[str, str]]) -> None:
        """Append a list of (text, style) tuples as plain text."""
        self._append_lines(None)

    @_mutmut_mutated(mutants_xǁMarkdownLogǁwrite_code_block__mutmut)
    def write_code_block(self, text: str) -> None:
        """Append a fenced code block (monospace, not interpreted as markdown)."""
        stripped = self._strip_rich_markup(text)
        self._plain_parts.append("```text")
        self._plain_parts.append(stripped)
        self._plain_parts.append("```")
        self._refresh_markdown()

    def xǁMarkdownLogǁwrite_code_block__mutmut_orig(self, text: str) -> None:
        """Append a fenced code block (monospace, not interpreted as markdown)."""
        stripped = self._strip_rich_markup(text)
        self._plain_parts.append("```text")
        self._plain_parts.append(stripped)
        self._plain_parts.append("```")
        self._refresh_markdown()

    def xǁMarkdownLogǁwrite_code_block__mutmut_1(self, text: str) -> None:
        """Append a fenced code block (monospace, not interpreted as markdown)."""
        stripped = None
        self._plain_parts.append("```text")
        self._plain_parts.append(stripped)
        self._plain_parts.append("```")
        self._refresh_markdown()

    def xǁMarkdownLogǁwrite_code_block__mutmut_2(self, text: str) -> None:
        """Append a fenced code block (monospace, not interpreted as markdown)."""
        stripped = self._strip_rich_markup(None)
        self._plain_parts.append("```text")
        self._plain_parts.append(stripped)
        self._plain_parts.append("```")
        self._refresh_markdown()

    def xǁMarkdownLogǁwrite_code_block__mutmut_3(self, text: str) -> None:
        """Append a fenced code block (monospace, not interpreted as markdown)."""
        stripped = self._strip_rich_markup(text)
        self._plain_parts.append(None)
        self._plain_parts.append(stripped)
        self._plain_parts.append("```")
        self._refresh_markdown()

    def xǁMarkdownLogǁwrite_code_block__mutmut_4(self, text: str) -> None:
        """Append a fenced code block (monospace, not interpreted as markdown)."""
        stripped = self._strip_rich_markup(text)
        self._plain_parts.append("XX```textXX")
        self._plain_parts.append(stripped)
        self._plain_parts.append("```")
        self._refresh_markdown()

    def xǁMarkdownLogǁwrite_code_block__mutmut_5(self, text: str) -> None:
        """Append a fenced code block (monospace, not interpreted as markdown)."""
        stripped = self._strip_rich_markup(text)
        self._plain_parts.append("```TEXT")
        self._plain_parts.append(stripped)
        self._plain_parts.append("```")
        self._refresh_markdown()

    def xǁMarkdownLogǁwrite_code_block__mutmut_6(self, text: str) -> None:
        """Append a fenced code block (monospace, not interpreted as markdown)."""
        stripped = self._strip_rich_markup(text)
        self._plain_parts.append("```text")
        self._plain_parts.append(None)
        self._plain_parts.append("```")
        self._refresh_markdown()

    def xǁMarkdownLogǁwrite_code_block__mutmut_7(self, text: str) -> None:
        """Append a fenced code block (monospace, not interpreted as markdown)."""
        stripped = self._strip_rich_markup(text)
        self._plain_parts.append("```text")
        self._plain_parts.append(stripped)
        self._plain_parts.append(None)
        self._refresh_markdown()

    def xǁMarkdownLogǁwrite_code_block__mutmut_8(self, text: str) -> None:
        """Append a fenced code block (monospace, not interpreted as markdown)."""
        stripped = self._strip_rich_markup(text)
        self._plain_parts.append("```text")
        self._plain_parts.append(stripped)
        self._plain_parts.append("XX```XX")
        self._refresh_markdown()

    @staticmethod
    @_mutmut_mutated(mutants_xǁMarkdownLogǁ_strip_rich_markup__mutmut)
    def _strip_rich_markup(text: str) -> str:
        """Convert Rich markup tags to plain text."""
        try:
            return Text.from_markup(text).plain
        except Exception:
            return text

    @staticmethod
    def xǁMarkdownLogǁ_strip_rich_markup__mutmut_orig(text: str) -> str:
        """Convert Rich markup tags to plain text."""
        try:
            return Text.from_markup(text).plain
        except Exception:
            return text

    @staticmethod
    def xǁMarkdownLogǁ_strip_rich_markup__mutmut_1(text: str) -> str:
        """Convert Rich markup tags to plain text."""
        try:
            return Text.from_markup(None).plain
        except Exception:
            return text

    @_mutmut_mutated(mutants_xǁMarkdownLogǁ_append_lines__mutmut)
    def _append_lines(self, lines: list[tuple[str, str]]) -> None:
        for text, _style in lines:
            if text:
                self._plain_parts.append(text)
        self._refresh_markdown()

    def xǁMarkdownLogǁ_append_lines__mutmut_orig(self, lines: list[tuple[str, str]]) -> None:
        for text, _style in lines:
            if text:
                self._plain_parts.append(text)
        self._refresh_markdown()

    def xǁMarkdownLogǁ_append_lines__mutmut_1(self, lines: list[tuple[str, str]]) -> None:
        for text, _style in lines:
            if text:
                self._plain_parts.append(None)
        self._refresh_markdown()

    @_mutmut_mutated(mutants_xǁMarkdownLogǁ_append_text__mutmut)
    def _append_text(self, text: str) -> None:
        if not text:
            return
        self._plain_parts.append(text)
        self._refresh_markdown()

    def xǁMarkdownLogǁ_append_text__mutmut_orig(self, text: str) -> None:
        if not text:
            return
        self._plain_parts.append(text)
        self._refresh_markdown()

    def xǁMarkdownLogǁ_append_text__mutmut_1(self, text: str) -> None:
        if text:
            return
        self._plain_parts.append(text)
        self._refresh_markdown()

    def xǁMarkdownLogǁ_append_text__mutmut_2(self, text: str) -> None:
        if not text:
            return
        self._plain_parts.append(None)
        self._refresh_markdown()

    @_mutmut_mutated(mutants_xǁMarkdownLogǁ_refresh_markdown__mutmut)
    def _refresh_markdown(self) -> None:
        new_markdown = "\n".join(self._plain_parts)
        if new_markdown != self._markdown:
            self._markdown = new_markdown
            try:
                self.update(new_markdown)
            except RuntimeError:
                pass

    def xǁMarkdownLogǁ_refresh_markdown__mutmut_orig(self) -> None:
        new_markdown = "\n".join(self._plain_parts)
        if new_markdown != self._markdown:
            self._markdown = new_markdown
            try:
                self.update(new_markdown)
            except RuntimeError:
                pass

    def xǁMarkdownLogǁ_refresh_markdown__mutmut_1(self) -> None:
        new_markdown = None
        if new_markdown != self._markdown:
            self._markdown = new_markdown
            try:
                self.update(new_markdown)
            except RuntimeError:
                pass

    def xǁMarkdownLogǁ_refresh_markdown__mutmut_2(self) -> None:
        new_markdown = "\n".join(None)
        if new_markdown != self._markdown:
            self._markdown = new_markdown
            try:
                self.update(new_markdown)
            except RuntimeError:
                pass

    def xǁMarkdownLogǁ_refresh_markdown__mutmut_3(self) -> None:
        new_markdown = "XX\nXX".join(self._plain_parts)
        if new_markdown != self._markdown:
            self._markdown = new_markdown
            try:
                self.update(new_markdown)
            except RuntimeError:
                pass

    def xǁMarkdownLogǁ_refresh_markdown__mutmut_4(self) -> None:
        new_markdown = "\n".join(self._plain_parts)
        if new_markdown == self._markdown:
            self._markdown = new_markdown
            try:
                self.update(new_markdown)
            except RuntimeError:
                pass

    def xǁMarkdownLogǁ_refresh_markdown__mutmut_5(self) -> None:
        new_markdown = "\n".join(self._plain_parts)
        if new_markdown != self._markdown:
            self._markdown = None
            try:
                self.update(new_markdown)
            except RuntimeError:
                pass

    def xǁMarkdownLogǁ_refresh_markdown__mutmut_6(self) -> None:
        new_markdown = "\n".join(self._plain_parts)
        if new_markdown != self._markdown:
            self._markdown = new_markdown
            try:
                self.update(None)
            except RuntimeError:
                pass

mutants_xǁMarkdownLogǁ__init____mutmut['_mutmut_orig'] = MarkdownLog.xǁMarkdownLogǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ__init____mutmut['xǁMarkdownLogǁ__init____mutmut_1'] = MarkdownLog.xǁMarkdownLogǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ__init____mutmut['xǁMarkdownLogǁ__init____mutmut_2'] = MarkdownLog.xǁMarkdownLogǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ__init____mutmut['xǁMarkdownLogǁ__init____mutmut_3'] = MarkdownLog.xǁMarkdownLogǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ__init____mutmut['xǁMarkdownLogǁ__init____mutmut_4'] = MarkdownLog.xǁMarkdownLogǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ__init____mutmut['xǁMarkdownLogǁ__init____mutmut_5'] = MarkdownLog.xǁMarkdownLogǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ__init____mutmut['xǁMarkdownLogǁ__init____mutmut_6'] = MarkdownLog.xǁMarkdownLogǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ__init____mutmut['xǁMarkdownLogǁ__init____mutmut_7'] = MarkdownLog.xǁMarkdownLogǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ__init____mutmut['xǁMarkdownLogǁ__init____mutmut_8'] = MarkdownLog.xǁMarkdownLogǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ__init____mutmut['xǁMarkdownLogǁ__init____mutmut_9'] = MarkdownLog.xǁMarkdownLogǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ__init____mutmut['xǁMarkdownLogǁ__init____mutmut_10'] = MarkdownLog.xǁMarkdownLogǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ__init____mutmut['xǁMarkdownLogǁ__init____mutmut_11'] = MarkdownLog.xǁMarkdownLogǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ__init____mutmut['xǁMarkdownLogǁ__init____mutmut_12'] = MarkdownLog.xǁMarkdownLogǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ__init____mutmut['xǁMarkdownLogǁ__init____mutmut_13'] = MarkdownLog.xǁMarkdownLogǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ__init____mutmut['xǁMarkdownLogǁ__init____mutmut_14'] = MarkdownLog.xǁMarkdownLogǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ__init____mutmut['xǁMarkdownLogǁ__init____mutmut_15'] = MarkdownLog.xǁMarkdownLogǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ__init____mutmut['xǁMarkdownLogǁ__init____mutmut_16'] = MarkdownLog.xǁMarkdownLogǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ__init____mutmut['xǁMarkdownLogǁ__init____mutmut_17'] = MarkdownLog.xǁMarkdownLogǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ__init____mutmut['xǁMarkdownLogǁ__init____mutmut_18'] = MarkdownLog.xǁMarkdownLogǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ__init____mutmut['xǁMarkdownLogǁ__init____mutmut_19'] = MarkdownLog.xǁMarkdownLogǁ__init____mutmut_19 # type: ignore # mutmut generated

mutants_xǁMarkdownLogǁ_on_mouse_up__mutmut['_mutmut_orig'] = MarkdownLog.xǁMarkdownLogǁ_on_mouse_up__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_on_mouse_up__mutmut['xǁMarkdownLogǁ_on_mouse_up__mutmut_1'] = MarkdownLog.xǁMarkdownLogǁ_on_mouse_up__mutmut_1 # type: ignore # mutmut generated

mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut['_mutmut_orig'] = MarkdownLog.xǁMarkdownLogǁ_copy_current_selection__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut['xǁMarkdownLogǁ_copy_current_selection__mutmut_1'] = MarkdownLog.xǁMarkdownLogǁ_copy_current_selection__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut['xǁMarkdownLogǁ_copy_current_selection__mutmut_2'] = MarkdownLog.xǁMarkdownLogǁ_copy_current_selection__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut['xǁMarkdownLogǁ_copy_current_selection__mutmut_3'] = MarkdownLog.xǁMarkdownLogǁ_copy_current_selection__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut['xǁMarkdownLogǁ_copy_current_selection__mutmut_4'] = MarkdownLog.xǁMarkdownLogǁ_copy_current_selection__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut['xǁMarkdownLogǁ_copy_current_selection__mutmut_5'] = MarkdownLog.xǁMarkdownLogǁ_copy_current_selection__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut['xǁMarkdownLogǁ_copy_current_selection__mutmut_6'] = MarkdownLog.xǁMarkdownLogǁ_copy_current_selection__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut['xǁMarkdownLogǁ_copy_current_selection__mutmut_7'] = MarkdownLog.xǁMarkdownLogǁ_copy_current_selection__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut['xǁMarkdownLogǁ_copy_current_selection__mutmut_8'] = MarkdownLog.xǁMarkdownLogǁ_copy_current_selection__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut['xǁMarkdownLogǁ_copy_current_selection__mutmut_9'] = MarkdownLog.xǁMarkdownLogǁ_copy_current_selection__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut['xǁMarkdownLogǁ_copy_current_selection__mutmut_10'] = MarkdownLog.xǁMarkdownLogǁ_copy_current_selection__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut['xǁMarkdownLogǁ_copy_current_selection__mutmut_11'] = MarkdownLog.xǁMarkdownLogǁ_copy_current_selection__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut['xǁMarkdownLogǁ_copy_current_selection__mutmut_12'] = MarkdownLog.xǁMarkdownLogǁ_copy_current_selection__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut['xǁMarkdownLogǁ_copy_current_selection__mutmut_13'] = MarkdownLog.xǁMarkdownLogǁ_copy_current_selection__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut['xǁMarkdownLogǁ_copy_current_selection__mutmut_14'] = MarkdownLog.xǁMarkdownLogǁ_copy_current_selection__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut['xǁMarkdownLogǁ_copy_current_selection__mutmut_15'] = MarkdownLog.xǁMarkdownLogǁ_copy_current_selection__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut['xǁMarkdownLogǁ_copy_current_selection__mutmut_16'] = MarkdownLog.xǁMarkdownLogǁ_copy_current_selection__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut['xǁMarkdownLogǁ_copy_current_selection__mutmut_17'] = MarkdownLog.xǁMarkdownLogǁ_copy_current_selection__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_current_selection__mutmut['xǁMarkdownLogǁ_copy_current_selection__mutmut_18'] = MarkdownLog.xǁMarkdownLogǁ_copy_current_selection__mutmut_18 # type: ignore # mutmut generated

mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['_mutmut_orig'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_1'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_2'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_3'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_4'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_5'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_6'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_7'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_8'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_9'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_10'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_11'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_12'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_13'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_14'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_15'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_16'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_17'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_18'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_19'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_20'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_21'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_21 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_22'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_22 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_23'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_23 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_24'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_24 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_25'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_25 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_26'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_26 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_27'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_27 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_28'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_28 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_29'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_29 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_30'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_30 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_31'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_31 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_32'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_32 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_33'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_33 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_copy_to_clipboard__mutmut['xǁMarkdownLogǁ_copy_to_clipboard__mutmut_34'] = MarkdownLog.xǁMarkdownLogǁ_copy_to_clipboard__mutmut_34 # type: ignore # mutmut generated

mutants_xǁMarkdownLogǁwrite__mutmut['_mutmut_orig'] = MarkdownLog.xǁMarkdownLogǁwrite__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁwrite__mutmut['xǁMarkdownLogǁwrite__mutmut_1'] = MarkdownLog.xǁMarkdownLogǁwrite__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁwrite__mutmut['xǁMarkdownLogǁwrite__mutmut_2'] = MarkdownLog.xǁMarkdownLogǁwrite__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁwrite__mutmut['xǁMarkdownLogǁwrite__mutmut_3'] = MarkdownLog.xǁMarkdownLogǁwrite__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁwrite__mutmut['xǁMarkdownLogǁwrite__mutmut_4'] = MarkdownLog.xǁMarkdownLogǁwrite__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁwrite__mutmut['xǁMarkdownLogǁwrite__mutmut_5'] = MarkdownLog.xǁMarkdownLogǁwrite__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁwrite__mutmut['xǁMarkdownLogǁwrite__mutmut_6'] = MarkdownLog.xǁMarkdownLogǁwrite__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁwrite__mutmut['xǁMarkdownLogǁwrite__mutmut_7'] = MarkdownLog.xǁMarkdownLogǁwrite__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁwrite__mutmut['xǁMarkdownLogǁwrite__mutmut_8'] = MarkdownLog.xǁMarkdownLogǁwrite__mutmut_8 # type: ignore # mutmut generated

mutants_xǁMarkdownLogǁwrite_lines__mutmut['_mutmut_orig'] = MarkdownLog.xǁMarkdownLogǁwrite_lines__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁwrite_lines__mutmut['xǁMarkdownLogǁwrite_lines__mutmut_1'] = MarkdownLog.xǁMarkdownLogǁwrite_lines__mutmut_1 # type: ignore # mutmut generated

mutants_xǁMarkdownLogǁwrite_code_block__mutmut['_mutmut_orig'] = MarkdownLog.xǁMarkdownLogǁwrite_code_block__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁwrite_code_block__mutmut['xǁMarkdownLogǁwrite_code_block__mutmut_1'] = MarkdownLog.xǁMarkdownLogǁwrite_code_block__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁwrite_code_block__mutmut['xǁMarkdownLogǁwrite_code_block__mutmut_2'] = MarkdownLog.xǁMarkdownLogǁwrite_code_block__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁwrite_code_block__mutmut['xǁMarkdownLogǁwrite_code_block__mutmut_3'] = MarkdownLog.xǁMarkdownLogǁwrite_code_block__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁwrite_code_block__mutmut['xǁMarkdownLogǁwrite_code_block__mutmut_4'] = MarkdownLog.xǁMarkdownLogǁwrite_code_block__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁwrite_code_block__mutmut['xǁMarkdownLogǁwrite_code_block__mutmut_5'] = MarkdownLog.xǁMarkdownLogǁwrite_code_block__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁwrite_code_block__mutmut['xǁMarkdownLogǁwrite_code_block__mutmut_6'] = MarkdownLog.xǁMarkdownLogǁwrite_code_block__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁwrite_code_block__mutmut['xǁMarkdownLogǁwrite_code_block__mutmut_7'] = MarkdownLog.xǁMarkdownLogǁwrite_code_block__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁwrite_code_block__mutmut['xǁMarkdownLogǁwrite_code_block__mutmut_8'] = MarkdownLog.xǁMarkdownLogǁwrite_code_block__mutmut_8 # type: ignore # mutmut generated

mutants_xǁMarkdownLogǁ_strip_rich_markup__mutmut['_mutmut_orig'] = MarkdownLog.xǁMarkdownLogǁ_strip_rich_markup__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_strip_rich_markup__mutmut['xǁMarkdownLogǁ_strip_rich_markup__mutmut_1'] = MarkdownLog.xǁMarkdownLogǁ_strip_rich_markup__mutmut_1 # type: ignore # mutmut generated

mutants_xǁMarkdownLogǁ_append_lines__mutmut['_mutmut_orig'] = MarkdownLog.xǁMarkdownLogǁ_append_lines__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_append_lines__mutmut['xǁMarkdownLogǁ_append_lines__mutmut_1'] = MarkdownLog.xǁMarkdownLogǁ_append_lines__mutmut_1 # type: ignore # mutmut generated

mutants_xǁMarkdownLogǁ_append_text__mutmut['_mutmut_orig'] = MarkdownLog.xǁMarkdownLogǁ_append_text__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_append_text__mutmut['xǁMarkdownLogǁ_append_text__mutmut_1'] = MarkdownLog.xǁMarkdownLogǁ_append_text__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_append_text__mutmut['xǁMarkdownLogǁ_append_text__mutmut_2'] = MarkdownLog.xǁMarkdownLogǁ_append_text__mutmut_2 # type: ignore # mutmut generated

mutants_xǁMarkdownLogǁ_refresh_markdown__mutmut['_mutmut_orig'] = MarkdownLog.xǁMarkdownLogǁ_refresh_markdown__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_refresh_markdown__mutmut['xǁMarkdownLogǁ_refresh_markdown__mutmut_1'] = MarkdownLog.xǁMarkdownLogǁ_refresh_markdown__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_refresh_markdown__mutmut['xǁMarkdownLogǁ_refresh_markdown__mutmut_2'] = MarkdownLog.xǁMarkdownLogǁ_refresh_markdown__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_refresh_markdown__mutmut['xǁMarkdownLogǁ_refresh_markdown__mutmut_3'] = MarkdownLog.xǁMarkdownLogǁ_refresh_markdown__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_refresh_markdown__mutmut['xǁMarkdownLogǁ_refresh_markdown__mutmut_4'] = MarkdownLog.xǁMarkdownLogǁ_refresh_markdown__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_refresh_markdown__mutmut['xǁMarkdownLogǁ_refresh_markdown__mutmut_5'] = MarkdownLog.xǁMarkdownLogǁ_refresh_markdown__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMarkdownLogǁ_refresh_markdown__mutmut['xǁMarkdownLogǁ_refresh_markdown__mutmut_6'] = MarkdownLog.xǁMarkdownLogǁ_refresh_markdown__mutmut_6 # type: ignore # mutmut generated
