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


class MarkdownLog(Markdown):
    """Markdown widget that accumulates content via write() calls.

    Supports native mouse text selection (Textual 8+): when the mouse button
    is released after a drag selection, the selected text is copied to the
    clipboard and a notification is shown.
    """

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

    @property
    def plain_text(self) -> str:
        """Plain-text buffer used for mouse selection."""
        return "\n".join(self._plain_parts)

    async def _on_mouse_up(self, event: events.MouseUp) -> None:
        await super()._on_mouse_up(event)
        self._copy_current_selection()

    def selection_updated(self, selection: Selection | None) -> None:
        """Copy the selected text to the clipboard on mouse release."""
        self._copy_current_selection()

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

    def write(self, renderable: object = "", expand: bool = False) -> None:  # noqa: ARG002
        """Append plain text, markdown, or a list of (text, style) tuples."""
        if isinstance(renderable, list):
            self._append_lines(renderable)
        elif isinstance(renderable, str):
            self._append_text(self._strip_rich_markup(renderable))
        elif renderable is not None:
            self._append_text(str(renderable))

    def write_lines(self, lines: list[tuple[str, str]]) -> None:
        """Append a list of (text, style) tuples as plain text."""
        self._append_lines(lines)

    def write_code_block(self, text: str) -> None:
        """Append a fenced code block (monospace, not interpreted as markdown)."""
        stripped = self._strip_rich_markup(text)
        self._plain_parts.append("```text")
        self._plain_parts.append(stripped)
        self._plain_parts.append("```")
        self._refresh_markdown()

    @staticmethod
    def _strip_rich_markup(text: str) -> str:
        """Convert Rich markup tags to plain text."""
        try:
            return Text.from_markup(text).plain
        except Exception:
            return text

    def _append_lines(self, lines: list[tuple[str, str]]) -> None:
        for text, _style in lines:
            if text:
                self._plain_parts.append(text)
        self._refresh_markdown()

    def _append_text(self, text: str) -> None:
        if not text:
            return
        self._plain_parts.append(text)
        self._refresh_markdown()

    def _refresh_markdown(self) -> None:
        new_markdown = "\n".join(self._plain_parts)
        if new_markdown != self._markdown:
            self._markdown = new_markdown
            try:
                self.update(new_markdown)
            except RuntimeError:
                pass
