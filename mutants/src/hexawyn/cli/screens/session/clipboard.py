"""Clipboard and export helpers for the session screen.

Platform-specific subprocess calls (pbcopy / wl-copy / xclip / open / xdg-open)
live here so the Textual screen stays focused on rendering and delegation and
the helpers stay unit-testable by mocking `platform` / `subprocess`.
"""

from __future__ import annotations

import platform
import subprocess
import tempfile

_COPIED = "✓ Copied to clipboard"
_SYSTEM_MISSING = "✗ Install xclip or wl-clipboard to enable copy"
_FAILED = "✗ Copy failed: {exc}"
_UNSUPPORTED = "✗ Copy not supported on {system}"

_MAC_COPY = ["pbcopy"]
_LINUX_COPY_TOOLS = (["wl-copy"], ["xclip", "-selection", "c"])


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_copy_to_clipboard__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_copy_to_clipboard__mutmut)
def copy_to_clipboard(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_orig(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_1(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = None
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_2(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system != "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_3(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "XXDarwinXX":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_4(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_5(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "DARWIN":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_6(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(None, input=text.encode(), check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_7(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=None, check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_8(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=None)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_9(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(input=text.encode(), check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_10(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_11(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), )
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_12(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=False)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_13(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system != "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_14(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "XXLinuxXX":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_15(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_16(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "LINUX":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_17(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(None, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_18(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=None, check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_19(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=None)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_20(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_21(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_22(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), )
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_23(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=False)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_24(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    break
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_25(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=None)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=exc)


def x_copy_to_clipboard__mutmut_26(text: str) -> str:
    """Copy ``text`` to the system clipboard and return a message string."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run(_MAC_COPY, input=text.encode(), check=True)
            return _COPIED
        if system == "Linux":
            for cmd in _LINUX_COPY_TOOLS:
                try:
                    subprocess.run(cmd, input=text.encode(), check=True)
                    return _COPIED
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            return _SYSTEM_MISSING
        return _UNSUPPORTED.format(system=system)
    except Exception as exc:  # noqa: BLE001 - never surface a clipboard failure
        return _FAILED.format(exc=None)

mutants_x_copy_to_clipboard__mutmut['_mutmut_orig'] = x_copy_to_clipboard__mutmut_orig # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_1'] = x_copy_to_clipboard__mutmut_1 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_2'] = x_copy_to_clipboard__mutmut_2 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_3'] = x_copy_to_clipboard__mutmut_3 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_4'] = x_copy_to_clipboard__mutmut_4 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_5'] = x_copy_to_clipboard__mutmut_5 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_6'] = x_copy_to_clipboard__mutmut_6 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_7'] = x_copy_to_clipboard__mutmut_7 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_8'] = x_copy_to_clipboard__mutmut_8 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_9'] = x_copy_to_clipboard__mutmut_9 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_10'] = x_copy_to_clipboard__mutmut_10 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_11'] = x_copy_to_clipboard__mutmut_11 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_12'] = x_copy_to_clipboard__mutmut_12 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_13'] = x_copy_to_clipboard__mutmut_13 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_14'] = x_copy_to_clipboard__mutmut_14 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_15'] = x_copy_to_clipboard__mutmut_15 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_16'] = x_copy_to_clipboard__mutmut_16 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_17'] = x_copy_to_clipboard__mutmut_17 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_18'] = x_copy_to_clipboard__mutmut_18 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_19'] = x_copy_to_clipboard__mutmut_19 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_20'] = x_copy_to_clipboard__mutmut_20 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_21'] = x_copy_to_clipboard__mutmut_21 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_22'] = x_copy_to_clipboard__mutmut_22 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_23'] = x_copy_to_clipboard__mutmut_23 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_24'] = x_copy_to_clipboard__mutmut_24 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_25'] = x_copy_to_clipboard__mutmut_25 # type: ignore # mutmut generated
mutants_x_copy_to_clipboard__mutmut['x_copy_to_clipboard__mutmut_26'] = x_copy_to_clipboard__mutmut_26 # type: ignore # mutmut generated
mutants_x_write_export_file__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_write_export_file__mutmut)
def write_export_file(text: str) -> str:
    """Write ``text`` to a temp file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False, encoding="utf-8"
    ) as handle:  # noqa: E501
        handle.write(text)
        return str(handle.name)


def x_write_export_file__mutmut_orig(text: str) -> str:
    """Write ``text`` to a temp file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False, encoding="utf-8"
    ) as handle:  # noqa: E501
        handle.write(text)
        return str(handle.name)


def x_write_export_file__mutmut_1(text: str) -> str:
    """Write ``text`` to a temp file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode=None, suffix=".txt", delete=False, encoding="utf-8"
    ) as handle:  # noqa: E501
        handle.write(text)
        return str(handle.name)


def x_write_export_file__mutmut_2(text: str) -> str:
    """Write ``text`` to a temp file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=None, delete=False, encoding="utf-8"
    ) as handle:  # noqa: E501
        handle.write(text)
        return str(handle.name)


def x_write_export_file__mutmut_3(text: str) -> str:
    """Write ``text`` to a temp file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=None, encoding="utf-8"
    ) as handle:  # noqa: E501
        handle.write(text)
        return str(handle.name)


def x_write_export_file__mutmut_4(text: str) -> str:
    """Write ``text`` to a temp file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False, encoding=None
    ) as handle:  # noqa: E501
        handle.write(text)
        return str(handle.name)


def x_write_export_file__mutmut_5(text: str) -> str:
    """Write ``text`` to a temp file and return its path."""
    with tempfile.NamedTemporaryFile(
        suffix=".txt", delete=False, encoding="utf-8"
    ) as handle:  # noqa: E501
        handle.write(text)
        return str(handle.name)


def x_write_export_file__mutmut_6(text: str) -> str:
    """Write ``text`` to a temp file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="w", delete=False, encoding="utf-8"
    ) as handle:  # noqa: E501
        handle.write(text)
        return str(handle.name)


def x_write_export_file__mutmut_7(text: str) -> str:
    """Write ``text`` to a temp file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", encoding="utf-8"
    ) as handle:  # noqa: E501
        handle.write(text)
        return str(handle.name)


def x_write_export_file__mutmut_8(text: str) -> str:
    """Write ``text`` to a temp file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False, ) as handle:  # noqa: E501
        handle.write(text)
        return str(handle.name)


def x_write_export_file__mutmut_9(text: str) -> str:
    """Write ``text`` to a temp file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="XXwXX", suffix=".txt", delete=False, encoding="utf-8"
    ) as handle:  # noqa: E501
        handle.write(text)
        return str(handle.name)


def x_write_export_file__mutmut_10(text: str) -> str:
    """Write ``text`` to a temp file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="W", suffix=".txt", delete=False, encoding="utf-8"
    ) as handle:  # noqa: E501
        handle.write(text)
        return str(handle.name)


def x_write_export_file__mutmut_11(text: str) -> str:
    """Write ``text`` to a temp file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix="XX.txtXX", delete=False, encoding="utf-8"
    ) as handle:  # noqa: E501
        handle.write(text)
        return str(handle.name)


def x_write_export_file__mutmut_12(text: str) -> str:
    """Write ``text`` to a temp file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".TXT", delete=False, encoding="utf-8"
    ) as handle:  # noqa: E501
        handle.write(text)
        return str(handle.name)


def x_write_export_file__mutmut_13(text: str) -> str:
    """Write ``text`` to a temp file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=True, encoding="utf-8"
    ) as handle:  # noqa: E501
        handle.write(text)
        return str(handle.name)


def x_write_export_file__mutmut_14(text: str) -> str:
    """Write ``text`` to a temp file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False, encoding="XXutf-8XX"
    ) as handle:  # noqa: E501
        handle.write(text)
        return str(handle.name)


def x_write_export_file__mutmut_15(text: str) -> str:
    """Write ``text`` to a temp file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False, encoding="UTF-8"
    ) as handle:  # noqa: E501
        handle.write(text)
        return str(handle.name)


def x_write_export_file__mutmut_16(text: str) -> str:
    """Write ``text`` to a temp file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False, encoding="utf-8"
    ) as handle:  # noqa: E501
        handle.write(None)
        return str(handle.name)


def x_write_export_file__mutmut_17(text: str) -> str:
    """Write ``text`` to a temp file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False, encoding="utf-8"
    ) as handle:  # noqa: E501
        handle.write(text)
        return str(None)

mutants_x_write_export_file__mutmut['_mutmut_orig'] = x_write_export_file__mutmut_orig # type: ignore # mutmut generated
mutants_x_write_export_file__mutmut['x_write_export_file__mutmut_1'] = x_write_export_file__mutmut_1 # type: ignore # mutmut generated
mutants_x_write_export_file__mutmut['x_write_export_file__mutmut_2'] = x_write_export_file__mutmut_2 # type: ignore # mutmut generated
mutants_x_write_export_file__mutmut['x_write_export_file__mutmut_3'] = x_write_export_file__mutmut_3 # type: ignore # mutmut generated
mutants_x_write_export_file__mutmut['x_write_export_file__mutmut_4'] = x_write_export_file__mutmut_4 # type: ignore # mutmut generated
mutants_x_write_export_file__mutmut['x_write_export_file__mutmut_5'] = x_write_export_file__mutmut_5 # type: ignore # mutmut generated
mutants_x_write_export_file__mutmut['x_write_export_file__mutmut_6'] = x_write_export_file__mutmut_6 # type: ignore # mutmut generated
mutants_x_write_export_file__mutmut['x_write_export_file__mutmut_7'] = x_write_export_file__mutmut_7 # type: ignore # mutmut generated
mutants_x_write_export_file__mutmut['x_write_export_file__mutmut_8'] = x_write_export_file__mutmut_8 # type: ignore # mutmut generated
mutants_x_write_export_file__mutmut['x_write_export_file__mutmut_9'] = x_write_export_file__mutmut_9 # type: ignore # mutmut generated
mutants_x_write_export_file__mutmut['x_write_export_file__mutmut_10'] = x_write_export_file__mutmut_10 # type: ignore # mutmut generated
mutants_x_write_export_file__mutmut['x_write_export_file__mutmut_11'] = x_write_export_file__mutmut_11 # type: ignore # mutmut generated
mutants_x_write_export_file__mutmut['x_write_export_file__mutmut_12'] = x_write_export_file__mutmut_12 # type: ignore # mutmut generated
mutants_x_write_export_file__mutmut['x_write_export_file__mutmut_13'] = x_write_export_file__mutmut_13 # type: ignore # mutmut generated
mutants_x_write_export_file__mutmut['x_write_export_file__mutmut_14'] = x_write_export_file__mutmut_14 # type: ignore # mutmut generated
mutants_x_write_export_file__mutmut['x_write_export_file__mutmut_15'] = x_write_export_file__mutmut_15 # type: ignore # mutmut generated
mutants_x_write_export_file__mutmut['x_write_export_file__mutmut_16'] = x_write_export_file__mutmut_16 # type: ignore # mutmut generated
mutants_x_write_export_file__mutmut['x_write_export_file__mutmut_17'] = x_write_export_file__mutmut_17 # type: ignore # mutmut generated
mutants_x_open_in_editor__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_open_in_editor__mutmut)
def open_in_editor(path: str) -> None:
    """Open ``path`` in the platform default editor."""
    system = platform.system()
    if system == "Darwin":
        subprocess.Popen(["open", path])
    elif system == "Linux":
        subprocess.Popen(["xdg-open", path])


def x_open_in_editor__mutmut_orig(path: str) -> None:
    """Open ``path`` in the platform default editor."""
    system = platform.system()
    if system == "Darwin":
        subprocess.Popen(["open", path])
    elif system == "Linux":
        subprocess.Popen(["xdg-open", path])


def x_open_in_editor__mutmut_1(path: str) -> None:
    """Open ``path`` in the platform default editor."""
    system = None
    if system == "Darwin":
        subprocess.Popen(["open", path])
    elif system == "Linux":
        subprocess.Popen(["xdg-open", path])


def x_open_in_editor__mutmut_2(path: str) -> None:
    """Open ``path`` in the platform default editor."""
    system = platform.system()
    if system != "Darwin":
        subprocess.Popen(["open", path])
    elif system == "Linux":
        subprocess.Popen(["xdg-open", path])


def x_open_in_editor__mutmut_3(path: str) -> None:
    """Open ``path`` in the platform default editor."""
    system = platform.system()
    if system == "XXDarwinXX":
        subprocess.Popen(["open", path])
    elif system == "Linux":
        subprocess.Popen(["xdg-open", path])


def x_open_in_editor__mutmut_4(path: str) -> None:
    """Open ``path`` in the platform default editor."""
    system = platform.system()
    if system == "darwin":
        subprocess.Popen(["open", path])
    elif system == "Linux":
        subprocess.Popen(["xdg-open", path])


def x_open_in_editor__mutmut_5(path: str) -> None:
    """Open ``path`` in the platform default editor."""
    system = platform.system()
    if system == "DARWIN":
        subprocess.Popen(["open", path])
    elif system == "Linux":
        subprocess.Popen(["xdg-open", path])


def x_open_in_editor__mutmut_6(path: str) -> None:
    """Open ``path`` in the platform default editor."""
    system = platform.system()
    if system == "Darwin":
        subprocess.Popen(None)
    elif system == "Linux":
        subprocess.Popen(["xdg-open", path])


def x_open_in_editor__mutmut_7(path: str) -> None:
    """Open ``path`` in the platform default editor."""
    system = platform.system()
    if system == "Darwin":
        subprocess.Popen(["XXopenXX", path])
    elif system == "Linux":
        subprocess.Popen(["xdg-open", path])


def x_open_in_editor__mutmut_8(path: str) -> None:
    """Open ``path`` in the platform default editor."""
    system = platform.system()
    if system == "Darwin":
        subprocess.Popen(["OPEN", path])
    elif system == "Linux":
        subprocess.Popen(["xdg-open", path])


def x_open_in_editor__mutmut_9(path: str) -> None:
    """Open ``path`` in the platform default editor."""
    system = platform.system()
    if system == "Darwin":
        subprocess.Popen(["open", path])
    elif system != "Linux":
        subprocess.Popen(["xdg-open", path])


def x_open_in_editor__mutmut_10(path: str) -> None:
    """Open ``path`` in the platform default editor."""
    system = platform.system()
    if system == "Darwin":
        subprocess.Popen(["open", path])
    elif system == "XXLinuxXX":
        subprocess.Popen(["xdg-open", path])


def x_open_in_editor__mutmut_11(path: str) -> None:
    """Open ``path`` in the platform default editor."""
    system = platform.system()
    if system == "Darwin":
        subprocess.Popen(["open", path])
    elif system == "linux":
        subprocess.Popen(["xdg-open", path])


def x_open_in_editor__mutmut_12(path: str) -> None:
    """Open ``path`` in the platform default editor."""
    system = platform.system()
    if system == "Darwin":
        subprocess.Popen(["open", path])
    elif system == "LINUX":
        subprocess.Popen(["xdg-open", path])


def x_open_in_editor__mutmut_13(path: str) -> None:
    """Open ``path`` in the platform default editor."""
    system = platform.system()
    if system == "Darwin":
        subprocess.Popen(["open", path])
    elif system == "Linux":
        subprocess.Popen(None)


def x_open_in_editor__mutmut_14(path: str) -> None:
    """Open ``path`` in the platform default editor."""
    system = platform.system()
    if system == "Darwin":
        subprocess.Popen(["open", path])
    elif system == "Linux":
        subprocess.Popen(["XXxdg-openXX", path])


def x_open_in_editor__mutmut_15(path: str) -> None:
    """Open ``path`` in the platform default editor."""
    system = platform.system()
    if system == "Darwin":
        subprocess.Popen(["open", path])
    elif system == "Linux":
        subprocess.Popen(["XDG-OPEN", path])

mutants_x_open_in_editor__mutmut['_mutmut_orig'] = x_open_in_editor__mutmut_orig # type: ignore # mutmut generated
mutants_x_open_in_editor__mutmut['x_open_in_editor__mutmut_1'] = x_open_in_editor__mutmut_1 # type: ignore # mutmut generated
mutants_x_open_in_editor__mutmut['x_open_in_editor__mutmut_2'] = x_open_in_editor__mutmut_2 # type: ignore # mutmut generated
mutants_x_open_in_editor__mutmut['x_open_in_editor__mutmut_3'] = x_open_in_editor__mutmut_3 # type: ignore # mutmut generated
mutants_x_open_in_editor__mutmut['x_open_in_editor__mutmut_4'] = x_open_in_editor__mutmut_4 # type: ignore # mutmut generated
mutants_x_open_in_editor__mutmut['x_open_in_editor__mutmut_5'] = x_open_in_editor__mutmut_5 # type: ignore # mutmut generated
mutants_x_open_in_editor__mutmut['x_open_in_editor__mutmut_6'] = x_open_in_editor__mutmut_6 # type: ignore # mutmut generated
mutants_x_open_in_editor__mutmut['x_open_in_editor__mutmut_7'] = x_open_in_editor__mutmut_7 # type: ignore # mutmut generated
mutants_x_open_in_editor__mutmut['x_open_in_editor__mutmut_8'] = x_open_in_editor__mutmut_8 # type: ignore # mutmut generated
mutants_x_open_in_editor__mutmut['x_open_in_editor__mutmut_9'] = x_open_in_editor__mutmut_9 # type: ignore # mutmut generated
mutants_x_open_in_editor__mutmut['x_open_in_editor__mutmut_10'] = x_open_in_editor__mutmut_10 # type: ignore # mutmut generated
mutants_x_open_in_editor__mutmut['x_open_in_editor__mutmut_11'] = x_open_in_editor__mutmut_11 # type: ignore # mutmut generated
mutants_x_open_in_editor__mutmut['x_open_in_editor__mutmut_12'] = x_open_in_editor__mutmut_12 # type: ignore # mutmut generated
mutants_x_open_in_editor__mutmut['x_open_in_editor__mutmut_13'] = x_open_in_editor__mutmut_13 # type: ignore # mutmut generated
mutants_x_open_in_editor__mutmut['x_open_in_editor__mutmut_14'] = x_open_in_editor__mutmut_14 # type: ignore # mutmut generated
mutants_x_open_in_editor__mutmut['x_open_in_editor__mutmut_15'] = x_open_in_editor__mutmut_15 # type: ignore # mutmut generated
